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


# (poo-construccion_de_clases_personalizada)=
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

# In[10]:


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


# In[11]:


# Creacion de corredores
nairo = Corredor('Nairo')
rigo = Corredor('Rigoberto')
lopez = Corredor('Superman')

# Revision de numeros asignados
print(nairo.num, rigo.num, lopez.num)


# In[12]:


# Eliminacion de Rigo
del rigo

# Revision de atributo privado
print(Corredor._Corredor__numeros_usados)


# In[13]:


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
    x = property(getx, setx, delx, 'Posicion en el eje de abscisas')

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
    y = property(gety, sety, dely, 'Posicion en el eje de ordenadas')


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


# Otra forma de implementar el comportamiento de las propiedades de un atributo se puede hacer con el uso del decorador `@property`
# 
# Se muestra la misma implementacion de la clase `Punto` pero con decoradores.

# In[1]:


class Punto:
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    # Propiedades de x

    ## getter
    @property
    def x(self) -> float:
        """
        x Posicion en el eje de abcisas

        Returns
        -------
        float
            Punto en x
        """

        return self._x
    
    ## deleter
    @x.deleter
    def x(self) -> None:
        del self._x

    # Propiedades en y

    ## getter
    @property
    def y(self) -> float:
        """
        y Posicion en el eje de las ordenadas

        Returns
        -------
        float
            Punto en y
        """
        return self._y

    ## setter    
    @y.setter
    def y(self, valor) -> None:
        self._y = valor


# In[2]:


#Creacion del punto
p1 = Punto(4,2)
print(p1.x, p1.y)


# In[3]:


#Intendo de modificacion de x
p1.x = 89


# In[4]:


#Modificacion de y
p1.y = 94


# In[5]:


#Revision del punto
print(p1.x, p1.y)


# In[6]:


#Eliminacion del punto x
del p1.x


# In[7]:


#Intento de eliminacion del punto y
del p1.y


# In[8]:


#Intento de obtencion del punto x luego de ser eliminado
print(p1.x)


# In[9]:


# Obtencion del punto y
print(p1.y)


# ```{tip}
# Cuando se usa `@property` y el decorador del atributo no es implementado (como `@x.setter` o `@y.deleter`) se eleva un error de tipo `AttributeError` lo cual indica que la propiedad no esta implementado por lo tanto no se ejecuta.
# ```

# ## Ejemplo
# 
# Para reforsar los conceptos vistos hasta ahora se pone el siguiente ejercicio.
# 
# Se pretende crear la clase `Finalista` que guarde la clasificacion de corredores que terminaron la carrera, respetando el orden en que pasaron por la linea de meta. La clase `Corredor` se definio en {ref}`poo-construccion_de_clases_personalizada` y es el unico objeto que debera ser usado como parametro del constructor de la clase `Finalista`. `Finalista` debera guardar el contador actual de todos los finalistas y cada finalista no puede modificar su posicion. {cite}`jimenez2021python`

# In[14]:


class Finalista:
    __finalizados = 0
    def __new__(cls, corredor):
        cls.__finalizados += 1
        puesto = cls.__finalizados
        instancia = super(Finalista, cls).__new__(cls)
        instancia.__init__(corredor)
        instancia._posicion = puesto
        return instancia
    
    def __init__(self, corredor) -> None:
        self.corredor = corredor

    @property
    def posicion(self):
        """
        Posicion en que el corredor finalizo la carrera
        """
        return self._posicion


# In[16]:


# Creacion de corredores
nairo = Corredor('Nairo')
rigo = Corredor('Rigoberto')
lopez = Corredor('Superman')

# Finalizacion de corredores
nairo_finalista = Finalista(nairo)
rigo_finalista = Finalista(rigo)


# In[17]:


# Revision de llegada
print(nairo_finalista.posicion, rigo_finalista.posicion)


# In[18]:


# Intento de modificacion de posicion de rigo_finalista
rigo_finalista.posicion = 1


# ## Metodos
# 
# Son **funciones** presentes en clases o en instancias y se encatgan de realizar tareas con los atributos de la clase o con datos fuera de la clase o instancia. {cite}`jimenez2021python`.
# 
# En `Python` se pueden generara tres tipos de metodos.
# 
# 1. Metodos de instancia.
# 2. Metodos de clase.
# 3. Metodos estaticos.

# ### Metodos de instancia
# 
# Son funciones que se crean dentro de una clase con la particularidad que su primer parametro es `self`.
# 
# Un ejemplo se muestra a continuacion:

# In[2]:


import math

