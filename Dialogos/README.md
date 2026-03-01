# 💬 Carpeta Dialogos – Sistema de extracción y conversión 📂
<img src="https://media.tenor.com/7m9K0FQ0QwEAAAAC/anime-writing.gif" width="100%"/>

![Sección](https://img.shields.io/badge/Sección-Diálogos-purple)
![Formato](https://img.shields.io/badge/Formato-DAT%20%7C%20DID-orange)
![Encoding](https://img.shields.io/badge/Encoding-Shift--JIS-red)
![Scripts](https://img.shields.io/badge/Scripts-Python-darkblue)
![Proyecto](https://img.shields.io/badge/Kamigami%20no%20Asobi-PSP-blue)

---

## 🌸 ¿Qué es esta carpeta?

La carpeta **Dialogos** contiene:

- 📦 Sistema de extracción y repack de `DATA01.dat`
- 🏷️ Sistema de trabajo para `TITLE01.dat`
- 🔄 Conversión `.dat ↔ .txt`
- 🧪 Pruebas de formato japonés (Shift-JIS)
- 🇪🇸 Adaptaciones al español

Los archivos originales del juego se encuentran en:
`KamigamiNoAsobi\PSP_GAME\USRDIR`

Dentro de esa ruta están:

- `DATA01.dat` hasta `DATA12.dat`
- `TITLE01.dat` hasta `TITLE11.dat`

Esta carpeta trabaja principalmente con **DATA01.dat** y **TITLE01.dat**.

---

# 📂 Estructura detallada

---

# 🗂️ Codigos_txt_a_dat_formato_japones

Carpeta estable que respeta el formato japonés original (Shift-JIS).

### Contiene:

- `01_Story.dat`  
  → Archivo DAT original.

- `01_Story_esp.txt`  
  → TXT convertido desde el DAT y editado con contenido en español.

- `dat_a_txt_con_formato.py`  
  → Convierte el DAT a TXT verificando que el formato interno se mantenga correcto.

- `txt_a_dat_esp_formato.py`  
  → Convierte el TXT a DAT transformando caracteres ASCII a JIS para que el juego los acepte.

>📌 Esta es la versión más segura cuando queremos mantener compatibilidad con el motor del juego.

---

# 🧪 Codigos_txt_a_dat_prueba_formato

Carpeta de pruebas y experimentación.

### Contiene:

- `01_Story.dat` → DAT original  
- `01_Story_esp.txt` → TXT editado en español  

### Scripts:

- `dat_a_txt_con_formato.py`  
  → Convierte a TXT comprobando formato JIS.

- `dat_a_txt_sin_formato.py`  
  → Convierte a TXT sin comprobar que se respete el formato JIS.

- `txt_a_dat_esp.py`  
  → Convierte TXT a DAT conservando el formato de caracteres en español.

>📌 Aquí se prueban comportamientos distintos del encoding y validación.

---

# 📦 Extraer_y_Repaquetar_DATA01

Sistema completo para extraer y reconstruir `DATA01.dat`.

---

## 📜 Scripts principales

- `nispack.bms`  
  → Script para QuickBMS que extrae archivos del DAT.

- `nispack.py`  
  → Versión en Python para no depender de QuickBMS.

- `repack.py`  
  → Script para reconstruir `DATA01.dat` y volver a insertarlo en el juego.

---

## 📂 Archivos_originales_DAT01

`DATA01.dat` contiene 3 archivos principales:

- `01_Story.dat`
- `01_Keyword.dat`
- `01_Story.did`

Aquí están los originales sin modificar para referencia segura.

---

## 📂 Pruebas

Carpeta de trabajo.

Aquí:

- Se copian los archivos originales.
- Se reemplaza el `01_Story.dat` editado.
- Se usa `repack.py` para generar un nuevo `DATA01.dat`.
- Ese archivo se prueba dentro del juego.

>⚠️ Nunca se modifican los originales directamente.

---

# 📖 Ficheros_DATA01_Story

Zona aislada para trabajar únicamente con `01_Story`.

Se duplicaron los archivos aquí para no tocar los de otras carpetas.

### Contiene:

- `01_Story.dat` → Copia del original  
- `01_Story_esp.txt` → Copia del archivo traducido  
- `dat_a_txt.py` → Script usado en pruebas  
- `txt_a_dat.py` → Conversión rápida sin modificar formato  

---

## 📂 Subcarpetas

### 🔹 Original

- `01_Story.dat` → Archivo original
- `01_Story.txt` → Archivo original convertido a TXT

---

### 🔹 Esp

- `01_Story_esp.txt`  
  → Archivo que estaba siendo traducido al español.

---

# 🏷️ Ficheros_Title_Selecters

Trabajo específico sobre los archivos de selección de título (`TITLE01.dat`).

---

## Contiene:

- `01_Selecter_prueba.txt`
- `dat_a_txt.py`
- `txt_a_dat.py`

Scripts usados para pruebas rápidas sin alterar formato complejo.

---

## 📂 Subcarpetas

### 🔹 Original

- `01_Selecter.dat`
- `01_Selecter.txt`

---

### 🔹 Eng

- `01_Selecter_eng.txt`  
  → Archivo traducido al inglés para pruebas.

---

### 🔹 Esp

- `01_Selecter_esp.txt`  
  → Archivo traducido al español.

---

# ⚙️ Flujo de trabajo general

1️⃣ Extraer `DATA01.dat`  
2️⃣ Convertir `01_Story.dat → TXT`  
3️⃣ Traducir TXT  
4️⃣ Convertir `TXT → DAT`  
5️⃣ Reemplazar en carpeta `Pruebas`  
6️⃣ Repackear  
7️⃣ Probar en PSP / emulador  

---

# ⚠️ Consideraciones técnicas importantes

- El juego usa **Shift-JIS**
- No soporta caracteres españoles nativos
- Es obligatorio respetar:
  - Longitud de bloques
  - Offsets
  - Bytes de control
  - Estructura interna

>Un error de bytes puede romper completamente el archivo.

---

# 💖 Nota para colaboradores

- No modificar archivos originales
- Trabajar siempre sobre copias
- Documentar cambios en scripts
- Indicar qué versión de conversión se está usando
- No borrar scripts de prueba sin revisar

>Esta carpeta mezcla versión estable + experimentación.

---

<img src="https://media.tenor.com/7m9K0FQ0QEAAAAC/anime-notebook.gif" width="100%"/>