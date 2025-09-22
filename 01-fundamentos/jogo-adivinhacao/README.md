# 🎯 Jogo de Adivinhação

> Um jogo simples que vai te ensinar loops, lógica e aleatoriedade em Python!

## 📋 Sobre o Projeto

Um jogo onde o computador escolhe um número aleatório e você tem que adivinhar. Parece fácil? Vamos ver! Este projeto ensina conceitos importantes de programação de forma divertida.

### 🎯 Objetivos de Aprendizado

- ✅ Geração de números aleatórios
- ✅ Loops while e controle de fluxo
- ✅ Lógica condicional avançada
- ✅ Contadores e acumuladores
- ✅ Validação de entrada
- ✅ Sistema de pontuação

## 🚀 Como Executar

```bash
# Navegue para a pasta do projeto
cd jogo-adivinhacao

# Execute o jogo
python main.py
```

## 💡 Funcionalidades

### 🎮 Modos de Jogo
- 🟢 **Fácil**: 1-50 (15 tentativas)
- 🟡 **Médio**: 1-100 (10 tentativas)
- 🔴 **Difícil**: 1-500 (8 tentativas)
- 🔥 **Extremo**: 1-1000 (7 tentativas)

### 🏆 Sistema de Pontuação
- Base: 1000 pontos
- Penalidade: -50 pontos por tentativa errada
- Bônus: +100 por acertar na primeira tentativa
- Multiplicador por dificuldade

### 📊 Estatísticas
- Tentativas utilizadas
- Pontuação final
- Histórico de palpites
- Taxa de acerto por dificuldade

## 🎮 Exemplo de Uso

```
🎯 JOGO DE ADIVINHAÇÃO

Escolha a dificuldade:
1. Fácil (1-50) - 15 tentativas
2. Médio (1-100) - 10 tentativas  
3. Difícil (1-500) - 8 tentativas
4. Extremo (1-1000) - 7 tentativas

Sua escolha: 2

🎯 Pensei em um número entre 1 e 100!
Você tem 10 tentativas para adivinhar.

Tentativa 1/10: 50
📈 Muito alto! Tente um número menor.

Tentativa 2/10: 25
📉 Muito baixo! Tente um número maior.

Tentativa 3/10: 37
🎉 Parabéns! Você acertou!

🏆 Pontuação: 850 pontos
📊 Acertou em 3 tentativas
```

## 🔧 Conceitos Aplicados

### 1. Números Aleatórios
```python
import random
numero_secreto = random.randint(1, 100)
```

### 2. Loops While
```python
tentativas = 0
max_tentativas = 10

while tentativas < max_tentativas:
    # lógica do jogo
    tentativas += 1
```

### 3. Validação de Entrada
```python
while True:
    try:
        palpite = int(input("Seu palpite: "))
        break
    except ValueError:
        print("Digite apenas números!")
```

## 🎯 Desafios Extras

Depois de fazer funcionar, tente implementar:

1. **Múltiplos jogadores**: Cada um tem sua vez
2. **Ranking**: Salvar melhores pontuações
3. **Dicas personalizadas**: "Está quente/frio"
4. **Modo versus**: Dois jogadores se revezam
5. **Estatísticas avançadas**: Gráficos de progresso

## 📚 O Que Você Aprendeu

- Gerar números aleatórios
- Usar loops while eficientemente
- Controlar fluxo com break/continue
- Implementar sistema de pontuação
- Validar entrada do usuário
- Criar lógica de jogo básica