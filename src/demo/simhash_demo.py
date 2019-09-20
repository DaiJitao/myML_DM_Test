from simhash import Simhash

print(Simhash("人造甜味范丞丞").distance(Simhash("很坏")))
print(Simhash("很好").distance(Simhash("不太好")))
print(Simhash("很好").distance(Simhash("非常好")))
