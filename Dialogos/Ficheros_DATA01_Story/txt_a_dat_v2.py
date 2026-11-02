#!/usr/bin/env python3
"""
txt_a_dat_v2.py - Inserta el TXT traducido en 01_Story.dat (sobrescribiendo en el sitio).

Uso:
  python txt_a_dat_v2.py --modo half              # ASCII normal (1 byte/letra, letras pequeñas)
  python txt_a_dat_v2.py --modo full              # ancho completo (como ahora, letras grandes)
  python txt_a_dat_v2.py --modo half --prueba 5   # solo parchea las 5 primeras líneas (test rápido)
  python txt_a_dat_v2.py --solo-informe           # no escribe nada, solo cuenta desbordes

Cambios respecto a tu script:
  * Modo half/full seleccionable.
  * Informe de líneas que NO caben (en vez de truncarlas en silencio).
  * Las líneas que no caben se dejan con el texto ORIGINAL japonés, no cortadas a la mitad
    (cortar a mitad puede partir un carácter de 2 bytes y romper el script).
  * Reconoce tus acentos escritos como  i'  a'  e'  o'  u'  n'  y los pasa a letras simples.
"""
import re, sys, argparse

ACENTOS = {'á':'a','é':'e','í':'i','ó':'o','ú':'u','Á':'A','É':'E','Í':'I','Ó':'O','Ú':'U',
           'ñ':'n','Ñ':'N','ü':'u','Ü':'U','¿':'','¡':''}

def limpiar(t):
    for k, v in ACENTOS.items():
        t = t.replace(k, v)
    # tus marcas manuales: vocal/n + apóstrofo (i' a' e' o' u' n')
    t = re.sub(r"([aeiouAEIOUnN])'", r"\1", t)
    return t

def a_ancho_completo(t):
    out = []
    for c in t:
        o = ord(c)
        if c == ' ':            out.append('\u3000')
        elif 0x21 <= o <= 0x7E: out.append(chr(o + 0xFEE0))
        else:                   out.append(c)
    return ''.join(out)

def codificar(texto, modo):
    texto = limpiar(texto)
    if modo == 'full':
        texto = a_ancho_completo(texto)
    return texto.encode('shift_jis', errors='replace')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--modo', choices=['half', 'full'], default='half')
    ap.add_argument('--dat', default='01_Story.dat')
    ap.add_argument('--txt', default='01_Story_esp.txt')
    ap.add_argument('--out', default='01_Story_new.dat')
    ap.add_argument('--prueba', type=int, default=0, help='parchear solo las N primeras líneas')
    ap.add_argument('--solo-informe', action='store_true')
    a = ap.parse_args()

    data = bytearray(open(a.dat, 'rb').read())
    lines = open(a.txt, encoding='utf-8').read().splitlines()

    total = cabe = nocabe = sin_traducir = 0
    peor = []
    parcheadas = []
    for ln in lines:
        m = re.match(r"Offset 0x([0-9A-Fa-f]+): (.*)", ln)
        if not m:
            continue
        off = int(m.group(1), 16)
        # en el .dat cifrado (XOR 0xFF) el fin de cadena es el primer 0xFF
        end = data.find(b'\xff', off)
        if end == -1:
            continue
        disponible = end - off          # bytes de texto sin contar el terminador
        nuevo = codificar(m.group(2), a.modo)
        actual = bytes(b ^ 0xFF for b in data[off:end])
        if nuevo == actual:
            sin_traducir += 1           # la línea sigue igual que el original (japonés)
            continue
        total += 1
        if len(nuevo) <= disponible:
            cabe += 1
            if a.solo_informe or (a.prueba and len(parcheadas) >= a.prueba):
                continue
            blob = nuevo + b'\x00' * (disponible - len(nuevo))
            data[off:off + disponible] = bytes(b ^ 0xFF for b in blob)
            parcheadas.append((hex(off), m.group(2)))
        else:
            nocabe += 1
            peor.append((len(nuevo) - disponible, hex(off), m.group(2)[:50]))

    print(f"Modo: {a.modo} | sin traducir (japones): {sin_traducir} | traducidas: {total} | caben: {cabe} | NO caben: {nocabe}")
    for exceso, off, t in sorted(peor, reverse=True)[:10]:
        print(f"   +{exceso} bytes de mas en {off}: {t}...")
    if parcheadas:
        print("Lineas parcheadas (buscalas en el juego):")
        for off, t in parcheadas[:15]:
            print("  ", off, t[:60])
    if not a.solo_informe:
        open(a.out, 'wb').write(data)
        print("Escrito:", a.out)

if __name__ == '__main__':
    main()