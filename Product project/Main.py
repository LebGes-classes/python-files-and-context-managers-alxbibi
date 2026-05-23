from ProductCard import *
from Parser import *
import Menu

txt_parser = TxtParser()
json_parser = JsonParser()

prods = json_parser.deserialize()
menu = Menu.Menu(products_dict=prods)

def run():
    is_running = True
    while is_running:
        is_running = menu.main_menu_logic(is_running)

run()

products = menu.get_products_dict()

json_parser.serialize(products)

