with open('demo.txt', mode='r') as f:
    # f.write('Hello World\n')
    # file_content = f.readlines()

    # f.close()

    # for line in file_content: 
    #     print(line[:-1])
    line = f.readline()

    while line: 
        print(line)
        line = f.readline()
print('Done')