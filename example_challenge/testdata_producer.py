import random
import json

data_set = []

# Both ints > 0
for index in range(100):
    a,b = random.randint(1,1001), random.randint(1,1001)
    data_set.append({'id':f'{index:04}', 'arguments':f'{a},{b}','return':f'{a+b}'})

# a is an integer, b is a float
for index in range(100, 200):
    a,b = random.randint(1,1001), random.uniform(1,1000)
    data_set.append({'id':f'{index:04}', 'arguments':f'{a},{b}','return':f'{a+b}'})

# b is an integer, a is a float
for index in range(200,300):
    b,a = random.randint(1,1001), random.uniform(1,1000)
    data_set.append({'id':f'{index:04}', 'arguments':f'{a},{b}','return':f'{a+b}'})

# a is 0, b is anything
for index in range(300,400):
    a,b = 0, random.randint(1,1001)
    data_set.append({'id':f'{index:04}', 'arguments':f'{a},{b}','return':'0'})

# b is 0, a is anything
for index in range(400,500):
    b , a = 0, random.randint(1,1001)
    data_set.append({'id':f'{index:04}', 'arguments':f'{a},{b}','return':'0'})

# both a & b are zero
data_set.append({'id':f'600', 'arguments':f'{0},{0}','return':'0'})

# a is -ve int, b is +ve value
for index in range(700,800):
    a,b = random.randint(-1000,0), random.uniform(1,1000)
    data_set.append({'id':f'{index:04}', 'arguments':f'{a},{b}','return':f'{0}'})

# a is +ve int, b is  -e int
for index in range(800,900):
    b,a = random.randint(-1000,0), random.uniform(1,1000)
    data_set.append({'id':f'{index:04}', 'arguments':f'{a},{b}','return':f'{0}'})

# a is -ve int, b is  -e int
for index in range(900,1000):
    b,a = random.randint(-1000,0), random.uniform(-100,0)
    data_set.append({'id':f'{index:04}', 'arguments':f'{a},{b}','return':'0','raises':'ValueError'})

with open('testdata.json', 'w') as json_fp:
    json.dump(obj=data_set, fp=json_fp)