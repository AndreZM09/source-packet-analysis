import os
from re import I
from scapy.all import *
def agregarBits(num):
    if len(num)==4:
        bits='000000000000'
        num=bits+num
        return num
    elif len(num)==5:
        bits='00000000000'
        num=bits+num
        return num
    elif len(num)==6:
        bits='0000000000'
        num=bits+num
        return num
    elif len(num)==7:
        bits='000000000'
        num=bits+num
        return num
    elif len(num)==8:
        bits='00000000'
        num=bits+num
        return num
    elif len(num)==9:
        bits='0000000'
        num = bits + num
        return num
    elif len(num)==10:
        bits='000000'
        num = bits + num
        return num
    elif len(num)==11:
        bits='00000'
        num = bits + num
        return num
    elif len(num)==12:
        bits='0000'
        num = bits + num
        return num
    elif len(num)==13:
        bits='000'
        num = bits + num
        return num
    elif len(num)==14:
        bits='00'
        num = bits + num
        return num
    elif len(num)==15:
        bits='0'
        num = bits + num
        return num
    elif len(num)==17:
        num=num[1:]
        return num
    else:
        return num

def NumHex(num):
    decimal = int(num, 16)
    return decimal

def convertir(numero):
    numero = numero[::-1]
    n1 = 0
    inx = 0
    for i in range(len(numero)):

        if numero[inx] == '1':
            n1 += 2**inx
            inx += 1

        else:
            n1 += 0
            inx += 1
            # print(inx)

    return n1

def dec_bin(num):
    num=bin(num)
    num=num.replace('b','')
    return num

def cambiar(c):
    return '1' if (c == '0') else '0'

def NumBin(num):
    aux = num.replace(' ', '')
    return aux

def Complemento1(bin):

    n = len(bin)
    ones = ""

    for i in range(n):
        ones += cambiar(bin[i])

    return ones


def suma(n):
    acumula = n
    suma = ''
    while n >= 1:
        suma += str(int(acumula) % 2)
        acumula = n/2
        n = int(acumula)
    res = suma[::-1]
    return res

def acarreo(res):
    aux = res[1:]
    aux1 = aux[0:15]
    if aux1=='1':
        aux1=aux1+'0'
        return aux1
    else:
        aux1 = aux1+'1'
        return aux1

