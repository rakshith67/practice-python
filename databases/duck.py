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
        self.fly = self.aviate

    def walk(self):
        print("waddle waddle I waddle too")

    def swim(self):
        print("Come on it, its bit chilly penguin")

    def quack(self):
        print("I am penguin")

    def aviate(self):
        print("I won the lottery")


class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        # if isinstance(duck, Duck):
        fly_method = getattr(duck, 'fly', None)
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add duck, Are you sure it's not a " + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError as e:
                print("One Duck Down")
                problem = e
        if problem:
            raise problem

# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()
#     duck.fly()


if __name__ == "__main__":
    donald = Duck()
    donald.fly()
