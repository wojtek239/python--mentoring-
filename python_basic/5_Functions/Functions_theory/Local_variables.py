def fun_1():
    arg_1 = "devs-mentoring"
    fun_2()


def fun_2():
    print(arg_1)


def fun_1_1():
    arg_1 = "devs-mentoring"
    fun_2_2(arg_1)


def fun_2_2(arg_1):
    print(arg_1)


if __name__ == "__main__":
    fun_1()
    fun_1_1()