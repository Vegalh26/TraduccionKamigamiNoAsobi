import re
import os


def a_ancho_completo(texto):
    """
    Convierte caracteres ASCII estándar a caracteres japoneses de ancho completo (Zen-kaku).
    También adapta caracteres españoles a equivalentes compatibles.
    """
    # Mapeo de caracteres españoles a equivalentes básicos
    # (Shift-JIS no soporta bien algunos de ellos)
    mapa_espanol = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ñ': 'n', 'Ñ': 'N', 'ü': 'u', 'Ü': 'U',
        '¿': '', '¡': ''
    }

    for buscar, reemplazar in mapa_espanol.items():
        texto = texto.replace(buscar, reemplazar)

    # Convertir letras/números/símbolos ASCII estándar a ancho completo
    resultado = ""
    for caracter in texto:
        codigo = ord(caracter)

        # Rango ASCII estándar (desde ! hasta ~)
        if 0x0021 <= codigo <= 0x007E:
            resultado += chr(codigo + 0xFEE0)

        elif codigo == 0x0020:  # Espacio normal
            resultado += chr(0x3000)  # Espacio de ancho completo

        else:
            resultado += caracter

    return resultado


def insertar_historia_espanol():
    ruta_dat = "Ficheros_DATA01_Story/01_Story.dat"
    ruta_txt = "Ficheros_DATA01_Story/01_Story_esp.txt"
    ruta_salida = "Ficheros_DATA01_Story/01_Story_new.dat"

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

        # 1. CONVERTIR A ANCHO COMPLETO (para que sea visible en el juego)
        texto_formateado = a_ancho_completo(texto_original)

        # 2. CODIFICAR Y ENCRIPTAR
        # Añadimos \x00 como terminador en texto plano.
        # Al hacer XOR con 0xFF se convierte en 0xFF dentro del archivo.
        codificado = texto_formateado.encode("shift_jis", errors="replace") + b'\x00'
        encriptado = bytes([b ^ 0xFF for b in codificado])

        # 3. CALCULAR ESPACIO (buscar el terminador original en el archivo)
        fin = datos.find(b'\xff', offset)
        if fin == -1:
            continue

        tamano_original = fin - offset + 1

        # 4. COMPROBAR TAMAÑO
        if len(encriptado) > tamano_original:
            print(f"⚠ DEMASIADO LARGO: {hex(offset)} (Necesita {len(encriptado)}, tiene {tamano_original})")

            # Recortar para evitar que el juego se cierre
            encriptado = encriptado[:tamano_original - 1] + b'\xff'

        # 5. ESCRIBIR Y RELLENAR
        datos[offset: offset + len(encriptado)] = encriptado

        restante = tamano_original - len(encriptado)
        if restante > 0:
            # Rellenar con 0x00 (al hacer XOR se convierte en 0xFF en memoria, seguro)
            datos[offset + len(encriptado): offset + tamano_original] = b'\x00' * restante

    with open(ruta_salida, "wb") as f:
        f.write(datos)

    print("¡Inserción completada! Usando caracteres de ancho completo.")


# Ejecutar el proceso
insertar_historia_espanol()