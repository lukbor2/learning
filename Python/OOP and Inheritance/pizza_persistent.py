from pizzashop import PizzaShop
import pickle

shop = PizzaShop()
print(shop.server, shop.chef)

pickle.dump(shop, open('shopfile.pkl', 'wb'))