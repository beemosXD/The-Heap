def decodestring(enstring):
    decstring = enstring.split("0")
    decodedcit = {}
    for i in range(0,len(decstring)):
        if decstring[i] != "":
            
            if i == 0:
                decodedcit["first_name"]  = decstring[i]
            elif i == len(decstring)-1 :    
                decodedcit["id"]  = decstring[i] 
            else:
                decodedcit["last_name"]  = decstring[i]


    return decodedcit

print(decodestring("Robert00Smith000123"))

