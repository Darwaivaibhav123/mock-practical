name = input ('enter a  name = ')
# longest length  of  string
def longest ():
    global long 
    long = 0
    for i in name.split():
        if (len(i)>long):
            long=len(i)
longest ()
print (f"longest word has {long} length ")
# frequncy of occuring of peritcular letter
charter = input ("enter a character = ")
def chare ():
    global chr1
    chr1 = 1
    for i in name :
        if (i==charter ):
            chr1 = chr1 +1
chare()  
print (f"the leterris comming {chr1} time")
# string is palindrome or not

newstring = ""
for i in name :
    newstring = i+newstring 
print (" reversed sitring ", newstring )
if  name ==name[::-1] :
    print ('given string is palindrome')
else :
    print ('given string is not palindrome')

# substring or not
r = input ("enter a new string = ")
def substr():
    if r in name :
        print ("substring is present ")
    else :
        print ("substring is not present ") 
substr ()
