# ⚙️ Carpeta System – Sistema SYSTEM.DAT 📦
<img src="https://i.pinimg.com/originals/db/ab/2f/dbab2f3be06e768e77a85f175e577955.gif" width="100%"/>

![Sección](https://img.shields.io/badge/Sección-SYSTEM.DAT-blue)
![Formato](https://img.shields.io/badge/Formato-DAT%20%7C%20LZS-orange)
![Encoding](https://img.shields.io/badge/Encoding-Desconocido-red)
![Scripts](https://img.shields.io/badge/Scripts-Python-darkblue)
![Proyecto](https://img.shields.io/badge/Kamigami%20no%20Asobi-PSP-purple)

---

## 🌸 ¿Qué es esta carpeta?

La carpeta **System** contiene todo el sistema de análisis, extracción y modificación del archivo:
`KamigamiNoAsobi\PSP_GAME\USRDIR\SYSTEM.DAT`  

`SYSTEM.DAT` es un contenedor que incluye:

- Archivos `.dat`
- Archivos `.txp`
- Archivos comprimidos `.lzs` (como `start.lzs`)
- Archivos de texto o diccionario (`dictionary.dat`)
- Posibles assets gráficos (`DB_tex.txp`, `head05.txp`)
- Tablas o índices internos

Esta carpeta permite:

- 📦 Extraer el contenido de `SYSTEM.DAT`  
- 🔄 Analizar y reconstruir archivos LZS internos (`start.lzs`)  
- 🧪 Editar y verificar archivos específicos sin corromper el contenedor original  

---

# 📂 Estructura principal

---

# 📜 Scripts principales

### `nispack.py`
Script en Python para extraer `SYSTEM.DAT`.  

Funciones:

- Genera `Extraido_System` con todos los archivos internos  
- Permite inspeccionar archivos `.lzs` internos  
- Mantiene el orden original para repack si es necesario  

---

### Carpeta `Extraer_Start`
Contiene scripts y archivos para analizar y extraer `start.lzs`:

- **extract_lzs.py** → Extrae los archivos de `start.lzs`  
- **scan_extructura_lzs.py** → Revisa si hay archivos dentro de `start.lzs` y su formato  
- **txt_lista_archivos_lzs.py** → Genera un TXT con la lista de archivos dentro de `start.lzs`  
- **start_strings.txt** → Contenido textual extraído de `start.lzs` para análisis  

La subcarpeta `Extraido_Start` contiene los archivos ya extraídos:

- `DB_tex.txp` → Posibles gráficos/texturas  
- `dictionary.dat` → Tabla de textos o diccionario interno  
- `file_unknown` → Archivo sin identificar  
- `head.dat` → Datos internos de cabecera o UI  
- `head05.txp` → Posible textura de interfaz  

---

# 📂 Original_System

Contiene los archivos originales sin modificar:

- `SYSTEM.DAT` → Backup absoluto  
- `Extraido_System` → Archivos extraídos de `SYSTEM.DAT` para referencia  

Sirve como base para repack y pruebas sin riesgo de corromper el original.

---

# ⚙️ Flujo de trabajo

1️⃣ Extraer `SYSTEM.DAT` con `nispack.py`  
2️⃣ Analizar `start.lzs` con `scan_extructura_lzs.py`  
3️⃣ Extraer archivos de `start.lzs` con `extract_lzs.py`  
4️⃣ Generar lista o TXT con `txt_lista_archivos_lzs.py`  
5️⃣ Modificar archivos si es necesario (DB_tex.txp, dictionary.dat, head*.txp)  
6️⃣ Reempaquetar si se requiere actualizar `SYSTEM.DAT`  

---

# ⚠️ Consideraciones importantes

- Mantener siempre el backup de `SYSTEM.DAT`  
- No modificar los archivos originales directamente  
- Los archivos `.lzs` tienen estructura comprimida; modificar sin repack adecuado puede corromperlos  
- Revisar los formatos antes de editar  

---

# 💖 Nota para colaboradores

- Trabajar solo en `Extraido_System` o `Extraer_Start/Extraido_Start`  
- Documentar cualquier cambio en scripts o extracción  
- Mantener la estructura de carpetas para evitar errores de repack  
- Usar `start_strings.txt` para verificar textos y cadenas de juego  

<img src="https://images.squarespace-cdn.com/content/v1/65ab1c1e44d969650c9801c4/30d44a9f-9f07-46ba-9d97-ac2e57eb47b9/animation_file_final.gif?format=750w" width="100%"/>