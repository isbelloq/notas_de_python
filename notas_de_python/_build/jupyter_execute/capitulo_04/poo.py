#!/usr/bin/env python
# coding: utf-8

# # Programacion orientada a objetos
# 
# ```{important} _Clase_: Molde que se utiliza para crear __objetos__
# ```
# 
# ```{important} _Instancia_: Objeto creado con una clase.
# ```
# 
# ```{important} _Atributo_: Informacion almacenada en una _clase_ o en una _instancia de clase_
# ```
# 
# ```{important} _Metodo_: Herramienta para operar datos propios de una _clase_ o de otros objetos
# ```

# ## Definicion de una clase
# 
# Para definir una clase se usa la palabra reservada `class` seguido de un nombre.
# 
# ```{tip} Segun [PEP-8](https://peps.python.org/pep-0008/#class-names) los nombres de clase se deben poner usando la convencion de __CamelCase__.
# ```

# In[1]:


# Creacion de una clase vacia
class MiPrimeraClase:
    pass


# In[2]:


# Cracion de instancias de clase

a = MiPrimeraClase()
b = MiPrimeraClase()

# Revision del tipo de dato de las instancias a y b
print(type(a))
print(type(b))


# ## Atributos
# 
# ```{important} Los _atributos_ guardan informacion de una clase
# ```
# 
# Se pueden agregar nuevos atributos a una clase de dos formas:
# 
# * `instancia.atriburo = valor`
# * `setattr(instancia, atributo, valor)`

# In[3]:


# Agregando atributos con .
a.nombre = 'Santiago'
a.edad = 29

# Agregando atributos con setattr
setattr(b, 'nombre', 'Ivan')
setattr(b, 'edad', 29)


# Se pueden acceder a los atributos de dos formas:
# 
# * `instancia.atributo`
# * `getattr(instancia, atributo)`

# In[4]:


# Accediendo con getattr
print(getattr(a, 'nombre'))
print(getattr(a, 'edad'))

# Accediedo con .
print(b.nombre)
print(b.edad)


# (poo-inicializar_clase)=
# ### Inicializar Clases
# 
# La funcion `__init__()` es una funcion **constructora** tiene el poder de asignar valores a propiedades de objetos o hacer las operaciones necesarias para que un objeto sea creado.
# 
# En el siguiente ejemplo se crea la clase `Consolas` con algunos atibutos.

# In[5]:


# Defincion de la clase Consola
class Consolas():
    def __init__(self, companhia: str, nombre: str) -> None:
        self.companhia = companhia
        self.nombre = nombre


# In[6]:


# Creacion de instancias
consola_1 = Consolas('Nintendo', 'Switch')
consola_2 = Consolas(companhia='Sony', nombre='Play Station 5')

# Obtencion de atributos de las instancias
print(consola_1.companhia, consola_1.nombre)
print(getattr(consola_2, 'companhia'), getattr(consola_2, 'nombre'))


# A una instancia ya creada se le puede agregar atriburos.
# 
# Ejemplo:

# In[7]:


# Creacion de atributo `lanzamiento` en instancia consola_1
consola_1.lanzamiento = 2017

print(consola_1.lanzamiento)


# In[8]:


# Comprobacion de no creacion de atributo `lanzamiento` en consola_2
print(consola_2.lanzamiento)


# ```{important} Al crear una instacia, los atributos nuevos que se definan despues de su creacion no son compartidos.
# ```

# ### Operaciones con los atributos
# 
# Hasta el momento hemos jugado con dos funciones que nos permiten assignar (`setattr`) y obtener (`getattr`) un atributo de una clase, sin embargo existen otras dos funciones:
# 
# * `hasattr(objeto, nombre)` Retorna `True` se el nombre esta dentro del objeto, `False` en caso contrario.
# * `delattr(objeto, nombre)` Elimina el atributo con el nombre especificado.
# 
# Aparte de estas dos funciones, la funcion `vars(objeto)` genera un diccionario donde las llaves son los nombres de los atributos y sus valores la asignacion.
# 
# Veamos algunos ejemplos:

# In[ ]:


# Creando una instanacia
c = Consolas('Nintendo', 'GameBoy')

# Revisando los atrubutos
print(vars(c))


# In[ ]:


# Creando un nuevo atributo a la clase
setattr(c, 'lanzamiento', 1989)

print(vars(c))


# In[ ]:


# Probando funcionalidad de getattr
getattr(c, 'juegos') # Genera error porque 'juegos' no existe


# In[ ]:


print(getattr(c, 'juegos', None)) # No se genera error porque se pone un valor por defecto
print(vars(c))


# In[ ]:


# Probando hasattr
print(hasattr(c, 'lanzamiento')) #True
print(hasattr(c, 'juegos')) #False


