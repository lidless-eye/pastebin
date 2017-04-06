with open("hostlist.txt","r") as hostlist:
    for line in hostlist:
        mylist = line.split(",")
	mylist = [x.strip() for x in mylist]
        port = mylist[2]
        print(port)
