import re
import os

def forensic_nis_extract(filename, output_file="Codigos_txt_a_dat_formato_japones/01_Story_prueba.txt"):
    if not os.path.exists(filename):
        print(f"Mal path: {filename}")
        return

    with open(filename, "rb") as f:
        data = f.read()

    decrypted = bytearray([b ^ 0xFF for b in data])

    sjis_regex = b'([\x81-\x9f\xe0-\xfc][\x40-\x7e\x80-\xfc]|[\x20-\x7e\xa1-\xdf])+'

    matches = re.finditer(sjis_regex, decrypted)

    with open(output_file, "w", encoding="utf-8") as out:
        for match in matches:
            text_bytes = match.group(0)
            if len(text_bytes) < 4:
                continue

            try:
                decoded = text_bytes.decode('shift_jis').strip()
                if any(ord(c) > 0x80 for c in decoded):
                    out.write(f"Offset {hex(match.start())}: {decoded}\n")
            except:
                continue

    print(f"Texto extraído guardado en: {output_file}")


# Usa la ruta correcta de tu .dat
forensic_nis_extract("Codigos_txt_a_dat_formato_japones/01_Story_new.dat")