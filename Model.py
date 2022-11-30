import pymongo


class Model:

    def __init__(self):
        self.client = pymongo.MongoClient(
            'localhost', 27017)  # create connectionn
        self.db = self.client.shop  # create db if not exist
        self.products = self.db.products  # create collection

    def getAllProductsModel(self):
        listProducts = []
        prods = self.products.find()
        for prod in prods:
            listProducts.append(prod)

        return listProducts

    def searchProductModel(self, name):
        try:
            prod = self.products.find_one({'searchable': name.upper()})
            return prod
        except:
            return 0

    def createProductModel(self, name, price, size, qtd):
        product = {
            'name': name,
            'searchable': name.upper(),
            'price': price,
            'size': size,
            'qtd': qtd
        }
        try:
            self.products.insert_one(product)
            return 1
        except:
            return 0

    def editProductModel(self, prevName, nextName, nextPrice, nextSize, nextQtd):
        prevProduct = self.products.find_one({'searchable': prevName.upper()})
        newProduct = {'$set': {
            'name': nextName,
            'searchable': nextName.upper(),
            'price': nextPrice,
            'size': nextSize,
            'qtd': nextQtd
        }}
        try:
            self.products.update_one(prevProduct, newProduct)
            return 1
        except:
            return 0

    def deleteProductModel(self, name):
        try:
            prod = self.products.find_one({'searchable': name.upper()})
            self.products.delete_one(prod)
            return prod
        except:
            return 0
