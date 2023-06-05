# you have to add 'b' to be able to use binary

file = open("binary_file.bin", "wb")

numbers = [1, 2, 10, 15]
bin_list = bytearray(numbers)

file.write(bin_list)
file.close()