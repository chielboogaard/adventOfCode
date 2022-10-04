def main():
    file = open('data.txt')
    fileData = file.read()
    data = fileData.splitlines()

    dataLength = len(data[0])

    oxList = data.copy()
    co2List = data.copy()
    print("oxygen")
    for index1 in range(0, dataLength):
        zeroList = []
        oneList = []
        zero = 0
        one = 0
        for index2, value in enumerate(oxList):
            thing = int(oxList[index2][index1])
            
            if thing == 0:
                zero+=1
                zeroList.append(value)
            elif thing == 1:
                one+=1
                oneList.append(value)

        # print(f"zerolist: {zeroList}")
        # print(f"onelist: {oneList}")
        #oxygen generator rating
        if one == zero or zero < one:
            for ele in zeroList:
                oxList.remove(ele)
        else:
            for ele in oneList:
                oxList.remove(ele)
        if len(oxList) <= 1:
            break
    print(f"oxList: {oxList}")

    print("CO2")
    for index1 in range(0, dataLength):
        zeroList = []
        oneList = []
        zero = 0
        one = 0
        for index2, value in enumerate(co2List):
            thing = int(co2List[index2][index1:index1+1])
            
            if thing == 0:
                zero+=1
                zeroList.append(value)
            elif thing == 1:
                one+=1
                oneList.append(value)

        # print(f"co2List: {co2List}")
        # print(f"zerolist: {zeroList}")
        # print(f"onelist: {oneList}")
        #oxygen generator rating
        if not(zero < one or zero == one):
            for ele in zeroList:
                co2List.remove(ele)
        else:
            for ele in oneList:
                co2List.remove(ele)
        if len(co2List) <= 1:
            break
    
    # print(f"oxlist: {oxList}")
    print(f"co2List: {co2List}")

    oxRes = int(oxList[0],2)
    co2Res = int(co2List[0],2)

    print(f"oxRes: {oxRes}")
    print(f"co2Res: {co2Res}")

    LifeSupportRating = oxRes * co2Res

    print(f"LifeSupportRating: {LifeSupportRating}")

if __name__ == '__main__':
   main()