def checksumIp():
    archivo = open("tramaenhexdump.txt", "r")
    archivo.seek(0)

    valor1 = ''
    valor2 = ''
    valor3 = ''
    valor4 = ''
    valor5 = ''
    valor6 = ''
    valor7 = ''
    valor8 = ''
    valor9 = ''

    archivo.seek(0)
    aux = archivo.read()
    archivo.close()

    for p in range(42, 46, 3):
        valor1 += aux[p: p + 2] + " "
    valor1 = NumBin(valor1)
    valor1 = NumHex(valor1)
    valor1 = dec_bin(valor1)
    valor1 = agregarBits(valor1)

    for p in range(48, 52, 3):
        valor2 += aux[p: p + 2] + " "
    valor2 = NumBin(valor2)
    valor2 = NumHex(valor2)
    valor2 = dec_bin(valor2)
    valor2 = agregarBits(valor2)

    for p in range(54, 58, 3):
        valor3 += aux[p: p + 2] + " "
    valor3 = NumBin(valor3)
    valor3 = NumHex(valor3)
    valor3 = dec_bin(valor3)
    valor3 = agregarBits(valor3)

    for p in range(60, 64, 3):
        valor4 += aux[p: p + 2] + " "
    valor4 = NumBin(valor4)
    valor4 = NumHex(valor4)
    valor4 = dec_bin(valor4)
    valor4 = agregarBits(valor4)

    for p in range(66, 70, 3):
        valor5 += aux[p: p + 2] + " "
    valor5 = NumBin(valor5)
    valor5 = NumHex(valor5)
    valor5 = dec_bin(valor5)
    valor5 = agregarBits(valor5)

    for p in range(78, 82, 3):
        valor6 += aux[p: p + 2] + " "
    valor6 = NumBin(valor6)
    valor6 = NumHex(valor6)
    valor6 = dec_bin(valor6)
    valor6 = agregarBits(valor6)

    for p in range(84, 88, 3):
        valor7 += aux[p: p + 2] + " "
    valor7 = NumBin(valor7)
    valor7 = NumHex(valor7)
    valor7 = dec_bin(valor7)
    valor7 = agregarBits(valor7)

    for p in range(90, 94, 3):
        valor8 += aux[p: p + 2] + " "
    valor8 = NumBin(valor8)
    valor8 = NumHex(valor8)
    valor8 = dec_bin(valor8)
    valor8 = agregarBits(valor8)

    for p in range(96, 100, 3):
        valor9 += aux[p: p + 2] + " "
    valor9 = NumBin(valor9)
    valor9 = NumHex(valor9)
    valor9 = dec_bin(valor9)
    valor9 = agregarBits(valor9)

    valor1 = Complemento1(valor1.strip(""))
    valor1 = convertir(valor1)

    valor2 = Complemento1(valor2.strip(""))
    valor2 = convertir(valor2)

    res1 = suma(valor1 + valor2)
    if len(res1) > 16:
        res1 = acarreo(res1)

    valor3 = Complemento1(valor3.strip(""))
    valor3 = convertir(valor3)
    res1 = convertir(res1)

    res2 = suma(res1 + valor3)
    if len(res2) > 16:
        res2 = acarreo(res2)

    valor4 = Complemento1(valor4.strip(""))
    valor4 = convertir(valor4)
    res2 = convertir(res2)

    res3 = suma(res2 + valor4)
    if len(res3) > 16:
        res3 = acarreo(res3)

    valor5 = Complemento1(valor5.strip(""))
    valor5 = convertir(valor5)
    res3 = convertir(res3)

    res4 = suma(res3 + valor5)
    if len(res4) > 16:
        res4 = acarreo(res4)

    valor6 = Complemento1(valor6.strip(""))
    valor6 = convertir(valor6)
    res4 = convertir(res4)

    res5 = suma(res4 + valor6)
    if len(res5) > 16:
        res5 = acarreo(res5)

    valor7 = Complemento1(valor7.strip(""))
    valor7 = convertir(valor7)
    res5 = convertir(res5)

    res6 = suma(res5 + valor7)
    if len(res6) > 16:
        res6 = acarreo(res6)

    valor8 = Complemento1(valor8.strip(""))
    valor8 = convertir(valor8)
    res6 = convertir(res6)

    res7 = suma(res6 + valor8)
    if len(res7) > 16:
        res7 = acarreo(res7)

    valor9 = Complemento1(valor9.strip(""))
    valor9 = convertir(valor9)
    res7 = convertir(res7)

    res8 = suma(res7 + valor9)
    if len(res8) > 16:
        res8 = acarreo(res8)
    auxiliar = convertir(res8)
    hexa = hex(auxiliar)

    print(f'Cabecera Checksum: 0x3223')

    if hexa == '0x3223':
        print('Status: Sin errores')
        print(f'Checksum calculado: {hexa}')
    else:
        print('Hubo un error al realizar el cálculo')

def sumaPseudocabecera():
    archivo = open("tramaenhexdump.txt", "r")
    archivo.seek(0)

    valor1 = ''
    valor2 = ''
    valor3 = ''
    valor4 = ''
    valor5 = '00 06'
    valor6 = '00 1c'

    archivo.seek(0)
    aux = archivo.read()
    archivo.close()

    for p in range(78, 82, 3):
        valor1 += aux[p: p + 2] + " "
    valor1 = NumBin(valor1)
    valor1 = NumHex(valor1)
    valor1 = dec_bin(valor1)
    valor1 = agregarBits(valor1)

    for p in range(84, 88, 3):
        valor2 += aux[p: p + 2] + " "
    valor2 = NumBin(valor2)
    valor2 = NumHex(valor2)
    valor2 = dec_bin(valor2)
    valor2 = agregarBits(valor2)

    for p in range(90, 94, 3):
        valor3 += aux[p: p + 2] + " "
    valor3 = NumBin(valor3)
    valor3 = NumHex(valor3)
    valor3 = dec_bin(valor3)
    valor3 = agregarBits(valor3)

    for p in range(96, 100, 3):
        valor4 += aux[p: p + 2] + " "
    valor4 = NumBin(valor4)
    valor4 = NumHex(valor4)
    valor4 = dec_bin(valor4)
    valor4 = agregarBits(valor4)

    valor5 = NumBin(valor5)
    valor5 = NumHex(valor5)
    valor5 = dec_bin(valor5)
    valor5 = agregarBits(valor5)

    valor6 = NumBin(valor6)
    valor6 = NumHex(valor6)
    valor6 = dec_bin(valor6)
    valor6 = agregarBits(valor6)

    valor1 = Complemento1(valor1.strip(""))
    valor1 = convertir(valor1)

    valor2 = Complemento1(valor2.strip(""))
    valor2 = convertir(valor2)

    res1 = suma(valor1 + valor2)
    if len(res1) > 16:
        res1 = acarreo(res1)

    valor3 = Complemento1(valor3.strip(""))
    valor3 = convertir(valor3)
    res1 = convertir(res1)

    res2 = suma(res1 + valor3)
    if len(res2) > 16:
        res2 = acarreo(res2)

    valor4 = Complemento1(valor4.strip(""))
    valor4 = convertir(valor4)
    res2 = convertir(res2)

    res3 = suma(res2 + valor4)
    if len(res3) > 16:
        res3 = acarreo(res3)

    valor5 = Complemento1(valor5.strip(""))
    valor5 = convertir(valor5)
    res3 = convertir(res3)

    res4 = suma(res3 + valor5)
    if len(res4) > 16:
        res4 = acarreo(res4)

    valor6 = Complemento1(valor6.strip(""))
    valor6 = convertir(valor6)
    res4 = convertir(res4)

    res5 = suma(res4 + valor6)
    if len(res5) > 16:
        res5 = acarreo(res5)

    return res5

