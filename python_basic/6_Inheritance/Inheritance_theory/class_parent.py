class Parent1:
    def __init__(self):
        super().__init__()
        print("in parent 1 class...")
 # pass


class Parent2:
    def __init__(self):
        print("in parent 2 class...")
 # pass


class Deriverd(Parent1, Parent2):
    def __init__(self):
        super().__init__()
        print("in deriverd class ...")
  #  pass


if __name__ == "__main__":
    main()

