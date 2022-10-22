# This function, implements for error handling of this program.
def error(instructions_set, instruction_operands):
    # Error handling 1.
    nk = -1
    for k in instructions_set:
        nk += 1
        string = k
        if string == '\n':
            break
        if string[5] == "+" and string[9:12] == "000":
            pass
        else:
            print("Invalid instruction in line ", nk)
            quit()

    # Error handling 2.
    nz = -1
    for z in instructions_set:
        if z == "\n":
            break
        nz += 1
        if len(z) != 17:
            print("Invalid instruction in line ", nz)
            quit()

    # Error handling 3.
    assembly_instructions = ["000", "BRU", "RWD", "LDA", "STO", "SUB", "BMI", "MPY", "ADD", "WWD", "HLT"]
    nn = -1
    for n in instruction_operands:
        nn += 1
        if n[1:4] in assembly_instructions:
            pass
        else:
            print("Invalid instruction in line ", nn)
            quit()


# BRU or branch unconditional command implementation.
def branch_unconditional(address):
    return int(address)


# RWD or read command implementation.
def read(database, address, value, counter=0):
    if type(value) is list:
        database.update({int(address): value[counter]})
    else:
        database.update({int(address): value})


# LDA or load command implementation.
def load(address, code):
    temp_val = code.get(int(address))
    if type(temp_val) is list:
        return int(temp_val[1])
    return temp_val


# STO or store command implementation.
def store(address, database, acc):
    database.update({int(address): acc})


# SUB or subtraction command implementation.
def subtraction(database, address, acc):
    temp_val = database.get(int(address))
    if type(temp_val) is list:
        result = int(acc) - int(temp_val[1])
        return result
    result = int(acc) - int(temp_val)
    return result


# BMI or branch if minus command implementation.
def branch_if_minus(acc, address):
    if acc < 0:
        return int(address)
    else:
        return -1


# MPY or multiply command implementation.
def multiply(database, address, acc):
    result = database.get(int(address)) * acc
    return result


# ADD or add command implementation.
def add(database, address, acc):
    temp_val = database.get(int(address))
    if type(temp_val) is list:
        result = int(temp_val[1]) + acc
        return result
    result = int(temp_val) + acc
    return result


# WWD or write command implementation.
def write(database, address):
    print(database.get(int(address)))


# HLT or halt command implementation.
def halt():
    quit()


# The main function of program.
def solve(the_memory, last_line, the_input, isList):
    the_acc = 0

    count_if_list = -1

    pc = 0
    while pc != last_line:

        cmd = the_memory.get(pc)[0]
        ads = the_memory.get(pc)[1]

        if cmd == "BRU":
            pc = branch_unconditional(ads)
        elif cmd == "RWD":
            if isList:
                count_if_list += 1
                read(the_memory, ads, the_input, count_if_list)
                pc += 1
            else:
                read(the_memory, ads, the_input)
                pc += 1
        elif cmd == "LDA":
            the_acc = load(ads, the_memory)
            pc += 1
        elif cmd == "STO":
            store(ads, the_memory, the_acc)
            pc += 1
        elif cmd == "SUB":
            the_acc = subtraction(the_memory, ads, the_acc)
            pc += 1
        elif cmd == "BMI":
            win = branch_if_minus(the_acc, ads)
            if win == -1:
                pc += 1
            else:
                pc = win
        elif cmd == "MPY":
            the_acc = multiply(the_memory, ads, the_acc)
            pc += 1
        elif cmd == "ADD":
            the_acc = add(the_memory, ads, the_acc)
            pc += 1
        elif cmd == "WWD":
            write(the_memory, ads)
            pc += 1
        elif cmd == "HLT":
            halt()
        else:
            # Error handling 3.
            print("Invalid instruction in line ", pc)
            quit()


# Find the input of our program in the .txt file.
def find_input(the_lines):
    the_nav = 0
    for nav in the_lines:
        if nav == "\n":
            main_input_line = the_lines[the_nav + 1:]
            return main_input_line, the_nav
        the_nav += 1


# This function check the input/input list to be standard (don't have "\n").
def make_input_std(input_list):
    nav_count = 0
    for nav in input_list:
        if "\n" in nav:
            input_list[nav_count] = nav[:-1]
        nav_count += 1
    return input_list


# Open the file and make a list of lines.
with open('sum_0_to_n.txt', 'r') as f:
    lines = f.readlines()
ni = -1

# Initialize everything we need to get input of our program.
memory = {}
temp = find_input(lines)
input_line = temp[0]
nav_index = temp[1]
dict_values = []

# Organize our command lines.
for i in range(nav_index):
    dict_values += [(lines[i].split())[1]]
for j in range(nav_index):
    memory.update({j: [dict_values[j][1:4], dict_values[j][-4:]]})

# Make the input list standard.
input_line = make_input_std(input_line)

# Check if the input of our program is list.
haveList = False
if type(input_line) is list:
    haveList = True

error(lines, dict_values)
solve(memory, nav_index, input_line, haveList)