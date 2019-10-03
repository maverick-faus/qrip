import numpy as np

def form(str): #Formato de String de Regex
    if(str==""):
        return ""
    else:
        if(len(str)==1):
            return str
        else:
         return "("+str+")"
     
     
s={1,2}
alfabeto={'a','b'}
inicial=1
aceptacion={2}
transiciones={
    (1,'a',1),
    (1,'b',2),
    (2,'a',2),
    (2,'b',2)
}

 
     
''' Ejemplo de la figura 1.69 del Sipser
s={1,2,3}
alfabeto={'a','b'}
inicial=1
aceptacion={2,3}
transiciones={
    (1,'a',2),
    (1,'b',3),
    (2,'a',1),
    (2,'b',2),
    (3,'a',2),
    (3,'b',1)
}
'''

noEStados=len(s)
m = np.full((noEStados+2,noEStados+2), "",dtype=np.dtype('U1000')) 

for t  in transiciones:
    if  m[t[0]][t[2]]!= "":
        aux=m[t[0]][t[2]]
        aux=aux+'|'+t[1]
        m[t[0]][t[2]]=aux
    else:
        m[t[0]][t[2]]= t[1]

#Aislamos estado de inicio
m[0][inicial]='e'
inicial=0

#Aislamos estados de aceptacion
nuevoAceptacion=noEStados+1

for estado in aceptacion:
    m[estado][nuevoAceptacion]='e'

#Creamos un conjunto con los nuevos estados
news=set()
for elem in s:
    news.add(elem)
news.add(0) #Agregamos el nuevo estado de inicio
news.add(nuevoAceptacion) #Agregamos el nuevo estado de aceptacion


for qk in s: #Para cada estado original
    qrip=qk
    news.remove(qrip)
    for qi in news:
        for qj in news:
            if not((qi)==nuevoAceptacion or qj == inicial):
               # print(qrip,qi,qj)
                r1 = m[qi][qrip]
                r2 = m[qrip][qrip]
                r3 = m[qrip][qj]
                r4 = m[qi][qj]
                
                #Formato del string de la Regex
                if(r1=='e'):r1=""
                if not(r2==''): r2=form(r2)+"*"
                if(r3=='e'):r3=""
                if not(r4=='') and not(form(r1)+r2+form(r3)=='') : r4="|"+form(r4)
                
                newregex=form(r1)+r2+form(r3)+r4
                m[qi][qj]=newregex 
    m[qrip] = np.full(noEStados+2 , "",dtype=np.dtype('U1000')) 
    m[:, qrip] =  ""            
print (m[inicial][nuevoAceptacion])
