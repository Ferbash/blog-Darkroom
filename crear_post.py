import tkinter as tk
from tkinter import filedialog
import os
import sys
import datetime
import subprocess

# Configuración
POSTS_DIR = os.path.join(os.getcwd(), '_posts')
IMAGES_DIR = os.path.join(os.getcwd(), 'assets', 'imagenes')
DATE_FORMAT = '%Y-%m-%d'

 
def crear_post(titulo, nombre_imagen, descripcion, categorias='fotografia'):
    hoy = datetime.datetime.now().strftime(DATE_FORMAT)
    nombre_archivo = f"{hoy}-{titulo.lower().replace(' ', '-')}.markdown"
    ruta_post = os.path.join(POSTS_DIR, nombre_archivo)
    ruta_imagen = os.path.join(IMAGES_DIR, nombre_imagen)

    # Solo miniatura y campos requeridos, sin zoom ni scripts
    front_matter = f"""---
layout: post
title: "{titulo}"
date: {hoy} 12:00:00 -0300
categories: {categorias}
thumbnail: "{nombre_imagen}"
---

{descripcion}
"""
    with open(ruta_post, 'w', encoding='utf-8') as f:
        f.write(front_matter)
    print(f"Post creado: {ruta_post}")
    return ruta_post

def agregar_imagen(origen, nombre_destino):
    destino = os.path.join(IMAGES_DIR, nombre_destino)
    os.makedirs(IMAGES_DIR, exist_ok=True)
    with open(origen, 'rb') as src, open(destino, 'wb') as dst:
        dst.write(src.read())
    print(f"Imagen copiada a: {destino}")
    return destino

def git_push(mensaje):
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', mensaje])
    subprocess.run(['git', 'push', 'origin', 'main'])
    print("Cambios subidos a GitHub.")

if __name__ == "__main__":
    print("=== Asistente para crear un nuevo post fotográfico ===\n")
    titulo = input("1. Escribe el título del post: ").strip()
    ruta_imagen_origen = input("2. Escribe la ruta completa de la imagen (ej: C:/Users/Bassi/Pictures/mi-foto.jpg) o presiona Enter para buscar: ").strip()
    if not ruta_imagen_origen:
        print("Abriendo selector de archivos...")
        root = tk.Tk()
        root.withdraw()
        ruta_imagen_origen = filedialog.askopenfilename(title="Selecciona la imagen", filetypes=[("Imágenes", "*.jpg *.jpeg *.png *.gif *.bmp")])
        if not ruta_imagen_origen:
            print("No se seleccionó ninguna imagen. Saliendo.")
            sys.exit(1)
    # Limpiar comillas dobles o simples si las hay
    ruta_imagen_origen = ruta_imagen_origen.strip('"').strip("'")
    descripcion = input("3. Escribe una breve descripción para el post: ").strip()
    categoria = input("4. Escribe la categoría (o presiona Enter para 'fotografia'): ").strip() or 'fotografia'

    print("\nCopiando imagen...")
    nombre_imagen = os.path.basename(ruta_imagen_origen)
    agregar_imagen(ruta_imagen_origen, nombre_imagen)

    print("\nCreando post...")
    crear_post(titulo, nombre_imagen, descripcion, categoria)

    print("\nSubiendo cambios a GitHub...")
    git_push(f"Nuevo post: {titulo}")

    print("\n¡Listo! El post y la imagen han sido publicados. Revisa tu blog online en unos minutos.")
