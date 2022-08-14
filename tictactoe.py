def display(r_1):
    print(r_1[0])
    print(r_1[1])
    print(r_1[2])


list_1 = [[" " ," "," "],[" " ," "," "],[" " ," "," "]]



def check_who_won(list__):
    t_1 = False
    for i in range(0,3):
        val_1 = list__[i][0]
        val_2 = list__[i][1]
        val_3 = list__[i][2]
        if val_1 == val_2 == val_3:
            print(val_1)
            return True

    for i in range(0,3):
        val_1 = list__[0][i]
        val_2 = list__[1][i]
        val_3 = list__[2][i]
        if val_1 == val_2 == val_3:
            print(val_1)
            return True
    if list__[0][0] == list__[1][1] == list__[2][2]:
        print(list__[0][0])
        return True
    if list__[2][0] == list__[1][1] == list__[2][0]:
        pass
            
            


def main_fun():
    print("Hello Welcome to the game")
    i = 0

    while True:
        display()
        if i % 2 == 0:
            print("P1 make your move!")
            print("Value range from 0-2")
            p_1_row = int(input("Enter row: "))
            p_1_col = int(input("Enter column: "))
            list_1[p_1_row][p_1_col] = 'O'
        else:
            print("P2 make your move!")
            print("Value range from 0-2")
            p_2_row = int(input("Enter row: "))
            p_2_col = int(input("Enter column: "))
            list_1[p_2_row][p_2_col] = 'X'
        i = i + 1
        display()
        

            


        

   
    