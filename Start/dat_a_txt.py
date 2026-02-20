import struct

file_path = "Start/Archivo_extraido_sart.dat/common.dat"

with open(file_path, "rb") as f:
    data = f.read()

# Cada entrada parece 16 bytes: 4 uint32
entry_size = 16
entries = []

for i in range(0, len(data), entry_size):
    chunk = data[i:i+entry_size]
    if len(chunk) < entry_size:
        continue
    # leer 4 uint32 little endian
    fields = struct.unpack("<4I", chunk)
    entries.append(fields)

# Guardar en TXT legible
with open("common.txt", "w") as f:
    for idx, e in enumerate(entries):
        f.write(f"{idx} | {e}\n")

print(f"{len(entries)} entradas guardadas en common.txt")