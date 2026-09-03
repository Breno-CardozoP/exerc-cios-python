text=input("insira uma linha de texto: ")

cipher=""

into=False
while(into==False):

    intervalo = int(input("insira um intervalo de troca(1-25): "))
    if (intervalo<1 or intervalo>25):
        print("numero invalido")
    else:into=True

for char in text:
    if char.isalpha():
        code = ord(char) + intervalo
        if(ord(char)>64 and ord(char)<91):
            if code>ord('Z'):
                code-=ord('Z')
                code=ord('@')+code
            
        if code>ord('z'):
            code-=ord('z')
            code=ord('`')+code
            
        cipher+=chr(code)
            
    else:
        cipher+=char

   

print(cipher)

    
        
    

