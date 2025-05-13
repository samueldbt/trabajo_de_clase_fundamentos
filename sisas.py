#caesar cypher with the additional condition of: every char in an even 
#position should use a key of 3 and every char in an odd position
#should use a key of 4.

#get the input
plain_text = input("plain text: ")
cypher_text = []
#get the key
key = int(input("key: "))

#cypher 
for idx, i in enumerate(plain_text):
    if idx % 2 == 0:
        key = 3
    else:
        key = 4

    if i.isalpha():
        if i.isupper():
            cb = ord(i) - ord("A") #give the char its respective base for transforming
            nueva_letra = cb + key #in this part transform the char with the respective key
            cbp = nueva_letra % 26 #makes sure its inside the bounds
            cypher_text.append(chr(cbp + ord("A")))
        elif i.islower():
            cb = ord(i) - ord("a") #give the char its respective base for transforming
            nueva_letra = cb + key #in this part transform the char with the respective key
            cbp = nueva_letra % 26 #makes sure its inside the bounds
            cypher_text.append(chr(cbp + ord("a"))) #adds the new char in the string giving again the base to the char
    else:
        cypher_text.append(i)

cypher_text = "".join(cypher_text)
print(cypher_text)