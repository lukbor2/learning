import pickle

obj = pickle.load(open('shopfile.pkl','rb'))
print(obj.server, obj.chef)

obj.order("LSP")