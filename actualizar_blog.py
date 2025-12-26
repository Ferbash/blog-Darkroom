import subprocess

def actualizar_blog():
    print("Actualizando el contenido del blog...")
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Actualización de contenido del blog'])
    subprocess.run(['git', 'push', 'origin', 'main'])
    print("\n¡Listo! Los cambios han sido subidos a GitHub. Revisa tu página online en unos minutos.")

if __name__ == "__main__":
    actualizar_blog()
