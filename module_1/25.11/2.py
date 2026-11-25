alphabet="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz "

a=input("message:")

def encrypt(text, key):
    result=[]
    for i in text:
        index = alphabet.index(i)
        new_index = (index + (key*2)) % len(alphabet)
        result.append(alphabet[new_index])

    return "".join(result)

print(encrypt(a, 2))

def decrypt(text, key):
    result=[]
    for i in text:
        index = alphabet.index(i)
        new_index = (index - (key*2)) % len(alphabet)
        result.append(alphabet[new_index])

    return "".join(result)

key=int(input("key"))

a=input("message:")

print(decrypt(a, key))