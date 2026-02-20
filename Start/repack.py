import struct
import os
import zlib

# Carpeta con los archivos a meter en START.DAT
folder = r"Start\Archivo_extraido_sart.dat"

# Obtenemos todos los archivos dentro de la carpeta (sin subcarpetas)
files = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

output_name = "START.DAT"

with open(output_name, "wb") as out:

    # Header
    out.write(b"NISPACK\x00")            # 8 bytes
    out.write(struct.pack("<I", 0))      # dummy
    out.write(struct.pack("<I", len(files)))  # número de archivos

    # Calculamos dónde empieza la data
    header_size = 8 + 4 + 4
    table_size = len(files) * (32 + 4 + 4 + 4)
    current_offset = header_size + table_size

    entries = []

    # Preparar tabla
    for filename in files:
        size = os.path.getsize(filename)
        crc = zlib.crc32(open(filename, "rb").read()) & 0xffffffff
        entries.append((filename, current_offset, size, crc))
        current_offset += size

    # Escribir tabla
    for filename, offset, size, crc in entries:
        # Solo el nombre del archivo, sin ruta
        name_only = os.path.basename(filename)
        name_bytes = name_only.encode("shift-jis")   # importante en juegos japoneses
        name_bytes = name_bytes.ljust(32, b"\x00")   # rellenar hasta 32 bytes

        out.write(name_bytes)
        out.write(struct.pack("<I", offset))
        out.write(struct.pack("<I", size))
        out.write(struct.pack("<I", crc))

    # Escribir datos reales
    for filename, _, _, _ in entries:
        with open(filename, "rb") as f:
            out.write(f.read())

print("Repack terminado ✔")