print ("\nConversor de Bases")

while (True): 
 print ("\nEscolha a opção desejada;")
 op = int(input("Digite: \n   • [1] Decimal para Binário \n   • [2] Decimal para Octal \n   • [3] Decimal para Hexadecimal \n   • [4] Binário para Octal \n   • [5] Binário para Hexadecimal\n   • [6] Hexadecimal para Binário\n   • [7] Hexadecimal para Octal\n   • [8] Octal para Binário\n   • [9] Octal para Hexadecimal\n  Sua opção : "))
 if op == 1:
   junta = ""
   base = 2
   num = int(input("\nInforme o número decimal: "))
   while (num >= base):
     resto = num % base
     junta = junta + str(resto)
     num = num // base
   junta = junta + str (num) 
   print ("Esse número convertido para Binário é: " + junta [::-1] )  
 elif op == 2:
   junta = ""
   base = 8
   num = int(input("\nInforme o número decimal: "))
   while (num >= base):
     resto = num % base
     junta = junta + str(resto)
     num = num // base
   junta = junta + str (num) 
   print ("Esse número convertido para Octal é: " + junta [::-1] )      
 elif op == 3:
   junta = ""
   base = 16
   num = int(input("\nInforme o número decimal: "))
   o = num
   while (num >= base):
     resto = num % base
     if (resto == 10):
       resto = "A"
     elif (resto == 11):
       resto = "B"
     elif (resto == 12):
       resto = "C"
     elif (resto == 13):
       resto = "D"
     elif (resto == 14):
       resto = "E"
     elif (resto == 15):
       resto = "F"
     junta = junta + str(resto)
     num = num // base
   junta = junta + str(num) 
   if (o < base):
      if (num == 10):
        num = str("A") 
      elif (num == 11):
        num = str("B")
      elif (num == 12):
        num = str("C")
      elif (num == 13):
        num = str("D")
      elif (num == 14):
        num = str("E")
      elif (num == 15):
        num = str("F")
      print("Essse número convertido para hexadecimal é " + str(num)[::-1]) 
   if (o >= base):
      print ("Esse número convertido para Hexadecimal é: " + junta [::-1] )
 elif op == 4 :
    num = str(input("\nInforme o número binário: "))
    tamanho = len(num)
    divisao = tamanho % 3
    faltam  = 3 - divisao
    partes  = "0" * faltam
    num     = partes + num
    octal   = ""
    for i in range (0,len(num),3):
      bloco = num[i:i+3:1]
      if bloco =="000":
        octal = octal + str(0)
      if bloco == "001":
        octal = octal + str(1)
      if bloco == "010":
        octal = octal + str(2)
      if bloco == "011":
        octal = octal + str(3)
      if bloco == "100":
        octal = octal + str(4)
      if bloco == "101":
        octal = octal + str(5)
      if bloco == "110":
        octal = octal + str(6)
      if bloco == "111":
        octal = octal + str(7)
    print ("Esse número convertido para Octal é:",octal,)  
 elif op == 5 :
    num = str(input("\nInforme o número Binário: "))
    tamanho = len(num)
    divisao = tamanho % 4
    faltam  = 4 - divisao
    partes  = "0" * faltam
    num     = partes+num
    hexadecimal   = ""
    for i in range (0,len(num),4):
      bloco = num[i:i+4:1]
      if bloco =="0000":
        hexadecimal = hexadecimal + str(0)
      if bloco == "0001":
        hexadecimal = hexadecimal + str(1)
      if bloco == "0010":
        hexadecimal= hexadecimal + str(2)
      if bloco == "0011":
        hexadecimal = hexadecimal + str(3)
      if bloco == "0100":
        hexadecimal = hexadecimal + str(4)
      if bloco == "0101":
        hexadecimal = hexadecimal + str(5)
      if bloco == "0110":
        hexadecimal = hexadecimal + str(6)
      if bloco == "0111":
        hexadecimal = hexadecimal + str(7)
      if bloco == "1000":
        hexadecimal = hexadecimal + str(8)
      if bloco == "1001":
        hexadecimal = hexadecimal +str(9)
      if bloco == "1010":
        hexadecimal = hexadecimal + str("A")
      if bloco == "1011":
        hexadecimal = hexadecimal + str("B")
      if bloco == "1100":
        hexadecimal = hexadecimal + str("C")
      if bloco == "1101":
        hexadecimal = hexadecimal + str("D")
      if bloco == "1110":
        hexadecimal = hexadecimal + str("E")
      if bloco == "1111":
        hexadecimal = hexadecimal + str("F")
    print ("Esse número convertido para Hexadecimal é:",hexadecimal,)
 elif op == 6 :
  num = str(input("\nInforme o número Hexadecimal: ")).upper()
  binario = ""
  for i in range (0,len(num),1):
    bloco = num[i:i+1:1]
    if bloco == "0":
      binario = binario + str("0000")
    if bloco == "1":
      binario = binario + str("0001")
    if bloco == "2":
      binario = binario + str("0010")
    if bloco == "3":
      binario = binario + str("0011")
    if bloco == "4":
      binario = binario + str("0100")
    if bloco == "5":
      binario = binario + str("0101")
    if bloco == "6":
      binario = binario + str("0110")
    if bloco == "7":
      binario = binario + str("0111")
    if bloco == "8":
      binario = binario + str("1000")
    if bloco == "9":
      binario = binario + str("1001")
    if bloco == "A":
      binario = binario + str("1010")
    if bloco == "B":
      binario = binario + str("1011")
    if bloco == "C":
      binario = binario + str("1100")
    if bloco == "D":
      binario = binario + str("1101")
    if bloco == "E":
      binario = binario + str("1110")
    if bloco == "F":
      binario = binario + str("1111")
  print ("Esse número convertido para Binário é:",binario,)  
 elif op == 7 :
   print ("oi")
   numHexadecimal = str(input("\nInforme o número hexadecimal: ")).upper()
   numInvertido = numHexadecimal[::-1]
   base = 16
   somaDecimal = 0
   tamanho = len(numInvertido)
   temErro = False
   for i in range(0, tamanho):
    caractere = str(numInvertido[i])
    if caractere.isdigit():
      numero = int(caractere)
    elif caractere == 'A':
      numero = 10
    elif caractere == 'B':
      numero = 11
    elif caractere == 'C':
      numero = 12
    elif caractere == 'D':
      numero = 13
    elif caractere == 'E':
      numero = 14
    elif caractere == 'F':
      numero = 15
    else:
      print("\nTem um caractere inválido: ", caractere)
      temErro = True
      break
    somaDecimal += (numero * (base ** i))
   if not temErro:
    junta = ""
    base2 = 8
    num = somaDecimal
    while (num >= base):
      resto = num % base2
      junta = junta + str(resto)
      num = num // base2
    junta = junta + str (num) 
    print ("Esse número convertido para Octal é: " + junta [::-1] )      
 elif op == 8 :
   num = str(input("\nInforme o número Octal: "))
   octal = ""
   for i in range (0,len(num),1):
    bloco = num[i:i+1:1]
    if bloco == "0":
      octal = octal + str("000")
    if bloco == "1":
      octal = octal + str("001")
    if bloco == "2":
      octal = octal + str("010")
    if bloco == "3":
      octal = octal + str("011")
    if bloco == "4":
      octal = octal + str("100")
    if bloco == "5":
      octal = octal + str("101")
    if bloco == "6":
      octal = octal + str("110")
    if bloco == "7":
      octal = octal + str("111")
   print ("Esse número convertido para Binário é:",octal,)  
 elif op == 9:
  num = str(input("\nInforme o número Octal: "))
  octal = ""
  for i in range (0,len(num),1):
    bloco = num[i:i+1:1]
    if bloco == "0":
      octal = octal + str("000")
    if bloco == "1":
      octal = octal + str("001")
    if bloco == "2":
      octal = octal + str("010")
    if bloco == "3":
      octal = octal + str("011")
    if bloco == "4":
      octal = octal + str("100")
    if bloco == "5":
      octal = octal + str("101")
    if bloco == "6":
      octal = octal + str("110")
    if bloco == "7":
      octal = octal + str("111")
  num2 = octal
  tamanho = len(num2)
  divisao = tamanho % 4
  faltam  = 4 - divisao
  partes  = "0" * faltam
  num2     = partes + num2
  hexadecimal   = ""
  for i in range (0,len(num2),4):
    bloco = num2[i:i+4:1]
    if bloco =="0000":
      hexadecimal = hexadecimal + str(0)
    if bloco == "0001":
      hexadecimal = hexadecimal + str(1)
    if bloco == "0010":
      hexadecimal= hexadecimal + str(2)
    if bloco == "0011":
      hexadecimal = hexadecimal + str(3)
    if bloco == "0100":
      hexadecimal = hexadecimal + str(4)
    if bloco == "0101":
      hexadecimal = hexadecimal + str(5)
    if bloco == "0110":
      hexadecimal = hexadecimal + str(6)
    if bloco == "0111":
      hexadecimal = hexadecimal + str(7)
    if bloco == "1000":
      hexadecimal = hexadecimal + str(8)
    if bloco == "1001":
      hexadecimal = hexadecimal +str(9)
    if bloco == "1010":
      hexadecimal = hexadecimal + str("A")
    if bloco == "1011":
      hexadecimal = hexadecimal + str("B")
    if bloco == "1100":
      hexadecimal = hexadecimal + str("C")
    if bloco == "1101":
      hexadecimal = hexadecimal + str("D")
    if bloco == "1110":
      hexadecimal = hexadecimal + str("E")
    if bloco == "1111":
      hexadecimal = hexadecimal + str("F")
  print ("Esse número convertido para Hexadecimal é:",hexadecimal,)