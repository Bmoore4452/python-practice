# with open("new_text.txt", "r") as file:
#     a = file.readlines()
#     print(a)


def read_file(file_name):
    with open(file_name) as file:
        f = file.read()
        print(f)
        return f


def read_file_as_list(file_name):
    file = open(file_name, "r")
    file_list = file.read()
    file_content = file_list.split("\n")
    return file_content


def output(file_contents, output_filename):
    file = open(file_contents, "r")
    a = file.readline()
    file2 = open(output_filename, "w")
    file2.write(a)


def every_other(file_name):
    file_list = read_file_as_list(file_name)
    a = file_list[::2]
    return a

def reverse_file(file_name):
    file_list = read_file_as_list(file_name)
    reversed_list = file_list[::-1]
    return reversed_list
    


def main():
    a = read_file("new_text.txt")
    b = read_file_as_list("new_text.txt")
    output("new_text.txt", "bmoore.txt")
    print(every_other("new_text.txt"))
    print(reverse_file("new_text.txt"))
    # print(b)


if __name__ == "__main__":
    main()
