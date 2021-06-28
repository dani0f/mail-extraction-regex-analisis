import re

#código basado de https://github.com/benstreb/regex-generator

def generate_regex(samples):
    characters_list = []
    for sample in samples:
        characters_list = extend_characters_list(characters_list, len(sample))
        for i, character in enumerate(sample):
            characters_list[i].add(character)
    return "".join(display_group(characters) for characters in characters_list)

def display_group(characters):
    if len(characters) == 1:
        template = "{}"
    else:
        template = "[{}]"
    return template.format("".join(sorted(characters)))


def extend_characters_list(characters_list, length):
    extension_length = max(length - len(characters_list), 0)
    return characters_list + [set() for i in range(extension_length)]

#Código para reducir el regex generado

def dif(str1,str2):
    minS = str1
    maxS = str2
    if(len(str1) > len(str2)):
        minS=str2
        maxS=str1
    num = len(minS)
    for i in range(num):
        maxS=maxS.replace(minS[i],"", 1)
    return(maxS)

def reduceRegex(resultArray):
    arraySintax= []
    for i in range(len(resultArray)):
        sintax=""
        if(resultArray[i][0] == "["):
            if(len(resultArray[i][1:]) > 5 ):
                stringAux = resultArray[i][1:]
                if(stringAux.isdigit()):
                    sintax= "\d"
                if(stringAux.isupper() and sintax==""):
                    sintax= "A-Z"
                if(stringAux.islower() and sintax==""):
                    sintax= "a-z"
                if(bool(re.search(r'[^A-Za-z0-9]', stringAux)) and sintax==""):
                    specialC =""
                    specialCArray=re.findall(r'[^A-Za-z0-9]', stringAux)
                    for c in specialCArray:
                        specialC= specialC +c
                    sintax = "a-zA-Z0-9"+specialC
                elif(sintax==""):
                    sintax= "^A-Za-z0-9"
                sintax = "["+sintax+"]"
            else:
                sintax = resultArray[i]+"]"
        else:
            arrayAux= resultArray[i].split("[")
            if( len(arrayAux) > 1):
                sintax=arrayAux[0]+"["+arrayAux[1]+"]"
            else:
                sintax=arrayAux[0]
        arraySintax.append(sintax)

    resFinalStr=""
    a=0
    while(a < len(arraySintax)):
        numAgrup = 0
        if(arraySintax[a][0]=="["):
            agrupFinal =""
            for b in range(a,len(arraySintax)):
                resDif=dif(arraySintax[a],arraySintax[b])
                cond = 0
                if(len(resDif) < 4):
                    if(len(arraySintax[a]) == len(arraySintax[b])):
                        if(len(resDif)!= 0):
                            arraySintax[a] = arraySintax[a][:-1] + resDif + "]"
                            cond = 1
                        numAgrup =numAgrup + 1                
                    if((len(arraySintax[a])> len(arraySintax[b])) and cond == 0):
                        arraySintax[a] = arraySintax[b][:-1]+resDif+"]"
                        numAgrup = numAgrup +1
                    if((len(arraySintax[a])< len(arraySintax[b])) and cond == 0):
                        arraySintax[a] = arraySintax[a][:-1]+resDif+"]"
                        numAgrup = numAgrup +1
                else:
                    agrupFinal = r"{"+ str(numAgrup) +r"}"
                    if(numAgrup == 1):
                        agrupFinal=""
                    arraySintax[a]=arraySintax[a]+agrupFinal
                    break
        resFinalStr = resFinalStr + arraySintax[a]
        if(numAgrup >0):
            a=a+numAgrup
        else:
            a=a+1

    return(resFinalStr)


def getRegexIdFile(namefile): 
    f = open (namefile,'r')
    msg = f.read()
    msgArray = msg.split()
    f.close()
    result = generate_regex(msgArray)
    result2 = reduceRegex(result.split("]"))
    return(result2)

def getRegexId(msgArray): 
    result = generate_regex(msgArray)
    result2 = reduceRegex(result.split("]"))
    return(result2)

#A partir de un archivo:
#a=getRegexIdFile("entrenamiento.txt")
#print(a)

#A partir de un arreglo
#a=getRegexId(["holaaa423423423","hola4343424332"])
#print(a)