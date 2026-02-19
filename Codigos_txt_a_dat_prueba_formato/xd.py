import re
import os


def clean_spanish_text(text):
    """
    Removes Spanish-specific characters that Shift-JIS cannot handle
    and converts them to standard ASCII.
    """
    rep = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ñ': 'n', 'Ñ': 'N', 'ü': 'u', 'Ü': 'U',
        '¿': '', '¡': '', '—': '-'
    }
    for search, replace in rep.items():
        text = text.replace(search, replace)
    return text


def insert_story_final():
    dat_path = "Codigos_txt_a_dat_prueba_formato/01_Story.dat"
    txt_path = "Codigos_txt_a_dat_prueba_formato/01_Story_esp.txt"
    output_path = "Codigos_txt_a_dat_prueba_formato/01_Story_new.dat"

    if not os.path.exists(dat_path):
        print(f"Error: {dat_path} not found.")
        return

    with open(dat_path, "rb") as f:
        data = bytearray(f.read())

    with open(txt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print("Inserting text...")

    for line in lines:
        # Match your format: Offset 0x123: Text
        match = re.match(r"Offset 0x([0-9A-Fa-f]+): (.*)", line.strip())
        if not match:
            continue

        offset = int(match.group(1), 16)
        text = match.group(2)

        # 1. Clean the Spanish characters (Crucial for Shift-JIS)
        text = clean_spanish_text(text)

        # 2. ENCODE & ENCRYPT
        # We add \x00 as a clear-text terminator.
        # XORed by 0xFF, this becomes 0xFF in the file.
        # When the game reads 0xFF and XORs it back, it gets 0x00 (Null).
        encoded = text.encode("shift_jis", errors="replace") + b'\x00'
        encrypted = bytes([b ^ 0xFF for b in encoded])

        # 3. Find the original space
        # Original terminator in file is 0xFF
        end = data.find(b'\xff', offset)
        if end == -1:
            continue

        original_size = end - offset + 1

        # 4. Check length
        # Since we are using Half-Width, 1 char = 1 byte.
        # Japanese was 1 char = 2 bytes.
        # You now have TWICE as much room for characters!
        if len(encrypted) > original_size:
            print(f"⚠ Still too long at {hex(offset)} ({len(encrypted)} > {original_size})")
            encrypted = encrypted[:original_size - 1] + b'\xff'

        # 5. Write to file
        data[offset: offset + len(encrypted)] = encrypted

        # 6. Padding (Very Important)
        # We fill the leftover space with 0x00 (file)
        # which is 0xFF (decrypted). This is the safest "Empty" byte.
        remaining = original_size - len(encrypted)
        if remaining > 0:
            data[offset + len(encrypted): offset + original_size] = b'\x00' * remaining

    with open(output_path, "wb") as f:
        f.write(data)

    print("Done! Check 01_Story_new.dat")


insert_story_final()