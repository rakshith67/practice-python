from player import Player
from enemy import Enemy, Troll, Vampire

me = Player("me")
print(me.name)
print(me.lives)
me.lives -= 1
me.lives -= 1
me.lives -= 1
me.lives -= 1
print(me)

my_enemy = Enemy("ds", 4, 1)
my_enemy.take_damage(4)
print(my_enemy)
my_enemy.take_damage(1)
print(my_enemy)

ugly_troll = Troll("Pug")
print(ugly_troll)
another_troll = Troll("Cut")
print(another_troll)
ugly_troll.grunt()
another_troll.grunt()

vamp = Vampire("Vlad")
print(vamp)
vamp.take_damage(5)
print(vamp)

print("-" * 40)
another_troll.take_damage(30)
print(another_troll)

while vamp._alive:
    vamp.take_damage(1)
    print(vamp)
