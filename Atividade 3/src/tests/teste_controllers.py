from src.controllers.product_controller import ProductController

from src.controllers.product_controller import Product



controller = ProductController()
items = controller.getALL
for item in items:
    print(item)

novo_item = Product("TESTESSSSS", "TESSSSSTE", 19.90)
print(controller.inserir_item(novo_item))

print("**************************************")
items = controller.getALL
for item in items:
    print(item)

print("**************************************")
"""
item = controller.pegar_item("CAF6")
print(item)

print("*************************")
items = controller.buscar_todos_itens_nome("Aula")
print(items)

"""




#from src.models.product import Product
#from models.product import Product
#from src.models.product import Product