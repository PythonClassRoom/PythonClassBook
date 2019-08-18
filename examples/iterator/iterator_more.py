import itertools

item_i = [0,1,2,4,8,16,32,64,128,256]
item_j = [0,1,2,4,8,16,32,64,128,256]
item_k = [0,1,2,4,8,16,32,64,128,256]

activation = ['relu', 'tanh', 'sigmu']
output = []

for z in list(itertools.product(activation, repeat=3)):
    for i in item_i:
        if i == 0:
            continue
        for j in item_j:
            for k in item_k:
                if j == 0 and k != 0:
                    continue
                output.append(((i, z[0]),(j,z[1]),(k,z[2])))

for p in output:
    print(p)
pass