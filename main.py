import json

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "r", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()
    
# Controle de Estoque
# 1 - Mostrar produtos
# 2 - Pesquisar produtos
# 3 - Adicionar produtos
# 4 - Remover produtos



while True:
    print("====CONTROLE DE ESTOQUE====")
    print("1 - Mostrar produtos")
    print("2 - Pesquisar produtos")
    print("3 - Adicionar produtos")
    print("4 - Remover produtos")
    
    opcao = input("Digite sua opção: ")
    
