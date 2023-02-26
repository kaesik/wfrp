import random
t1 = [[random.randint(1,100),random.randint(1,100),random.randint(1,100)],[random.randint(1,100),random.randint(1,100),random.randint(1,100)],[random.randint(1,100),random.randint(1,100),random.randint(1,100)]]
t2 = [[random.randint(1,100),random.randint(1,100),random.randint(1,100)],[random.randint(1,100),random.randint(1,100),random.randint(1,100)],[random.randint(1,100),random.randint(1,100),random.randint(1,100)]]
t3 = [[],[],[]]
for y in range(0,3):
	for x in range(0,3):
		t3[x].append(t1[y][x] + t2[y][x])
print(t1)
print(t2)
print(t3)
