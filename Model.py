import pymongo

client = pymongo.MongoClient('localhost', 27017)  # create connectionn
db = client.shop  # create db if not exist
products = db.products  # create collection


class Model:

    def __init__(self):
        pass

    def getAllProductsModel():
        listProducts = []
        prods = products.find()
        for prod in prods:
            print(prod)
            listProducts.append(prod)

        return listProducts

    def searchProductModel(name):
        try:
            prod = products.find_one({'searchable': name.upper()})
            return prod
        except:
            return 0

    def createProductModel(name, price, size, qtd):
        product = {
            'name': name,
            'searchable': name.upper(),
            'price': price,
            'size': size,
            'qtd': qtd
        }
        try:
            products.insert_one(product)
            return 1
        except:
            return 0

    def editProductModel(prevName, nextName, nextPrice, nextSize, nextQtd):
        prevProduct = products.find_one({'searchable': prevName.upper()})
        newProduct = {'$set': {
            'name': nextName,
            'searchable': nextName.upper(),
            'price': nextPrice,
            'size': nextSize,
            'qtd': nextQtd
        }}
        try:
            products.update_one(prevProduct, newProduct)
            return 1
        except:
            return 0

    def deleteProductModel(name):
        try:
            prod = products.find_one({'searchable': name.upper()})
            products.delete_one(prod)
            return prod
        except:
            return 0
