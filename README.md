# 🎮 Kamigami no Asobi PSP – Traducción al Español 🇪🇸
<img src="https://entresabanasyalmohadas.com/wp-content/uploads/2014/06/aso.gif" width="100%"/>

![Estado](https://img.shields.io/badge/Estado-Traducción%20En%20progreso-yellow)
![Idioma](https://img.shields.io/badge/Idioma-Japonés%20→%20Español-red)
![Plataforma](https://img.shields.io/badge/Plataforma-PSP-blue)
![Python](https://img.shields.io/badge/Script-Python-darkblue)
![Licencia](https://img.shields.io/badge/Licencia-FanProject%20💖-lightgrey)
![Owzi](https://img.shields.io/badge/Autora-Owzi%20-pink)

---

## 🌸 Acerca del juego

**Kamigami no Asobi** es un juego de aventuras y romance en PSP donde conocerás a diversos dioses de distintas mitologías.  
Originalmente lanzado únicamente en japonés, este proyecto permite disfrutar la historia en español, manteniendo la esencia del juego.  

---

## 🛠️ Objetivo del proyecto

- Traducir todos los textos del juego del japonés al español.  
- Mantener la integridad de los archivos originales del juego.  
- Facilitar que otros fans puedan jugar sin necesidad de conocer japonés.  

---

## 📂 Estructura del repositorio

El proyecto está organizado por sistemas del juego y módulos de trabajo:

- `/Dialogos` → Sistema principal de extracción, edición y recompilación de los archivos `DATA01.dat` (diálogos y selectores).
  - Conversión `.dat ↔ .txt`
  - Pruebas de formato japonés
  - Repack del contenedor DATA01
  - Archivos originales y pruebas separadas

- `/Start` → Sistema completo de extracción y repack de `START.DAT`.
  - Análisis de fuentes (`.fnt`, `.ftd`, `.txp`)
  - Conversión de fuentes a PNG
  - Tablas Shift-JIS (`jis2ucs.bin`, `ucs2jis.bin`)
  - Sistema de pruebas sin modificar originales

- `/System` → Análisis y extracción de `SYSTEM.DAT`.
  - Extracción del contenedor principal
  - Análisis del archivo comprimido `start.lzs`
  - Scripts para inspección de estructura LZS
  - Carpeta de originales intactos

- `fnt(sin_comprobar).py` → Script experimental relacionado con fuentes

- `/README.md` → Documento principal del proyecto

---

### 📦 Tipos de archivos del juego

**DAT / DID**  
Archivos de datos del juego que contienen diálogos, estructura narrativa y selectores.

**TXP / TX2**  
Archivos gráficos (texturas, ventanas, iconos, fuentes gráficas).

**FNT / FTD**  
Definición estructural de fuentes del juego.

**LZS**  
Archivos comprimidos internos (ej: `start.lzs` dentro de `SYSTEM.DAT`).

**BIN (jis2ucs / ucs2jis)**  
Tablas de conversión de caracteres (Shift-JIS ↔ UCS).

**Scripts (Python)**  
Herramientas propias para:
- Extraer contenedores
- Convertir texto
- Reempaquetar DAT
- Analizar estructuras internas 

---

## 📈 Actualizaciones y progreso de la traducción

**Estado actual:** Extracción de archivos y prueba de modificación completada ✅  

- ✅ Archivos de diálogo extraídos (`DATA01.dat` y otros)  
- ✅ Modificación de los archivos posible  
- ✅ El juego acepta y corre los archivos editados  
- ⚠️ Limitación: Actualmente **no soporta caracteres españoles (solo Shift-JIS)**  

### Barra de progreso aproximada de la traducción

| Tarea | Progreso |
|-------|---------|
| ✅ Extracción de archivos | ██████████ 100% |
| ✅ Modificación de archivos | ██████████ 100% |
| 📝 Soporte de caracteres españoles | ████░░░░░░ 40% |
| ⚠️ Traducción de diálogos | ░░░░░░░░░░ 0% |
| ⚠️ Pruebas y correcciones | ░░░░░░░░░░ 0% |

> Esta barra se irá actualizando a medida que avancemos con la traducción y la adaptación completa del juego.

---

<img src="https://entresabanasyalmohadas.com/wp-content/uploads/2014/06/asobi.gif" width="100%"/>