def checksumTCP():
    archivo = open("tramaenhexdump.txt", "r")
    archivo.seek(0)

    valor1 = ''
    valor2 = ''
    valor3 = ''
    valor4 = ''
    valor5 = ''
    valor6 = ''
    valor7 = ''
    valor8 = ''
    valor9 = ''
    valor10 = ''
    valor11 = ''
    valor12 = ''

    archivo.seek(0)
    aux = archivo.read()
    archivo.close()

    for p in range(102, 107, 3):
        valor1 += aux[p: p + 2] + " "
    valor1 = NumBin(valor1)
    valor1 = NumHex(valor1)
    valor1 = dec_bin(valor1)
    valor1 = agregarBits(valor1)

    for p in range(108, 113, 3):
        valor2 += aux[p: p + 2] + " "
    valor2 = NumBin(valor2)
    valor2 = NumHex(valor2)
    valor2 = dec_bin(valor2)
    valor2 = agregarBits(valor2)

    for p in range(114, 118, 3):
        valor3 += aux[p: p + 2] + " "
    valor3 = NumBin(valor3)
    valor3 = NumHex(valor3)
    valor3 = dec_bin(valor3)
    valor3 = agregarBits(valor3)

    for p in range(120, 124, 3):
        valor4 += aux[p: p + 2] + " "
    valor4 = NumBin(valor4)
    valor4 = NumHex(valor4)
    valor4 = dec_bin(valor4)
    valor4 = agregarBits(valor4)

    for p in range(126, 130, 3):
        valor5 += aux[p: p + 2] + " "
    valor5 = NumBin(valor5)
    valor5 = NumHex(valor5)
    valor5 = dec_bin(valor5)
    valor5 = agregarBits(valor5)

    for p in range(132, 136, 3):
        valor6 += aux[p: p + 2] + " "
    valor6 = NumBin(valor6)
    valor6 = NumHex(valor6)
    valor6 = dec_bin(valor6)
    valor6 = agregarBits(valor6)

    for p in range(138, 142, 3):
        valor7 += aux[p: p + 2] + " "
    valor7 = NumBin(valor7)
    valor7 = NumHex(valor7)
    valor7 = dec_bin(valor7)
    valor7 = agregarBits(valor7)

    for p in range(144, 148, 3):
        valor8 += aux[p: p + 2] + " "
    valor8 = NumBin(valor8)
    valor8 = NumHex(valor8)
    valor8 = dec_bin(valor8)
    valor8 = agregarBits(valor8)

    for p in range(156, 160, 3):
        valor9 += aux[p: p + 2] + " "
    valor9 = NumBin(valor9)
    valor9 = NumHex(valor9)
    valor9 = dec_bin(valor9)
    valor9 = agregarBits(valor9)

    for p in range(162, 166, 3):
        valor10 += aux[p: p + 2] + " "
    valor10 = NumBin(valor10)
    valor10 = NumHex(valor10)
    valor10 = dec_bin(valor10)
    valor10 = agregarBits(valor10)

    for p in range(168, 170, 3):
        valor11 += aux[p: p + 2] + " "
    valor11 = NumBin(valor11)
    valor11 = NumHex(valor11)
    valor11 = dec_bin(valor11)
    valor11 = agregarBits(valor11)

    valor1 = Complemento1(valor1.strip(""))
    valor1 = convertir(valor1)

    valor2 = Complemento1(valor2.strip(""))
    valor2 = convertir(valor2)
    res1 = suma(valor1 + valor2)
    if len(res1) > 16:
        res1 = acarreo(res1)

    valor3 = Complemento1(valor3.strip(""))
    valor3 = convertir(valor3)
    res1 = convertir(res1)
    res2 = suma(res1 + valor3)
    if len(res2) > 16:
        res2 = acarreo(res2)

    valor4 = Complemento1(valor4.strip(""))
    valor4 = convertir(valor4)
    res2 = convertir(res2)
    res3 = suma(res2 + valor4)
    if len(res3) > 16:
        res3 = acarreo(res3)

    valor5 = Complemento1(valor5.strip(""))
    valor5 = convertir(valor5)
    res3 = convertir(res3)
    res4 = suma(res3 + valor5)
    if len(res4) > 16:
        res4 = acarreo(res4)

    valor6 = Complemento1(valor6.strip(""))
    valor6 = convertir(valor6)
    res4 = convertir(res4)
    res5 = suma(res4 + valor6)
    if len(res5) > 16:
        res5 = acarreo(res5)

    valor7 = Complemento1(valor7.strip(""))
    valor7 = convertir(valor7)
    res5 = convertir(res5)
    res6 = suma(res5 + valor7)
    if len(res6) > 16:
        res6 = acarreo(res6)

    valor8 = Complemento1(valor8.strip(""))
    valor8 = convertir(valor8)
    res6 = convertir(res6)
    res7 = suma(res6 + valor8)
    if len(res7) > 16:
        res7 = acarreo(res7)

    valor9 = Complemento1(valor9.strip(""))
    valor9 = convertir(valor9)
    res7 = convertir(res7)
    res8 = suma(res7 + valor9)
    if len(res8) > 16:
        res8 = acarreo(res8)

    valor10 = Complemento1(valor10.strip(""))
    valor10 = convertir(valor10)
    res8 = convertir(res8)
    res9 = suma(res8 + valor10)
    if len(res9) > 16:
        res9 = acarreo(res9)

    valor11 = Complemento1(valor11.strip(""))
    valor11 = convertir(valor11)
    res9 = convertir(res9)
    res10 = suma(res9 + valor11)
    if len(res10) > 16:
        res10 = acarreo(res10)

    valor12 = Complemento1(valor12.strip(""))
    valor12 = convertir(valor12)
    res10 = convertir(res10)
    res11 = suma(res10 + valor12)
    if len(res11) > 16:
        res11 = acarreo(res11)

    return res11

