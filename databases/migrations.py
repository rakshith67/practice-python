import duck

flock = duck.Flock()
duck1 = duck.Duck()
duck1 = duck.Duck()
duck2 = duck.Duck()
duck3 = duck.Duck()
duck4 = duck.Duck()
duck5 = duck.Duck()
duck6 = duck.Duck()
duck7 = duck.Duck()
penguin1 = duck.Penguin()

flock.add_duck(duck1)
flock.add_duck(duck2)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)
flock.add_duck(penguin1)

flock.migrate()
