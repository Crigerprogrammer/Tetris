## ¿Que es Python?

Python es un lenguaje de programación creado por Guido Van Rossum, con una sintaxis muy limpia, ideado para enseñar a la gente a programar bien. Se trata de un lenguaje interpretado o de script.
## Ventajas:
- **Legible** : sintaxis intuitiva y estricta.
- **Productivo** : ahorra mucho código.
- **Portable** : para todo sistema operativo.
- **Recargado** : viene con muchas librerías por defecto.

## Instalación:

### Windows

Para descargar Python en sistemas operativos Windows, deberemos ir a python.org, y en la sección de descargas descargar la versión recomendada, al momento de escribir este documento la última versión es Python 3.8.0. Tendremos un archivo ejecutable **exe**, el cuál deberemos de ejecutar y se descargará todo el lenguaje. **RECOMENDACION**: Habilitar las variables de entorno para utilizar python en cmd (terminal).

### Linux
Generalmente en Linux python está integrado, en caso no este instalado podremos instalarlo de las siguientes maneras en las siguientes distribuciones:

***Ubuntu ó Debian***
``` 
$ sudo apt-get install python3.8
```
***Red Hat o Centos***
``` 
$ sudo yum install python
```

### Utilizando Python

Para correr python se necesita de una terminal de comandos (cmd en Windows) ó Terminal en usuarios Linux ó Mac. Se puede instalar terminales con comandos linux en sistemas operativos Windows como Ejemplo **Cmder**, **Hyper**, entre otros. Dentro de la terminal colocamos el siguiente comando:
``` 
python
```
Luego de dar enter en el comando, entraremos python y podremos ejecutar código python.

**Extensión de archivos python**
Los archivos que contienen líneas de código Python, se deben de guardar con la extensión .py **Ejemplo**: holamundo.py
### Ejecutando Archivos Python
Para ejecutar archivos .py , basta con colocar la palabra python seguido del nombre del archivo con la extensión correspondiente. ***Ejemplo***:
``` 
python hola.py
```

## Tipos de Datos en Python

- **Enteros (int)**: En este grupo están todos los números enteros y long
- **Booleanos (bool)**: Son los valores falso o verdadero, compatible con las operaciones booleanas ( and, not, or). 
- **Cadenas (str)**: Son una cadena de texto, ***Ejemplo***: "Hola"
- **Listas**: Son un grupo o array de datos, pueden contener cualquier de los datos anteriores, ***Ejemplo***: [1,2,3,"hola",true]
- **Diccionarios**: Son un grupo de datos que se acceden a partir de una clave, ***Ejemplo***: {"clave":"valor"}
- **Tuplas** : También son un grupo de datos igual que una lista con la diferencia que una tupla después de ser creada, no puede ser modificada.

## Funciones

Las funciones se definen con la palabra reservada **def** seguido del nombre de la función y parentesis y dentro de ellos parametros, en dado caso utilice.
***Ejemplo***:
``` python
def hola_mundo()
... return "Hola mundo"
...
hola_mundo()
```
El resultado de la anterior función, sería ***Hola Mundo***

## Variables
Las variables, a diferencia de otro lenguaje de programación, no deben ser definidas, ni tampoco indicar su tipo de dato, Python al conocer lo que se alamcena en la variable, conoce su tipo.
***Ejemplo***
``` python
A = 3
B = A
C = "Hola"
```

## Sintaxis Listas
Las listas se declaran con corchetes, y dentro de una lista puede haber otra lista o algún tipo de dato.
***Ejemplo***
``` python
lista = [21, False, "cadena", [0,1]]
```

## Sintaxis Tuplas
Las tuplas se declaran con paréntesis.
**Recordatorio**, Las tuplas no pueden ser modificadas después de haberlas creado.
***Ejemplo***
``` python
tupla = (21, False, "cadena", [0,1])
```

## Sintaxis Diccionario
Los diccionarios de declaran con llaves {}, y la sintaxis es la primer cadena es la clave y la segunda es el valor de dicha clave
***Ejemplo***
``` python
diccionario =  {"clave":"valor", "Nombre":"Cristian" }
```


