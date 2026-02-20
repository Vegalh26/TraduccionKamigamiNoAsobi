import struct
from PIL import Image

def deswizzle8(src, width, height):
    dst = bytearray(len(src))
    tile_w, tile_h = 8, 8
    tiles_x = width // tile_w
    tiles_y = height // tile_h

    for ty in range(tiles_y):
        for tx in range(tiles_x):
            for y in range(tile_h):
                for x in range(tile_w):
                    src_index = ((ty * tiles_x + tx) * 64) + (y * tile_w) + x
                    dst_index = (ty * tile_h + y) * width + (tx * tile_w + x)
                    if src_index < len(src) and dst_index < len(dst):
                        dst[dst_index] = src[src_index]
    return dst

def read_txp(path, output_png):
    with open(path, "rb") as f:
        w, h = struct.unpack("<HH", f.read(4))
        color_count = struct.unpack("<H", f.read(2))[0]
        _ = f.read(10)  # ignoramos los otros ushorts del header
        palette_width, palette_height = struct.unpack("<HH", f.read(4))
        swizzle_flag = struct.unpack("<H", f.read(2))[0]
        f.read(2)  # unknown

        # Leer paleta
        palette = []
        for py in range(palette_height):
            for _ in range(palette_width):
                a, b, g, r = struct.unpack("4B", f.read(4))
                palette.append((r, g, b, a))

        # Leer pixeles
        if color_count == 256:
            pixel_data = bytearray(f.read(w*h))
            if swizzle_flag != 0:
                pixel_data = deswizzle8(pixel_data, w, h)
        else:
            # 4-bit no implementado todavía
            raise NotImplementedError("4-bit TXP aún no implementado")

        # Convertir a imagen
        img = Image.new("RGBA", (w, h))
        img.putdata([palette[p] for p in pixel_data])
        img.save(output_png)
        print("Guardado:", output_png)

# USO
read_txp("Ajustes\extracted\start_extracted\head05.txp", "output.png")