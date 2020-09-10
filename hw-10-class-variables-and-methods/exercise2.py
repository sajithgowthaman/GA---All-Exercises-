class Vampire:
  coven =[]

  def __init__(self, name, age):
    self.name = name
    self.age = 0
    self.in_coffin = bool
    self.drank_blood_today = bool
    __class__.coven.append(self)

  def drink_blood(self):
    self.drank_blood_today = True

  @classmethod
  def sunset(cls):
    for vamps in cls.coven:
      vamps.in_coffin = False
      vamps.drank_blood_today = False

  def go_home(self):
    self.in_coffin = True

  @classmethod
  def sunrise(cls):
    dead = []
    alive = cls.coven
    for vamps in cls.coven:
      if vamps.in_coffin == False or vamps.drank_blood_today == False:
        dead.append(vamps) #dead = vamps needed to be removed
    for vamps in dead:
      alive.remove(vamps)
    return alive #We could alter this line using cls.coven itself, but lets not mess up the OG list

def main():
  riley = Vampire('Riley', 25)
  alice = Vampire('Alice', 24)
  jasper = Vampire('Jasper', 23)
  renesmee = Vampire('Renesmee', 25)
  marcus = Vampire('Marcus', 28)
  zafrina = Vampire('Zafrina', 49)
  demetri = Vampire('Demetri', 28)

  print('Coven at the beginning:')
  for vampire in Vampire.coven:
    print(vampire.name)

  Vampire.sunset()
  riley.drink_blood()
  riley.go_home()
  jasper.drink_blood()
  renesmee.drink_blood()
  renesmee.go_home()
  marcus.go_home()
  Vampire.sunrise() # Should remove all vampires except 'Riley' and 'Renesmee'

  print('Coven at the end:')
  for vampire in Vampire.coven:
    print(vampire.name) #--> 'Riley', 'Renesmee'

main()
