# 类定义和使用
class Player:
    def __init__(self, name):
        self.name = name

    def sayhello(self):
        print("hello", self.name.title())

    def intro(self):
        print("I am player.")


curry = Player("curry")
print(curry.name)
curry.sayhello()
curry.intro()

james = Player("james")
print(james.name)
james.sayhello()
james.intro()
