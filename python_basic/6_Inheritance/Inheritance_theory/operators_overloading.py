class Area:
    def __init__(self, area_):
        self.area = area_

    def __add__(self, obj):
        return self.area + obj.area


def main(self):
    area1 = Area(100)
    area2 = Area(200)

    print(area1 + area2)


if __name__ == "__main__":
    main()


# __sub__
# __lt__
# __eq__
# __str__