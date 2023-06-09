from utils import show_welcome


def main():
    print(__name__)
    name_u = input("give your name: ")
    name_r = input("give your parent name: ")
    show_welcome(name_u, name_r)

    user_name = input("give fake name: ")
    parent_name = input("give second parent name: ")
    show_welcome(user_name, parent_name)


if __name__ == "__main__":
    main()
