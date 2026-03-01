# 💬 Carpeta Dialogos – Estructura y Función 📂
<img src="https://media.tenor.com/7m9K0FQ0QwEAAAAC/anime-writing.gif" width="100%"/>

![Sección](https://img.shields.io/badge/Sección-Diálogos-purple)
![Formato](https://img.shields.io/badge/Formato-DAT%20%7C%20DID-orange)
![Scripts](https://img.shields.io/badge/Scripts-Python-darkblue)
![Proyecto](https://img.shields.io/badge/Kamigami%20no%20Asobi-PSP-blue)

---

## 🌸 ¿Qué contiene esta carpeta?

La carpeta **Dialogos** reúne todos los scripts, pruebas y archivos relacionados con:

- 📖 Extracción de diálogos del juego  
- 🔄 Conversión `.dat ↔ .txt`  
- 🧪 Pruebas de formato japonés y español  
- 📦 Reempaquetado de `DATA01.dat`  

Es el núcleo del sistema de traducción.

---

# 📂 Estructura detallada

---

## 📜 `exporter_gonzalo_separado.py`

Script experimental para exportar textos desde los archivos originales separando correctamente bloques de diálogo.

Sirve como base para:
- Analizar estructura interna
- Detectar offsets
- Entender formato de control

---

## 🗂️ `Codigos_txt_a_dat_formato_japones`

🔹 Versión estable que respeta el formato japonés original.

Contiene:

- `01_Story.dat` → Archivo original de prueba  
- `01_Story_esp.txt` → Texto traducido al español  
- `dat_a_txt_con_formato.py` → Convierte DAT a TXT manteniendo estructura  
- `txt_a_dat_esp_gonzalo.py` → Reconstruye DAT respetando formato japonés  

👉 Esta carpeta es importante porque mantiene la compatibilidad estructural con el juego.

---

## 🧪 `Codigos_txt_a_dat_prueba_formato`

🔹 Carpeta de experimentación.

Incluye diferentes versiones de scripts para probar:

- Conversión con formato
- Conversión sin formato
- Reconstrucción alternativa
- Pruebas fallidas o temporales (`xd (1).py`)

Se usa para:
- Testear cambios
- Probar hipótesis
- Ver cómo reacciona el juego ante modificaciones

---

## 📦 `Extraer_y_Repaquetar_DATA01`

🔹 Sistema completo para extraer y reconstruir `DATA01.dat`.

Contiene:

### 📜 Scripts principales
- `nispack.bms` → Script QuickBMS original  
- `nispack.py` → Versión Python adaptada  
- `repack.py` → Script para reconstruir el DAT  

### 📂 `Archivos_originales_DAT01`
Archivos originales sin modificar:
- `01_Keyword.dat`
- `01_Story.did`

Sirven como referencia base limpia.

### 📂 `Extraido`
Archivos ya extraídos:
- `01_Keyword.dat`
- `01_Story.did`
- `dat_a_txt.py`
- `txt_a_dat.py`

Aquí se trabaja directamente con los diálogos una vez descomprimidos.

---

## 📖 `Ficheros_DATA01_Story`

Trabajo específico sobre `01_Story`.

Contiene:

- `dat_a_txt.py`
- `txt_a_dat.py`
- `01_Story.dat`
- `01_Story_esp.txt`

### 📂 Subcarpetas

🔹 `Original`
- Archivo original en DAT
- Versión TXT sin traducir

🔹 `Esp`
- Archivo traducido
- Versiones reconstruidas en español

Es la carpeta más estable para pruebas funcionales.

---

## 🏷️ `Ficheros_Title_Selecters`

Trabajo sobre selectores de menú / títulos.

Incluye:

- `dat_a_txt.py`
- `txt_a_dat.py`
- `01_Selecter_prueba.txt`
- `01_Selecter_esp.dat`

### 📂 Subcarpetas

🔹 `Original` → Archivos base  
🔹 `Eng` → Versión en inglés (referencia)  
🔹 `Esp` → Versión en español  

Sirve para:
- Probar textos cortos
- Ver cómo reacciona el juego ante caracteres modificados
- Testear compatibilidad de encoding

---

# ⚙️ Flujo de trabajo recomendado

1️⃣ Extraer `DATA01.dat`  
2️⃣ Convertir `.dat → .txt`  
3️⃣ Traducir el `.txt`  
4️⃣ Reconstruir `.txt → .dat`  
5️⃣ Reempaquetar  
6️⃣ Probar en emulador / PSP  

---

# ⚠️ Consideraciones importantes

- El juego trabaja en **Shift-JIS**
- No soporta directamente caracteres españoles
- Es fundamental respetar:
  - Longitud de bloques
  - Offsets
  - Bytes de control

Modificar mal un bloque puede romper el archivo completo.

---

# 💖 Nota para colaboradores

Si vas a tocar algo:

- Trabaja siempre sobre copia  
- Documenta cambios  
- No borres scripts de prueba sin revisar  
- Indica qué versión del script estás usando  

Esta carpeta es experimental y evoluciona constantemente.

---

<img src="https://media.tenor.com/7m9K0FQ0QEAAAAC/anime-notebook.gif" width="100%"/>