class Punto:
    def __init__(self, x: float, y:float) -> None:
        self.x = x
        self.y = y

    # Creacion de metodo de instancia: distancia    
    def distancia(self, otro_punto) -> float:
        """
        La raiz cuadrada de los cuadrados de las diferencias

        Parameters
        ----------
        otro_punto : Punto
            Otro punto para hacer el calculo de la distancia

        Returns
        -------
        float
            distancia entre el punto de la clase y otro punto
        """

        xs = (self.x - otro_punto.x) ** 2
        ys = (self.y - otro_punto.y) ** 2

        return math.sqrt(xs + ys)
     
    # Creacion de metodo de instancia: mover_x    
    def mover_x(self, cantidad: float) -> None:
        """
        mover_x se mueve el punto x una cantidad definida

        Parameters
        ----------
        cantidad : float
            Cantidad a mover el punto x
        """

        self.x += cantidad
    
    # Creacion de metodo de instancia: mover_y    
    def mover_y(self, cantidad: float) -> None:
        """
        mover_y se mueve el punto y una cantidad definida

        Parameters
        ----------
        cantidad : float
            Cantidad a mover el punto y
        """

        self.y += cantidad


# In[3]:


# Definicion de intancias de prueba
p1 = Punto(7,5)
p2 = Punto(4,1)

# Prueba de metodos
## distancia
print(p1.distancia(p2))
print(p2.distancia(p1))

## mover_x
p1.mover_x(5)
print(p1.x, p1.y)

## mover_y
p2.mover_y(-10)
print(p2.x, p2.y)


# (poo-metodos_de_clase)=
# ### Metodos de clase
# 
# Son metodos que estan orientados a nivel de **clase**. Para definir un metodo de clase se debe usar el decorador `@classmethod` y el primer parametro debe ser `cls`.
# 
# Un ejemplo:

# In[4]:


class Foo(object):
    # Atributo de clase
    x = 10

    def __init__(self, x) -> None:
        # Atributo de instancia
        self.x = x

    @classmethod
    def get_x_clase(cls):
        return cls.x


# In[5]:


# Creacion de instancia
f = Foo(-2)

# Obtencion del atributo de instancia
print(f.x)

# Obtencion del atributo de clase usando el metodod de clase
print(f.get_x_clase())


# Uno de los usos que se le puede dar a los metodos de clase son:
# 
# * Creacion de instancias predefinidas.
# * Inicializacion de instancia con una logica particular.
# 
# Para ilustara esto se plantea el siguiente problema:
# 
# Se pretende crear una clase que modele animales con distinto nombre, tipo, largo, y masa, pero que tambien se puedan inicializar intancias si se provee una cadena de caracteres separada por comas con los valores de los atributos necesarios. Adicionalmente, queremos tener metodos simples que construyan un gato o un perro:
# * Un gato es de tipo "Gato", tiene un largo de 120 cm y una masa de 3.8 kg.
# * Un perro es de tipo "Perro", tiene un largo de 500 cm y una masa de 25.4kg.
# 
# {cite}`jimenez2021python`

# In[2]:


class Animal:
    def __init__(self, tipo: str, largo: float, masa:float) -> None:
        self.tipo = tipo
        self.largo = largo
        self.masa = masa

    @classmethod
    def desde_str(cls, cadena:str):
        """
        desde_str Creacion de la instancia animal desde una cadena de caracteres

        Parameters
        ----------
        cadena : str
            Cadena de la forma tipo,largo,masa

        Returns
        -------
        _type_
            instanca del animal
        """
        tipo, largo, masa = cadena.split(',')
        return cls(tipo, float(largo), float(masa))
    
    @classmethod
    def gato(cls):
        """
        gato Creacion de la instancia Gato

        Returns
        -------
        _type_
            instancia gato con tipo Gato, largo 120cm y masa 3.8kg
        """
        return cls("Gato", 120, 3.8)
 
    @classmethod
    def perro(cls):
        """
        perro Creacion de la instancia Perro

        Returns
        -------
        _type_
            instancia perro con tipo Perro, largo 500cm y masa 25.4kg
        """
        return cls("Perro", 500, 25.4)


# In[3]:


# Creacion de instancia de forma usual
cebra = Animal("Cebra", 15000, 150)

# Creacion de intancias con los metodos de clase
## Con el metodo desde_str
elefante = Animal.desde_str("Elefante,300000,2600")
## Con el metodo gato
gato = Animal.gato()
## Con el metodo perro
perro = Animal.perro()

print(cebra, elefante, gato, perro)


# ### Metodos estaticos
# 
# Son metodos que petenecen a la clase pero no necesariamente hacen uso de los atributos de la clase o de la instancia. En algunos casos se usa para mejorar la legibilidad del codigo o poerque fuera de la clase realmente no tiene mucho sentido {cite}`jimenez2021python`
# 
# Para crear un metodo estatico se debe hacer uso del decorador `@staticmethod`.
# 
# Como ejemplo se usara la clase `Animal` definida en {ref}`poo-metodos_de_clase` y se agregara un metodo de instancia que calcule el peso del animal y un metodo estatico con el valor de la gavedad.

