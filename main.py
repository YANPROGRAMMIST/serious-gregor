class Ship():
  ship_class = "Крейсер"

  def  __init__(self, name):
    self.name = name
    print("Корабль {name} класса {ship_class} cоздан".format(name = name, ship_class = self.ship_class))
  
  def fire(self, ship):
    print("Огонь по кораблю {0}".format(ship.name))

ship1 = Ship("Победа")
ship2 = Ship("Беда")
# print(ship1.name)
# print(ship2.name)
# print(ship1.ship_class)
# print(ship2.ship_class)

ship1.fire(ship2)
ship2.fire(ship1)