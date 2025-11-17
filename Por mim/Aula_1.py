"""""
numero = 10;
numerob = 11;

print(numero + numerob);
"""

# Estrutura de reptição
"""""
x = 1;
while x <= 10:
    print(x);
    x = x + 1;
"""

"""""
for i in range(5):
    print(i);

"""

"""""
x=1;
while x == 2:
    print(x);

while True:
    print(x)
"""

"""""
# tabuada
n = int(input("Digite um número: "));
x = 1;
while x <= 10:
    print(n+x)
    x = x+1 #contador
"""

"""""
x =1;
soma = 0;
while x<=10:
    n = int(input("Digite um número: "));
    soma = soma + n; # acumulador
    x = x + 1;
print(soma);
"""

"""""
#interrupção de repetição
x = 1;
while x <= 10:
    if x == 5:
        break; #interrompe a repetição
    print(x);
    x = x + 1;
"""

x = 0;
while True:
    num = int(input("Digite um número: "));
    if num == 0:
        break
    x = x + num;
print(x);