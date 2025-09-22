#!/usr/bin/env python3
"""
Jogo de Adivinhação - Segundo projeto do Python Roadmap

Um jogo interativo que demonstra:
- Geração de números aleatórios
- Loops e controle de fluxo
- Lógica condicional
- Sistema de pontuação
- Validação de entrada

Autor: Python Roadmap
Versão: 1.0
"""

import random
import time


def exibir_titulo():
    """Exibe o título do jogo com arte ASCII."""
    print("\n" + "="*50)
    print("           🎯 JOGO DE ADIVINHAÇÃO")
    print("="*50)
    print("Eu vou pensar em um número e você tenta adivinhar!")
    print("Quanto menos tentativas usar, maior sua pontuação!")
    print("-"*50)


def escolher_dificuldade():
    """
    Permite ao usuário escolher a dificuldade do jogo.
    
    Returns:
        tuple: (nivel, min_num, max_num, max_tentativas, multiplicador)
    """
    print("\n🎮 Escolha a dificuldade:")
    print("1. 🟢 Fácil    (1-50)   - 15 tentativas")
    print("2. 🟡 Médio    (1-100)  - 10 tentativas")
    print("3. 🔴 Difícil  (1-500)  - 8 tentativas")
    print("4. 🔥 Extremo  (1-1000) - 7 tentativas")
    
    dificuldades = {
        "1": ("Fácil", 1, 50, 15, 1.0),
        "2": ("Médio", 1, 100, 10, 1.5),
        "3": ("Difícil", 1, 500, 8, 2.0),
        "4": ("Extremo", 1, 1000, 7, 3.0)
    }
    
    while True:
        escolha = input("\nSua escolha (1-4): ").strip()
        if escolha in dificuldades:
            return dificuldades[escolha]
        else:
            print("❌ Escolha inválida! Digite 1, 2, 3 ou 4.")


def obter_palpite(tentativa, max_tentativas):
    """
    Obtém um palpite válido do usuário.
    
    Args:
        tentativa (int): Número da tentativa atual
        max_tentativas (int): Máximo de tentativas permitidas
        
    Returns:
        int: Palpite do usuário
    """
    while True:
        try:
            palpite = int(input(f"\nTentativa {tentativa}/{max_tentativas}: "))
            return palpite
        except ValueError:
            print("❌ Digite apenas números inteiros!")


def dar_dica(palpite, numero_secreto, min_num, max_num):
    """
    Fornece dica baseada no palpite do usuário.
    
    Args:
        palpite (int): Palpite do usuário
        numero_secreto (int): Número que deve ser adivinhado
        min_num (int): Número mínimo do intervalo
        max_num (int): Número máximo do intervalo
    """
    diferenca = abs(palpite - numero_secreto)
    intervalo = max_num - min_num
    
    if palpite > numero_secreto:
        print("📈 Muito alto! Tente um número menor.")
    else:
        print("📉 Muito baixo! Tente um número maior.")
    
    # Dicas adicionais baseadas na proximidade
    if diferenca <= intervalo * 0.05:  # Muito próximo (5% do intervalo)
        print("🔥 Você está MUITO próximo!")
    elif diferenca <= intervalo * 0.15:  # Próximo (15% do intervalo)
        print("♨️  Você está próximo!")
    elif diferenca <= intervalo * 0.3:   # Morno (30% do intervalo)
        print("🌡️  Morno...")
    else:
        print("🧊 Frio! Ainda está longe.")


def calcular_pontuacao(tentativas, max_tentativas, multiplicador, acertou_primeira=False):
    """
    Calcula a pontuação final baseada no desempenho.
    
    Args:
        tentativas (int): Número de tentativas usadas
        max_tentativas (int): Máximo de tentativas permitidas
        multiplicador (float): Multiplicador da dificuldade
        acertou_primeira (bool): Se acertou na primeira tentativa
        
    Returns:
        int: Pontuação final
    """
    pontuacao_base = 1000
    penalidade_tentativa = 50
    bonus_primeira = 500
    
    pontuacao = pontuacao_base - (tentativas - 1) * penalidade_tentativa
    
    if acertou_primeira:
        pontuacao += bonus_primeira
    
    # Aplicar multiplicador da dificuldade
    pontuacao = int(pontuacao * multiplicador)
    
    # Garantir que a pontuação não seja negativa
    return max(pontuacao, 0)


