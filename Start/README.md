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

<table>
  <thead>
    <tr>
      <th>#</th>
      <th>Estado</th>
      <th>Archivo</th>
      <th>Descripción</th>
      <th>Prioridad</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><center>1</center></td><td><center>✅</center></td><td>00_Selecter.dat</td><td>Opciones en el juego (visible)</td><td><center>🟢</center></td></tr>
    <tr><td><center>2</center></td><td><center>⛔</center></td><td>anm9000.dat</td><td></td><td><center>⚪</center></td></tr>
    <tr><td><center>3</center></td><td><center>⛔</center></td><td>BackLog_Window.txp</td><td></td><td><center>🟡</center></td></tr>
    <tr><td><center>4</center></td><td><center>⛔</center></td><td>ci0090.txp</td><td></td><td><center>⚪</center></td></tr>
    <tr><td><center>5</center></td><td><center>⛔</center></td><td>ci0095.txp</td><td></td><td><center>⚪</center></td></tr>
    <tr><td><center>6</center></td><td><center>⛔</center></td><td>common.dat</td><td></td><td><center>⚪</center></td></tr>
    <tr><td><center>7</center></td><td><center>⛔</center></td><td>fontA.fnt</td><td>Posible definición de fuente</td><td><center>🔴</center></td></tr>
    <tr><td><center>8</center></td><td><center>⛔</center></td><td>fontA.ftd</td><td>Posible datos complementarios de fuente</td><td><center>🔴</center></td></tr>
    <tr><td><center>9</center></td><td><center>✅</center></td><td>FontA000–001.txp</td><td>Fuente convertible a PNG. Caracteres latinos</td><td><center>🔴</center></td></tr>
    <tr><td><center>10</center></td><td><center>✅</center></td><td>FontA002.txp</td><td>Fuente convertible a PNG. Solo caracteres japoneses</td><td><center>🔴</center></td></tr>
    <tr><td><center>11</center></td><td><center>✅</center></td><td>FontA100–111.txp</td><td>Fuente convertible a PNG. Solo caracteres japoneses</td><td><center>🔴</center></td></tr>
    <tr><td><center>12</center></td><td><center>✅</center></td><td>FontA200–202.txp</td><td>Fuente convertible a PNG. Solo caracteres japoneses</td><td><center>🔴</center></td></tr>
    <tr><td><center>13</center></td><td><center>❓</center></td><td>ICON0_NEW.png</td><td>Icono de casilla de guardado vacío</td><td><center>🟡</center></td></tr>
    <tr><td><center>14</center></td><td><center>✅</center></td><td>ICON0_PLAY00–08.png</td><td>Iconos de casilla de guardado con personajes (Yui, Apollo, Hades, Tsukito, Takeru, Balder, Loki, Anubis, Thoth)</td><td><center>🟢</center></td></tr>
    <tr><td><center>15</center></td><td><center>✅</center></td><td>ICON0_SYSTEM.png</td><td>Icono de casilla de guardado sin personaje</td><td><center>🟢</center></td></tr>
    <tr><td><center>16</center></td><td><center>❓</center></td><td>jis2ucs.bin</td><td>Sospecha: Shift JIS → UCS. Posible uso en menús / textos en inglés</td><td><center>🔴</center></td></tr>
    <tr><td><center>17</center></td><td><center>❓</center></td><td>loading00–08.txp</td><td>Posibles iconos de carga convertibles a PNG</td><td><center>🟡</center></td></tr>
    <tr><td><center>18</center></td><td><center>⛔</center></td><td>music_icon.txp</td><td></td><td><center>⚪</center></td></tr>
    <tr><td><center>19</center></td><td><center>⛔</center></td><td>music_parts.txp</td><td></td><td><center>⚪</center></td></tr>
    <tr><td><center>20</center></td><td><center>⛔</center></td><td>music_select_01.txp</td><td></td><td><center>⚪</center></td></tr>
    <tr><td><center>21</center></td><td><center>⛔</center></td><td>nowLoading.txp</td><td>Posible gráfico de pantalla de carga</td><td><center>🟡</center></td></tr>
    <tr><td><center>22</center></td><td><center>⛔</center></td><td>quiz_text.txp</td><td></td><td><center>⚪</center></td></tr>
    <tr><td><center>23</center></td><td><center>⛔</center></td><td>SE00.pbd</td><td>Posible banco de efectos de sonido</td><td><center>⚪</center></td></tr>
    <tr><td><center>24</center></td><td><center>⛔</center></td><td>SE00.phd</td><td>Posible índice de efectos de sonido</td><td><center>⚪</center></td></tr>
    <tr><td><center>25</center></td><td><center>⛔</center></td><td>selectChoice.txp</td><td></td><td><center>🟡</center></td></tr>
    <tr><td><center>26</center></td><td><center>⛔</center></td><td>setable.dat</td><td></td><td><center>🔴</center></td></tr>
    <tr><td><center>27</center></td><td><center>⛔</center></td><td>shortCutDecision.txp</td><td></td><td><center>🟡</center></td></tr>
    <tr><td><center>28</center></td><td><center>⛔</center></td><td>start_cancel.txp</td><td></td><td><center>🟡</center></td></tr>
    <tr><td><center>29</center></td><td><center>⛔</center></td><td>subMenuWindow.txp</td><td></td><td><center>🟡</center></td></tr>
    <tr><td><center>30</center></td><td><center>⛔</center></td><td>sys1.txp</td><td></td><td><center>🟡</center></td></tr>
    <tr><td><center>31</center></td><td><center>⛔</center></td><td>systemMenu_BG.txp</td><td></td><td><center>🟡</center></td></tr>
    <tr><td><center>32</center></td><td><center>⛔</center></td><td>systemMenu_ChapterIcons.txp</td><td></td><td><center>🟡</center></td></tr>
    <tr><td><center>33</center></td><td><center>⛔</center></td><td>systemMenu_Parts.txp</td><td></td><td><center>🟡</center></td></tr>
    <tr><td><center>34</center></td><td><center>⛔</center></td><td>sys_name.txp</td><td></td><td><center>🟡</center></td></tr>
    <tr><td><center>35</center></td><td><center>⛔</center></td><td>textParts.txp</td><td></td><td><center>🟡</center></td></tr>
    <tr><td><center>36</center></td><td><center>⛔</center></td><td>textWindow.txp</td><td></td><td><center>🟡</center></td></tr>
    <tr><td><center>37</center></td><td><center>⛔</center></td><td>ThreadOfFatePARTS.txp</td><td></td><td><center>🟡</center></td></tr>
    <tr><td><center>38</center></td><td><center>❓</center></td><td>ucs2jis.bin</td><td>Sospecha: UCS → Shift JIS. Posible uso al escribir nombre del jugador</td><td><center>🔴</center></td></tr>
    <tr><td><center>39</center></td><td><center>🟡</center></td><td>Wbg0–2.txp</td><td>Posibles fondos de ventana (Window Background)</td><td><center>🟡</center></td></tr>
    <tr><td><center>40</center></td><td><center>🟡</center></td><td>Wfm0–2.txp</td><td>Posibles marcos de ventana (Window Frame)</td><td><center>🟡</center></td></tr>
    <tr><td><center>41</center></td><td><center>⛔</center></td><td>window_sys3.txp</td><td></td><td><center>🟡</center></td></tr>
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