#Using pickle to save the entire pizza shop object
#It can be retrieved later (see pizza_persisten_retrieve.py

from pizzashop import PizzaShop
import pickle

shop = PizzaShop()
print(shop.server, shop.chef)

pickle.dump(shop, open('shopfile.pkl', 'wb'))