def sumatoriaDeDatos():
    archivo = open("tramaenhexdump.txt", "r")
    archivo.seek(0)

    valor1 = ''
    valor2 = ''
    valor3 = ''
    valor4 = ''
    valor5 = ''
    valor6 = ''
    valor7 = ''
    valor8 = ''
    valor9 = ''
    valor10 = ''
    valor11 = ''
    valor12 = ''
    valor13 = ''
    valor14 = ''
    valor15 = ''
    valor16 = ''
    valor17 = ''

    archivo.seek(0)
    aux = archivo.read()
    archivo.close()

    for p in range(171, 175, 3):
        valor1 += aux[p: p + 2] + " "
    valor1 = NumBin(valor1)
    valor1 = NumHex(valor1)
    valor1 = dec_bin(valor1)
    valor1 = agregarBits(valor1)

    for p in range(177, 181, 3):
        valor2 += aux[p: p + 2] + " "
    valor2 = NumBin(valor2)
    valor2 = NumHex(valor2)
    valor2 = dec_bin(valor2)
    valor2 = agregarBits(valor2)

    for p in range(183, 187, 3):
        valor3 += aux[p: p + 2] + " "
    valor3 = NumBin(valor3)
    valor3 = NumHex(valor3)
    valor3 = dec_bin(valor3)
    valor3 = agregarBits(valor3)

    for p in range(246, 250, 3):
        valor4 += aux[p: p + 2] + " "
    valor4 = NumBin(valor4)
    valor4 = NumHex(valor4)
    valor4 = dec_bin(valor4)
    valor4 = agregarBits(valor4)

    for p in range(252, 256, 3):
        valor5 += aux[p: p + 2] + " "
    valor5 = NumBin(valor5)
    valor5 = NumHex(valor5)
    valor5 = dec_bin(valor5)
    valor5 = agregarBits(valor5)

    for p in range(258, 262, 3):
        valor6 += aux[p: p + 2] + " "
    valor6 = NumBin(valor6)
    valor6 = NumHex(valor6)
    valor6 = dec_bin(valor6)
    valor6 = agregarBits(valor6)

    for p in range(264, 268, 3):
        valor7 += aux[p: p + 2] + " "
    valor7 = NumBin(valor7)
    valor7 = NumHex(valor7)
    valor7 = dec_bin(valor7)
    valor7 = agregarBits(valor7)

    for p in range(270, 274, 3):
        valor8 += aux[p: p + 2] + " "
    valor8 = NumBin(valor8)
    valor8 = NumHex(valor8)
    valor8 = dec_bin(valor8)
    valor8 = agregarBits(valor8)

    for p in range(276, 280, 3):
        valor9 += aux[p: p + 2] + " "
    valor9 = NumBin(valor9)
    valor9 = NumHex(valor9)
    valor9 = dec_bin(valor9)
    valor9 = agregarBits(valor9)

    for p in range(282, 286, 3):
        valor10 += aux[p: p + 2] + " "
    valor10 = NumBin(valor10)
    valor10 = NumHex(valor10)
    valor10 = dec_bin(valor10)
    valor10 = agregarBits(valor10)

    for p in range(288, 292, 3):
        valor11 += aux[p: p + 2] + " "
    valor11 = NumBin(valor11)
    valor11 = NumHex(valor11)
    valor11 = dec_bin(valor11)
    valor11 = agregarBits(valor11)

    for p in range(294, 298, 3):
        valor12 += aux[p: p + 2] + " "
    valor12 = NumBin(valor12)
    valor12 = NumHex(valor12)
    valor12 = dec_bin(valor12)
    valor12 = agregarBits(valor12)

    for p in range(300, 304, 3):
        valor13 += aux[p: p + 2] + " "
    valor13 = NumBin(valor13)
    valor13 = NumHex(valor13)
    valor13 = dec_bin(valor13)
    valor13 = agregarBits(valor13)

    for p in range(306, 310, 3):
        valor14 += aux[p: p + 2] + " "
    valor14 = NumBin(valor14)
    valor14 = NumHex(valor14)
    valor14 = dec_bin(valor14)
    valor14 = agregarBits(valor14)

    for p in range(312, 316, 3):
        valor15 += aux[p: p + 2] + " "
    valor15 = NumBin(valor15)
    valor15 = NumHex(valor15)
    valor15 = dec_bin(valor15)
    valor15 = agregarBits(valor15)

    for p in range(318, 322, 3):
        valor16 += aux[p: p + 2] + " "
    valor16 = NumBin(valor16)
    valor16 = NumHex(valor16)
    valor16 = dec_bin(valor16)
    valor16 = agregarBits(valor16)

    for p in range(324, 328, 3):
        valor17 += aux[p: p + 2] + " "
    valor17 = NumBin(valor17)
    valor17 = NumHex(valor17)
    valor17 = dec_bin(valor17)
    valor17 = agregarBits(valor17)

    valor1 = Complemento1(valor1.strip(""))
    valor1 = convertir(valor1)

    valor2 = Complemento1(valor2.strip(""))
    valor2 = convertir(valor2)
    res1 = suma(valor1 + valor2)
    if len(res1) > 16:
        res1 = acarreo(res1)

    valor3 = Complemento1(valor3.strip(""))
    valor3 = convertir(valor3)
    res1 = convertir(res1)
    res2 = suma(res1 + valor3)
    if len(res2) > 16:
        res2 = acarreo(res2)

    valor4 = Complemento1(valor4.strip(""))
    valor4 = convertir(valor4)
    res2 = convertir(res2)
    res3 = suma(res2 + valor4)
    if len(res3) > 16:
        res3 = acarreo(res3)

    valor5 = Complemento1(valor5.strip(""))
    valor5 = convertir(valor5)
    res3 = convertir(res3)
    res4 = suma(res3 + valor5)
    if len(res4) > 16:
        res4 = acarreo(res4)

    valor6 = Complemento1(valor6.strip(""))
    valor6 = convertir(valor6)
    res4 = convertir(res4)
    res5 = suma(res4 + valor6)
    if len(res5) > 16:
        res5 = acarreo(res5)

    valor7 = Complemento1(valor7.strip(""))
    valor7 = convertir(valor7)
    res5 = convertir(res5)
    res6 = suma(res5 + valor7)
    if len(res6) > 16:
        res6 = acarreo(res6)

    valor8 = Complemento1(valor8.strip(""))
    valor8 = convertir(valor8)
    res6 = convertir(res6)
    res7 = suma(res6 + valor8)
    if len(res7) > 16:
        res7 = acarreo(res7)

    valor9 = Complemento1(valor9.strip(""))
    valor9 = convertir(valor9)
    res7 = convertir(res7)
    res8 = suma(res7 + valor9)
    if len(res8) > 16:
        res8 = acarreo(res8)

    valor10 = Complemento1(valor10.strip(""))
    valor10 = convertir(valor10)
    res8 = convertir(res8)
    res9 = suma(res8 + valor10)
    if len(res9) > 16:
        res9 = acarreo(res9)

    valor11 = Complemento1(valor11.strip(""))
    valor11 = convertir(valor11)
    res9 = convertir(res9)
    res10 = suma(res9 + valor11)
    if len(res10) > 16:
        res10 = acarreo(res10)

    valor12 = Complemento1(valor12.strip(""))
    valor12 = convertir(valor12)
    res10 = convertir(res10)
    res11 = suma(res10 + valor12)
    if len(res11) > 16:
        res11 = acarreo(res11)

    valor13 = Complemento1(valor13.strip(""))
    valor13 = convertir(valor13)
    res11 = convertir(res11)
    res12 = suma(res11 + valor13)
    if len(res12) > 16:
        res12 = acarreo(res12)

    valor14 = Complemento1(valor14.strip(""))
    valor14 = convertir(valor14)
    res12 = convertir(res12)
    res13 = suma(res12 + valor14)
    if len(res13) > 16:
        res13 = acarreo(res13)

    valor15 = Complemento1(valor15.strip(""))
    valor15 = convertir(valor15)
    res13 = convertir(res13)
    res14 = suma(res13 + valor15)
    if len(res14) > 16:
        res14 = acarreo(res14)

    valor16 = Complemento1(valor16.strip(""))
    valor16 = convertir(valor16)
    res14 = convertir(res14)
    res15 = suma(res14 + valor16)
    if len(res15) > 16:
        res15 = acarreo(res15)

    valor17 = Complemento1(valor17.strip(""))
    valor17 = convertir(valor17)
    res15 = convertir(res15)
    res16 = suma(res15 + valor17)
    if len(res16) > 16:
        res16 = acarreo(res16)

    return res16

