class Controller:

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def getAllProductsController(self):
        return self.model.getAllProductsModel()

    def searchProductController(self, name):
        return self.model.searchProductModel(name)

    def createProductController(self, name, price, size, qtd):
        self.model.createProductModel(name, price, size, qtd)

    def editProductController(self, prevName, nextName, nextPrice, nextSize, nextQtd):
        self.model.editProductModel(
            prevName, nextName, nextPrice, nextSize, nextQtd)

    def deleteProductController(self, name):
        return self.model.deleteProductModel(name)
