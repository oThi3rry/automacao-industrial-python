# Sistema de Gestão de Peças, Qualidade e Armazenamento

pecas_aprovadas = []
pecas_reprovadas = []

def recalcular_caixas():
    """Recalcula as caixas sempre que uma peça é adicionada ou removida."""
    caixas_fechadas = []
    caixa_atual = []
    
    for peca in pecas_aprovadas:
        caixa_atual.append(peca)
        if len(caixa_atual) == 10:
            caixas_fechadas.append(caixa_atual)
            caixa_atual = []
            
    return caixas_fechadas, caixa_atual

def cadastrar_peca():
    print("\n--- CADASTRAR NOVA PEÇA ---")
    try:
        id_peca = int(input("Digite o ID da peça: "))
        peso = float(input("Digite o peso (em gramas): "))
        cor = input("Digite a cor da peça: ").strip().lower()
        comprimento = float(input("Digite o comprimento (em cm): "))
        
        # Validação das regras de negócio
        motivos_reprovacao = []
        
        if peso < 95 or peso > 105:
            motivos_reprovacao.append("Peso fora do padrão (95g - 105g)")
        if cor not in ['azul', 'verde']:
            motivos_reprovacao.append("Cor inválida (deve ser azul ou verde)")
        if comprimento < 10 or comprimento > 20:
            motivos_reprovacao.append("Comprimento fora do padrão (10cm - 20cm)")
            
        peca = {"id": id_peca, "peso": peso, "cor": cor, "comprimento": comprimento}
        
        if len(motivos_reprovacao) == 0:
            pecas_aprovadas.append(peca)
            print("✅ Peça APROVADA com sucesso!")
        else:
            peca["motivo"] = " | ".join(motivos_reprovacao)
            pecas_reprovadas.append(peca)
            print("❌ Peça REPROVADA.")
            print(f"Motivo(s): {peca['motivo']}")
            
    except ValueError:
        print("Erro: Digite valores numéricos válidos para ID, peso e comprimento.")

def listar_pecas():
    print("\n--- LISTA DE PEÇAS ---")
    print("\n🟢 APROVADAS:")
    if not pecas_aprovadas:
        print("Nenhuma peça aprovada.")
    for p in pecas_aprovadas:
        print(f"ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comp: {p['comprimento']}cm")
        
    print("\n🔴 REPROVADAS:")
    if not pecas_reprovadas:
        print("Nenhuma peça reprovada.")
    for p in pecas_reprovadas:
        print(f"ID: {p['id']} | Motivo: {p['motivo']}")

def remover_peca():
    print("\n--- REMOVER PEÇA ---")
    try:
        id_remover = int(input("Digite o ID da peça que deseja remover: "))
        removida = False
        
        # Procura nas aprovadas
        for p in pecas_aprovadas:
            if p['id'] == id_remover:
                pecas_aprovadas.remove(p)
                print("Peça removida da lista de APROVADAS.")
                removida = True
                break
                
        # Procura nas reprovadas
        if not removida:
            for p in pecas_reprovadas:
                if p['id'] == id_remover:
                    pecas_reprovadas.remove(p)
                    print("Peça removida da lista de REPROVADAS.")
                    removida = True
                    break
                    
        if not removida:
            print("Peça não encontrada.")
            
    except ValueError:
        print("Erro: ID deve ser um número inteiro.")

def listar_caixas():
    print("\n--- CAIXAS FECHADAS ---")
    caixas_fechadas, caixa_atual = recalcular_caixas()
    
    if not caixas_fechadas:
        print("Nenhuma caixa fechada no momento.")
    else:
        for i, caixa in enumerate(caixas_fechadas):
            print(f"\n📦 Caixa {i+1} (10 peças):")
            for p in caixa:
                print(f"  - ID: {p['id']}")
                
    print(f"\nStatus da caixa atual (aberta): {len(caixa_atual)}/10 peças.")

def gerar_relatorio():
    print("\n====== RELATÓRIO FINAL ======")
    caixas_fechadas, _ = recalcular_caixas()
    
    print(f"Total de peças aprovadas: {len(pecas_aprovadas)}")
    print(f"Total de peças reprovadas: {len(pecas_reprovadas)}")
    print(f"Quantidade de caixas fechadas utilizadas: {len(caixas_fechadas)}")
    
    if pecas_reprovadas:
        print("\nMotivos de Reprovação:")
        for p in pecas_reprovadas:
            print(f"ID {p['id']}: {p['motivo']}")
    print("=============================")

# Loop Principal (Menu)
while True:
    print("\n" + "="*30)
    print("  CONTROLE DE QUALIDADE 1.0  ")
    print("="*30)
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == '1':
        cadastrar_peca()
    elif opcao == '2':
        listar_pecas()
    elif opcao == '3':
        remover_peca()
    elif opcao == '4':
        listar_caixas()
    elif opcao == '5':
        gerar_relatorio()
    elif opcao == '0':
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")