import os
import struct
from PIL import Image


def unswizzle_psp(data, width, height, bpp):
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

            if swizzled_offset < len(data) and linear_offset < len(out):
                out[linear_offset] = data[swizzled_offset]

    return out


def extract_txp(file_path):
    try:
        print(f"\nProcessing: {file_path}")

        with open(file_path, 'rb') as f:
            width = struct.unpack('<H', f.read(2))[0]
            height = struct.unpack('<H', f.read(2))[0]

            bpp = 4  # tus archivos son 4bpp

            f.seek(16)
            palette_data = f.read(16 * 4)

            palette = []
            for i in range(16):
                offset = i * 4
                r = palette_data[offset]
                g = palette_data[offset + 1]
                b = palette_data[offset + 2]
                a = palette_data[offset + 3]
                palette.append((r, g, b, a))

            raw_pixels = f.read()

        unswizzled = unswizzle_psp(raw_pixels, width, height, bpp)

        expanded = bytearray()
        for byte in unswizzled:
            low = byte & 0x0F
            high = (byte >> 4) & 0x0F
            expanded.append(low)
            expanded.append(high)

        img = Image.new("RGBA", (width, height))
        pixels = [palette[i] for i in expanded[:width * height]]
        img.putdata(pixels)

        out_path = file_path.replace(".txp", ".png")
        img.save(out_path)

        print(f"Saved: {out_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")


# ------------------------
# LISTA MANUAL DE ARCHIVOS
# ------------------------

if __name__ == "__main__":

    files = [
        "Start\Fonts_en_png\FontA_patched_variants\FontA001_adv12.txp",
    ]

    for file in files:
        extract_txp(file)

    print("\nDone processing selected files.")