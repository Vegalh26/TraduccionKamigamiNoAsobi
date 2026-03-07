import struct
from PIL import Image


def unswizzle_4bpp(data, width, height):

    width_bytes = width // 2
    pitch = width_bytes

    out = bytearray(len(data))

    for y in range(height):
        for x in range(width_bytes):

            block_x = x // 16
            block_y = y // 8

            block_index = block_x + block_y * (pitch // 16)
            block_address = block_index * 128

            x_in_block = x % 16
            y_in_block = y % 8

            swizzle_index = block_address + y_in_block * 16 + x_in_block
            linear_index = y * pitch + x

            if swizzle_index < len(data) and linear_index < len(out):
                out[linear_index] = data[swizzle_index]

    return out


def extract_txp(file_path):

    with open(file_path, "rb") as f:

        width = struct.unpack("<H", f.read(2))[0]
        height = struct.unpack("<H", f.read(2))[0]

        print("Width:", width)
        print("Height:", height)

        f.seek(16)

        palette_data = f.read(64)

        palette = []
        for i in range(16):

            r = palette_data[i*4+0]
            g = palette_data[i*4+1]
            b = palette_data[i*4+2]
            a = palette_data[i*4+3]

            palette.append((r,g,b,a))

        raw_pixels = f.read()

    # unswizzled = unswizzle_4bpp(raw_pixels, width, height)
    unswizzled = raw_pixels 

    pixels = []

    for byte in unswizzled:

        p1 = byte & 0x0F
        p2 = (byte >> 4) & 0x0F

        pixels.append(palette[p1])
        pixels.append(palette[p2])

    img = Image.new("RGBA",(width,height))
    img.putdata(pixels[:width*height])

    out = file_path.replace(".txp",".png")
    img.save(out)

    print("Saved:", out)


if __name__ == "__main__":

    files = [
        "Start/Archivos_repaquetar_start/textParts.txp",
    ]

    for f in files:
        extract_txp(f)

    print("Done")