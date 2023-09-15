
# Start with the number 2894
#paso1
numero = 45434921
# Calcula la primera parte usando divisiones y módulo
mitad_alta = numero // 10000
# Calcula la segunda parte usando el módulo
mitad_baja = numero % 10000

# Función para ordenar los dígitos de un número
#paso#2
def ordenar_numero(numero):
    numero_ordenado = 0
    while numero > 0:
        digito = numero % 10  # Obtener el último dígito
        numero //= 10  # Eliminar el último dígito del número original
        numero_ordenado = insertar_digito(numero_ordenado, digito)  # Insertar el dígito en su lugar correspondiente
    return numero_ordenado
def insertar_digito(numero_ordenado, digito):
    resultado = 0
    multiplicador = 1
    while numero_ordenado > 0:
        if numero_ordenado % 10 >= digito:
            resultado += numero_ordenado % 10 * multiplicador
            multiplicador *= 10
            numero_ordenado //= 10
        else:
            break
    resultado += digito * multiplicador
    resultado += numero_ordenado * multiplicador * 10
    return resultado
# Ordenar cada mitad por separado
mitad_alta_invertida = ordenar_numero(mitad_alta)
mitad_baja_invertida = ordenar_numero(mitad_baja)

print(mitad_alta_invertida)
print(mitad_baja_invertida)
#paso#3
unir_mitades = mitad_baja_invertida * 10000 + mitad_alta_invertida
#paso#4
def decimal_a_octal(numero):
    # Convertir a base octal
    resultado = 0
    base = 1
    while numero > 0:
        digito = numero % 8
        resultado += digito * base
        numero //= 8
        base *= 10
    return resultado

clave_encriptada = decimal_a_octal(unir_mitades)

print(f"La clave encriptada es: {clave_encriptada}")


    

