#caesar cypher with the additional condition of: every char in an even 
#position should use a key of 3 and every char in an odd position
#should use a key of 4.

#get the input
plain_text = input("plain text: ")
cypher_text = []
#get the key
key = int(input("key: "))

#cypher 
for i in plain_text:
    if plain_text[i].isalpha():
        cypher_text[i] = plain_text[i] + 1
    else:
        

print(str(cypher_text))

#show the new ouput