# In[ ]:


# Probando delattr
delattr(c, 'nombre')

print(vars(c))

# otra forma de hacer delattr
del c.companhia

print(vars(c))


# ### Atributos de clase
# 
# Los atributos vistos hasta ahora son propios de cada instancia y no son compartidos entre instancias, tal y como se vio en {ref}`poo-inicializar_clase`. Para crear atributos que se compartan por todas las instancias de clase se deben definir los atributos en el primer bloque logico como se muestra a continuacion.

# In[ ]:


# Definicion de clase con atributos de clase
class Michi:
    #Atributos de clase
    papitas = 4
    color = 'Negro'
    nombres = []
    def __init__(self, nombre: str) -> None:
        #Atributos de instancia
        self.nombre = nombre
        self.nombres.append(nombre)


# In[ ]:


# Instanciando michis
venus = Michi('Venus')
hera = Michi('Hera')
gaia = Michi('Gaia')


# In[ ]:


#Examinando atributos
print(venus.color, gaia.color)
print(venus.papitas, gaia.papitas)

#Modificando el color de gaia
gaia.color = 'Plateado'

#Examinando atributos luego del cambio
print(venus.color, gaia.color)
print(venus.papitas, gaia.papitas)


# ```{important} Aunque al inicializar las instancias compartan atributos, si se modifica un atributo en una instancia determinada, este cambio solo se ve reflejado en la instancia modificada y no se replicara en el resto de instancias definidas.
# ```

# Cuando se crean atributos de clase, no es necesario instanciar objetos para acceder a sus valores. Un ejemplo se ve a continuacion.

# In[ ]:


# Examinando atributos de la Clase
print(vars(Michi))

# Obtencion de atributos de clase
print(Michi.papitas)


# In[ ]:


# Generando error por intentar acceder a atributo de instancia
print(Michi.nombre)


# Al utilizar atributos de clase hay que prestar especial atencion a la mutabilidad de los objetos que se usan para asignar los valores, dado que al estar en el contexto de clase y no de instancia, si cualquier intancia modifica los atributos de clase en cualquier momento, por ejemplo, al instanciar la clase en el metodo `__init__`, estara modificando tambien los atributos de todas las instancias de la misma clase. Ocurre lo mismo si los atributos de la clase se modifican diretamente, el cambio se propaga por todas las instancias que no definan el atributo en la instancia. {cite}`jimenez2021python`

# In[ ]:


# __init__ modifica atributos de clase porque esta en el contexto de clase
print(Michi.nombres)

# revision de nombres en hera y gaia
print(hera.nombres)
print(gaia.nombres)


# In[ ]:


# Modificar nombres en instancia, solo se modifica hera
# porque el cambio se hace en el contexto de instancia
hera.nombres = []

# Revision de atributo nombes en Michi (clase) y en venus (instancia)
print(Michi.nombres)
print(venus.nombres)

# Revision de atributo nombes en hera
print(hera.nombres)


# In[ ]:


# Modificacion de nombres en clase, el cambio se progara
# a venus y gaia porque no se asigno el atributo nombres
# a nivel de instancia
Michi.nombres = ['Josefina', 'Pancracio', 'Misifus']

# Se modifica gaia y venus pero no hera
print(Michi.nombres)
print(venus.nombres)
print(gaia.nombres)
print(hera.nombres)


# ## Proteccion y privacidad en clases
# 
# * `_protegido`: Se considera un atributo o metodo _protegido_ de la clase, segun el [PEP-8](https://peps.python.org/pep-0008/#descriptive-naming-styles) es un indicador debil de uso intero, esto significa que no deberia ser usada fuera de la clase en la que se definio.
# 
# * `__privado`: Se considera un atributo o metodo _privado_ de la clase, segun el [PEP-8](https://peps.python.org/pep-0008/#descriptive-naming-styles) invoca el _name mangling_, esto quiere decir, que para acceder al abributo/metodo se deba usar `instancia._Clase__privado`. Se recomienda fuertemente no usar el atriburto/metodo fuera de la clase.
# 
# ```{tip}
# `Python` no tiene los conceptos de _protegido_ o _privado_, como si lo tiene `Java` por lo que se puede acceder y modificar los atributos/metodos si se sabe como acceder a ellos. **NO** se recomienda la manipulacion de los atributros/metodos que sean `_protegidos` o `__privados`
# ```
# 
# Ejemplo:

# In[1]:


# Definicion de clase
class Foo:
    _protegido = 0
    __privado = 0

    def __init__(self, x) -> None:
        self.x = x
        self._x = x*2
        self.__x = x*3


# In[2]:


# Intancia de clase
foo = Foo(2)

# dir muestra todos los atributos de la clase
print(dir(foo))


# In[3]:


