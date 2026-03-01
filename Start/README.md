# 🚀 Carpeta Start – Sistema START.DAT 📦
<img src="https://media.tenor.com/7m9K0FQ0QwEAAAAC/anime-writing.gif" width="100%"/>

![Sección](https://img.shields.io/badge/Sección-START.DAT-blue)
![Formato](https://img.shields.io/badge/Formato-DAT%20%7C%20TXP-orange)
![Encoding](https://img.shields.io/badge/Encoding-Shift--JIS-red)
![Scripts](https://img.shields.io/badge/Scripts-Python-darkblue)
![Proyecto](https://img.shields.io/badge/Kamigami%20no%20Asobi-PSP-purple)

---

## 🌸 ¿Qué es esta carpeta?

La carpeta **Start** contiene todo el sistema de análisis, extracción y modificación del archivo:
`KamigamiNoAsobi\PSP_GAME\USRDIR\START.DAT`

`START.DAT` es un contenedor que incluye:

- Archivos `.dat`
- Archivos `.txp`
- Fuentes (`.fnt`, `.ftd`)
- Imágenes `.png`
- Tablas de conversión (`jis2ucs.bin`, `ucs2jis.bin`)
- Sonido (`.pbd`, `.phd`)

Esta carpeta permite:

- 📦 Extraer su contenido
- 🔄 Reempaquetarlo sin que el juego crashee
- 🧪 Editar archivos específicos (como fuentes o `setable.dat`)
- 🔤 Analizar sistema de caracteres

---

# 📂 Estructura principal

---

## 📜 Scripts principales

### `dat_a_txt.py`

Este script sirve para convertir a texto los archivos `.dat` internos que están dentro de `START.DAT`.

Es decir:

1️⃣ Se extrae `START.DAT`  
2️⃣ Dentro aparecen archivos como `00_Selecter.dat`  
3️⃣ `dat_a_txt.py` permite convertir esos `.dat` internos a `.txt` para poder leer su contenido  

No trabaja sobre el contenedor `START.DAT`, sino sobre los `.dat` que están dentro de él.

Se mantiene para análisis y futuras investigaciones.

---

### `nispack.py`

Script en Python para extraer `START.DAT`.

Además:
- Genera `tabla_archivos.txt`
- Lista el orden exacto de los archivos internos
- Permite verificar offsets y tamaños

Es importante porque el orden afecta al repack.

---

### `repack.py`

Script para reconstruir `START.DAT`.

Características:
- Respeta el orden original
- Evita crashes
- Usa los archivos de la carpeta de repaquetado

---

### `tabla_archivos.txt`

Archivo generado automáticamente por `nispack.py`.

Contiene:
- Orden de archivos
- Offsets
- Tamaños

Sirve como referencia estructural.

---

# 📂 Archivos_editados

Contiene archivos que se están modificando.

Actualmente:

- `setable.dat` → Archivo en pruebas de edición

Aquí se testean cambios antes de repackear.

---

# 📦 Archivos_repaquetar_start

Carpeta de trabajo segura.

Contiene copias de los archivos originales extraídos desde `START.DAT`.

⚠️ Nunca se modifican los originales directamente.

Aquí se:

1️⃣ Copian los archivos originales  
2️⃣ Se reemplaza el archivo editado (ej: `setable.dat`)  
3️⃣ Se ejecuta `repack.py`  
4️⃣ Se genera nuevo `START.DAT`  

Incluye archivos como:

- Fuentes (`fontA.fnt`, `fontA.ftd`)
- Texturas `.txp`
- Iconos `.png`
- Tablas JIS (`jis2ucs.bin`, `ucs2jis.bin`)
- Sonido (`SE00.pbd`, `SE00.phd`)
- Ventanas y UI (`textWindow.txp`, `systemMenu_BG.txp`, etc.)

Es el núcleo del repack.

---

# 🔤 Fonts_en_png

Sistema para trabajar con las fuentes gráficas del juego.

Los `.txp` de fuentes se convierten a `.png` para poder editarlos visualmente.

---

## Contiene:

- `FontA000.png` hasta `FontA202.png`
- Scripts de conversión:
  - `txp_a_png.py`
  - `png_a_txp.py`

⚠️ Estos scripts funcionan correctamente solo con fuentes.

---

## 📂 Subcarpeta Pruebas

### 🔹 Editados
Contiene:
- PNG modificados
- Sus correspondientes `.txp` regenerados

---

### 🔹 Originales
Contiene:
- `.txp` originales
- Usados como base para conversión

Sirve para no perder referencia limpia.

---

# 📂 Original

Archivos principales originales sin modificar:

- `START.DAT`
- `setable.dat`

Se mantienen intactos como respaldo absoluto.

---

# 📂 Start_extraido_original

Contenido extraído del `START.DAT` original.

Sirve como:

- Referencia estructural
- Comparación
- Base para copiar archivos a la carpeta de repack

Contiene todos los archivos internos originales antes de cualquier modificación.

# 🗂 Archivos internos de START.DAT

A continuación se detallan los archivos que contiene `START.DAT`, su posible función y estado de análisis. 
[🔗 Ver archivos internos de START.DAT](#🗂-archivos-internos-de-startdat) 

Se agrupan y enumeran según tipo y prioridad de estudio.

<h2>🗂 Archivos internos de START.DAT</h2>
<p>A continuación se detallan los archivos que contiene <code>START.DAT</code>, su posible función y estado de análisis.</p>

<table style="width:100%; border-collapse: collapse;">
  <thead>
    <tr style="background-color:#f0f0f0;">
      <th style="text-align:center; border: 1px solid #ccc;">#</th>
      <th style="border: 1px solid #ccc;">Archivo</th>
      <th style="border: 1px solid #ccc;">Estado / Descripción</th>
      <th style="border: 1px solid #ccc;">Prioridad</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:center; border: 1px solid #ccc;">1</td>
      <td style="border: 1px solid #ccc;">00_Selecter.dat</td>
      <td style="border: 1px solid #ccc;">
        ✅ Confirmado<br>
        Opciones en el juego (visible)
      </td>
      <td style="border: 1px solid #ccc;">🟢 Alta</td>
    </tr>
    <tr>
      <td style="text-align:center; border: 1px solid #ccc;">2</td>
      <td style="border: 1px solid #ccc;">anm9000.dat</td>
      <td style="border: 1px solid #ccc;">
        ⛔ Sin analizar
      </td>
      <td style="border: 1px solid #ccc;">⚪ Baja</td>
    </tr>
    <tr>
      <td style="text-align:center; border: 1px solid #ccc;">3</td>
      <td style="border: 1px solid #ccc;">BackLog_Window.txp</td>
      <td style="border: 1px solid #ccc;">
        ⛔ Sin analizar
      </td>
      <td style="border: 1px solid #ccc;">🟡 Media</td>
    </tr>
    <tr>
      <td style="text-align:center; border: 1px solid #ccc;">4</td>
      <td style="border: 1px solid #ccc;">ci0090.txp</td>
      <td style="border: 1px solid #ccc;">
        ⛔ Sin analizar
      </td>
      <td style="border: 1px solid #ccc;">⚪ Baja</td>
    </tr>
    <tr>
      <td style="text-align:center; border: 1px solid #ccc;">5</td>
      <td style="border: 1px solid #ccc;">ci0095.txp</td>
      <td style="border: 1px solid #ccc;">
        ⛔ Sin analizar
      </td>
      <td style="border: 1px solid #ccc;">⚪ Baja</td>
    </tr>
    <!-- Continúa con el resto de archivos de la misma manera -->
  </tbody>
</table>

> 🔹 **Leyenda de prioridad:**  
> 🟢 Alta → Confirmado o crítico para visualización / juego  
> 🟡 Media → Importante para pruebas, pero no crítico  
> ⚪ Baja → Solo análisis opcional por ahora  
> 🔴 Crítico → Necesita confirmación urgente  

> Esta tabla se actualizará a medida que vayamos confirmando funciones y formatos de cada archivo.  
> Permite priorizar el trabajo de análisis y edición de `START.DAT`.

---

# ⚙️ Flujo de trabajo

1️⃣ Extraer `START.DAT` con `nispack.py`  
2️⃣ Analizar `tabla_archivos.txt`  
3️⃣ Copiar archivos a `Archivos_repaquetar_start`  
4️⃣ Editar archivo deseado (ej: `setable.dat` o fuentes)  
5️⃣ Ejecutar `repack.py`  
6️⃣ Insertar nuevo `START.DAT` en el juego  
7️⃣ Probar en emulador / PSP  

---

# ⚠️ Consideraciones importantes

- El orden interno del contenedor es crítico
- Cambiar tamaños puede provocar crash
- Las fuentes están ligadas al sistema Shift-JIS
- Las tablas `jis2ucs.bin` y `ucs2jis.bin` controlan conversión de caracteres
- El repack debe respetar offsets y estructura

Un solo byte mal colocado puede romper el arranque del juego.

---

# 💖 Nota para colaboradores

- No modificar archivos en `Original`
- Trabajar siempre en `Archivos_repaquetar_start`
- Mantener el orden de archivos
- Documentar cualquier cambio en fuentes
- No borrar `tabla_archivos.txt`

Esta carpeta controla el arranque visual del juego.

---

<img src="https://media.tenor.com/7m9K0FQ0QEAAAAC/anime-notebook.gif" width="100%"/>