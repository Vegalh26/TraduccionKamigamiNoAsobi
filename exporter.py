import re
import os


def forensic_export(filename, output_txt):
    with open(filename, "rb") as f:
        data = f.read()

    decrypted = bytearray([b ^ 0xFF for b in data])
    sjis_regex = b'([\x81-\x9f\xe0-\xfc][\x40-\x7e\x80-\xfc]|[\x20-\x7e\xa1-\xdf])+'

    matches = re.finditer(sjis_regex, decrypted)

    with open(output_txt, "w", encoding="utf-8") as out:
        for match in matches:
            text_bytes = match.group(0)
            if len(text_bytes) < 4: continue

            try:
                decoded = text_bytes.decode('shift_jis').strip()
                if any(ord(c) > 0x80 for c in decoded):
                    # We save the offset so the importer knows what to search for
                    out.write(f"[{hex(match.start())}]\nOR: {decoded}\nTR: \n\n")
            except:
                continue
    print(f"Exported all text to {output_txt}")


forensic_export("Ficheros_DATA01_Story/Original/01_Story.dat", "01_Story_TR.txt")