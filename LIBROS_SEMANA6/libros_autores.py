import json
    
@staticmethod
def guardar_autores(autor):
    datos_autor = {
        "nombre":autor.nombre,
        "edad": autor.edad,
        "nacionalidad": autor.nacionalidad
    }
    try:
        with open("autores.json", "r", encoding="utf-8") as archivo:
            autores_existentes = json.load(archivo)
    except FileNotFoundError:
           autores_existentes = []

    autores_existentes.append(datos_autor)

    with open("autores.json", "w", encoding="utf-8") as archivo:
        json.dump(autores_existentes, archivo, indent=4)
    
    
    
@staticmethod
def mostrar_autores():
    try:
        with open("autores.json", "r", encoding="utf-8") as archivo:
            autores = json.load(archivo)
            print("\n📚 Autores registrados:")
            for autor in autores:
             print(f"👤 Nombre: {autor['nombre']} | Edad: {autor['edad']} | Nacionalidad: {autor['nacionalidad']}")
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo 'autores.json'. Aún no hay autores guardados.")


@staticmethod
def guardar_libro_json(libro):
    datos_libro = {
        "titulo": libro.titulo,
        "anio_publicacion": libro.anio_publicacion
    }
    try:
        with open("libros.json", "r", encoding="utf-8") as archivo:
                libros_existentes = json.load(archivo)
    except FileNotFoundError:
        libros_existentes = []

    libros_existentes.append(datos_libro)

    with open("libros.json", "w", encoding="utf-8") as archivo:
        json.dump(libros_existentes, archivo, indent=4)
    
    
@staticmethod
def mostrar_libros_json():
    try:
        with open("libros.json", "r", encoding="utf-8") as archivo:
            libros = json.load(archivo)
            print("\n📚 Libros guardados:")
            for libro in libros:
                print(f"📖 Título: {libro['titulo']} | Año: {libro['anio_publicacion']}")
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo 'libros.json'. Aún no hay libros guardados.")
