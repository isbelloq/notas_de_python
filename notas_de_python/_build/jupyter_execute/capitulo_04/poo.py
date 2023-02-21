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

