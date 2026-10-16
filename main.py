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
# 3 - Pesquisa por categoria
# 4 - Adicionar produtos
# 5 - Remover produtos

def mostrar():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    print(produtos)
    
def pesquisar():
    nome = input("Digite o nome do produto que você deseja buscar: ")
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    for produto in produtos:
        if nome in produto["nome"]:
            print(produto)
            
def pesquisa_categoria():
    categoria = input("Digite o nome do produto que você deseja buscar: ")
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    for produto in produtos:
        if categoria in produto["categoria"]:
            print(produto)

while True:
    print("====CONTROLE DE ESTOQUE====")
    print("1 - Mostrar produtos")
    print("2 - Pesquisar produtos")
    print("3 - Pesquisa por categoria")
    print("4 - Adicionar produtos")
    print("5 - Remover produtos")
    print("0 - Sair")
    
    opcao = input("Digite sua opção: ")
    
    if opcao == "1":
        mostrar()
    elif opcao == "2":
        pesquisar()
    elif opcao == "3":
        pesquisa_categoria()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente")
        