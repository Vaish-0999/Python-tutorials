numbers=[1,2,3]
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


p1=Point()
p1.x=10
p1.y=20
print(p1.x)
p1.move()
p1.draw()
