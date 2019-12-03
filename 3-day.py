import math

def manDist(point):
    return abs(point[0]) + abs(point[1])

def part_1(wire1, wire2):
    w1_path = {}
    intersects = []

    current = [0,0]
    for i in wire1:
        dist = int(i[1:])
        if(i[0] == 'U'):
            for j in range(dist):
                w1_path[(current[0], current[1]+j+1)] = 1
            current[1] += dist
        elif(i[0] == 'R'):
            for j in range(dist):
                w1_path[(current[0]+j+1, current[1])] = 1
            current[0] += dist
        elif(i[0] == 'D'):
            for j in range(dist):
                w1_path[(current[0], current[1]-j-1)] = 1
            current[1] -= dist
        elif(i[0] == 'L'):
            for j in range(dist):
                w1_path[(current[0]-j-1, current[1])] = 1
            current[0] -= dist

    current = [0,0]
    for i in wire2:
        dist = int(i[1:])
        if(i[0] == 'U'):
            for j in range(dist):
                if((current[0], current[1]+j+1) in w1_path):
                    intersects.append([current[0], current[1]+j+1])
            current[1] += dist
        elif(i[0] == 'R'):
            for j in range(dist):
                if((current[0]+j+1, current[1]) in w1_path):
                    intersects.append([current[0]+j+1, current[1]])
            current[0] += dist
        elif(i[0] == 'D'):
            for j in range(dist):
                if((current[0], current[1]-j-1) in w1_path):
                    intersects.append([current[0], current[1]-j-1])
            current[1] -= dist
        elif(i[0] == 'L'):
            for j in range(dist):
                if((current[0]-j-1, current[1]) in w1_path):
                    intersects.append([current[0]-j-1, current[1]])
            current[0] -= dist


    # print(len(intersects))
    min = manDist(intersects[0])
    for i in intersects:
        if(manDist(i) < min):
            min = manDist(i)
    
    print(min)

def part_2(wire1, wire2):
    w1_path = {}
    intersects = []

    current = [0,0]
    steps = 0
    for i in wire1:
        dist = int(i[1:])
        if(i[0] == 'U'):
            for j in range(dist):
                steps += 1
                w1_path[(current[0], current[1]+j+1)] = steps
            current[1] += dist
        elif(i[0] == 'R'):
            for j in range(dist):
                steps += 1
                w1_path[(current[0]+j+1, current[1])] = steps
            current[0] += dist
        elif(i[0] == 'D'):
            for j in range(dist):
                steps += 1
                w1_path[(current[0], current[1]-j-1)] = steps
            current[1] -= dist
        elif(i[0] == 'L'):
            for j in range(dist):
                steps += 1
                w1_path[(current[0]-j-1, current[1])] = steps
            current[0] -= dist

    current = [0,0]
    steps = 0
    for i in wire2:
        dist = int(i[1:])
        if(i[0] == 'U'):
            for j in range(dist):
                steps += 1
                if((current[0], current[1]+j+1) in w1_path):
                    intersects.append(w1_path[(current[0], current[1]+j+1)] + steps)
            current[1] += dist
        elif(i[0] == 'R'):
            for j in range(dist):
                steps += 1
                if((current[0]+j+1, current[1]) in w1_path):
                    intersects.append(w1_path[(current[0]+j+1, current[1])] + steps)
            current[0] += dist
        elif(i[0] == 'D'):
            for j in range(dist):
                steps += 1
                if((current[0], current[1]-j-1) in w1_path):
                    intersects.append(w1_path[(current[0], current[1]-j-1)] + steps)
            current[1] -= dist
        elif(i[0] == 'L'):
            for j in range(dist):
                steps += 1
                if((current[0]-j-1, current[1]) in w1_path):
                    intersects.append(w1_path[(current[0]-j-1, current[1])] + steps)
            current[0] -= dist


    # print(len(intersects))
    min = intersects[0]
    for i in intersects:
        if(i < min):
            min = i
    
    print(min)

def main():
    with open("3-input.txt") as raw:
        instr = raw.read().splitlines()

        # # Sample Test
        # raw = "R8,U5,L5,D3\nU7,R6,D4,L4"
        # instr = raw.splitlines()

        wire1 = instr[0].split(',')
        wire2 = instr[1].split(',')
        part_1(wire1, wire2)
        part_2(wire1, wire2)

if __name__ == "__main__":
    main()

