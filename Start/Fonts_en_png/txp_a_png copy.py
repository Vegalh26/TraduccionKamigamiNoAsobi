import struct

# ← Cambia estas rutas según tus archivos
txp_path = "Start/Fonts_en_png/Pruebas/Originales/FontA000.txp"   # Ruta del TXP original
txt_path = "Start/Fonts_en_png/Pruebas/Editados/FontA000.txt"     # Ruta donde quieres guardar el TXT

def txp_to_txt(txp_path, txt_path):
    with open(txp_path, "rb") as f:
        data = f.read()

    # Leer header (suponiendo 4 bytes para ancho y alto)
    width = struct.unpack_from("<H", data, 0)[0]   # bytes 0-1
    height = struct.unpack_from("<H", data, 2)[0]  # bytes 2-3

    print(f"Ancho: {width}, Alto: {height}")

    # Datos de imagen empiezan en byte 16 (ajusta si tu TXP tiene otro header)
    img_data = data[16:]

    # TXP 4bpp: cada byte contiene dos píxeles
    pixels = []
    for b in img_data:
        high = (b >> 4) & 0xF
        low = b & 0xF
        pixels.append(high)
        pixels.append(low)

    # Guardar como TXT
    with open(txt_path, "w") as f:
        for y in range(height):
            row = pixels[y*width:(y+1)*width]
            f.write(" ".join(f"{p:X}" for p in row) + "\n")

    print(f"TXP convertido a TXT en {txt_path}")

# Ejecutar
txp_to_txt(txp_path, txt_path)