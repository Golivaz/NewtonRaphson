# 🧮 Calculadora de Newton-Raphson

Este repositório contém um código em **Python** que emula uma **calculadora de Newton-Raphson**, um método iterativo utilizado para encontrar aproximações das raízes de uma função não-linear. O método de Newton-Raphson é amplamente utilizado em problemas matemáticos e científicos por sua eficiência na solução de equações.

---

## 📚 Sobre o Método de Newton-Raphson

O método de **Newton-Raphson** usa aproximações sucessivas para encontrar a raiz de uma função \( f(x) = 0 \). Dada uma aproximação inicial \( x_0 \), a próxima aproximação \( x_1 \) é dada por:

\[
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
\]

Onde:
- \( f(x) \) é a função alvo.
- \( f'(x) \) é a derivada de \( f(x) \).
  
O processo é repetido até que a solução convirja para um valor satisfatório, ou seja, quando o erro absoluto entre as iterações for menor que um valor de tolerância definido.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Linguagem de programação utilizada para implementar o método de Newton-Raphson.
- **Bibliotecas Matemáticas**: Como `math` para funções matemáticas padrão (se necessário).

---
