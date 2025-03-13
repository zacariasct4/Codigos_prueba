class Libro():
    
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print("Libro prestado con éxito")
        else:
            print("El libro ya está prestado")
            
    def devolver(self):
        if self.disponible:
            print("El libro ya estaba disponible")
        else:
            self.disponible = True
            print("Libro devuelto con éxito")

    def mostrar(self):
        estado = "Sí" if self.disponible is True else "No"
        print(f"{self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponible: {estado}")

    def buscar(self, isbn):
        if self.isbn == isbn:
            self.mostrar()

# Se decide crear otra clase para poder crear una lista que almacene cada uno de los libros introducidos en una clase
class Biblioteca():

    def __init__(self, libros: list):
        self.libros = libros

    # Se crea el método agregar en una clase diferente a Libro ya que se considera que dicho método según
    # las normas sería exactamente igual que el método __init__ de Libro. 
    def agregar(self, titulo: str, autor: str, isbn: str):
        nuevo_libro = Libro(titulo, autor, isbn) # utiliza la clase Libro para crear cada libro que se añade a la lista de la clase Biblioteca
        self.libros.append(nuevo_libro)
        print("Libro agregado con éxito")


opcion = 0
biblioteca = Biblioteca([])

print("Bienvenido al Sistema de Gestión de Biblioteca")
print("1. Agregar libro\n"
    "2. Prestar libro\n"
    "3. Devolver libro\n"
    "4. Mostrar libros\n"
    "5. Buscar\n"
    "6. Salir")

# Se utiliza un bucle while que se rompe con un break cuando opcion = 6
while True: 

    opcion = int(input("Elige una opción:"))

    # agregar: Pide los atributos del libro y lo añade a la lista biblioteca
    if opcion == 1:
        titulo = input("Título:")
        autor = input("Autor:")
        isbn = input("ISBN:")
        biblioteca.agregar(titulo, autor, isbn)

    # prestar: Pide el ISBN del libro y comprueba si está en la lista de libros de biblioteca. Si está, ejecuta prestar y lo pone como no disponible
    # o te dice que ya está prestado. Si no hay ningún libro con ese ISBN te dice que no cuentan con el libro actualmente
    elif opcion == 2: 
        isbn = input("Ingresa el ISBN:")
        for libro in biblioteca.libros:
            if libro.isbn == isbn:
                libro.prestar()
                break
        if libro.isbn != isbn:
            print("No contamos con el libro con ISBN: " + isbn + " en estos momentos. Disculpe las molestias")

    # devolver: Pide el ISBN del libro y comprueba si está en la lista de libros de biblioteca. Si está, ejecuta devolver y lo pone como disponible 
    # o te dice que ya estaba en la biblioteca. Si no hay ningún libro con ese ISBN te dice que no cuentan con el libro actualmente
    elif opcion == 3: 
        isbn = input("Ingresa el ISBN:")
        for libro in biblioteca.libros:
            if libro.isbn == isbn:
                libro.devolver()
                break
        if libro.isbn != isbn:
            print("No contamos con el libro con ISBN: " + isbn + " en estos momentos. Si quiere agregarlo elija opción 1")

    # mostrar: Muestra todos los libros con todos sus atributos recorriendo la lista "biblioteca" con un bucle for
    elif opcion == 4:
        for libro in biblioteca.libros:
            libro.mostrar()

    # buscar: Busca el libro con el ISBN introducido y muestra todos sus atributos siguiendo el método de "Libro" "mostrar". 
    # Si no está el libro en la biblioteca, se recomienda agregarlo
    elif opcion == 5:
        isbn = input("Ingresa el ISBN:")
        for libro in biblioteca.libros:
            libro.buscar(isbn)
        if libro.isbn != isbn:
            print("No contamos con el libro con ISBN: " + isbn + " en estos momentos. Si quiere agregarlo elija opción 1")

    # Opción para romper el bucle while y salir del programa
    elif opcion == 6:
        print("Saliendo del programa")
        break
    
    # Cualquier opción diferente de las comentadas te devolverá a la elección de la opción
    else:
        print("Ha introducido una opción invalida. Inténtelo de nuevo")
        

