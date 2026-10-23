import json

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()
    
# Controle de Estoque
# 1 - Mostrar produtos
# 2 - Pesquisar produtos
# 3 - Pesquisa por categoria
# 4 - Adicionar produtos
# 5 - Remover produtos

def mostrar():
    produtos = carregar_produtos()
    for produto in produtos:
        print(f"ID: {produto["id"]}, Nome: {produto["nome"]}, Categoria: {produto["categoria"]}, Preço: {produto["preco"]}, Estoque: {produto["estoque"]}.")
    
def pesquisar():
    produtos = carregar_produtos()
    nome = input("Digite o nome do produto que você deseja buscar: ")
    for produto in produtos:
        if nome in produto["nome"]:
            print(f"ID: {produto["id"]}, Nome: {produto["nome"]}, Categoria: {produto["categoria"]}, Preço: {produto["preco"]}, Estoque: {produto["estoque"]}.")
            
def pesquisa_categoria():
    produtos = carregar_produtos()
    categoria = input("Digite o nome do produto que você deseja buscar: ")
    for produto in produtos:
        if categoria in produto["categoria"]:
            print(produto)
            
def pesquisa_preco():
    produtos = carregar_produtos()
    preco = float(input("Digite o preço máximo que você deseja buscar: "))
    for produto in produtos:
        if preco <= produtos["preco"]:
            print(produto)

def adicionar():
    produtos = carregar_produtos()
    id = carregar_produtos()[-1]["id"]
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = input("Digite o estoque do produto: ")
    id += 1
    
    novo_produto = {
        "id": id,
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "estoque": estoque
    }
    
    produtos.append(novo_produto)
    salvar_produtos(produtos)
    print("Seu produto foi adicionado!")

def remover():
    produtos = carregar_produtos()
    produto_removido = input("Digite o nome do produto que irá ser removido: ")
    for produto in produtos:
        if produto["nome"] == produto_removido:
            produtos.remove(produto)
            salvar_produtos(produtos)
    print("Seu produto foi removido.")

while True:
    print("====CONTROLE DE ESTOQUE====")
    print("1 - Mostrar produtos")
    print("2 - Pesquisar produtos")
    print("3 - Pesquisa por categoria")
    print("4 - Pesquisa por preço")
    print("5 - Adicionar produtos")
    print("6 - Remover produtos")
    print("0 - Sair")
    
    opcao = input("Digite sua opção: ")
    
    if opcao == "1":
        mostrar()
    elif opcao == "2":
        pesquisar()
    elif opcao == "3":
        pesquisa_categoria()
    elif opcao == "4":
        pesquisa_preco()
    elif opcao == "5":
        adicionar()
    elif opcao == "6":
        remover()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente")
        