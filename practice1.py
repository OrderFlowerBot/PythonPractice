print("Jesus saves you")
print ("I will not leave you comfortless",7)
x=1+1
y=2-1
z=3*4
a=4/4
print(x);
print(y);
print(z,a);

#While function
con=1
while con<10:
    print("Daddy")
    con+=1;

#for

list=[1,2,3,4,5,6,7,8,9,0]
for x in list:
    print(x)


for x in range(list[0],list[5]):
    print(x)

#if
g=50
h=60
i=70
if(g>h):
    print("winner is g")
elif(g>i):
    print("winner is g")
else:
    print("winner is h and i")

#function
def EXAMPLE():
    print("WELCOME")
    A=1+1
    print(A)

EXAMPLE()


#global
a=9
def daddy():
    global a
    print("Started now")
    print(a);
    print(a+10);
    a+=1;
    print(a)

daddy()



#global
b=9
def daddy():
    globx=b;
    print("Started now")
    print(b);
    print(globx+10);
    globx+=1;
    print(globx)
    return globx

b=daddy()
print("Funtion Output",b);


#File Writing
text="Jesus Guides you"
saveFile=open("example.txt",'w');
saveFile.write(text);
saveFile.close();

#File Append
text="JEsus Loves You"
appendFile=open("example.txt",'a');
appendFile.write(text);
appendFile.close();

