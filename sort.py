g=[]
l=[]
def sort():
    fileName = input("Enter the path:")
    inputFile = open(fileName, 'r')

    lineList = inputFile.readlines()
    lineList.sort()
    #print('The input in alphabetical order below :')
    for line in  lineList:
        print(line)
        g.append(line)
    print ('do u want to create file')
    qq=input("enter ur choice[Y/N:")
    if(qq=="y"):
        path=input("enter path:")
        thefile = open(path, 'w')
        for item in g:
            thefile.write("%s\n" % item)

        thefile.close()
def rev():
    fileName = input("Enter the path:")
    inputFile = open(fileName, 'r')

    for line in reversed(list(inputFile)):
        print(line.rstrip())
        l.append(line)
    print(l)
    print('do u want to create file')
    qq1 = input("enter ur choice[Y/N:")
    if(qq1=="y"):
        path=input("enter path:")
        thefile1 = open(path, 'w')
        for item in l:
             thefile1.write("%s" % item)

#print(g,l)
def welcome():
    print('welcome to command line')
    print('1.Sort')
    print('2.Reverse')
    #print('3.sorttonewfile')
    #print('4.revtonewfile')
    a=int(input(("enter your choise:")))
    if(a==1):
        sort()
    elif(a==2):
        rev()
    #elif(a==3):
       # sorttofile()
    #elif(a==4):
        #revtofile()
    else:
        print('SORRY::wrong entry')
        exit(0)

welcome()