def jogar_rodada():
    """
    Executa uma rodada completa do jogo.
    
    Returns:
        dict: Estatísticas da rodada
    """
    # Escolher dificuldade
    nivel, min_num, max_num, max_tentativas, multiplicador = escolher_dificuldade()
    
    # Gerar número secreto
    numero_secreto = random.randint(min_num, max_num)
    
    print(f"\n🎯 Pensei em um número entre {min_num} e {max_num}!")
    print(f"Você tem {max_tentativas} tentativas para adivinhar.")
    print("💡 Dica: Use a estratégia de busca binária para ser mais eficiente!")
    
    # Variáveis do jogo
    tentativas = 0
    historico_palpites = []
    acertou = False
    
    # Loop principal do jogo
    while tentativas < max_tentativas:
        tentativas += 1
        
        # Obter palpite
        palpite = obter_palpite(tentativas, max_tentativas)
        historico_palpites.append(palpite)
        
        # Verificar se acertou
        if palpite == numero_secreto:
            acertou = True
            print(f"\n🎉 PARABÉNS! Você acertou!")
            print(f"O número era {numero_secreto}")
            
            # Som de vitória (simulado)
            print("🎵 ♪ Ta-da! ♪")
            time.sleep(0.5)
            break
        else:
            # Dar dica
            dar_dica(palpite, numero_secreto, min_num, max_num)
            
            # Mostrar tentativas restantes
            restantes = max_tentativas - tentativas
            if restantes > 0:
                print(f"⏳ Tentativas restantes: {restantes}")
    
    # Resultado final
    if not acertou:
        print(f"\n💀 Suas tentativas acabaram!")
        print(f"O número era {numero_secreto}")
        print("💡 Dica: Tente a estratégia de busca binária na próxima vez!")
    
    # Calcular pontuação
    pontuacao = 0
    if acertou:
        acertou_primeira = tentativas == 1
        pontuacao = calcular_pontuacao(tentativas, max_tentativas, multiplicador, acertou_primeira)
    
    # Estatísticas da rodada
    estatisticas = {
        "nivel": nivel,
        "acertou": acertou,
        "tentativas": tentativas,
        "max_tentativas": max_tentativas,
        "pontuacao": pontuacao,
        "numero_secreto": numero_secreto,
        "historico": historico_palpites,
        "multiplicador": multiplicador
    }
    
    return estatisticas


def exibir_estatisticas(stats):
    """
    Exibe as estatísticas da rodada.
    
    Args:
        stats (dict): Estatísticas da rodada
    """
    print("\n" + "="*40)
    print("           📊 ESTATÍSTICAS")
    print("="*40)
    print(f"🎮 Dificuldade: {stats['nivel']}")
    print(f"🎯 Número secreto: {stats['numero_secreto']}")
    print(f"🔄 Tentativas usadas: {stats['tentativas']}/{stats['max_tentativas']}")
    
    if stats['acertou']:
        print(f"🏆 Pontuação: {stats['pontuacao']} pontos")
        
        if stats['tentativas'] == 1:
            print("🌟 INCRÍVEL! Acertou de primeira!")
        elif stats['tentativas'] <= 3:
            print("⭐ EXCELENTE! Muito eficiente!")
        elif stats['tentativas'] <= stats['max_tentativas'] // 2:
            print("👍 BOM! Acima da média!")
        else:
            print("😅 No limite, mas conseguiu!")
    else:
        print("💀 Pontuação: 0 pontos")
        print("💪 Não desista! Tente novamente!")
    
    # Histórico de palpites
    print(f"\n📈 Seus palpites: {' → '.join(map(str, stats['historico']))}")
    
    # Dicas para melhoria
    if not stats['acertou'] or stats['tentativas'] > stats['max_tentativas'] // 2:
        print("\n💡 DICA PRO: Use busca binária!")
        print("   1. Comece pelo meio do intervalo")
        print("   2. Se for alto, vá para o meio da metade inferior")
        print("   3. Se for baixo, vá para o meio da metade superior")
        print("   4. Continue dividindo até acertar!")


def jogar_novamente():
    """
    Pergunta se o usuário quer jogar novamente.
    
    Returns:
        bool: True se quer jogar novamente, False caso contrário
    """
    while True:
        resposta = input("\n🎮 Quer jogar novamente? (s/n): ").strip().lower()
        if resposta in ["s", "sim", "y", "yes"]:
            return True
        elif resposta in ["n", "não", "nao", "no"]:
            return False
        else:
            print("❌ Digite 's' para sim ou 'n' para não.")


def main():
    """Função principal do jogo."""
    print("🐍 Bem-vindo ao Jogo de Adivinhação Python!")
    print("Segundo projeto do Python Roadmap!")
    
    # Estatísticas globais
    total_jogos = 0
    total_vitorias = 0
    melhor_pontuacao = 0
    
    while True:
        exibir_titulo()
        
        # Jogar uma rodada
        stats = jogar_rodada()
        
        # Atualizar estatísticas globais
        total_jogos += 1
        if stats['acertou']:
            total_vitorias += 1
            melhor_pontuacao = max(melhor_pontuacao, stats['pontuacao'])
        
        # Exibir estatísticas da rodada
        exibir_estatisticas(stats)
        
        # Verificar se quer jogar novamente
        if not jogar_novamente():
            break
    
    # Estatísticas finais da sessão
    if total_jogos > 1:
        print("\n" + "="*40)
        print("        🏆 ESTATÍSTICAS DA SESSÃO")
        print("="*40)
        print(f"🎮 Jogos jogados: {total_jogos}")
        print(f"🏆 Vitórias: {total_vitorias}")
        print(f"📊 Taxa de vitória: {(total_vitorias/total_jogos)*100:.1f}%")
        if melhor_pontuacao > 0:
            print(f"⭐ Melhor pontuação: {melhor_pontuacao}")
    
    print(f"\n👋 Obrigado por jogar!")
    print("🚀 Próximo desafio: Conversor de Unidades!")
    print("💪 Continue sua jornada no Python Roadmap!")


if __name__ == "__main__":
    main()