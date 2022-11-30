import sys
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from tkinter.messagebox import showinfo


class View():
    def __init__(self, info=None):
        # Inicializando o tkinter
        self.root = tk.Tk()

        # Estilizando
        self.root.title("Estoque de Produtos")
        self.root.geometry("450x450")
        # self.root.configure(background="black")

        # Generate Interface
        self.generateInterface()

        # Clicar na tecla ESC e sair
        self.root.bind('<Escape>', self.close)

    def generateInterface(self):
        self.labelTitulo = tk.Label(self.root,
                                    height=3,
                                    text="Loja do Leonardo")
        self.labelTitulo.pack()

        # Botoes
        self.space = tk.Label(self.root,
                              height=2,)
        self.space.pack()
        self.btnSearch = tk.Button(self.root,
                                   width=20,
                                   height=2,
                                   text='Produtos',
                                   command=self.windowProducts)
        self.btnSearch.pack()
        self.space = tk.Label(self.root,
                              height=2,)
        self.space.pack()
        self.btnCreate = tk.Button(self.root,
                                   width=20,
                                   height=2,
                                   text='Inserir Produto',
                                   command=self.windowCreate)
        self.btnCreate.pack()
        self.space = tk.Label(self.root,
                              height=2,)
        self.space.pack()
        self.btnEdit = tk.Button(self.root,
                                 width=20,
                                 height=2,
                                 text='Editar Produto',
                                 command=self.windowEdit)
        self.btnEdit.pack()
        self.space = tk.Label(self.root,
                              height=2,)
        self.space.pack()
        self.btnDelete = tk.Button(self.root,
                                   width=20,
                                   height=2,
                                   text='Apagar Produto',
                                   command=self.windowDelete)
        self.btnDelete.pack()

    # Janelas
    def windowProducts(self):
        self.create = tk.Tk()
        self.create.title("Produtos")
        self.create.geometry("820x400")

        columns = ('name', 'price', 'size', 'qtd')

        tree = ttk.Treeview(self.create, columns=columns, show='headings')

        tree.heading('name', text='Produto')
        tree.heading('price', text='Preço')
        tree.heading('size', text='Tamanho')
        tree.heading('qtd', text='Quantidade')

        try:
            products = self.controller.getAllProductsController()
        except:
            showinfo(title='Erro', message='Nenhum dado no cadastrado!')

        for prod in products:
            tree.insert('', tk.END, values=(
                prod['name'], prod['price'], prod['size'], prod['qtd']))

        tree.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(
            self.create, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # Buscar prod
        self.space = tk.Label(self.create,
                              height=3,)
        self.space.grid(row=1, column=0)

        self.labelTituloCreate = tk.Label(self.create,
                                          height=2,
                                          text="Buscar Produto")
        self.labelTituloCreate.grid(row=1, column=0)

        self.name = tk.Entry(self.create,
                             bd=3)
        self.name.grid(row=2, column=0)

        self.space = tk.Label(self.create,
                              height=1,)
        self.space.grid(row=3, column=0)

        self.btnListProd = tk.Button(self.create,
                                     width=15,
                                     text='Procurar Produto',
                                     command=self.searchProductList)
        self.btnListProd.grid(row=4, column=0)

    def windowCreate(self):
        self.create = tk.Tk()
        self.create.title("Inserindo Produto")
        self.create.geometry("400x400")

        self.labelTituloCreate = tk.Label(self.create,
                                          height=3,
                                          text="Inserindo um Produto")
        self.labelTituloCreate.pack()
        # Entradas
        # Name
        self.nameLabel = tk.Label(self.create,
                                  text="Produto")
        self.nameLabel.pack()

        self.name = tk.Entry(self.create,
                             bd=3)
        self.name.pack()

        # Price
        self.priceLabel = tk.Label(self.create,
                                   text="Preço")
        self.priceLabel.pack()

        self.price = tk.Entry(self.create,
                              bd=3)
        self.price.pack()

        # Tamanho
        self.sizeLabel = tk.Label(self.create,
                                  text="Tamanho")
        self.sizeLabel.pack()

        self.size = tk.Entry(self.create,
                             bd=3)
        self.size.pack()

        # Quantidade
        self.qtdLabel = tk.Label(self.create,
                                 text="Quantidade")
        self.qtdLabel.pack()

        self.qtd = tk.Entry(self.create,
                            bd=3)
        self.qtd.pack()

        self.space = tk.Label(self.create,
                              height=2,)
        self.space.pack()

        # Botao
        self.btnInsertProduct = tk.Button(self.create,
                                          width=15,
                                          text='Criar Produto',
                                          command=self.createProduct)
        self.btnInsertProduct.pack()

        self.space = tk.Label(self.create,
                              height=2,)
        self.space.pack()

    def windowEdit(self):
        self.create = tk.Tk()
        self.create.title("Editando Produto")
        self.create.geometry("400x500")

        self.labelTituloCreate = tk.Label(self.create,
                                          height=3,
                                          text="Editando um Produto")
        self.labelTituloCreate.pack()
        # Entradas
        # prevName
        self.prevNameLabel = tk.Label(self.create,
                                      text="Produto Editavel")
        self.prevNameLabel.pack()

        self.prevName = tk.Entry(self.create,
                                 bd=3)
        self.prevName.pack()

        self.space = tk.Label(self.create,
                              height=2,)
        self.space.pack()

        self.btnEditProduct = tk.Button(self.create,
                                        width=15,
                                        text='Procurar Produto',
                                        command=self.searchProduct)
        self.btnEditProduct.pack()

        self.space = tk.Label(self.create,
                              height=2,)
        self.space.pack()

        # Name
        self.nameLabel = tk.Label(self.create,
                                  text="Editando Produto")
        self.nameLabel.pack()

        self.name = tk.Entry(self.create,
                             bd=3)
        self.name.pack()

        # Price
        self.priceLabel = tk.Label(self.create,
                                   text="Editando Preço")
        self.priceLabel.pack()

        self.price = tk.Entry(self.create,
                              bd=3)
        self.price.pack()

        # Tamanho
        self.sizeLabel = tk.Label(self.create,
                                  text="Editando Tamanho")
        self.sizeLabel.pack()

        self.size = tk.Entry(self.create,
                             bd=3)
        self.size.pack()

        # Quantidade
        self.qtdLabel = tk.Label(self.create,
                                 text="Editando Quantidade")
        self.qtdLabel.pack()

        self.qtd = tk.Entry(self.create,
                            bd=3)
        self.qtd.pack()

        self.space = tk.Label(self.create,
                              height=2,)
        self.space.pack()

        # Botao
        self.btnEditProduct = tk.Button(self.create,
                                        width=15,
                                        text='Editar Produto',
                                        command=self.editProduct)
        self.btnEditProduct.pack()

        self.space = tk.Label(self.create,
                              height=2,)
        self.space.pack()

    def windowDelete(self):
        self.create = tk.Tk()
        self.create.title("Deletando Produto")
        self.create.geometry("400x400")

        self.labelTituloCreate = tk.Label(self.create,
                                          height=3,
                                          text="Deletar um Produto")
        self.labelTituloCreate.pack()
        # Entradas
        # Name
        self.nameLabel = tk.Label(self.create,
                                  text="Digite o Produto")
        self.nameLabel.pack()

        self.name = tk.Entry(self.create,
                             bd=3)
        self.name.pack()

        self.space = tk.Label(self.create,
                              height=2,)
        self.space.pack()

        # Botao
        self.btnDeleteProduct = tk.Button(self.create,
                                          width=15,
                                          text='Excluir Produto',
                                          command=self.deleteProduct)
        self.btnDeleteProduct.pack()

        self.space = tk.Label(self.create,
                              height=2,)
        self.space.pack()

    # Chamadas no Controller
    # Criar Produto
    def createProduct(self):
        try:
            self.controller.createProductController(
                self.name.get(),
                float(self.price.get()),
                self.size.get(),
                int(self.qtd.get())
            )
            showinfo(title='Sucesso', message="Produto criado com sucesso!")
        except:
            showinfo(title='Erro', message="ERRO, Tente novamente!")

    # Buscar Produto
    def searchProduct(self):
        try:
            prod = self.controller.searchProductController(self.prevName.get())
            self.name.insert(0, prod['name'])
            self.price.insert(0, prod['price'])
            self.size.insert(0, prod['size'])
            self.qtd.insert(0, prod['qtd'])
        except:
            showinfo(title='Erro', message="Produto não existe!")

    # Buscar Produto List
    def searchProductList(self):
        try:
            prod = self.controller.searchProductController(self.name.get())
            showinfo(
                title='Sucesso', message=f"- {prod['name']}, {prod['price']}, {prod['size']}, {prod['qtd']} -")
        except:
            showinfo(title='Erro', message="Produto não existe!")

    # Editar Produto
    def editProduct(self):
        try:
            self.controller.editProductController(
                self.prevName.get(),
                self.name.get(),
                float(self.price.get()),
                self.size.get(),
                int(self.qtd.get())
            )
            showinfo(title='Sucesso', message="Produto atualizado com sucesso!")
        except:
            showinfo(title='Erro', message="ERRO, Tente novamente!")

    # Deletar Produto
    def deleteProduct(self):
        try:
            prod = self.controller.deleteProductController(
                self.name.get(),
            )
            showinfo(title='Sucesso',
                     message=f"{prod['name']} removido com sucesso")
        except:
            showinfo(title='Erro', message="ERRO, Tente novamente!")

    # Controller
    def setController(self, controller):
        self.controller = controller

    # Manter em loop
    def run(self):
        self.root.mainloop()

    # Fechar velha
    def close(self, evento=None):
        sys.exit()
