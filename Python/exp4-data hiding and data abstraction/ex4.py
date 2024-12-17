class Rect:
    length = 4
    width = 6
    height = 2

    def volume(self):
        return self.length * self.width * self.height


class Sphere:
    radius = 8

    def volume(self):
        return 3.14 * self.radius * self.radius * self.radius


class Cube:
    edge = 5

    def volume(self):
        return self.edge * self.edge * self.edge


class Rectangle3D:
    length = 5
    width = 4

    def volume(self):
        return 0.5 * self.length * self.width


# Create objects of each class
rr = Rect()
ss = Sphere()
cc = Cube()
tt = Rectangle3D()

# Print volumes
print("Volume of rectangle =", rr.volume())
print("Volume of sphere =", ss.volume())
print("Volume of cube =", cc.volume())
print("Volume of rectangle 3D =", tt.volume())
