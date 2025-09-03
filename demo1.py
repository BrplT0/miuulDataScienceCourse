message = "hello, my name is berat. i am the one who works on this project"
newMessage = []

for i in range(0,len(message)):
    chir = message[i]
    if i % 2 == 0:
        chars = chir.upper()
    else:
        chars = chir.lower()
    newMessage.append(chars)

newMessage = "".join(newMessage)
print(newMessage)