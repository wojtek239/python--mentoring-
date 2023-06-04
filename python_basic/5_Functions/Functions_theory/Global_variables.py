# NEVER USE

def fun_1():
    global arg_1
    arg_1 = "devs-mentoring"
    fun_2()


def fun_2():
    print(arg_1)


if __name__ == "__main__":
    fun_1()