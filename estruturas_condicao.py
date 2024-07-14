import math
import decimal

value = float(input( "digite seu número real:"))
number = float(value)
round(value,2)

def decToBin(number,base, precision):
  number= str(number)
  parte_inteira = int( number[ : number.index(".") ] )
  parte_fracionada = float( number[ number.index(".") : ] )

  output = ""

  while parte_inteira !=0:
    output = str ( parte_inteira % base) + output
    parte_inteira //= base
  if parte_fracionada == 0:
      return output

  output += "."
  while parte_fracionada !=0 and precision != 0 :
       parte_fracionada *= base
       parte_fracionada_string = str(parte_fracionada)
       output += parte_fracionada_string[ : parte_fracionada_string.index(".") ]
       parte_fracionada = float( parte_fracionada_string[ parte_fracionada_string.index(".") : ] )
       precision -= 1
  return output

print ("Conversão para base binária: ", "%.2f" %value , "é" , decToBin(value, 2, 10) )