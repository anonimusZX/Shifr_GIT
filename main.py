from colorama import Back , init
import random
init()
print(Back.BLUE + """
________$$$$
_______$$__$
_______$___$$
_______$___$$
_______$$___$$
________$____$$
________$$____$$$
_________$$_____$$
_________$$______$$
__________$_______$$
____$$$$$$$________$$
__$$$_______________$$$$$$
_$$____$$$$____________$$$
_$___$$$__$$$____________$$
_$$________$$$____________$
__$$____$$$$$$____________$
__$$$$$$$____$$___________$
__$$_______$$$$___________$
___$$$$$$$$$__$$_________$$
____$________$$$$_____$$$$
____$$____$$$$$$____$$$$$$
_____$$$$$$____$$__$$
_______$_____$$$_$$$
________$$$$$$$$$$
""")
start_wel = "Введіть слово:"
wel_input = input(start_wel)
input_list = [wel_input[0] ,wel_input[1] ,wel_input[2] ,wel_input[3] ,wel_input[4]]
num_prog = input("Введіть номер програми (1-5):")
if num_prog == "1":
    first_prog = input_list[0] * 2 + input_list[1] * 2 + input_list[2] *  2 + input_list[3] * 2 + input_list[4] * 2    
    print(first_prog)
if num_prog == "2":
    second_prog = input_list[1] + input_list[0] + input_list[3] + input_list[2] + input_list[4]
    print(second_prog)
if num_prog == "3":
    third_prog = input_list[0] + input_list[4] + input_list[1] + input_list[4] + input_list[2] + input_list[4] + input_list[3] + input_list[4] + input_list[4]
    print(third_prog)
if num_prog == "4":
    pass
if num_prog == "5":
    f_list = ['б' , 'з' , 'ф']
    fint = random.randint(0 ,2)
    if fint == "2":
        pntf = input_list[4] + input_list[3] * 3 + f_list[2] * 2
        print(pntf)
    else:
        pntrf = input_list[1] + input_list[4] * 2 + f_list[2] * 5
        print(pntrf)
