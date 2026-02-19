import re
import os


def insertar_historia_espanol():
    ruta_dat = "Codigos_txt_a_dat_prueba_formato/01_Story.dat"
    ruta_txt = "Codigos_txt_a_dat_prueba_formato/01_Story_esp.txt"
    ruta_salida = "Codigos_txt_a_dat_prueba_formato/01_Story_new.dat"

    if not os.path.exists(ruta_dat):
        print("Error: ¡No se encontró el archivo .dat original!")
        return

    with open(ruta_dat, "rb") as f:
        datos = bytearray(f.read())

    with open(ruta_txt, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    for linea in lineas:
        # Buscar patrón: "Offset 0x123: Texto"
        coincidencia = re.match(r"Offset 0x([0-9A-Fa-f]+): (.*)", linea.strip())
        if not coincidencia:
            continue

        offset = int(coincidencia.group(1), 16)
        texto_original = coincidencia.group(2)

        # 🔹 Limpiar caracteres no compatibles con Shift-JIS
        mapa_espanol = {
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
            'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
            'ñ': 'n', 'Ñ': 'N', 'ü': 'u', 'Ü': 'U',
            '¿': '', '¡': ''
        }

        for buscar, reemplazar in mapa_espanol.items():
            texto_original = texto_original.replace(buscar, reemplazar)

        # 1️⃣ Codificar directamente en Shift-JIS (ASCII normal)
        codificado = texto_original.encode("shift_jis", errors="replace") + b'\x00'

        # 2️⃣ Aplicar XOR 0xFF (encriptación del juego)
        encriptado = bytes([b ^ 0xFF for b in codificado])

        # 3️⃣ Buscar terminador original (0xFF)
        fin = datos.find(b'\xff', offset)
        if fin == -1:
            continue

        tamano_original = fin - offset + 1

        # 4️⃣ Comprobar tamaño
        if len(encriptado) > tamano_original:
            print(f"⚠ DEMASIADO LARGO: {hex(offset)} (Necesita {len(encriptado)}, tiene {tamano_original})")
            encriptado = encriptado[:tamano_original - 1] + b'\xff'

        # 5️⃣ Escribir datos
        datos[offset: offset + len(encriptado)] = encriptado

        # 6️⃣ Rellenar si sobra espacio
        restante = tamano_original - len(encriptado)
        if restante > 0:
            datos[offset + len(encriptado): offset + tamano_original] = b'\x00' * restante

    with open(ruta_salida, "wb") as f:
        f.write(datos)

    print("¡Inserción completada usando ASCII normal (half-width)!")


# Ejecutar
insertar_historia_espanol()
