import re

def insert_story():

    dat_path = "Ficheros_DATA01_Story/01_Story.dat"
    txt_path = "Ficheros_DATA01_Story/01_Story_esp.txt"
    output_path = "Ficheros_DATA01_Story/01_Story_new.dat"

    with open(dat_path, "rb") as f:
        data = bytearray(f.read())

    with open(txt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        match = re.match(r"Offset 0x([0-9A-Fa-f]+): (.*)", line.strip())
        if not match:
            continue

        offset = int(match.group(1), 16)
        text = match.group(2)

        # Codificar igual que el juego
        encoded = text.encode("shift_jis", errors="replace") + b'\xff'
        encrypted = bytes([b ^ 0xFF for b in encoded])

        # Buscar fin del bloque original
        end = data.find(b'\xff', offset)
        if end == -1:
            print(f"No se encontró terminador en {hex(offset)}")
            continue

        original_size = end - offset + 1

        if len(encrypted) > original_size:
            print(f"⚠ Texto demasiado largo en {hex(offset)} "
                  f"({len(encrypted)} > {original_size})")
            continue

        # Escribir nuevo texto
        data[offset:offset+len(encrypted)] = encrypted

        # Padding si sobra espacio
        remaining = original_size - len(encrypted)
        if remaining > 0:
            data[offset+len(encrypted):offset+original_size] = b'\x00' * remaining

    with open(output_path, "wb") as f:
        f.write(data)

    print("Inserción completada sin modificar offsets.")

insert_story()
