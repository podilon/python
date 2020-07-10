# função Delta
def calc_delta(x,y,z):
    resultado =(y**2)-(4*x*z)
    return resultado

# função Raiz
def calc_raiz (x):
    resultado = abs(x)**0.5
    return resultado
    
# função X1
def calc_x1(x,y,z):
    resultado = (-y + z)/(2*x)
    return resultado

# função X2
def calc_x2(x,y,z):
    resultado = (-y - z)/(2*x)
    return resultado

# Menu
def menu():
    print('----------------------------------------------------------------------')
    print('1 - equação do 1º Grau')
    print('2 - equação do 2º Grau')
    print('3 - Sair')
    print('----------------------------------------------------------------------')


# Switch
On = 1

while On==1:
    print('\n')
    menu()
    entrada = int(input("Digite a opção desejada:"))
    print('----------------------------------------------------------------------')
    print('\n')
    if entrada<1 or entrada>3:
        On=1
    elif entrada==1:
        print('Equação de 1º Grau:\nex.  2x + 4 = 0 => (A = 2 e B = 4)\n')
        b = int(input('Digite A:'))
        c = int(input('Digite B:'))
        
        #  Equação do 1º Grau
        if c>=0:
            print('\nEquação: ',b,'x+',c,' = 0')
            x1 = -1*(c/b)
            print('X: ',x1)
            
        else:
            print('\nEquação: ',b,'x',c,' = 0')
            x1 = abs(c)/b
            print('X: ',x1)
            
        On=1
    elif entrada==2:
        print('Equação de 2º Grau:\nex.  4x² - 3x + 6 = 0 => (A = 4 , B = -3 e C = 6)\n')
        a = int(input('Digite A:'))
        while a==0:
            a=int(input('Valor 0(ZERO) Invalida a equação de 2º Grau!\n Digite A:'))
        b = int(input('Digite B:'))
        c = int(input('Digite C:'))
        print('\nEquação: ',a,'X² (+) ',b,'X (+) ',c,' = 0')
        # Equação do 2º Grau 
        delta = calc_delta(a,b,c)
        raiz = calc_raiz(delta)
        x1 = calc_x1(a,b,raiz)
        x2 = calc_x2(a,b,raiz)
        print('Delta: ',delta)
        print('Raiz: ',raiz)
        print('x1: ',x1)
        print('x2: ',x2)
        
        On=1
    elif entrada==3:
        On=0        
        
input()   
