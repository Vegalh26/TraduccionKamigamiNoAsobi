import os

input_file = "Ajustes/extracted/start.lzs"
output_dir = "Ajustes/extracted/start_extracted"
os.makedirs(output_dir, exist_ok=True)

keywords = [b".dat", b".txp", b".fnt"]

with open(input_file, "rb") as f:
    data = f.read()

# Buscar todos los nombres
file_entries = []
for keyword in keywords:
    pos = 0
    while True:
        index = data.find(keyword, pos)
        if index == -1:
            break

        # Retroceder hasta el null para obtener el inicio del nombre
        name_start = index
        while name_start > 0 and data[name_start-1] != 0:
            name_start -= 1

        name_bytes = data[name_start:index + len(keyword)]
        try:
            name = name_bytes.decode("shift_jis")
        except:
            name = "file_unknown"

        file_entries.append((name, index))
        pos = index + 1

# Ordenar por offset
file_entries.sort(key=lambda x: x[1])

# Extraer los archivos
for i, (name, start) in enumerate(file_entries):
    end = file_entries[i+1][1] if i+1 < len(file_entries) else len(data)
    file_data = data[start:end]
    out_path = os.path.join(output_dir, name)
    with open(out_path, "wb") as f:
        f.write(file_data)
    print("Extraído:", name)

print("Extracción completada ✔")
