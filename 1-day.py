import math

def part_1():
    with open("1-input.txt") as raw:
        data = raw.read().splitlines()

        total = 0
        for i in data:
            total += math.floor(int(i)/3)-2

        print("total fuel:", total)

def find_fuel(a):
    total = 0;
    fuel = math.floor(a/3)-2
    if(fuel <= 0):
        return total
    return fuel + find_fuel(fuel) 

def part_2():
    with open("1-input.txt") as raw:
        data = raw.read().splitlines()

        total = 0
        for i in data:
            total += find_fuel(int(i))

        print("actual total fuel:", total)

def main():
    part_1()
    part_2()



if __name__ == "__main__":
    main()