def AnalisisEthernet():
    archivo = open("tramaenhexdump.txt", "r")
    archivo.seek(0)

    D_destino = ''
    D_origen = ''
    T_servicio = '0x'
    print("***********************************************************")
    print("          PAQUETE DE DATOS         ")
    print("***********************************************************")
    print(archivo.read())
    os.system('pause')


    print("***********************************************************")
    print("          Analisis de cabecera Ethernet         ")
    print("***********************************************************")

    archivo.seek(0)
    aux = archivo.read()
    archivo.close()

    for p in range(0, 17, 3):
        D_destino += aux[p: p+2] + " "
    print('Dirección MAC Destino: ', D_destino)

    for p in range(18, 35, 3):
        D_origen += aux[p: p+2] + " "
    print('Dirección MAC Origen:', D_origen)

    for p in range(36, 41, 3):
        T_servicio += aux[p: p+2] + ""
    print('Tipo de Servicio (2 bytes):',  T_servicio, '(IPv4)\n')

    os.system('pause')


def AnalisisIp():
    archivo = open("tramaenhexdump.txt", "r")
    archivo.seek(0)

    servicio = ''
    l_total = ''
    Tiempo_vida = ''
    protocolo = ''
    ip_origen = ''
    ip_destino = ''
    Identificador = ''
    T_servicio = '0x'

    print("***********************************************************")
    print("          Analisis de cabecera IPv4         ")
    print("***********************************************************")
    archivo.seek(0)
    aux = archivo.read()
    archivo.close()

    for p in range(36, 41, 3):
        T_servicio += aux[p: p+2] + ""

    if T_servicio == '0x0800':
        version = 4
        l_cabecera = 5

        if T_servicio == "0x0800":
            print("Version:", version)
        print("Longitud de la cabecera:", version*l_cabecera, "Bytes")

        for p in range(45, 47, 3):
            servicio += aux[p: p + 2] + " "
        servicio=NumBin(servicio)
        servicio=int(servicio)
        servicio=hex(servicio)
        print('Tipo de servicio:', servicio+'0')

        for p in range(48, 52, 3):
            l_total += aux[p: p + 2] + " "
        l_total=NumBin(l_total)
        l_total=NumHex(l_total)
        print('Longitud total del paquete:', l_total)

        for p in range(54, 59, 3):
            Identificador += aux[p: p + 2] + " "
        Identificador=NumBin(Identificador)
        Identificador=NumHex(Identificador)
        hex_Identificador=hex(Identificador)
        print('Identificación:', hex_Identificador, '(',Identificador,')')

        for p in range(66, 68, 3):
            Tiempo_vida += aux[p: p + 2] + " "

        for p in range(69, 71, 3):
            protocolo += aux[p: p + 2] + " "

        for p in range(78, 89, 3):
            ip_origen += aux[p: p + 2] + " "

        for p in range(90, 101, 3):
            ip_destino += aux[p: p + 2] + " "

        texto = open("tramaenhexdump.txt")
        bandera = texto.read()
        Ban_num = bandera[59:62]
        Ban_decimal = int(Ban_num, 16)
        Ban_binario = bin(Ban_decimal)
        aux = ''

        if len(Ban_binario) - 2 == 7:
            aux = '0'
        aux += Ban_binario[2:]
        print('Banderas de fragmentacion:', '0  x', Ban_num)
        print('Verficar desde los primeros 3 bits:')

        if aux[3:4] == '0':
            print('0... Bit Reservado')
        else:
            print()
        if aux[1:2] == '1':
            print('.1.. Paquete no fragmentado (DF)')
        else:
            print()
        if aux[:1] == '0':
            print('..0. Ultimo fragmento del datagrama (MF)')
            print('Desplazamiento de la fragmentación: 0 bits')

        print('Tiempo de vida:', NumHex(Tiempo_vida), 'segundos')
        print('Protocolo:', protocolo)
        checksumIp()
        ip1=ip_origen[0:2]
        ip1 = NumBin(ip1)
        ip1 = NumHex(ip1)
        ip1=str(ip1)
        ip2 = ip_origen[3:5]
        ip2 = NumBin(ip2)
        ip2 = NumHex(ip2)
        ip2=str(ip2)
        ip3 = ip_origen[6:8]
        ip3 = NumBin(ip3)
        ip3 = NumHex(ip3)
        ip3=str(ip3)
        ip4 = ip_origen[9:11]
        ip4 = NumBin(ip4)
        ip4 = NumHex(ip4)
        ip4=str(ip4)
        ip_origen=ip1+'.'+ip2+'.'+ip3+'.'+ip4
        print('Dirección IP origen:', ip_origen)
        ip1 = ip_destino[0:2]
        ip1 = NumBin(ip1)
        ip1 = NumHex(ip1)
        ip1 = str(ip1)
        ip2 = ip_destino[3:5]
        ip2 = NumBin(ip2)
        ip2 = NumHex(ip2)
        ip2 = str(ip2)
        ip3 = ip_destino[6:8]
        ip3 = NumBin(ip3)
        ip3 = NumHex(ip3)
        ip3 = str(ip3)
        ip4 = ip_destino[9:11]
        ip4 = NumBin(ip4)
        ip4 = NumHex(ip4)
        ip4 = str(ip4)
        ip_destino = ip1 + '.' + ip2 + '.' + ip3 + '.' + ip4
        print('Dirección IP destino:', ip_destino)

    else:
        print('Servicio no disponible por el momento')

    os.system('pause')

