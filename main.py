import game_mod as gm

ishora = 'yes'

while ishora == 'yes':
    my_attempts = gm.find_the_number()
    pc_attempts = gm.find_the_number_pc()

    if my_attempts < pc_attempts:
        print(f"Tabriklayman siz yutdingiz. Men {pc_attempts} urinishda, siz {my_attempts} urinishda topdingiz")
    elif my_attempts > pc_attempts:
        print(f"Men yutdim. Men {pc_attempts} urinishda, siz {my_attempts} urinishda topdingiz.")
    else:
        print(f"Do'stlik g'alaba qozondi. {my_attempts} urinishda topdik")

    ishora = input("Yana o'ynaysizmi (yes/no)? ")
