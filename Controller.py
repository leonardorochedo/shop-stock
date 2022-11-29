from View import View
from Model import Model


class Controller:

    def __init__(self):
        self.view = View()
        self.model = Model()

    def getAllProductsController():
        return Model.getAllProductsModel()

    def searchProductController(name):
        return Model.searchProductModel(name)

    def createProductController(name, price, size, qtd):
        Model.createProductModel(name, price, size, qtd)

    def editProductController(prevName, nextName, nextPrice, nextSize, nextQtd):
        Model.editProductModel(
            prevName, nextName, nextPrice, nextSize, nextQtd)

    def deleteProductController(name):
        return Model.deleteProductModel(name)
