hm = int(input());
long = str();
for x in range(0, hm+1):
    if(x <10):
        file = open("VirusShare_0000"+str(x)+".txt","r");
        long += file.read();
        file.close();
        print ("VirusShare_0000"+str(x)+".txt")
    elif(x <100):
        file = open("VirusShare_000"+str(x)+".txt","r");
        long += file.read();
        file.close();
        print ("VirusShare_000"+str(x)+".txt")
    elif(x <1000):
        file = open("VirusShare_00"+str(x)+".txt","r");
        long += file.read();
        file.close();
        print ("VirusShare_00"+str(x)+".txt")
    
    


file = open("md5.data","w");
file.write(long);
file.close();
