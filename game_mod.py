import random

def find_the_number(number = 10):
    num = random.randint(1, number)
    my_num = None
    k = 0

    print(f"Kompyuter 1 va {number} oraliqdagi sonni o'yladi.")

    while num != my_num:
        my_num = int(input("Son kiriting: "))
        k += 1

        if my_num > num:
            print(f"Men o'ylagan son {my_num} dan kichikroq")
        elif my_num < num:
            print(f"Men o'ylagan son {my_num} dan kattaroq")

    print("Tabriklayman to'g'ri topdingiz")
    return k

def find_the_number_pc():
    input("Son o'ylang: ")
    first_num = 1
    last_num = 10
    k = 0

    while True:
        pc_num = random.randint(first_num, last_num)
        ishora = input(f"Siz o'ylagan son {pc_num} mi? " 
                        f"Undan kattami (+), kichckinami (-), to'g'rimi (t)? Belgini kiriting: ")

        if ishora == '+':
            first_num = pc_num + 1
        elif ishora == '-':
            last_num = pc_num - 1
        elif ishora == 't':
            k += 1
            break

        k += 1

    return k
        
        
