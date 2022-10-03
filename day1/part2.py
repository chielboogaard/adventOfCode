def main():
    increase = 0

    file = open('data.txt')
    fileData = file.read()
    data = fileData.splitlines()

    # data = [1,2,3,4,5,6]
    
    for index, number in enumerate(data[3:]):
        prev = int(data[index]) + int(data[index+1]) + int(data[index+2])
        curr = int(data[index+1]) + int(data[index+2]) + int(data[index+3])

        print(prev, curr)
        if prev < curr:
            increase+=1
    print(increase)
if __name__ == '__main__':
   main()