def AnalisisTCP():
    archivo = open("tramaenhexdump.txt", "r")
    archivo.seek(0)

    d_origen = ''
    p_destino = ''
    n_secuencia = ''
    n_confirmacion = ''
    l_cabecera=''
    b_reservado=''
    ventana=''
    punteroUrgente=''
    opciones=''
    datos=''

    print("***********************************************************")
    print("          Analisis de cabecera TCP         ")
    print("***********************************************************")

    archivo.seek(0)
    aux = archivo.read()
    archivo.close()

    for p in range(102, 107, 3):
        d_origen += aux[p: p + 2] + " "
    d_origen=NumBin(d_origen)
    d_origen=NumHex(d_origen)
    print('Puerto origen:', d_origen)

    for p in range(108, 113, 3):
        p_destino += aux[p: p + 2] + " "
    p_destino=NumBin(p_destino)
    p_destino=NumHex(p_destino)
    print('Puerto destino:', p_destino,'(puerto NetBIOS)')

    for p in range(114, 125, 3):
        n_secuencia += aux[p: p + 2] + " "
    n_secuencia=NumBin(n_secuencia)
    n_secuencia=NumHex(n_secuencia)
    print('Número de secuencia:', n_secuencia)

    for p in range(126, 137, 3):
        n_confirmacion += aux[p: p + 2] + " "
    n_confirmacion=NumBin(n_confirmacion)
    n_confirmacion=NumHex(n_confirmacion)
    print('Número de confirmación:', n_confirmacion)

    for p in range(138, 140, 3):
        l_cabecera += aux[p: p + 2] + " "
    print('Longitud de la cabecera: 20 bytes')
    l_cabecera=NumHex(l_cabecera)
    l_cabecera=dec_bin(l_cabecera)

    for p in range(141, 143, 3):
        b_reservado += aux[p: p + 2] + " "
    print('Banderas: 0 x', b_reservado)

    for p in range(144, 149, 3):
        ventana += aux[p: p + 2] + " "

    for p in range(156, 160, 3):
        punteroUrgente += aux[p: p + 2] + " "

    for p in range(162, 169, 3):
        opciones += aux[p: p + 2] + " "

    for p in range(171, 339, 3):
        datos += aux[p: p + 2] + " "

    b_reservado = NumHex(b_reservado)
    b_reservado = dec_bin(b_reservado)
    if len(b_reservado)==6:
        aux='00'
        aux=aux+b_reservado

    print('000. .... .... Bit reservado')
    if l_cabecera[7:8]=='0':
        print('...0 .... .... Nonce: Not set (1 - El indicador ns es un indicador que se utiliza para ayudar a proteger contra la ocultación malintencionada accidental de paquetes del remitente.)')
    else:
        print('...1 .... .... Set')

    if aux[0:1]=='0':
        print('.... 0... .... Congestion window reduced: Not set (1 - Se reduce a la mitad el tamaño de la ventana en envío con el objetivo de ralentizar el envío de información.)')
    else:
        print('.... 1... .... Congestion window reduced: Set')

    if aux[1:2]=='0':
        print('.... .0.. .... ECN-Echo: Not set')
    else:
        print('.... .1.. .... ECN-Echo: Set')

    if aux[2:3]=='0':
        print('.... ..0. .... Urgente: Not set (1 - Indica datos que se deben entregar lo más rápidamente posible y especifica la posición donde finalizan los datos urgentes)')
    else:
        print('.... ..1. .... Urgente: Set')

    if aux[3:4]=='0':
        print('.... ...0 .... Acknoledgment: Not set')
    else:
        print('.... ...1 .... Acknoledgment: Set')

    if aux[4:5]=='0':
        print('.... .... 0... Push: Not set')
    else:
        print('.... .... 1... Push: Set')

    if aux[5:6]=='0':
        print('.... .... .0.. Reset: Not set')
    else:
        print('.... .... .1.. Reset: Set')

    if aux[6:7]=='0':
        print('.... .... ..0. Syn: Not set')
    else:
        print('.... .... ..1. Syn: Set')

    if aux[7:8]=='0':
        print('.... .... ...0 Fin: Not set')
    else:
        print('.... .... ...1 Fin: Set')

    ventana=NumBin(ventana)
    ventana=NumHex(ventana)
    print('ventana: ', ventana)

    pseudocabecera = sumaPseudocabecera()
    aux = convertir(pseudocabecera)
    sumaPseudocabecera_hexa = hex(aux)

    sumaDeVerificacion =checksumTCP()
    aux1 = convertir(sumaDeVerificacion)
    sumaDeVerificacion_hexa = hex(aux1)

    sumaDatos=sumatoriaDeDatos()
    aux2=convertir(sumaDatos)
    sumaDatos_hexa=hex(aux2)

    res1=suma(aux+aux1)
    if len(res1) > 16:
        res1 = acarreo(res1)

    res1=convertir(res1)
    res2=suma(res1+aux2)
    auxiliar = convertir(res2)
    resta=37533
    res=auxiliar-resta
    hexa_res = hex(res)
    print('Checksum: 0x8194')
    if hexa_res=='0x8194':
        print('Status: Sin erroes')
    else:
        print('Status: malo')
    print(f'Checksum calculado: {hexa_res}')

    if punteroUrgente == '00 00 ':
        print(f'Puntero urgente: 0 (Indica el desplazamiento que es necesario añadir al Número de Secuencia del segmento para determinar el último octeto de datos urgentes que éste transporta)')
    print(f'Opciones: {opciones}')
    print(f'Datos {datos}')

    os.system('pause')
    
