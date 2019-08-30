item_i = [i for i in [0,1,2,4,8,16,32,63,128,256]]
item_j = [i for i in [0,1,2,4,8,16,32,63,128,256]]
item_k = [i for i in [0,1,2,4,8,16,32,63,128,256]]

output = []
for i in item_i:
    for j in item_j:
        for k in item_k:
            output.append((i,j,k))
pass