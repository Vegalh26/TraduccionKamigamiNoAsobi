import struct
from PIL import Image


def deswizzle4(src, width, height):
    dst = bytearray(width * height)

    tile_w, tile_h = 8, 8
    tiles_x = width // tile_w
    tiles_y = height // tile_h

    src_index = 0

    for ty in range(tiles_y):
        for tx in range(tiles_x):
            for y in range(tile_h):
                for x in range(0, tile_w, 2):

                    if src_index >= len(src):
                        break

                    byte = src[src_index]
                    src_index += 1

                    low = byte & 0x0F
                    high = byte >> 4

                    px = tx * tile_w + x
                    py = ty * tile_h + y

                    dst[py * width + px] = low
                    dst[py * width + px + 1] = high

    return dst


def read_txp_4bit(path, output_png):
    with open(path, "rb") as f:

        # HEADER REAL (24 bytes)
        w, h = struct.unpack("<HH", f.read(4))
        color_count = struct.unpack("<H", f.read(2))[0]
        f.read(18)  # <-- CORREGIDO

        print("Width:", w)
        print("Height:", h)
        print("Color count:", color_count)
        print("Header size:", f.tell())

        if color_count != 16:
            raise ValueError("Este código solo soporta TXP 4-bit (16 colores)")

        # Leer paleta
        palette = []
        for _ in range(16):
            b, g, r, a = struct.unpack("4B", f.read(4))
            palette.append((r, g, b, 255))

        print("Palette offset:", f.tell())

        pixel_bytes = f.read()
        print("Pixel data size:", len(pixel_bytes))

        pixels = deswizzle4(pixel_bytes, w, h)

        img = Image.new("RGBA", (w, h))
        img.putdata([palette[p] for p in pixels])
        img.save(output_png)

        print("Guardado:", output_png)


read_txp_4bit(
    "Start/Archivos_repaquetar_start/FontA000.txp",
    "output.png"
)