**Analisis de codigo**

para este codigo utlice el **multipage** en Streamlit, esto nos permite crear aplicaciones web con multiples paginas, esto con el fin de organizar las funciones que desarrolle en una forma estructurada, cada pagina contiene su contenido, con el fin de proporcionarle al usuario una experiencia mas organizada y facil de navegar para el usuario

---

**Homepage.py**

Este archivo contiene la implementacion de la pagina principal de mi aplicacion. En esta seccion, el usuario puede encontrar informacion general sobre la pagina web, incluyendo sus funciones

---

**Calculadora Simple.py**

Este archivo nos permite utilizar una pagina que ofrece la funcion de una calculadora, la funcion le permite al usuario, ingresar dos numeros, depues debe ingresar el nombre (en minusculas) de la operacion aritmetica que desea utilizar, el archivo contiene una funcion llamada **calculadora_flex()** en ella se encuentran tres parametros **a**, **b** y **op**. dentro de nuestra funcion encontramos la estructura de if anidados, la cual dependiendo de la opcion que el usuario eliga tomara la decision de hacer alguna operacion aritmetica, en caso de que el usuario ingrese el nombre de una operacion aritmetica no definida, la funcion retornara un mensaje **"operacion no valida**, en caso de que el nombre ingresada por el usuario exista en la funcion, retornara la operacion y el resultado aparecera en un mensaje

---

**Calcular area de un triangulo.py**

Una funcion llamada **Calcular_area_de_un_triangulo()** que recibe como parametro **base** y **altura** nos desarrolla uun calculo aplicando la formula para calcular el area de un triangulo ([base * altura]/2), almacenamos dicha operacion en la variable res, para despues retornar nuestra variable resulatado y mostrarla al usuario en un mensaje

--- 

**Calcular precio total.py** 

Con la funcion **calcular_precio_final()** que toma los parametros **precio**, **descuento** e **impuesto**, nos permite calcular el precio de un producto tomando encuenta un decuento del 10% y un impuesto del 16% sobre el precio del producto, dentro de nuestra funcion encontramos los calculos, primero definimos la variable **precio_cd** donde almacena el calculo del precio con descuento (precio*descuento/100), pasamos con la variable **preciof** donde tomamos en cuenta el precio con descuento multiplicando el precio con impuesto el cual es equivalente a la operacion (precio con descuento * impuesto)/100, por ultimo retornamos nuestro precio final y escribimos en un mensaje visible para el usuario  

--- 

**Informacion Personal.py**

**info_per()** es una funcion que toma como argumentos una clave-valor (**kwargs) es un parametro especial de python que permite recibir un numero variable de argumentos en formato de pares y devuelve los pares como tuplas, contiene un ciclo for para recorrer cada par, cada iteracion toma una clave, un ejemplo de clave seria el **nombre** y su valor correspondiente seria el nombre del usuario por ejemplo **Juan**, la funcion recibe los datos que el usuario ha ingresado en el formulario (tales como lo son: el nombre, edad, direccion, email, finalmete los usuarion presionan un boton **enviar** y toda la informacion ingresada se muestra ordenadamente 

---

**Multiplicar.py**

Para este archivo implementamos la funcion **multiplicar_todo()** permite multiplicar todos los numetos que se le pasan como argumento, con el *args permite que la funcion reciba una cantidad variable de argumentos, args es una tupla que contendra todos los argumetnso que se pase al llamar la funcion, usamos un condicional el cual verifica si no existe un argumento para la funcion, se devuelve 1, se inicializa una variable **resultado** en 1, para despues almacenar el resultado de multiplicar los numeros (separados por comas) que ingreso el usuario, finalmente la funcion retorna la variable resultado 

--- 

**Numeros pares e impares.py**

**numeros_pares_e_impares()** es una funcion para separar numeros pares e impares, dentro de la funcion encontramos dos listas **pares = []** **impares=[]** las cuales nos permitiran almacenar los numeros pares e impares que ingrese el usuario (separados por comas), despues encontramos un ciclo for que recorre cada numero en una lista numeros, se usa un condicional **if numero % 2 == 0:** el cual toma en cuenta el resto de dividir el numeros entre 2, si el resto es 0 significa que el numero es par y se añade a la lista **pares**, en el caso de que el numero no sea par entra al bloque **else** y se añade a la lista **impares**. finalmente se recorren todos los numeros en la lista numeros y la funcion retorna dos lista **pares e impares**

---

**Producto.py**

con la funcion **producto()** que tiene como parametros **nombrep, cantidad y precio** se calcula el precio total del producto, en una variable llamda **total** se desarrolla una multiplicacion de la cantida del producto por el precio, la funcion retorna un mensaje donde se muestra el nombre del producto, la cantidad del producto, su precio y su precio final.

--- 

**Saludo.py** 

Se trata del archivo mas sencillo en esta pania web, contiene una funcion **saludo()** toma como parametro un nombre, se podria considerar que el usuario ingresara su nombre y la funcion le retornara un saludo de bienvenida, que contenga el nombre del usuario, la estructura del saludo seria **"Hola [nombre] bienvenido!**

**Suma.py**

La funcion **sumar()** recibe parametros **a y b** despues en una variable se alamacena la operacion aritmetica suma de estos dos numeros ingresados por el usuario, para despues retornar un mensaje donde el usuario pueda visualizar el resultado de la suma. 

---

**Suma lista.py** 

la funcion que esta definida en este archivo es **sumar_lista()** rescibe como parametro una lista llamada **numeros** donde se almacenan los numeros ingresados por el usuario, la funcion utiliza un ciclo for para sumar cada uno de los numeros almacenados en la lista, la suma se almacena en una variable **suma** la cual retornaremos en un mensaje para hacerla visual al usuario 














