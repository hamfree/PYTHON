dic = {}
fichero=open('Persona.txt','r')
for linea in fichero:
        persona=linea.split('$')
        personasinnombre=[persona[1],persona[2],persona[3]]
        dic[persona[0]] = personasinnombre 
print dic