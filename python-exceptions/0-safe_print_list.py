#!/usr/bin/python3
def safe_print_list(my_list, x):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass  # Listdə element qurtararsa, heç nə etmə
    print()  # Yuxarıda çap olunan elementlərin ardınca bir yeni sətir əlavə et
    return count 
