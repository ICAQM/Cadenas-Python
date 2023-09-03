Precio = input("Escrive el precio del producto con 2 decimales: ")
print(Precio[:Precio.find('.')], 'Euros y', Precio[Precio.find('.')+1:], 'céntimos.')
