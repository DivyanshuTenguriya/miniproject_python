#Write a program in which which first take username,age. If age is greater than or equal to 18 then then print username and print message that you are eligible for vote then give four options for choose a single vote option according to user input.
name=input('Enter your name:-')
print('Welcome',name)
age=int(input('Enter your age-'))
if(age>=18):
    print('You are eligible to vote')
    print('1-BJP')
    print('2-AAP')
    print('3-Congress')
    print('4-SPA')
    c=int(input('Choose your party no. for vote:-'))
    if(c==1):
        print('BJP')
    elif(c==2):
        print('AAp')
    elif(c==3):
        print('Congress')
    elif(c==4):
        print('SPA')
    else:
        print('you are entering a invalid value')
else:
    print('You are not eligible to vote')