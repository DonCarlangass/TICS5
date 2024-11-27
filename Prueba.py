class animal():

    def __init__(self, raza,nombre, edad):
        self.raza = raza
        self.nombre = nombre
        self.edad = edad

    def caracteristicas(self):
        print("nombre: ", self.nombre)
        print("edad: ", self.edad, " años")

    def comer(self):
        if( self.raza=="perro"):
            print(self.nombre,"es un perro que come 3 veces al día.")
        
        if(self.raza=="gato"):
            print(self.nombre,"es un gato que come 2 veces al día.")

miperrito = animal("perro","Lucky", 2)
miperrito.caracteristicas()
miperrito.comer()