# In[4]:


class Animal:
    def __init__(self, tipo: str, largo: float, masa:float) -> None:
        self.tipo = tipo
        self.largo = largo
        self.masa = masa

    @classmethod
    def desde_str(cls, cadena:str):
        """
        desde_str Creacion de la instancia animal desde una cadena de caracteres

        Parameters
        ----------
        cadena : str
            Cadena de la forma tipo,largo,masa

        Returns
        -------
        _type_
            instanca del animal
        """
        tipo, largo, masa = cadena.split(',')
        return cls(tipo, float(largo), float(masa))
    
    @classmethod
    def gato(cls):
        """
        gato Creacion de la instancia Gato

        Returns
        -------
        _type_
            instancia gato con tipo Gato, largo 120cm y masa 3.8kg
        """
        return cls("Gato", 120, 3.8)
 
    @classmethod
    def perro(cls):
        """
        perro Creacion de la instancia Perro

        Returns
        -------
        _type_
            instancia perro con tipo Perro, largo 500cm y masa 25.4kg
        """
        return cls("Perro", 500, 25.4)

    def peso(self) -> float:
        """
        peso metodo de calculo del peso del animal

        Returns
        -------
        float
            Peso del animal
        """

        return self.masa * self.gravedad()

    @staticmethod
    def gravedad() -> float:
        """
        gravedad valor constante de la gravedad
 
        Returns
        -------
        float
            valor de la gravidad en m/s^2
        """

        return 9.8


# In[5]:


# Revision del metodo estatico
print(Animal.gravedad())

# Creacion de instancia elefante y calculo del peso
elefante = Animal.desde_str("Elefante,300000,2600")
print(elefante.peso())


# ## Metodos magicos
# 
# Son metodos que que **estandarizan potrocolos** comunes en `Python` como lo pueden ser las operaciones de comparacion (`==`, `!=`, `<`, `>`, ect.), las operaciones matematicas (`+`, `-`, `*`, `/`, ect.) u otros metodos comuntes (`len`, `bool`, etc.). Los metodos magicos inician y terminana con `__`.
# 
# En las secciones anteriores se ha usar `__init__` o `__new__` que son metodos magicos para inicializar y construir una instancia, pero existen muchos mas.
# 
# Para ver su uso, se plantea el siguente reto: Se desea crear la clase `Planta` con los siguientes requisitos:
# 
# * Dos plantas son iguales si su tipo es el mismo. Para utilizar el operador `==` se debe definir el metodo magico `__eq__` en la clase.
# * Una planta es mayor que otra, si su altura es mayor. Para utilizar el operador `>` se debe definir el metodo magico `__gt__` y para usar el operador `>=` se debe definir el metodo magico `__ge__`.

# In[6]:


class Planta:
    def __init__(self, nombre: str, tipo: str, altura: float) -> None:
        self.nombre = nombre
        self.tipo = tipo
        self. altura = altura

    def __eq__(self, otra_planta) -> bool:
        """
        __eq__ operador de igualdad para una planta.

        Dos plantas son iguales si tienen el mismo tipo

        Parameters
        ----------
        otra_planta : _type_
            Planta a comparar

        Returns
        -------
        bool
            True si las plantas tienen el mismo tipo False en caso contrario
        """
        return self.tipo == otra_planta.tipo

    def __gt__(self, otra_planta) -> bool:
        """
        __gt__ Comparacion de dos plantas

        Se compara la altura de la planta

        Parameters
        ----------
        otra_planta : _type_
            Planta a comparar

        Returns
        -------
        bool
            True si la plana tiene mayor altura que otra_planta
        """

        return self.altura > otra_planta.altura
 
    def __ge__(self, otra_planta) -> bool:
        """
        __ge__ Comparacion de dos plantas

        Se compara la altura de la planta

        Parameters
        ----------
        otra_planta : _type_
            Planta a comparar

        Returns
        -------
        bool
            True si la plana tiene mayor o igual altura que otra_planta
        """

        return self.altura >= otra_planta.altura


# In[7]:


## Creacion de instancias
camelia = Planta('Camelia', 'Arbusto', 2)
celindo = Planta('Celindo', 'Arbusto', 5)
pino = Planta('Pino', 'Arbol', 9)

## Comparacion de igualdad
print(camelia == celindo)
print(camelia == pino)


# In[8]:


## Comparacion de mayor o igual
print(camelia > pino)
print(celindo <= celindo)
print(celindo >= pino)


# ```{tip}
# Si se implementa `__gt__` Se puede usar el operador `>` y a su vez `<`.
# 
# Si se implementa `__ge__` Se puede usar el operador `>=` y a su vez `<=`
# ```

# Una lista de los metodos magicos se encuentra en la [documentacion de `Python`](https://docs.python.org/3/reference/datamodel.html)

# ### Metodos para usar operaciones matematicas
