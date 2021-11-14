
class Usuario:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido #Es para inicializar la clase
    
    def Saludo(self):
        print('Hola mi nombre es,', self.nombre, self.apellido)

class Admin(Usuario):
    def superSaludo(self):
        print('Me llamo,', self.nombre, 'Y soy administrador')









# usuarios = Usuario('Felide', 'Feliz')
# usuarios2 = Usuario('Chanchito','Feliz')

# print(usuarios.nombre, usuarios.apellido, usuarios2.nombre,usuarios2.apellido)
# del usuarios.nombre
# usuarios.nombre = 'Felipe'
# usuarios.Saludo()

# del usuarios
# admin = Admin('Super', 'Feliz')
# admin.superSaludo()

# usuarios

class Animal:
    def __init__(self,nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def Saludo(self):
        print('Hola, soy un ',self.tipo,' y mi sonido es el', self.onomatopeya)


class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self,nombre, onomatopeya)
        print('Hola, soy un gato extendido!')
        
class Perro(Animal):
   tipo = 'perro'
   def __init__(self, nombre, onomatopeya):
       super().__init__(nombre, onomatopeya)
       print('Instanciando un perro')

class Canario(Animal):
   tipo = 'Canario'

perro = Perro('Firulais','Ladrido')
perro.Saludo()
gato = Gato('Fluffy', 'maullido')
gato.Saludo()
canario = Canario('Piolin', 'sivido')
canario.Saludo()