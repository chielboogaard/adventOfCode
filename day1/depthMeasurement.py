def main():
    increase = 0

    file = open('data.txt')
    fileData = file.read()
    data = fileData.splitlines()

    # print(fileDataSplit)
    # data = [1,2,3,4,5]
    
    for number in data:
        current = int(number)
        try:
            if previous < current:
                increase+=1
        except:
            firstnumber = None
        previous = current
    print(increase)
if __name__ == '__main__':
   main()