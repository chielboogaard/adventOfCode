def main():
    horizontal = 0
    depth = 0
    aim = 0

    file = open('data.txt')
    fileData = file.read()
    data = fileData.splitlines()

    for move in data:
        direction, amount = move.split()
        
        amount = int(amount)

        if "up" in direction:
            aim = aim - amount
        elif "down" in direction:
            aim = aim + amount
        elif 'forward' in direction:
            horizontal = horizontal + amount
            depth = depth + (amount * aim)

    # print(f"aim: {aim}")
    # print(f"horizontal: {horizontal}")
    # print(f"depth: {depth}")

    plannedCourse = horizontal * depth

    print(plannedCourse)

if __name__ == '__main__':
   main()