def main():
    file = open('data.txt')
    fileData = file.read()
    data = fileData.splitlines()

    dataLength = len(data[0])
    datasLength = len(data)

    gamma = []
    epsilon = []
    for index1 in range(0, dataLength):
        zero = 0
        one = 0
        for index2 in range(0, datasLength):
            thing = int(data[index2][index1:index1+1])
            
            if thing == 0:
                zero+=1
            elif thing == 1:
                one+=1
            
        if zero > one:
            gamma.append(0)
            epsilon.append(1)
        else:
            gamma.append(1)
            epsilon.append(0)

    gammaRes = int("".join(str(x) for x in gamma), 2)
    epsilonRes = int("".join(str(x) for x in epsilon), 2)

    print(f"gammaRes: {gammaRes}")
    print(f"epsilonRes: {epsilonRes}")

    powerConsumption = gammaRes * epsilonRes

    print(f"powerConsumption: {powerConsumption}")

if __name__ == '__main__':
   main()