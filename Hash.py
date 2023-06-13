import random
def cezar_enscrypt(message:str, shift:int):
    encrypted_message = ""
    new_position = 0
    for x in message:
        if x.isalpha() != True:
            encrypted_message += x 
        else:
            new_position = shift + ord(x)
            if new_position >= ord("z"):
                new_position = (ord(x) - ord("a") + shift)%26+ord("a")
                encrypted_message += chr(new_position)
                new_position = 0
            elif new_position < ord("z"):
                encrypted_message += chr(new_position)
            new_position= 0
    return encrypted_message    

def keyf() :
    key = {}
    alphabet = []
    for x in range(65,90):
        alphabet.append(chr(x))
    for x in range(97,122):
        alphabet.append(chr(x))
    alphabet2 = alphabet.copy()
    for x in range(len(alphabet)):
        temp = alphabet2[random.randint(0,len(alphabet2)-1)]
        key[alphabet[x]] = temp
        alphabet2.remove(temp)
    return key

def substitution_encrypt(message):
    encrypted_message = []
    temp1 = ""
    key = keyf()
    for ch in message:
        if ch.isalpha() != True:
            encrypted_message.append(ch)
        else:
            temp = key[ch]
            encrypted_message.append(temp) 
            
    for x in encrypted_message:
        temp1 += x 
    return temp1       
        
print(substitution_encrypt("lista"))

        
