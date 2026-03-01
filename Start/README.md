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
Se agrupan y enumeran según tipo y prioridad de estudio.

| #  | Archivo | Descripción / Estado | Prioridad |
|----|---------|--------------------|-----------|
| 1  | 00_Selecter.dat | Opciones en el juego (visible). ✅ Confirmado | 🟢 Alta |
| 2  | anm9000.dat | ⛔ Sin analizar | ⚪ Baja |
| 3  | BackLog_Window.txp | ⛔ Sin analizar | 🟡 Media |
| 4  | ci0090.txp | ⛔ Sin analizar | ⚪ Baja |
| 5  | ci0095.txp | ⛔ Sin analizar | ⚪ Baja |
| 6  | common.dat | ⛔ Sin analizar | ⚪ Baja |
| 7  | fontA.fnt | ⛔ Posible definición de fuente | 🔴 Alta |
| 8  | fontA.ftd | ⛔ Posible datos complementarios de fuente | 🔴 Alta |
| 9  | FontA000–001.txp | Fuente convertible a PNG. Caracteres latinos. ✅ Confirmado | 🔴 Alta |
| 10 | FontA002.txp | Fuente convertible a PNG. Solo caracteres japoneses. ✅ Confirmado | 🔴 Alta |
| 11 | FontA100–111.txp | Fuente convertible a PNG. Solo caracteres japoneses. ✅ Confirmado | 🔴 Alta |
| 12 | FontA200–202.txp | Fuente convertible a PNG. Solo caracteres japoneses. ✅ Confirmado | 🔴 Alta |
| 13 | ICON0_NEW.png | Icono de casilla de guardado vacío. ❓ Pendiente | 🟡 Media |
| 14 | ICON0_PLAY00–08.png | Iconos de casilla de guardado con personajes (Yui, Apollo, Hades, Tsukito, Takeru, Balder, Loki, Anubis, Thoth). ✅ Confirmado | 🟢 Alta |
| 15 | ICON0_SYSTEM.png | Icono de casilla de guardado sin personaje. ✅ Confirmado | 🟢 Alta |
| 16 | jis2ucs.bin | Sospecha: Shift JIS → UCS. Posible uso en menús / textos en inglés. ❓ Pendiente | 🔴 Alta |
| 17 | loading00–08.txp | Posibles iconos de carga convertibles a PNG. ❓ Pendiente | 🟡 Media |
| 18 | music_icon.txp | ⛔ Sin analizar | ⚪ Baja |
| 19 | music_parts.txp | ⛔ Sin analizar | ⚪ Baja |
| 20 | music_select_01.txp | ⛔ Sin analizar | ⚪ Baja |
| 21 | nowLoading.txp | ⛔ Posible gráfico de pantalla de carga | 🟡 Media |
| 22 | quiz_text.txp | ⛔ Sin analizar | ⚪ Baja |
| 23 | SE00.pbd | ⛔ Posible banco de efectos de sonido | ⚪ Baja |
| 24 | SE00.phd | ⛔ Posible índice de efectos de sonido | ⚪ Baja |
| 25 | selectChoice.txp | ⛔ Sin analizar | 🟡 Media |
| 26 | setable.dat | ⛔ Sin analizar | 🔴 Alta |
| 27 | shortCutDecision.txp | ⛔ Sin analizar | 🟡 Media |
| 28 | start_cancel.txp | ⛔ Sin analizar | 🟡 Media |
| 29 | subMenuWindow.txp | ⛔ Sin analizar | 🟡 Media |
| 30 | sys1.txp | ⛔ Sin analizar | 🟡 Media |
| 31 | systemMenu_BG.txp | ⛔ Sin analizar | 🟡 Media |
| 32 | systemMenu_ChapterIcons.txp | ⛔ Sin analizar | 🟡 Media |
| 33 | systemMenu_Parts.txp | ⛔ Sin analizar | 🟡 Media |
| 34 | sys_name.txp | ⛔ Sin analizar | 🟡 Media |
| 35 | textParts.txp | ⛔ Sin analizar | 🟡 Media |
| 36 | textWindow.txp | ⛔ Sin analizar | 🟡 Media |
| 37 | ThreadOfFatePARTS.txp | ⛔ Sin analizar | 🟡 Media |
| 38 | ucs2jis.bin | Sospecha: UCS → Shift JIS. Posible uso al escribir nombre del jugador. ❓ Pendiente | 🔴 Alta |
| 39 | Wbg0–2.txp | Posibles fondos de ventana (Window Background) | 🟡 Media |
| 40 | Wfm0–2.txp | Posibles marcos de ventana (Window Frame) | 🟡 Media |
| 41 | window_sys3.txp | ⛔ Sin analizar | 🟡 Media |

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