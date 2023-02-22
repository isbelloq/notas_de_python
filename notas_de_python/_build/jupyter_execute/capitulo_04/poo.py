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

# In[17]:


# Creando una instanacia
c = Consolas('Nintendo', 'GameBoy')

# Revisando los atrubutos
print(vars(c))


# In[18]:


# Creando un nuevo atributo a la clase
setattr(c, 'lanzamiento', 1989)

print(vars(c))


# In[12]:


# Probando funcionalidad de getattr
getattr(c, 'juegos') # Genera error porque 'juegos' no existe


# In[13]:


print(getattr(c, 'juegos', None)) # No se genera error porque se pone un valor por defecto
print(vars(c))


# In[14]:


# Probando hasattr
print(hasattr(c, 'lanzamiento')) #True
print(hasattr(c, 'juegos')) #False


# In[19]:


# Probando delattr
delattr(c, 'nombre')

print(vars(c))

# otra forma de hacer delattr
del c.companhia

print(vars(c))


# ### Atributos de clase
# 
# Los atributos vistos hasta ahora son propios de cada instancia y no son compartidos entre instancias, tal y como se vio en {ref}`poo-inicializar_clase`. Para crear atributos que se compartan por todas las instancias de clase se deben definir los atributos en el primer bloque logico como se muestra a continuacion.

# In[25]:


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


# In[26]:


# Instanciando michis
venus = Michi('Venus')
hera = Michi('Hera')
gaia = Michi('Gaia')


# In[27]:


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

# In[30]:


# Examinando atributos de la Clase
print(vars(Michi))

# Obtencion de atributos de clase
print(Michi.papitas)


# In[31]:


# Generando error por intentar acceder a atributo de instancia
print(Michi.nombre)


# Al utilizar atributos de clase hay que prestar especial atencion a la mutabilidad de los objetos que se usan para asignar los valores, dado que al estar en el contexto de clase y no de instancia, si cualquier intancia modifica los atributos de clase en cualquier momento, por ejemplo, al instanciar la clase en el metodo `__init__`, estara modificando tambien los atributos de todas las instancias de la misma clase. Ocurre lo mismo si los atributos de la clase se modifican diretamente, el cambio se propaga por todas las instancias que no definan el atributo en la instancia. {cite}`jimenez2021python`

# In[33]:


# __init__ modifica atributos de clase porque esta en el contexto de clase
print(Michi.nombres)

# revision de nombres en hera y gaia
print(hera.nombres)
print(gaia.nombres)


# In[34]:


# Modificar nombres en instancia, solo se modifica hera
# porque el cambio se hace en el contexto de instancia
hera.nombres = []

# Revision de atributo nombes en Michi (clase) y en venus (instancia)
print(Michi.nombres)
print(venus.nombres)

# Revision de atributo nombes en hera
print(hera.nombres)


# In[35]:


# Modificacion de nombres en clase, el cambio se progara
# a venus y gaia porque no se asigno el atributo nombres
# a nivel de instancia
Michi.nombres = ['Josefina', 'Pancracio', 'Misifus']

# Se modifica gaia y venus pero no hera
print(Michi.nombres)
print(venus.nombres)
print(gaia.nombres)
print(hera.nombres)

