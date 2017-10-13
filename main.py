message = input('Enter message to encrypt:' )
translation = ''

i = len(message) - 1
while i >=  0 :
    translation += message[i]
    i -= 1
print(translation)
