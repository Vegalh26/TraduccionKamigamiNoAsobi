#!/usr/bin/env python3
"""
ftd_ajustar_ancho.py - Ajusta los márgenes de glifos en fontA.ftd (START.DAT) para que las
letras de ancho completo ocupen solo lo que miden, en vez de la celda entera de 18 px.

Formato descubierto de fontA.ftd:
  * 4 bytes de cabecera (5F 2D 00 00)
  * luego 2 bytes por glifo: (margen_izquierdo, margen_derecho) dentro de la celda de 18 px
  * Pagina 0 (FontA000): el glifo de la celda N (0-255, de izquierda a derecha y de arriba a abajo)
    es la entrada N-1. Comprobado: 164 de 255 coinciden exactos con los píxeles y el resto
    difiere en 1 px. Los glifos de ancho completo (０１２...) tienen (0,0) = 18 px enteros.

Uso (desde la carpeta Start):
  python ftd_ajustar_ancho.py --celdas 242-255
  -> crea fontA_new.ftd; cópialo como fontA.ftd en Archivos_repaquetar_start y reempaqueta.

IMPORTANTE: solo está verificado para la página 0. Para otras páginas la numeración del .ftd
no es consecutiva (hay que descubrirla). Haz primero la prueba con digitos ０-９ (celdas 242-251).
"""
import argparse
from PIL import Image
import numpy as np

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ftd', default='Archivos_repaquetar_start/fontA.ftd')
    ap.add_argument('--png', default='Fonts_en_png/FontA000.png')
    ap.add_argument('--celdas', default='242-251', help='rango, p.ej. 242-255')
    ap.add_argument('--out', default='fontA_new.ftd')
    ap.add_argument('--margen', type=int, default=1, help='píxeles extra de separación entre letras (por lado)')
    a = ap.parse_args()

    ini, fin = [int(x) for x in a.celdas.split('-')]
    ftd = bytearray(open(a.ftd, 'rb').read())
    alpha = np.array(Image.open(a.png).convert('RGBA'))[:, :, 3]

    for cell in range(ini, fin + 1):
        r, c = divmod(cell, 16)
        cols = np.where(alpha[r*18:(r+1)*18, c*18:(c+1)*18].max(axis=0) > 40)[0]
        if len(cols) == 0:
            continue
        izq = max(0, int(cols.min()) - a.margen)
        der = max(0, 17 - int(cols.max()) - a.margen)
        j = cell - 1
        antes = (ftd[4+2*j], ftd[5+2*j])
        ftd[4+2*j], ftd[5+2*j] = izq, der
        print(f"celda {cell}: {antes} -> {(izq, der)}  (ancho avance {18-izq-der}px)")

    open(a.out, 'wb').write(ftd)
    print("Escrito", a.out)

if __name__ == '__main__':
    main()
