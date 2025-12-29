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

 
def crear_post(titulo, nombre_imagen, descripcion, categorias='fotografia', fecha_programada=None, hora_programada=None, ubicacion='', pelicula='', camara='', excerpt=''):
    if fecha_programada and hora_programada:
        fecha_post = fecha_programada
        hora_post = hora_programada
    else:
        fecha_post = datetime.datetime.now().strftime(DATE_FORMAT)
        hora_post = "12:00:00"
    
    nombre_archivo = f"{fecha_post}-{titulo.lower().replace(' ', '-')}.markdown"
    ruta_post = os.path.join(POSTS_DIR, nombre_archivo)
    ruta_imagen = os.path.join(IMAGES_DIR, nombre_imagen)

    # Front matter con todos los campos para SEO y pie de foto
    front_matter = f"""---
layout: post
title: "{titulo}"
date: {fecha_post} {hora_post} -0300
categories: {categorias}
thumbnail: "{nombre_imagen}"""
    
    # Agregar campos opcionales solo si tienen valor
    if ubicacion:
        front_matter += f"\nlocation: \"{ubicacion}\""
    if pelicula:
        front_matter += f"\nfilm: \"{pelicula}\""
    if camara:
        front_matter += f"\ncamera: \"{camara}\""
    if excerpt:
        front_matter += f"\nexcerpt: \"{excerpt}\""
    
    # Agregar image para redes sociales
    front_matter += f"\nimage: /assets/imagenes/{nombre_imagen}"
    front_matter += f"""\n---

<img src="{{{{ site.baseurl }}}}/assets/imagenes/{{{{ page.thumbnail | uri_escape }}}}" alt="{titulo}" style="max-width: 100%; border: 1px solid #ddd; margin-bottom: 18px;" />

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
    
    # Campos para pie de foto y SEO
    print("\n--- Información adicional (opcional, presiona Enter para omitir) ---")
    ubicacion = input("   Ubicación (ej: Tres Arroyos): ").strip()
    pelicula = input("   Película utilizada (ej: Ektar 100): ").strip()
    camara = input("   Cámara (ej: OM10): ").strip()
    excerpt = input("   Descripción para SEO/redes (40-60 palabras): ").strip()
    
    # Programar fecha y hora
    programar = input("\n5. ¿Quieres programar la publicación para otra fecha? (s/n, Enter=no): ").strip().lower()
    fecha_programada = None
    hora_programada = None
    
    if programar == 's':
        while True:
            fecha_input = input("   Ingresa la fecha (DD/MM/YYYY): ").strip()
            try:
                fecha_obj = datetime.datetime.strptime(fecha_input, "%d/%m/%Y")
                fecha_programada = fecha_obj.strftime(DATE_FORMAT)
                break
            except ValueError:
                print("   Formato de fecha incorrecto. Intenta de nuevo.")
        
        while True:
            hora_input = input("   Ingresa la hora (HH:MM, formato 24h): ").strip()
            try:
                hora_obj = datetime.datetime.strptime(hora_input, "%H:%M")
                hora_programada = hora_obj.strftime("%H:%M:00")
                break
            except ValueError:
                print("   Formato de hora incorrecto. Intenta de nuevo.")
        
        print(f"\n   Post programado para: {fecha_input} a las {hora_input}")
    else:
        print("\n   Publicando con fecha y hora actual.")

    print("\nCopiando imagen...")
    nombre_imagen = os.path.basename(ruta_imagen_origen)
    agregar_imagen(ruta_imagen_origen, nombre_imagen)

    print("\nCreando post...")
    crear_post(titulo, nombre_imagen, descripcion, categoria, fecha_programada, hora_programada, ubicacion, pelicula, camara, excerpt)

    print("\nSubiendo cambios a GitHub...")
    git_push(f"Nuevo post: {titulo}")

    print("\n¡Listo! El post y la imagen han sido publicados. Revisa tu blog online en unos minutos.")
