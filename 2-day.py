import math

def run_comp(instr):
    cur = 0;
    while(instr[cur] != 99):
        if(instr[cur] == 1):
            instr[instr[cur+3]] = instr[instr[cur+1]] + instr[instr[cur+2]]
        elif(instr[cur] == 2):
            instr[instr[cur+3]] = instr[instr[cur+1]] * instr[instr[cur+2]]
        cur += 4;
    return instr

def part_1(instr):
    test = instr.copy()
    test[1] = 12
    test[2] = 2
    run_comp(test)
    print(test[0])

def part_2(instr):
    for i in range(100):
        for j in range(100):
            test = instr.copy()
            test[1] = i
            test[2] = j
            try:
                run_comp(test)
                if(test[0] == 19690720):
                    print(100*i + j)
                    return
            except:
                IndexError
    print("nothing found")

def main():
    with open("2-input.txt") as raw:
        instr = list(map(int, raw.read().split(',')))
        part_1(instr)
        part_2(instr)

if __name__ == "__main__":
    main()

