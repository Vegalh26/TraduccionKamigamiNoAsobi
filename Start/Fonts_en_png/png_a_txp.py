import os
import struct
from PIL import Image

#Comprobar si funciona todo

def swizzle_psp(data, width, height, bpp):
    out = bytearray(len(data))
    bytes_per_pixel = bpp / 8
    pitch = int((width * bpp) / 8)

    for y in range(height):
        for x in range(width):
            block_x = int((x * bytes_per_pixel) / 16)
            block_y = int(y / 8)

            block_index = block_x + (block_y * (pitch // 16))
            block_address = block_index * 16 * 8

            x_in_block = int((x * bytes_per_pixel) % 16)
            y_in_block = y % 8

            swizzled_offset = int(block_address + x_in_block + (y_in_block * 16))
            linear_offset = int((x * bytes_per_pixel) + (y * pitch))

            if swizzled_offset < len(out) and linear_offset < len(data):
                out[swizzled_offset] = data[linear_offset]

    return out


def repack_png_to_txp(original_txp, edited_png):

    print(f"\nRepacking {edited_png} → {original_txp}")

    # Leer TXP original
    with open(original_txp, "rb") as f:
        txp_data = bytearray(f.read())

    width = struct.unpack("<H", txp_data[0:2])[0]
    height = struct.unpack("<H", txp_data[2:4])[0]

    print(f"Dimensions: {width}x{height}")

    # Offset donde empiezan los píxeles
    palette_offset = 16
    pixel_offset = palette_offset + (16 * 4)

    # Cargar PNG
    img = Image.open(edited_png).convert("RGBA")

    if img.size != (width, height):
        print("ERROR: PNG size does not match TXP size")
        return

    # Leer paleta original
    palette = []
    for i in range(16):
        off = palette_offset + (i * 4)
        r = txp_data[off]
        g = txp_data[off + 1]
        b = txp_data[off + 2]
        a = txp_data[off + 3]
        palette.append((r, g, b, a))

    # Convertir imagen a índices de paleta
    pixels = list(img.getdata())
    indexed_pixels = []

    for px in pixels:
        if px in palette:
            indexed_pixels.append(palette.index(px))
        else:
            # Si el color no existe, usar el más cercano
            distances = []
            for p in palette:
                dist = (px[0]-p[0])**2 + (px[1]-p[1])**2 + (px[2]-p[2])**2
                distances.append(dist)
            indexed_pixels.append(distances.index(min(distances)))

    # Convertir 8bpp index → 4bpp packed
    packed = bytearray()

    for i in range(0, len(indexed_pixels), 2):
        low = indexed_pixels[i]
        high = indexed_pixels[i+1] if i+1 < len(indexed_pixels) else 0
        packed.append((high << 4) | low)

    # Swizzle
    swizzled = swizzle_psp(packed, width, height, 4)

    # Reemplazar datos en TXP
    txp_data[pixel_offset:pixel_offset+len(swizzled)] = swizzled

    # Carpeta fija donde se guardarán los TXP modificados
    output_dir = "Start/Fonts_en_png/Pruebas/Editados"
    os.makedirs(output_dir, exist_ok=True)  # crea la carpeta si no existe

    # Crear el nombre del archivo modificado conservando el original
    filename = os.path.basename(original_txp)          # por ejemplo: FontA000.txp
    filename_mod = filename.replace(".txp", "_mod.txp")  # FontA000_mod.txp

    # Ruta completa donde se guardará
    out_path = os.path.join(output_dir, filename_mod)

    # Guardar
    with open(out_path, "wb") as f:
        f.write(txp_data)

    print("Saved:", out_path)


# ------------------------
# USO
# ------------------------

if __name__ == "__main__":

    repack_png_to_txp(
        "Start/Fonts_en_png/Pruebas/Originales/FontA001.txp",
        "Start/Fonts_en_png/Pruebas/Editados/FontA001.png"
    )