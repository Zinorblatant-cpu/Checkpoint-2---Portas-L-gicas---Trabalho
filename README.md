# README - Exercícios de Lógica Digital

Este repositório contém soluções em Python para exercícios de lógica digital, com foco em expressões booleanas e tabelas verdade. Cada exercício implementa uma função lógica diferente, 
baseada em problemas práticos como controle de acesso, sistemas de emergência e validação de senhas.

---

## Exercícios Resolvidos

### Exercício 1: Detecção de Dois Inputs Verdadeiros
- **Expressão lógica**: (¬A ⋅ B ⋅ C) + (A ⋅ ¬B ⋅ C) + (A ⋅ B ⋅ ¬C)
- **Descrição**: Retorna 1 quando exatamente dois dos três inputs (A, B, C) são verdadeiros.
- **Aplicação**: Utilizado em sistemas que requerem detecção de combinações específicas (ex.: circuitos de paridade) [[2]].
- **Saída**: Tabela verdade com todas as combinações possíveis.

### Exercício 2: Função XOR (Ou Exclusivo)
- **Expressão lógica**: (¬A ⋅ B) + (A ⋅ ¬B)
- **Descrição**: Retorna 1 quando apenas um dos inputs (A, B) é verdadeiro.
- **Aplicação**: Comum em operações de criptografia e detecção de erros [[6]].
- **Saída**: Tabela verdade demonstrando o comportamento da porta XOR.

### Exercício 3: Condições Complexas com Quatro Variáveis
- **Expressão lógica**: ((¬A ⋅ B) + C) ⋅ (¬A + D)
- **Descrição**: Combina duas condições:
  1. (¬A ⋅ B) + C (verdadeiro se ¬A e B forem verdadeiros ou C for verdadeiro).
  2. (¬A + D) (verdadeiro se ¬A ou D forem verdadeiros).
- **Aplicação**: Modelagem de sistemas com múltiplas dependências [[2]].

### Exercício 4: Controle de Acesso a um Cofre Eletrônico
- **Expressão lógica**: ((A ⋅ B) + C) ⋅ ¬D
- **Descrição**: O cofre abre se:
  - A senha estiver correta (A=1) e o horário permitido (B=1), **ou** o supervisor liberar manualmente (C=1),
  - E o alarme não estiver ativo (D=0) [[Checkpoint 2 - Portas Lógicas - Trabalho.pdf, Questão 4]].
- **Aplicação**: Sistema de segurança baseado em condições lógicas.

### Exercício 5: Ativação de Modo de Emergência
- **Expressão lógica**: (A + B) ⋅ ¬C ⋅ D
- **Descrição**: O modo de emergência ativa se:
  - Prioridade para ambulância (A=1) ou botão de emergência pressionado (B=1),
  - Fora do horário de pico (C=0),
  - E o sistema estiver funcional (D=1) [[Checkpoint 2 - Portas Lógicas - Trabalho.pdf, Questão 5]].
- **Aplicação**: Sistemas de emergência com restrições temporais.

### Exercício 6: Validação de Senha Binária
- **Expressão lógica**: ¬A ⋅ B ⋅ ¬C ⋅ D
- **Descrição**: Valida a senha binária 0101 (onde A=0, B=1, C=0, D=1).
- **Aplicação**: Sistemas de autenticação baseados em combinações binárias [[Checkpoint 2 - Portas Lógicas - Trabalho.pdf, Questão 6]].

---

