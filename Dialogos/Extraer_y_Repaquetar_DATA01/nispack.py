import struct
import os
import zlib

# Nombre del DAT que quieres extraer
dat_file = "Dialogos\Extraer_y_Repaquetar_DATA01\Archivos_originales_DAT01\DATA01.DAT"

# Carpeta donde se guardarán los archivos extraídos
output_dir = "Dialogos\Extraer_y_Repaquetar_DATA01\Archivos_originales_DAT01"
os.makedirs(output_dir, exist_ok=True)

with open(dat_file, "rb") as f:
    # Leer header
    magic = f.read(8)
    if magic != b"NISPACK\x00":
        raise ValueError("No es un archivo NISPACK válido")
    
    dummy = struct.unpack("<I", f.read(4))[0]
    file_count = struct.unpack("<I", f.read(4))[0]
    
    print(f"Archivos encontrados: {file_count}\n")
    
    entries = []

    # Leer tabla de archivos
    for i in range(file_count):
        name_bytes = f.read(32)
        name = name_bytes.split(b'\x00')[0].decode("shift-jis")
        offset = struct.unpack("<I", f.read(4))[0]
        size = struct.unpack("<I", f.read(4))[0]
        crc = struct.unpack("<I", f.read(4))[0]

        entries.append((name, offset, size, crc))

        print(f"{i+1}: {name} | Offset: {offset} | Size: {size} | CRC: {hex(crc)}")

    # Extraer archivos
    for name, offset, size, crc in entries:
        f.seek(offset)
        data = f.read(size)

        # Comprobar CRC
        calc_crc = zlib.crc32(data) & 0xffffffff
        if calc_crc != crc:
            print(f"⚠️  CRC mismatch en {name}: esperado {hex(crc)}, calculado {hex(calc_crc)}")
        else:
            print(f"✅ CRC correcto en {name}")

        # Guardar archivo
        out_path = os.path.join(output_dir, name)
        with open(out_path, "wb") as out_file:
            out_file.write(data)

print("\nExtracción completada ✔")
