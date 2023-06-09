import copy


class Object:
    def __init__(self, name_):
        self.name = name_


class Box:
    def __init__(self, obj_name_):
        self.object = Object(obj_name_)
        self.amount_elements = 1


def main():
    box_for_stuff = Box("laptop")
    box_for_new_stuff = copy.copy(box_for_stuff)

    box_for_new_stuff.object.name = "tv"
    box_for_new_stuff.amount_elements = 2

    print("value of first object should stay the same (laptop), and it's containing "
          "value: ", box_for_stuff.object.name)

    print("first box should still have field amount_elements = 1 now its equal to: ",
          box_for_stuff.amount_elements)


if __name__ == "__main__":
    main()