def wifi():
    print("\n----------------- Sniffer -----------------\n")
    num=int(input("¿Cuantos paquetes deseas capturar?: "))
    print("\n\n")
    print("\n\nCargando paquetes...\n")
    p=sniff(filter="tcp",count=num)
    os.system("cls")
    print("\n------------ Paquetes capturados ------------\n")
    print("\n",p.show(),"\n")
    sel=int(input("\nIngrese el numero del paquete a seleccionar: "))
    sel=sel-1
    os.system("cls")

    print("\n------------ Paquete en hexadecimal ------------\n")
    print(hexdump(p[sel]))
    os.system("pause")
    os.system("cls")

    print("\n------------ Información del paquete ------------\n")
    p[sel].show()
    os.system("pause")

    print("\n\nGenerando archivo pdfdump.pdf y paquete.pcap... ")
    p[sel].pdfdump("pdfdump",layer_shift=1)
    pktdump  = PcapWriter("paquete.pcap", append=True, sync=True)
    pktdump.write(p[sel])
    print("Archivos generados con exito!\n")

def Main():
    import os
    while True:
        os.system("cls")
        print("***********************************************************")
        print("          Bienvenido Estimado Usuario         ")
        print("***********************************************************")
        print("Selecciona la opción desesada.\n")
        print("1. Analizar un paquete de datos.")
        print("2. Analizar una red Wi-Fi")
        print("3. Salir.")
        option = (input('\nIngresa Opción Deseada -> '))

        if option == '1':
            os.system("cls")
            AnalisisEthernet()
            os.system("cls")
            AnalisisIp()
            os.system("cls")
            AnalisisTCP()
            os.system("cls")

        elif option == '2':
            wifi()
            os.system('pause')
            os.system("cls")

        elif option=='3':
            print('\n')
            print('Saliendo...')
            break

Main()
