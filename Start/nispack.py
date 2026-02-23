import struct
import os
import zlib

# Nombre del DAT que quieres extraer
dat_file = "Start/Original/START.DAT"

# Carpeta donde se guardarán los archivos extraídos
output_dir = "Start/Start_extraido_original"
os.makedirs(output_dir, exist_ok=True)

# Ruta del TXT con la tabla
table_txt_path = os.path.join("Start/tabla_archivos.txt")

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
    print("=== TABLA DE ARCHIVOS ===")

    with open(table_txt_path, "w", encoding="utf-8") as table_file:
        table_file.write("=== TABLA DE ARCHIVOS ===\n")
        table_file.write(f"Total archivos: {file_count}\n\n")
        table_file.write("ID | Nombre | Offset (hex) | Offset (dec) | Size | CRC\n")
        table_file.write("-" * 80 + "\n")

        for i in range(file_count):
            name_bytes = f.read(32)
            name = name_bytes.split(b'\x00')[0].decode("shift-jis")
            offset = struct.unpack("<I", f.read(4))[0]
            size = struct.unpack("<I", f.read(4))[0]
            crc = struct.unpack("<I", f.read(4))[0]

            entries.append((name, offset, size, crc))

            line = f"{i+1:03} | {name} | 0x{offset:08X} | {offset} | {size} | {hex(crc)}"
            
            print(line)
            table_file.write(line + "\n")

    print(f"\n📄 Tabla guardada en: {table_txt_path}")
    print("\n=== INICIANDO EXTRACCIÓN ===")

    # Extraer archivos mostrando el orden
    for index, (name, offset, size, crc) in enumerate(entries, start=1):
        print(f"\n[{index}/{file_count}] Extrayendo: {name}")
        print(f"   Offset: 0x{offset:08X} | Size: {size}")

        f.seek(offset)
        data = f.read(size)

        # Comprobar CRC
        calc_crc = zlib.crc32(data) & 0xffffffff
        if calc_crc != crc:
            print(f"   ⚠️ CRC mismatch: esperado {hex(crc)}, calculado {hex(calc_crc)}")
        else:
            print(f"   ✅ CRC correcto")

        # Guardar archivo
        out_path = os.path.join(output_dir, name)
        with open(out_path, "wb") as out_file:
            out_file.write(data)

        print(f"   ✔ Guardado en: {out_path}")

print("\nExtracción completada ✔")