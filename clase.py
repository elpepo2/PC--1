'''
Problema N°1 19/09/24
'''
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.distancia_recorrida = 0
    
    def caminar (self):
        self.distancia_recorrida += 2

    
    

class Atleta(Persona):
    def __init__(self, nombre):
        super().__init__(nombre) 
        self.calorías_consumidas = 0
    def entrenar(self, distancia = 10):
        self.distancia_recorrida += distancia
        self.calorías_consumidas += distancia * 500
    
    def competir(self, distancia = 20):
        self.distancia_recorrida += distancia
        self.calorías_consumidas += distancia * 750





        





 













 

