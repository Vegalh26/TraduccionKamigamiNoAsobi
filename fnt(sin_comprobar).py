import os


def dump_hex(data):
    print("\n--- FIRST 64 BYTES (HEX) ---")
    print(data[:64].hex())

    print("\n--- FIRST 256 BYTES (HEX DUMP STYLE) ---")
    for i in range(0, 256, 16):
        chunk = data[i:i+16]
        hex_part = " ".join(f"{b:02X}" for b in chunk)

        # Mostrar posible UTF-16
        try:
            ascii_part = chunk.decode("utf-16le", errors="replace")
        except:
            ascii_part = "." * len(chunk)

        print(f"{i:08X}  {hex_part:<47}  {ascii_part}")


def dump_utf16_table(data, start_offset=4, max_entries=512):
    """
    Lee la tabla de caracteres típica de estos FNT.
    Cada entrada = 2 bytes (UTF-16LE codepoint).
    """

    print("\n--- CHARACTER MAP (UTF-16LE) ---")

    pos = start_offset
    count = 0

    while pos + 2 <= len(data) and count < max_entries:
        codepoint = int.from_bytes(data[pos:pos+2], "little")
        pos += 2

        try:
            char = chr(codepoint)
            printable = char if char.isprintable() else "."
        except:
            printable = "?"

        print(f"Glyph {count:04d} -> U+{codepoint:04X} -> {printable}")
        count += 1

    print(f"\nTotal glyphs parsed: {count}")


def guess_format(data):
    print("\n--- FORMAT GUESS ---")

    if data.startswith(b"<?xml"):
        print("Looks like XML font.")
    elif b"info face=" in data:
        print("Looks like BMFont text format.")
    elif b"BMF" in data[:4]:
        print("Looks like BMFont binary format.")
    else:
        print("Likely proprietary binary font format (UTF-16 charmap).")


def inspect_fnt(file_path):

    if not os.path.exists(file_path):
        print("File not found.")
        return

    size = os.path.getsize(file_path)
    print(f"\nFile: {file_path}")
    print(f"Size: {size} bytes")

    with open(file_path, "rb") as f:
        data = f.read()

    dump_hex(data)
    guess_format(data)

    # 🔴 Parte importante: leer tabla real del font
    dump_utf16_table(data)


# --------------------
# USO
# --------------------

if __name__ == "__main__":
    inspect_fnt("Start/Archivos_repaquetar_start/fontA.fnt")