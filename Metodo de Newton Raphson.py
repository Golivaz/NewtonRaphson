import tkinter as tk
import sympy as sp

# Função para calcular o método de Newton-Raphson

def calcular():
    x = sp.symbols("x")
    epslon = 0.001
    erro = 1
    f = x**3 - x - 4
    df = sp.diff(f,x)

    # Obtenha o valor inicial de x0 a partir da entrada da interface

    try:
        x0 = float(entry_x0.get())
    except ValueError:
        resultado_label.config(text="Erro: Insira um número válido.")
        return

    x1 = 0
    while erro > epslon:
        x1 = x0 - ((f.subs(x, x0).evalf()) / (df.subs(x, x0).evalf()))
        erro = (abs(x1 - x0)) / (abs(x1)) 
        x0 = x1

    # Exibe o resultado na interface gráfica
    resultado_label.config(text=f"Solução final: x = {round(x1, 6)}, Erro = {round(erro, 6)}")

# Criar a janela principal do Tkinter
root = tk.Tk()
root.title("Método de Newton-Raphson")

# Adicionar elementos à interface gráfica
label_instrucao = tk.Label(root, text="Insira o valor inicial de x0:")
label_instrucao.pack()

entry_x0 = tk.Entry(root)
entry_x0.pack()

botao_calcular = tk.Button(root, text="Calcular", command=calcular)
botao_calcular.pack()

resultado_label = tk.Label(root, text="")
resultado_label.pack()

# Iniciar o loop da interface gráfica
root.mainloop()
