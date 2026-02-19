import os

input_file = "Ajustes/extracted/start.lzs"
output_file = "Ajustes/extracted/start_strings.txt"

MIN_LENGTH = 4  # longitud mínima de string para guardar

with open(input_file, "rb") as f:
    data = f.read()

strings = []
current = bytearray()

i = 0
while i < len(data):
    byte = data[i]

    # Rango típico Shift-JIS
    if (
        0x20 <= byte <= 0x7E or         # ASCII visible
        0x81 <= byte <= 0x9F or
        0xE0 <= byte <= 0xEF
    ):
        current.append(byte)
    else:
        if len(current) >= MIN_LENGTH:
            try:
                decoded = current.decode("shift_jis")
                strings.append(decoded)
            except:
                pass
        current = bytearray()

    i += 1

# Último bloque
if len(current) >= MIN_LENGTH:
    try:
        decoded = current.decode("shift_jis")
        strings.append(decoded)
    except:
        pass

# Guardar resultado
with open(output_file, "w", encoding="utf-8") as f:
    for s in strings:
        f.write(s + "\n")

print("Extracción completada ✔")
print("Strings encontradas:", len(strings))