# Obtencion de x
print(foo.x)


# In[4]:


# Obtencion de _x `protegido`
print(foo._x)


# In[5]:


# Intendo de obtencion de __x `privado`
print(foo.__x) # Falla porque no tiene la forma `name mangling`


# In[6]:


# Obtencion de __x `privado`
print(foo._Foo__x)


# In[7]:


# Obtencion de `_protegido` atributo de clase 
print(Foo._protegido)


# In[8]:


# Intento de obtencion de `__privado` atributo de clase
print(Foo.__privado) # Falla porque no tiene `name mangling`


# In[9]:


# Obtencion de `__privado` atributo de clase
print(Foo._Foo__privado)


# ## Construccion de clases personalizada
# 
# Existen dos metodos importantes en las clases `__new__` construye una instancio e `__init__` la inicializa.
# 
# 
# * `__new__` llamado para __crear una nueva instancia__ de la clase, __el valor devuelto por el metodo debe ser una instancia de un objeto__ cualquiera, no necesariamente de la clase creada. Cuando se define `__new__` en una clase es porque se quieren modificar la clase en el constructor.
# 
# * `__init__` es llamado despues de `__new__` e inicializa la instancia que es devuelta por `__new__`.
# 
# Para afianzar los conocimientos del uso de `__new__` e `__init` se plantea el siguiente problema:
# 
# Se pretende crear la clase `Corredor` en la que se asigna los numeros de cada corredor de forma correlativa y, en caso de eliminar algun objeto `Corredor`, el hueco que ocupaba se queda vacio para poder ser asignado a algun nuevo corredor {cite}`jimenez2021python`

# In[18]:


class Corredor:
    # atributo privado con el historal de numeros usados
    __numeros_usados = set()

    # constructor de la clase 
    def __new__(cls, nombre, num=1):
        #Generador de numeros no usados
        while num in cls.__numeros_usados:
            num += 1
        cls.__numeros_usados.add(num) # Agregacion de numero ya usado 
        instancia = super(Corredor, cls).__new__(cls) # Creacion de instancia dentro del constructor
        instancia.__init__(nombre) # Inicializacion de la instancia
        instancia.num = num # Modificacion de la instancia en el constructor
        return instancia
        
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __del__(self):
        self.__numeros_usados.remove(self.num)


# In[19]:


# Creacion de corredores
nairo = Corredor('Nairo')
rigo = Corredor('Rigoberto')
lopez = Corredor('Superman')

# Revision de numeros asignados
print(nairo.num, rigo.num, lopez.num)


# In[20]:


# Eliminacion de Rigo
del rigo

# Revision de atributo privado
print(Corredor._Corredor__numeros_usados)


# In[21]:


# Creacion de nuevo ciclista
chaves = Corredor('Chavito')

# Revision de numero de chaves
print(chaves.num)


# ## Propiedades en clases
# 
# Una propiedad de la clase define si un atributo puede ser obtenido (`getter`), modificado o definido (`setter`) y eliminado (`deleter`). para hacer uso de estas propiedad en Python se define `property` para controlar que hacer en los tres casos definidos anteriormente.
# 
# Para ver como funciona se pide construir la clase `Punto` con las siguietnes reglas:
# * El punto `x` se debe poder acceder y eliminar, pero no modificar.
# * El punto `y` se debe poder acceder y modificar, pero no eliminar.
# 
# La implementacion se muestra a continacion.

# In[1]:


class Punto:
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    #Definicion de x    
    ## getter
    def getx(self):
        return self._x

    ## setter
    def setx(self,valor):
        raise Exception('Valor x no puede ser modificado')

    ## deleter
    def delx(sefl):
        del sefl._x

    ## configuracion de las propiedades de x
    x = property(getx, setx, delx, 'Posicionen el eje de abscisas')

    #Definicion de y
    ## getter
    def gety(self):
        return self._y

    ## setter
    def sety(self,valor):
        self._y = valor

    ## deleter
    def dely(sefl):
        raise Exception('El atributo y no puede ser eliminado')

    ## configuracion de las propiedades de y 
    y = property(gety, sety, dely, 'Posicionen el eje de ordenadas')


# In[14]:


#Creacion del punto
p1 = Punto(4,2)
print(p1.x, p1.y)


# In[16]:


#Intendo de modificacion de x
p1.x = 89


# In[17]:


#Modificacion de y
p1.y = 94


# In[19]:


#Revision del punto
print(p1.x, p1.y)


# In[20]:


#Eliminacion del punto x
del p1.x


# In[21]:


#Intento de eliminacion del punto y
del p1.y


# In[9]:


#Intento de obtencion del punto x luego de ser eliminado
print(p1.x)


# In[22]:


# Obtencion del punto y
print(p1.y)

