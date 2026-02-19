import re
import os


def clean_to_half_width(text):
    """
    Converts Spanish characters to standard ASCII (Half-Width)
    because Shift-JIS cannot handle 'ñ' or 'á' in single-byte mode.
    """
    spanish_map = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ñ': 'n', 'Ñ': 'N', 'ü': 'u', 'Ü': 'U',
        '¿': '', '¡': ''
    }
    for search, replace in spanish_map.items():
        text = text.replace(search, replace)
    return text


def insert_story_half_width():
    dat_path = "Codigos_txt_a_dat_prueba_formato/01_Story.dat"
    txt_path = "Codigos_txt_a_dat_prueba_formato/01_Story_esp.txt"
    output_path = "Codigos_txt_a_dat_prueba_formato/01_Story_new.dat"

    if not os.path.exists(dat_path):
        print(f"❌ Error: {dat_path} not found.")
        return

    with open(dat_path, "rb") as f:
        data = bytearray(f.read())

    with open(txt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print("--- Inserting Half-Width Text ---")

    for line in lines:
        # Match "Offset 0x123: Text"
        match = re.match(r"Offset 0x([0-9A-Fa-f]+): (.*)", line.strip())
        if not match:
            continue

        offset = int(match.group(1), 16)
        original_text = match.group(2)

        # 1. CLEAN TEXT (Force Half-Width/ASCII)
        # We removed "to_full_width" and replaced it with this cleaner.
        formatted_text = clean_to_half_width(original_text)

        # 2. ENCODE & ENCRYPT (Exact same logic as the working script)
        # We add \x00 as a clear-text terminator.
        # When XORed by 0xFF, it becomes 0xFF in the file.
        try:
            encoded = formatted_text.encode("shift_jis", errors="replace") + b'\x00'
        except:
            print(f"Encoding error at {hex(offset)}")
            continue

        encrypted = bytes([b ^ 0xFF for b in encoded])

        # 3. FIND SPACE
        end = data.find(b'\xff', offset)
        if end == -1:
            continue

        original_size = end - offset + 1

        # 4. SIZE CHECK
        # Note: Since we are using Half-Width, you have DOUBLE the space now.
        if len(encrypted) > original_size:
            print(f"⚠ TOO LONG: {hex(offset)} (Needs {len(encrypted)}, has {original_size})")
            # Truncate to prevent crash
            encrypted = encrypted[:original_size - 1] + b'\xff'

        # 5. WRITE & PAD (Exact same logic as the working script)
        data[offset: offset + len(encrypted)] = encrypted

        remaining = original_size - len(encrypted)
        if remaining > 0:
            # Padding with 0x00
            data[offset + len(encrypted): offset + original_size] = b'\x00' * remaining

    with open(output_path, "wb") as f:
        f.write(data)

    print(f"✅ Done. Saved to {output_path}")


insert_story_half_width()