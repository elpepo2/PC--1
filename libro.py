class libro:
    def __init__(self, titulo, autor, anio_de_publicacion, num_de_paginas):
        self.titulo = titulo
        self.autor = autor
        self.anio_de_publicacion = anio_de_publicacion
        self.num_de_paginas = num_de_paginas
    
    def mostrar_info(self):
        print(f"titulo: {self.titulo}")
        print(f"autor: {self.autor}")
        print(f"anio_de_publicacion: {self.anio_de_publicacion}")
        print(f"num_de_paginas: {self.num_de_paginas}")
    

libro1 = libro("Le dedico mi silencio", "Mario Vargas Llosa", 2023, 312)
libro2 = libro("El diario de Greg 1", "Jeff Kinney", 2007, 224)

libros = [libro1 , libro2]

for libro in libros:
    print(f"Titulo: {libro.titulo}, Autor: {libro.autor}, Anio de publicacion: {libro.anio_de_publicacion}, Numero de paginas: {libro.num_de_paginas}")


    





        





 













 

