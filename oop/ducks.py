class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee this is fun")
        elif self.ratio == 1:
            print("This is hard work, I am flying")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("waddle waddle waddle")

    def swim(self):
        print("Come on it, its lovely")

    def quack(self):
        print("Quack Quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def __init__(self):
        self._wing = Wing(0.8)

    def walk(self):
        print("waddle waddle I waddle too")

    def swim(self):
        print("Come on it, its bit chilly penguin")

    def quack(self):
        print("I am penguin")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()
    duck.fly()


if __name__ == "__main__":
    donald = Duck()
    test_duck(donald)

    donald_penguin = Penguin()
    test_duck(donald_penguin)
