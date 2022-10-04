def main():
    horizontal = 0
    depth = 0

    file = open('data.txt')
    fileData = file.read()
    data = fileData.splitlines()

    for move in data:
        direction, amount = move.split()
        
        amount = int(amount)

        if 'forward' in direction:
            horizontal = horizontal + amount
        elif "up" in direction:
            depth = depth - amount
        elif "down" in direction:
            depth = depth + amount
    
    plannedCourse = horizontal * depth

    print(plannedCourse)

if __name__ == '__main__':
   main()