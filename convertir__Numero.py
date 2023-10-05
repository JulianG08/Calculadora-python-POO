def numeros_a_palabras(numero: float) -> str:
    if numero == 0:
        return 'Cero'

    unidades = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
    otros = ['', 'mil', 'millones', 'mil millones']
    otros_grandes = ['', 'mil', 'millones', 'mil millones', 'mil billones', 'millón de millones', 'mil billones de billones']
    
    casos_especiales = {
        10: "diez",
        11: "once",
        12: "doce",
        13: "trece",
        14: "catorce",
        15: "quince"
    }
    
    def armar_cientos(num: str) -> str:
        unidades = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
        decenas = ['', 'dieci', 'veinti', 'treinta y ', 'cuarenta y ', 'cincuenta y ', 'sesenta y ', 'setenta y ', 'ochenta y ', 'noventa y ']
        centenas = ['', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']
        
        cientos = int(num[0]) if len(num) > 2 else 0
        decena, unidad = num[-2:]
        return (f"{centenas[cientos]} " if cientos != 0 else '') + decenas[int(decena)] + unidades[int(unidad)]
    
    def dividir_num(num: str) -> list:
        return [num[i:i+3] for i in range(0, len(num), 3)]
    
    parte_entera = int(numero)
    parte_decimal = int((numero - parte_entera) * 100)

    en_palabras = ''

    if parte_entera > 0:
        grupos = dividir_num(str(parte_entera)[::-1])

        for i, parte in enumerate(grupos):
            parte = parte[::-1]
            num = int(parte)

            if num == 0:
                continue

            if len(str(num)) == 1:
                en_palabras = unidades[num] + f" {otros_grandes[i]} " + en_palabras
            elif num > 15:
                resultado = armar_cientos(parte).strip()

                if resultado[-1] == 'i':
                    resultado = resultado[:-1] + ('e' if parte[-2] == '2' else 'a')
                elif resultado == 'ciento':
                    resultado = 'cien'

                en_palabras = resultado + f" {otros_grandes[i]} " + en_palabras
            else:
                en_palabras = casos_especiales[num] + f" {otros_grandes[i]} " + en_palabras

    # Convertir la parte decimal
    if parte_decimal > 0:
        en_palabras += 'punto ' + unidades[parte_decimal // 10] + ' ' + unidades[parte_decimal % 10]

    if en_palabras.startswith('uno'):
        en_palabras = en_palabras[3:]

    return en_palabras.strip().capitalize()

print(numeros_a_palabras(2))
print(numeros_a_palabras(100))
print(numeros_a_palabras(520))
print(numeros_a_palabras(1000))
print(numeros_a_palabras(2023))
print(numeros_a_palabras(16091))
print(numeros_a_palabras(99))
print(numeros_a_palabras(1000000))
print(numeros_a_palabras(4000000))
print(numeros_a_palabras(99999999999999999999))
print(numeros_a_palabras(12345.67))