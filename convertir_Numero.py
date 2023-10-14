class ConvertidorTexto:
    unidades = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
    decenas = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince', 'dieciséis', 'diecisiete', 'dieciocho',
               'diecinueve']
    diez_en_diez = ['veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']
    centenas = ['cien', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos',
                'setecientos', 'ochocientos', 'novecientos']

    def convertir_a_texto(self, numero):
        def convertir_decimal(decimal_part):
            palabras = []
            for d in decimal_part:
                palabras.append(ConvertidorTexto.unidades[int(d)])
            return 'coma ' + ' '.join(palabras)

        resultado = ""

        if isinstance(numero, int) or isinstance(numero, float):
            numero = str(numero)

            if numero.startswith('-'):
                resultado = 'menos '
                numero = numero[1:]

            partes = numero.split('.')
            parte_entera = int(partes[0])

            if 21 <= parte_entera <= 29:
                resultado += {
                    21: "veintiuno",
                    22: "veintidós",
                    23: "veintitrés",
                    24: "veinticuatro",
                    25: "veinticinco",
                    26: "veintiséis",
                    27: "veintisiete",
                    28: "veintiocho",
                    29: "veintinueve"
                }[parte_entera]
            elif 0 <= parte_entera < 10:
                resultado += ConvertidorTexto.unidades[parte_entera]
            elif 10 <= parte_entera < 20:
                resultado += ConvertidorTexto.decenas[parte_entera - 10]
            elif 20 <= parte_entera < 100:
                decena = parte_entera // 10
                unidad = parte_entera % 10
                if unidad == 0:
                    resultado += ConvertidorTexto.diez_en_diez[decena - 2]
                else:
                    resultado += ConvertidorTexto.diez_en_diez[decena - 2] + ' y ' + ConvertidorTexto.unidades[unidad]
            elif 100 <= parte_entera < 1000:
                centena = parte_entera // 100
                resto = parte_entera % 100
                if resto == 0:
                    if centena == 1:
                        resultado += 'cien'
                    else:
                        resultado += ConvertidorTexto.centenas[centena]
                else:
                    resultado += ConvertidorTexto.centenas[centena] + ' ' + self.convertir_a_texto(resto)  # Cambia a self
            elif 1000 <= parte_entera < 1000000:
                millar = parte_entera // 1000
                resto = parte_entera % 1000
                if millar == 1:
                    resultado += 'mil ' + self.convertir_a_texto(resto)  # Cambia a self
                else:
                    resultado += self.convertir_a_texto(
                        millar) + ' mil ' + self.convertir_a_texto(resto)  # Cambia a self
            elif 1000000 <= parte_entera < 1000000000:
                millon = parte_entera // 1000000
                resto = parte_entera % 1000000
                if millon == 1:
                    resultado += 'un millón'
                else:
                    resultado += self.convertir_a_texto(millon) + ' millones'
                if resto > 0:
                    resultado += ' ' + self.convertir_a_texto(resto)  # Cambia a self
            elif 1000000000 <= parte_entera < 1000000000000:
                billon = parte_entera // 1000000000
                resto = parte_entera % 1000000000
                if billon == 1:
                    resultado += 'mil millones'
                else:
                    resultado += self.convertir_a_texto(billon) + ' mil millones'
                if resto > 0:
                    resultado += ' ' + self.convertir_a_texto(resto)  # Cambia a self
            elif 1000000000000 <= parte_entera < 1000000000000000:
                billones = parte_entera // 1000000000000
                resto = parte_entera % 1000000000000
                if billones == 1:
                    resultado += 'un billón'
                else:
                    resultado += self.convertir_a_texto(billones) + ' billones'
                if resto > 0:
                    resultado += ' ' + self.convertir_a_texto(resto)  # Cambia a self
            else:
                resultado = 'Número fuera de rango'

            if len(partes) > 1 and int(partes[1]) > 0:
                resultado += ' ' + convertir_decimal(partes[1])  # Cambia a self

        return resultado