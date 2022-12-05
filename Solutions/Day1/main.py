import os
import sys
def main():
    findMax()

def findMax():
    elf_num = 1
    max_cals_and_elf_num = [0, 0]
    current_cals = 0
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            if(line == ""):
                if(current_cals > max_cals_and_elf_num[0]):
                    max_cals_and_elf_num[0] = current_cals
                    max_cals_and_elf_num[1] = elf_num
                    elf_num += 1
                    current_cals = 0
                else:
                    current_cals = 0
                    elf_num += 1 
            else:
                current_cals += int(line)

    print("Elf number", str(max_cals_and_elf_num[1]), "is carrying the most calories with", str(max_cals_and_elf_num[0]) + ".")

main()
