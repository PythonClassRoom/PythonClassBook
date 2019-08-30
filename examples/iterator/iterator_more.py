import itertools

layer_0 = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256]
layer_1 = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256]
layer_2 = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256]

activation = ['relu', 'tanh', 'sigmu']
arqui_recipe = []

for z in list(itertools.product(activation, repeat=3)):
    for i in layer_0:
        if i == 0:
            continue
        for j in layer_1:
            for k in layer_2:
                if j == 0 and k != 0:
                    continue
                arqui_recipe.append(((i, z[0]), (j, z[1]), (k, z[2])))

for p in arqui_recipe:
    for q in p:
        q
pass