
# EXERCÍCIO 1
# Expressão lógica: (¬A ⋅ B ⋅ C) + (A ⋅ ¬B ⋅ C) + (A ⋅ B ⋅ ¬C)
# Representa uma função lógica que retorna 1 quando exatamente dois dos três inputs (A, B, C) são verdadeiros.
# A tabela verdade mostra todas as combinações possíveis de inputs e o resultado da expressão.
print("\nEXERCICIO 1")
print("A | B | C | (¬A ⋅ B ⋅ C) + (A ⋅ ¬B ⋅ C) + (A ⋅ B ⋅ ¬C)")
print("--------------------------------------------------------")
for A in range(2):
    for B in range(2):
        for C in range(2):
            out = 0
            if (((not A) and B and C) or (A and (not B) and C) or (A and B and (not C))):
                out += 1
            print(f'{A:>2} | {B:>2} | {C:>2} | {out:>2}')
            


# EXERCÍCIO 2
# Expressão lógica: (¬A ⋅ B) + (A ⋅ ¬B)
# Esta é a definição da porta lógica XOR, que retorna 1 quando apenas um dos inputs (A ou B) é verdadeiro.
# A tabela verdade ilustra o comportamento da função XOR.
print("\nEXERCICIO 2")
print("A | B | (¬A ⋅ B) + (A ⋅ ¬B)")
print("----------------------------")
for A in range(2):
    for B in range(2):
        out = 0
        if (((not A) and B) or (A and (not B))):
            out += 1
        print(f'{A:>2} | {B:>2} | {out:>2}')


# EXERCÍCIO 3
# Expressão lógica: ((¬A ⋅ B) + C) ⋅ (¬A + D)
# Combina duas condições: 
# 1. "(¬A ⋅ B) + C" (verdadeiro se ¬A e B forem verdadeiros ou C for verdadeiro).
# 2. "¬(A + D)" (verdadeiro se ¬A ou D forem verdadeiros).
# A tabela verdade mostra a interação entre as variáveis A, B, C e D.
print("\nEXERCICIO 3")
print("A | B | C | D | ((¬A ⋅ B) + C) ⋅ (¬A + D)")
print("------------------------------------------")
for A in range(2):
    for B in range(2):
        for C in range(2):
            for D in range(2):
                out = 0
                if ((((not A) and B) or C) and not(A or D)):
                    out += 1
                print(f'{A:>2} | {B:>2} | {C:>2} | {D:>2} | {out:>2}')


# EXERCÍCIO 4
# Expressão lógica: ((A ⋅ B) + C) ⋅ ¬D
# O resultado é 1 se:
# - (A ⋅ B) ou C forem verdadeiros (primeira parte da expressão),
# - E D for falso (segunda parte da expressão).
# Representa um cenário de controle de acesso, como no problema 4 do trabalho.
print("\nEXERCICIO 4")
print("A | B | C | D | ((A ⋅ B) + C) ⋅ ¬D")
print("-----------------------------------")
for A in range(2):
    for B in range(2):
        for C in range(2):
            for D in range(2):
                out = 0
                if ((((A and B) or C) and not D)):
                    out += 1
                print(f'{A:>2} | {B:>2} | {C:>2} | {D:>2} | {out:>2}')


# EXERCÍCIO 5
# Expressão lógica: (A + B) ⋅ ¬C ⋅ D
# O resultado é 1 se:
# - A ou B forem verdadeiros (primeira parte),
# - C for falso (segunda parte),
# - E D for verdadeiro (terceira parte).
# Representa um sistema de emergência, como no problema 5 do trabalho.
print("\nEXERCICIO 5")
print("A | B | C | D | (A + B) ⋅ ¬C ⋅ D")
print("---------------------------------")
for A in range(2):
    for B in range(2):
        for C in range(2):
            for D in range(2):
                out = 0
                if ((A or B) and not C and D):
                    out += 1
                print(f'{A:>2} | {B:>2} | {C:>2} | {D:>2} | {out:>2}')


# EXERCÍCIO 6
# Expressão lógica: ¬A ⋅ B ⋅ ¬C ⋅ D
# Retorna 1 somente quando A=0, B=1, C=0, D=1, validando a senha 0101.
# A tabela verdade confirma que a saída é 1 apenas para esta combinação específica.
print("\nEXERCICIO 6")
print("A | B | C | D | ¬A ⋅ B ⋅ ¬C ⋅ D")
print("---------------------------------")
for A in range(2):
    for B in range(2):
        for C in range(2):
            for D in range(2):
                out = 0
                if ((not A) and B and (not C) and D):
                    out += 1
                print(f'{A:>2} | {B:>2} | {C:>2} | {D:>2} | {out:>2}')
