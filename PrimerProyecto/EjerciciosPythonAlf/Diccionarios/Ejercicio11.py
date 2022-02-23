# Cadena con los datos de los clientes de la empresa
datos_clientes = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

# Se divide la cadena por el caracter de cambio de linea \n y creamos una lista de subcadenas
lista_clientes = datos_clientes.split('\n')

# Inicializamos el directorio que va a contener el directorio de clientes a vacio
directorio = {}

# Dividimos la cadena del primer elemento de la lista de clientes (que contiene los nombres de los campos)
# por el caracter ; y creamos una lista con los campos
lista_campos = lista_clientes[0].split(';')

# Bucle iterativo para recorrer los elementos de la lista lista_cliente.
# la variable cliente recorre desde el segundo elemento hasta el ultimo elemento de la lista
# (el primer elemento contiene los nombres de campo as[i que no corresponde al cliente
for i in lista_clientes[1:]:
    # Inicializamos el diccionario que va a contener lso datos del cliente actual a vacio.
    cliente = {}
    # Dividimos la cadena i por el caracter ; y creamos una lista con las subcadenas con la
    # informacion del cliente
    lista_info = i.split(';')
    # Bucle iterativo para recorrer los campos y anadir los pares al diccionario del cliente.
    # j toma los valores de 1 al numero de campos menos 1. El primer elemento (posicion 0) corresponde
    # al nif y no se anade al diccionario porque se utilzara despues como clave en el diccionario principal
    for j in range(1, len(lista_campos)):
        # Condicional. Si el campo actual es descuento convertimos su valor real
        if lista_campos[j] == 'descuento':
            lista_info[j] = float(lista_info[j])
        cliente[lista_campos[j]] = lista_info[j]
    # Anadiremos un par al diccionario del directorio con la clave el nif del cliente y valor
    # el diccionario que acabamos de crear con el resto de sus datos.
    directorio[lista_info[0]] = cliente
# mostramos el directorio por pantalla
print(directorio)