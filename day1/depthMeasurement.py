def main():
    increase = 0
    previous = 0

    file = open('data.txt')
    fileData = file.read()
    data = fileData.splitlines()

    # print(fileDataSplit)
    # data = [1,2,3,4,5]
    
    for number in data:
        current = int(number)
        if previous < current:
            increase+=1
        previous = current
    print(increase -1 )
if __name__ == '__main__':
   main()