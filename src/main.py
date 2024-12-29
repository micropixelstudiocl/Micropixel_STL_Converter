import os
import time
import shutil
import trimesh
from tkinter import filedialog, messagebox
import customtkinter as ctk

# Configuración global de CustomTkinter
ctk.set_appearance_mode("dark")  # Tema oscuro
ctk.set_default_color_theme("blue")  # Esquema de colores base


class ObjToStlConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de ventana principal
        self.title("Conversor OBJ a STL - MicropixelCl")
        self.geometry("800x750")
        self.resizable(False, False)
        self.files = []
        self.converted_files = []  # Contendrá las rutas temporales de los archivos convertidos

        # Crear carpeta de descargas en el escritorio
        self.output_folder = os.path.join(os.path.expanduser("~"), "Desktop", "MicropixelCl_Converted")
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        # Copiar ícono de MPCL a la carpeta de salida
        self.icon_path = os.path.join(os.getcwd(), "assets", "MPCL.ico")
        if os.path.exists(self.icon_path):
            shutil.copy(self.icon_path, self.output_folder)

        # Pantalla inicial
        self.init_main_screen()

    def init_main_screen(self):
        """Crea la pantalla de inicio."""
        self.clear_widgets()

        ctk.CTkLabel(self, text="Bienvenidos al conversor de archivos de MicropixelCl",
                     font=("Arial", 24)).pack(pady=40)

        ctk.CTkButton(self, text="Iniciar", command=self.init_upload_screen,
                      corner_radius=10, fg_color="#3498db", hover_color="#2ecc71").pack(pady=20)

    def init_upload_screen(self):
        """Crea la pantalla de subida de archivos."""
        self.clear_widgets()

        ctk.CTkLabel(self, text="Sube tus archivos .OBJ (Máximo 7)", font=("Arial", 20)).pack(pady=20)

        self.file_list_frame = ctk.CTkFrame(self, width=600, height=250, corner_radius=10)
        self.file_list_frame.pack(pady=10)

        ctk.CTkButton(self, text="Cargar archivos", command=self.load_files,
                      corner_radius=10, fg_color="#3498db", hover_color="#2ecc71").pack(pady=10)

        ctk.CTkLabel(self, text="Estado:", font=("Arial", 16)).pack(pady=5)
        self.status_label = ctk.CTkLabel(self, text="Esperando archivos...", font=("Arial", 14))
        self.status_label.pack(pady=5)

        # Botón para iniciar la conversión
        self.convert_button = ctk.CTkButton(self, text="Iniciar Conversión", command=self.start_conversion_screen,
                                            corner_radius=10, fg_color="#2ecc71", hover_color="#27ae60", state="disabled")
        self.convert_button.pack(pady=10)

        ctk.CTkButton(self, text="Volver al inicio", command=self.init_main_screen,
                      corner_radius=10, fg_color="#7f8c8d", hover_color="#95a5a6").pack(pady=10)

    def load_files(self):
        """Carga archivos OBJ y muestra sus nombres con opción de eliminarlos."""
        if len(self.files) >= 7:
            messagebox.showwarning("Límite alcanzado", "Ya has cargado el máximo de 7 archivos.")
            return

        files = filedialog.askopenfilenames(filetypes=[("OBJ Files", "*.obj")])
        if files:
            for file in files:
                if len(self.files) < 7 and file not in self.files:
                    self.files.append(file)

            self.update_file_list()
            self.status_label.configure(text="Archivos cargados correctamente.")
            self.convert_button.configure(state="normal")

    def update_file_list(self):
        """Actualiza la lista de archivos en la interfaz."""
        for widget in self.file_list_frame.winfo_children():
            widget.destroy()

        for index, file in enumerate(self.files):
            frame = ctk.CTkFrame(self.file_list_frame, fg_color="transparent", height=40, corner_radius=5)
            frame.pack(fill="x", pady=5)

            file_label = ctk.CTkLabel(frame, text=os.path.basename(file), font=("Arial", 14), width=480, anchor="w")
            file_label.pack(side="left", padx=10)

            delete_button = ctk.CTkButton(
                frame, text="X", width=30, fg_color="#e74c3c", text_color="white",
                hover_color="#c0392b", command=lambda f=file: self.remove_file(f)
            )
            delete_button.pack(side="right", padx=10)

    def remove_file(self, file):
        """Elimina un archivo de la lista."""
        if file in self.files:
            self.files.remove(file)
            self.update_file_list()

        if not self.files:
            self.convert_button.configure(state="disabled")

    def convert_obj_to_stl(self, file):
        """Convierte un archivo OBJ a STL real y guarda en una carpeta temporal."""
        try:
            # Cargar el archivo OBJ y exportar como STL
            mesh = trimesh.load_mesh(file)
            temp_folder = os.path.join(os.getcwd(), "temp_converted")
            if not os.path.exists(temp_folder):
                os.makedirs(temp_folder)
            stl_file = os.path.join(temp_folder, os.path.basename(file).replace(".obj", ".stl"))
            mesh.export(stl_file, file_type='stl')
            self.converted_files.append(stl_file)
        except Exception as e:
            messagebox.showerror("Error", f"Error al convertir {file}: {e}")

    def start_conversion_screen(self):
        """Muestra la pantalla de barra de progreso y ejecuta la conversión visual."""
        self.clear_widgets()

        ctk.CTkLabel(self, text="Convirtiendo archivos...", font=("Arial", 20)).pack(pady=20)

        progress_var = ctk.IntVar()
        progress_bar = ctk.CTkProgressBar(self, variable=progress_var, width=600)
        progress_bar.pack(pady=10)
        progress_bar.set(0)

        percentage_label = ctk.CTkLabel(self, text="0%", font=("Arial", 16))
        percentage_label.pack(pady=5)

        total_files = len(self.files)
        step = 100 // total_files if total_files > 0 else 100

        for i, file in enumerate(self.files):
            self.convert_obj_to_stl(file)
            progress = (i + 1) * step
            progress_var.set(progress)
            percentage_label.configure(text=f"{int(progress)}%")
            self.update()
            time.sleep(0.9)

        self.init_result_screen()

    def init_result_screen(self):
        """Muestra la pantalla de resultados con opciones de descarga."""
        self.clear_widgets()

        ctk.CTkLabel(self, text="Archivos Convertidos", font=("Arial", 20)).pack(pady=20)

        result_frame = ctk.CTkFrame(self, width=600, height=300, corner_radius=10)
        result_frame.pack(pady=10)

        for file in self.converted_files:
            frame = ctk.CTkFrame(result_frame, fg_color="transparent", height=40, corner_radius=5)
            frame.pack(fill="x", pady=5)

            file_label = ctk.CTkLabel(frame, text=os.path.basename(file), font=("Arial", 14), width=480, anchor="w")
            file_label.pack(side="left", padx=10)

            download_button = ctk.CTkButton(
                frame, text="Descargar", command=lambda f=file: self.download_file(f),
                fg_color="#3498db", hover_color="#2ecc71"
            )
            download_button.pack(side="right", padx=10)

        ctk.CTkButton(self, text="Descargar Todos", command=self.download_all,
                      corner_radius=10, fg_color="#2ecc71", hover_color="#27ae60").pack(pady=10)

        ctk.CTkButton(self, text="Volver al inicio", command=self.init_main_screen,
                      corner_radius=10, fg_color="#7f8c8d", hover_color="#95a5a6").pack(pady=10)

    def download_file(self, file):
        """Descarga un archivo específico a la carpeta de salida."""
        try:
            shutil.copy(file, self.output_folder)
            messagebox.showinfo("Descarga Completa", f"{os.path.basename(file)} se guardó en {self.output_folder}.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo descargar el archivo {file}: {e}")

    def download_all(self):
        """Guarda todos los archivos convertidos en la carpeta de salida."""
        try:
            for file in self.converted_files:
                shutil.copy(file, self.output_folder)
            messagebox.showinfo("Éxito", f"Todos los archivos se guardaron en {self.output_folder}.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar los archivos: {e}")

    def clear_widgets(self):
        """Elimina todos los widgets actuales de la ventana."""
        for widget in self.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    app = ObjToStlConverterApp()
    app.mainloop()
