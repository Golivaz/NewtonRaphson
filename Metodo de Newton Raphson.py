import time
import math
import sympy as sp
#Este print existe neste programa para aprensentar a função do programa
print("Este programa calcula e imprime o resultado de uma função utilizando do método de Newton-Raphson.")

x = sp.symbols("x")
epslon = 0.001
erro = 1
f = x**3 - x - 4
df = sp.diff(f,x)
k=-1

display("F(x)=",f)
display("F'(x)=",df)

x0=float(input("Insira o valor de x inicial para iniciar o calculo: "))
x1=0
while erro>epslon:
    x1 = x0-((f.subs(x, x0).evalf())/(df.subs(x, x0).evalf()))
    erro = (abs(x1-x0))/(abs(x1)) 
    x0=x1
    
    print("Erro maior que ÉPSLON, refazendo calculo com Xk+1")
    print('x1=',x1,'erro=',erro,'.')
    time.sleep(2)
    
      
    
    
print("A solução final da função é:")
print("x1=",round(x1,6)," .")
print("Erro=",round(erro,6)," .")