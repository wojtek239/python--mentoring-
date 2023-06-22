class Polygon:
    def __init__(self, sides_, angles_sum_):
        self.sides = sides_
        self.angles_sum = angles_sum_

    def get_perimeter(self):
        return sum(self.sides)

    def get_angles_sum(self):
        print(self.angles_sum)


class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__([a,b,c], 180)

    def get_area(self):
        a,b,c = self.sides[0], self.sides[1], self.sides[2]
        p = (self.sides[0] + self.sides[1] + self.sides[2]) / 2
        return (p*(p-a)*(p-b)*(p-c)) ** 0.5

def main():
    even_arm_triangle = Triangle(5,5,5)
    print(even_arm_triangle.get_perimeter())
    even_arm_triangle.get_angles_sum()
    print("{:.4f}".format(even_arm_triangle.get_perimeter()))

if __name__ == "__main__":
    main()