#calculo da bissecao de uma função

def f(x): 
    return x*x - 4 #definição da função x² - 4

def bissecao(a,b):
    
    if (f(a)*f(b) >= 0):
        print("Não existem raízes entre os intervalos")
        return
    
    while((b-a) >= 1e-6):
        
        k = (a+b)/2
        
        if (abs(f(k)) < 1e-6): #módulo de f(k)
            break
        
        if (f(k)*f(a) < 0):
            b = k #se for menor que z, b recebe o valor de k
        else: 
            a = k #se for maior que zero, a recebe o valor de k
    print(f"O valor da raíz é: {k: .4f}")
    

a = 0
b = 3
bissecao(a, b)