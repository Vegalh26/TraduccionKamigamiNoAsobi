import struct
import os
import zlib

folder = r"Start\Archivos_repaquetar_start"
files = sorted([os.path.join(folder, f)
                for f in os.listdir(folder)
                if os.path.isfile(os.path.join(folder, f))])

output_name = "START.DAT"

def align(value, alignment=0x800):
    return (value + alignment - 1) & ~(alignment - 1)

with open(output_name, "wb") as out:

    out.write(b"NISPACK\x00")
    out.write(struct.pack("<I", 0))
    out.write(struct.pack("<I", len(files)))

    header_size = 8 + 4 + 4
    table_size = len(files) * (32 + 4 + 4 + 4)

    current_offset = align(header_size + table_size, 0x800)

    entries = []

    # Preparar tabla
    for filename in files:
        size = os.path.getsize(filename)
        crc = zlib.crc32(open(filename, "rb").read()) & 0xffffffff

        entries.append((filename, current_offset, size, crc))

        current_offset = align(current_offset + size, 0x800)

    # Escribir tabla
    for filename, offset, size, crc in entries:
        name_only = os.path.basename(filename)
        name_bytes = name_only.encode("shift-jis")
        name_bytes = name_bytes.ljust(32, b"\x00")

        out.write(name_bytes)
        out.write(struct.pack("<I", offset))
        out.write(struct.pack("<I", size))
        out.write(struct.pack("<I", crc))

    # Rellenar hasta primer offset alineado
    current_pos = out.tell()
    padding = align(current_pos, 0x800) - current_pos
    out.write(b"\x00" * padding)

    # Escribir archivos con padding
    for filename, offset, size, crc in entries:
        with open(filename, "rb") as f:
            out.write(f.read())

        current_pos = out.tell()
        padding = align(current_pos, 0x800) - current_pos
        out.write(b"\x00" * padding)

print("Repack terminado ✔")