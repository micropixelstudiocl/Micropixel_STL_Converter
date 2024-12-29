# MicropixelCl Converter

MicropixelCl Converter es una herramienta sencilla para convertir archivos 3D en formato OBJ a STL, ideal para su posterior impresión 3D.

---

## Índice
1. [Descripción](#descripción)
2. [Características](#características)
3. [Requisitos](#requisitos)
4. [Instalación](#instalación)
5. [Uso](#uso)
6. [Contribuciones](#contribuciones)
7. [Licencia](#licencia)
8. [Contacto](#contacto)

---

## Descripción
MicropixelCl Converter facilita la conversión de modelos 3D en formato OBJ a STL con una interfaz amigable y funciones adicionales como:
- Límite de 7 archivos por sesión para una mejor gestión.
- Barra de progreso visual para indicar el estado de la conversión.
- Descarga individual o masiva de los archivos convertidos.
- Generación automática de una carpeta de salida en el escritorio.

Este proyecto está diseñado para aficionados y profesionales que buscan preparar modelos 3D para su impresión con software como **PrusaSlicer** o **Cura**.

---

## Características
- **Soporte para archivos OBJ:** Compatible con modelos complejos.
- **Conversión a STL:** Archivos listos para laminadores.
- **Interfaz intuitiva:** Basada en `CustomTkinter`.
- **Icono personalizado:** Representa a MicropixelCl con un diseño único.
- **Descarga eficiente:** Guardado de los archivos directamente en el escritorio.

---

## Requisitos
- **Sistema Operativo:** Windows 10 o superior.
- **Python:** Versión 3.10 o superior.
- **Librerías necesarias:** 
  ```bash
  pip install -r requirements.txt

  Dependencias incluidas
  - Trimesh
  - CustomTkinter

---

## Instalación
1. **Clonar el repositorio**
      git clone https://github.com/micropixelstudiocl/Micropixel_STL_Converter
2. **Instalar dependencias**
    /Desde la terminal, asegúrate de estar en la carpeta del proyecto y ejecuta/
      pip install -r requirements.txt
3. **Ejecuta el programa**
    python src/main.py  
4. **(opcional) Crear un ejecutable: Si deseas generar un programa instalable**
    pyinstaller --onefile --windowed --icon=assets/MPCL.ico src/main.py --name "MicropixelCl_Converter"

---

## Uso
1. Abrir el programa: Al abrir, verás la pantalla principal con un botón para iniciar la carga de archivos.
2. Subir archivos OBJ:
   - Usa el botón "Cargar archivos" y selecciona hasta 7 archivos OBJ.
   - Los archivos seleccionados aparecerán listados en la pantalla.
3. Iniciar conversión:
    - Haz clic en "Iniciar Conversión".
    - Aparecerá una barra de progreso indicando el estado.
4. Descargar archivos convertidos:
    - Al finalizar la conversión, selecciona "Descargar Todos" o descarga cada archivo individual.

---

## Contribuciones
¡Contribuciones son bienvenidas! Si encuentras un problema o tienes una idea para mejorar, sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una rama con tu mejora:
    git checkout -b mejora-nueva-funcionalidad
3. Realiza los cambios y súbelos:
    git commit -m "Añadida nueva funcionalidad"
    git push origin mejora-nueva-funcionalidad
4. Abre un pull request en el repositorio original.

---

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más información.

---

## Contacto
Si tienes dudas, sugerencias o quieres conocer más sobre MicropixelCl, no dudes en contactarme:
    - 📧 Correo: Micropixelcl@gmail.com
    - 🐙 Github. micropixelstudiocl
