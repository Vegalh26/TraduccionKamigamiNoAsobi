input_file = "Ajustes/extracted/start.lzs"

with open(input_file, "rb") as f:
    data = f.read()

keywords = [b".dat", b".txp", b".fnt"]

for keyword in keywords:
    pos = 0
    while True:
        index = data.find(keyword, pos)
        if index == -1:
            break

        print("Encontrado", keyword.decode(), "en offset", hex(index))

        # Mostrar 16 bytes antes
        start = max(0, index - 16)
        snippet = data[start:index + 16]
        print("Contexto:", snippet.hex())
        print("-" * 40)

        pos = index + 1
