inventario = [
    {'material':'Chatarra Pesada',
     'peso':50},
    {'material':'Chatarra Ligera',
     'peso':20},
    {'material':'Arrabio',
     'peso':80},
    {'material':'Ferroaleaciones',
     'peso':20}, 
]

new_list = [list(filter(lambda insumo: insumo['peso'] >= 20, inventario))]
print('Los insumos con peso mayor a 20 toneladas son: ', new_list)