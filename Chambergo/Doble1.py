#Programa 01
import os
medicamento,cant_de_medicamento_por_dia="",0

#INPUT VIA OS
medicamento=os.sys.argv[1]
cant_de_medicamento_por_dia=int(os.sys.argv[2])

#PROCESSING
#Si el numero de medicamento supera 15, mostrar "automedicacion"
#Caso contrario mostar "medicacion normal"
if(cant_de_medicamento_por_dia > 15 ):
    print(medicamento, "automedicacion")
else:
    print(medicamento,"medicacion normal")
#fin_if

