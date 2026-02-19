import re
import os


def to_full_width(text):
    """
    Converts standard ASCII characters to Japanese Full-width (Zen-kaku) characters.
    Also maps common Spanish characters to compatible ones.
    """
    # Map Spanish characters to basic equivalents (Shift-JIS doesn't support them)
    spanish_map = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ñ': 'n', 'Ñ': 'N', 'ü': 'u', 'Ü': 'U',
        '¿': '', '¡': ''
    }
    for search, replace in spanish_map.items():
        text = text.replace(search, replace)

    # Convert standard letters/numbers/symbols to Full-width
    result = ""
    for char in text:
        code = ord(char)
        # Standard ASCII range (Space to ~)
        if 0x0021 <= code <= 0x007E:
            result += chr(code + 0xFEE0)
        elif code == 0x0020:  # Space
            result += chr(0x3000)
        else:
            result += char
    return result


def insert_story_spanish():
    dat_path = "Ficheros_DATA01_Story/01_Story.dat"
    txt_path = "Ficheros_DATA01_Story/01_Story_esp.txt"
    output_path = "Ficheros_DATA01_Story/01_Story_new.dat"

    if not os.path.exists(dat_path):
        print("Error: Original .dat not found!")
        return

    with open(dat_path, "rb") as f:
        data = bytearray(f.read())

    with open(txt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        # Match "Offset 0x123: Text"
        match = re.match(r"Offset 0x([0-9A-Fa-f]+): (.*)", line.strip())
        if not match:
            continue

        offset = int(match.group(1), 16)
        original_text = match.group(2)

        # 1. CONVERT TO FULL-WIDTH (This makes it visible in game)
        formatted_text = to_full_width(original_text)

        # 2. ENCODE & ENCRYPT
        # We add \x00 as a clear-text terminator.
        # When XORed by 0xFF, it becomes 0xFF in the file.
        encoded = formatted_text.encode("shift_jis", errors="replace") + b'\x00'
        encrypted = bytes([b ^ 0xFF for b in encoded])

        # 3. CALCULATE SPACE (Find original terminator in file)
        end = data.find(b'\xff', offset)
        if end == -1:
            continue

        original_size = end - offset + 1

        # 4. SIZE CHECK
        if len(encrypted) > original_size:
            print(f"⚠ TOO LONG: {hex(offset)} (Needs {len(encrypted)}, has {original_size})")
            # Truncate to prevent crash
            encrypted = encrypted[:original_size - 1] + b'\xff'

        # 5. WRITE & PAD
        data[offset: offset + len(encrypted)] = encrypted

        remaining = original_size - len(encrypted)
        if remaining > 0:
            # Padding with 0x00 (XORs to 0xFF in memory, which is safe)
            data[offset + len(encrypted): offset + original_size] = b'\x00' * remaining

    with open(output_path, "wb") as f:
        f.write(data)
    print("Insertion complete! Using Full-Width characters.")


# Run the process
insert_story_spanish()