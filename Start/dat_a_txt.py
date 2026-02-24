import struct
import os


def decrypt_final(filename, output_file="Start/00_Selecter.txt"):
    if not os.path.exists(filename):
        print("Mal path")
        return

    with open(filename, "rb") as f, open(output_file, "w", encoding="utf-8") as out:

        count_data = f.read(4)
        num_files = struct.unpack('<I', count_data)[0]

        offsets = []
        for _ in range(num_files):
            offsets.append(struct.unpack('<I', f.read(4))[0])

        f.seek(0, 2)
        offsets.append(f.tell())

        for i in range(num_files):
            start = offsets[i]
            end = offsets[i + 1]
            size = end - start

            f.seek(start)
            raw_block = f.read(size)

            decrypted_bytes = bytes([b ^ 0xFF for b in raw_block])
            clean_data = decrypted_bytes.split(b'\xff')[0]

            if len(clean_data) > 0:
                try:
                    text = clean_data.decode('shift_jis')
                    out.write(f"ID {i + 1:02d}: {text}\n")
                except UnicodeDecodeError:
                    text = clean_data.decode('shift_jis', errors='ignore')
                    out.write(f"ID {i + 1:02d}: {text} [decode error]\n")
            else:
                out.write(f"ID {i + 1:02d}: [Vacío]\n")

    print(f"Texto guardado en {output_file}")


decrypt_final("Start/Archivos_repaquetar_start/00_Selecter.dat")