#num1=20
#num2=40
#print(num1+num2)
#print("--------------------------------------------------------------------------------")

#num1=input()
#num2=input()
#print(num1+num2)
#print("--------------------------------------------------------------------------------")

#num1=input("Enter first number:")
#num2=input("Enter second number:")
#print(num1+num2)
#print("--------------------------------------------------------------------------------")

#num1=int(input("Enter first number:"))
#num2=float(input("Enter second number:"))
#print(num1+num2)
#print("--------------------------------------------------------------------------------")

#r=float(input("Enter radius:"))
#pi=3.14
#area=pi*r**2
#print(area)
#print("--------------------------------------------------------------------------------")

#r=float(input("Enter radius:"))
#pi=3.14
#area=pi*r**2
#print("Area of circle is",area)
#print("--------------------------------------------------------------------------------")

#days=int(input("Enter days:"))
#year=days//365
#days=days%365
#month=days//30
#days=days%30
#week=days//7
#days=days%7
#print("year=",year)
#print("month=",month)
#print("week=",week)
#print("days=",days)
#print("--------------------------------------------------------------------------------")

#seconds=int(input("Enter seconds:"))
#hours=seconds//3600
#seconds=seconds%3600
#minutes=seconds//60
#seconds=seconds%60
#print("hours=",hours)
#print("minutes=",minutes)
#print("seconds=",seconds)
#print("--------------------------------------------------------------------------------")

#x=10
#print(x)
#x+=5
#print(x)
#x-=2
#print(x)
#x*=4
#print(x)
#x/=2
#print(x)
#x%=3
#print(x)
#x**=5
#print(x)
#x//=3
#print(x)
#print("--------------------------------------------------------------------------------")

#x=10
#y=15
#print(x==y)
#print("--------------------------------------------------------------------------------")

#x=10
#y=15
#z=x!=y
#print(z)
#print("--------------------------------------------------------------------------------")

#x=10
#y=15
#print(x<y)
#print(x>y)
#print(x<=9)
#print(y>=15)
#print("--------------------------------------------------------------------------------")

#x=10
#y=15
#z=20
#print(x<y and x<z)
#print(y>x and y>z)
#print("--------------------------------------------------------------------------------")

#x=10
#y=15
#z=20
#print(z>x and z>y and x!=y)
#print("--------------------------------------------------------------------------------")

#x=10
#y=15
#z=20
#print(x<y or x<z)
#print(y>x or y>z)
#print("--------------------------------------------------------------------------------")

#x=10
#y=15
#z=20
#print(not x==y)
#print(not z>=x)
#print("--------------------------------------------------------------------------------")

#x='Python'
#y='Hello World'
#print('z' in x)
#print('h' in y)
#print('Hell' in y)
#print("--------------------------------------------------------------------------------")

##x='Python'
#y='Hello World'
#print('z' not in x)
#print('o' not in y)
#print("--------------------------------------------------------------------------------")

#x=9
#y=9
#print(x is y)
#print(x is 9)
#print("--------------------------------------------------------------------------------")

#x=9
#y=9
#z=x
#print(z is x)
#print("--------------------------------------------------------------------------------")

#a=10
#b=20
#print(a is not b)
#print("--------------------------------------------------------------------------------")

#x=0110
#y=0011
#print(x&y)
#print(x|y)
#print(x^y)
#print(~x)
#print(~y)
#print(x<<1)
#print(x<<2)
#print(y>>1)
#print(y>>3)
#print("--------------------------------------------------------------------------------")

#num=4
#if num%2==0:
    #print(num,"is even")
#print("--------------------------------------------------------------------------------")

#num=int(input("Enter num:"))
#if num%2==0:
    #print(num,"is even")
#print("--------------------------------------------------------------------------------")

#num=7
#if num%2==0:
    #print(num,'is even')
#if num%2!=0:
    #print(num,'is odd')
#print("--------------------------------------------------------------------------------")

#num=float(input("Enter number:"))
#if num==0:
    #print(num,'is neutral')
#if num>0:
    #print(num,'is positive')
#if num<0:
    #print(num,'is negative')
#print("--------------------------------------------------------------------------------")

#ch=input("Enter character:")
#if ch in 'aeiouAEIOU':
    #print(ch,'is vowel')
#if ch not in 'aeiouAEIOU':
    #print(ch,'is not vowel')
#print("--------------------------------------------------------------------------------")

#ch=input("Enter character:")
#if ch in "0123456789":
    #print(ch,'is number')
#if ch not in "0123456789":
    #print(ch,'is not number')
#print("--------------------------------------------------------------------------------")

#num=int(input("Enter Number:"))
#if num==1:
    #print('Monday')
#if num==2:
    #print('Tuesday')
#if num==3:
    #print('Wednesday')
#if num==4:
    #print('Thursday')
#if num==5:
    #print('Friday')
#if num==6:
    #print('Saturday')
#if num==7:
    #print('Sunday')
#if num>7 or num<1:
    #print('Invalid Number')
#print("--------------------------------------------------------------------------------")

#ch=input("Enter Character:")
#if ch in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
    #print(ch,'is not a special character')
#if ch not in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
    #print(ch,'is a special character')
#print("--------------------------------------------------------------------------------")

#num=int(input('Enter Number:'))
#if num%2==0:
    #print(num,'is even')
#else:
    #print(num,'is odd')
#print("--------------------------------------------------------------------------------")

#ch=input("Enter character:")
#if ch in'aeiouAEIOU':
    #print(ch,'is vowel')
#else:
    #print(ch,'is not vowel')
#print("--------------------------------------------------------------------------------")

#ch=input("Enter character:")
#if ch in "0123456789":
    #print(ch,'is a number')
#else:
    #print(ch,'is not a number')
#print("--------------------------------------------------------------------------------")

#num=float(input("Enter Number:"))
#if num>0:
    #print(num,'is positive')
#elif num<0:
    #print(num,'is negative')
#else:
    #print(num,'is neutral')
#print("--------------------------------------------------------------------------------")

#marks=float(input("Enter Marks:"))
#if marks>=0 and marks<=30:
    #print('FAIL')
#elif marks>=31 and marks<=50:
    #print('PASS')
#elif marks>=51 and marks<=70:
    #print('Grade B')
#elif marks>=71 and marks<=80:
    #print('Grade B+')
#elif marks>=81 and marks<=90:
    #print('Grade A')
#elif marks>=91 and marks<=100:
    #print('Grade A+')
#else:
    #print('Invalid')
#print("--------------------------------------------------------------------------------")

#num1=int(input("num1:"))
#num2=int(input("num2:"))
#if num1>num2:
    #print("Greatest number is",num1)
#else:
    #print("Greatest Number is",num2)
#print("--------------------------------------------------------------------------------")

#num1=int(input("num1:"))
#num2=int(input("num2:"))
#num3=int(input("num3:"))
#if (num1>num2 and num1>num3):
    #print(num1,"is greater")
#elif (num2>num1 and num2>num3):
    #print(num2,"is greater")
#else:
    #print(num3,"is greater")

#day=int(input("Enter day:"))
#if(day==1):
    #print("Monday")
#elif(day==2):
    #print("Tuesday")
#elif(day==3):
    #print("Wednesday")
#elif(day==4):
    #print("Thursday")
#elif(day==5):
    #print("Friday")
#elif(day==6):
    #print("Saturday")
#elif(day==7):
    #print("Sunday")
#else:
    #print("Invalid")

#num=int(input("Enter num:"))
#if(num==1):
    #print("January")
#elif(num==2):
    #print("February")
#elif(num==3):
    #print("March")
#elif(num==4):
    #print("April")
#elif(num==5):
    #print("May")
#elif(num==6):
    #print("June")
#elif(num==7):
    #print("July")
#elif(num==8):
    #print("August")
#elif(num==9):
    #print("September")
#elif(num==10):
    #print("October")
#elif(num==11):
    #print("November")
#elif(num==12):
    #print("December")
#else:
    #print("Invalid")

#num=int(input("Enter num:"))
#if(num==2 or num==3):
    #print("Spring")
#elif(num==4 or num ==5 or num==6):
    #print("Summer")
#elif(num==7 or num==8):
    #print("Monsoon")
#elif(num==9 or num==10):
    #print("Autumn")
#elif(num==11 or num==12 or num==1):
    #print("Winter")
#else:
    #print("Invalid")

#P=int(input("Enter amount:"))
#T=int(input("Enter time(in yrs):"))
#R=0
#S_I=(P*R*T)/100
#if(T>=1 and T<=3):
    #R=5
#elif(T>=4 and T<=6):
    #R=7
#elif(T>=7 and T<=10):
    #R=10
#elif(T>10):
    #R=15

#S_I=(P*R*T)/100
#print("Total Interest=",S_I)
#print("Total Amount=",P+S_I)

#p=int(input("Enter Amount:"))
#t=int(input("Enter time:"))
#if p<=0 or t<=0:
    #print("Invalid Amount or Time")
#else:
    #r=0
    #if t>=1 and t<=3:
        #r=3
    #elif t>=4 and t<=6:
        #r=5
    #elif t>=7 and t<=10:
        #r=10
    #elif t>10:
        #r=15

    #interest=(p*r*t)/100
    #print("Total Interest=",interest)
    #print("Total Amount=",p+interest)

#num1=int(input("num1:"))
#num2=int(input("num2:"))
#num3=int(input("num3:"))
#if num1==num2 or num2==num3 or num1==num3:
    #print("Two or more numbers are same")
#else:
    #if num1>num2 and num1>num3:
        #print(num1,"is greatest")
    #elif num2>num3 and num2>num1:
        #print(num2,"is greatest")
    #elif num3>num1 and num3>num2:
        #print(num3,"is greatest")

#i=1
#while i<=5:
    #print("Hello World")
    #i+=1

#i=1
#while i<=5:
    #print(i)
    #i+=1

#i=1
#while i<=100:
    #print(i)
    #i+=1

#i=1
#while i<=20:
    #if i%2==0:
        #print(i)
    #i+=1

#n=int(input("n:"))
#i=1
#while i<=n:
    #print(i)
    #i+=1

#n=int(input("n:"))
#i=0
#while i<n:
    #print(i)
    #i+=1

#n=int(input("n:"))
#i=1
#sum=0
#while i<=n:
    #sum=sum+i
    #i+=1

#print("sum=",sum)

#n=int(input("n:"))
#i=1
#p=1
#while i<=n:
    #p=p*i
    #i+=1

#print("Product=",p)

#n=int(input("n:"))
#i=1
#sum_odd=0
#sum_even=0
#while i<=n:
    #if i%2==0:
        #sum_even+=i
    #else:
        #sum_odd+=i
    #i+=1
#print("Sum of even numbers=",sum_even)
#print("Sum of odd numbers=",sum_odd)

#num=int(input("num:"))
#i=1
#while i<=num:
    #if num%i==0:
        #print(i)
    #i+=1

#num=int(input("num:"))
#i=1
#count=0
#while i<=num:
    #if num%i==0:
        #count+=1
    #i+=1
#print("Total Count=",count)

#num=int(input("num:"))
#i=1
#count=0
#while i<=num:
    #if num%i==0:
        #count+=1
    #i+=1

#if count==2:
    #print(num,"is Prime")
#else:
    #print(num,"is not Prime")

#num=int(input("num:"))
#if num > 0:
    #i = 1
    #count = 0
    #while i <= num:
        #if num%i == 0:
            #count+=1
        #i+=1
    #if count == 2:
        #print(num,"is prime")
    #else:
        #print(num,"is not prime")
#else:
    #print("Invalid Number")
    
#num=int(input("num:"))
#i=1
#f=1
#while i <= num:
    #f *= i
    #i += 1
#print("Factorial=",f)

#sum = 0
#count = 0
#while count != 10:
    #num = int(input("num:"))
    #sum += num
    #count += 1
#avg = sum/count
#print("Average=",avg)

#sum=0
#i=1
#while i<=10:
    #num=int(input("num:"))
    #sum+=num
    #i+=1
#avg=sum/i
#print("Average=",avg)

#sum = 0
#while sum <= 200:
    #num=int(input("num:"))
    #if num>=1

#sum=0
#while sum<=200:
    #num=int(input("n:"))
    #if num>=1 and num<=25:
        #sum=sum+num
#print("sum",sum)

#range=int(input("r:"))
#n1=0
#n2=1
#print(n1)
#print(n2)
#count=2
#while count!=range:
    #n3=n1+n2
    #print(n3)
    #count+=1
    #n1=n2
    #n2=n3

#range=int(input("r:"))
#n1=0
#n2=1
#print(n1)
#print(n2)
#i=1
#while i<=range-2:
    #n3=n1+n2
    #print(n3)
    #i+=1
    #n1=n2
    #n2=n3

#num=int(input("n:"))
#while num != 0:
    #digit=num%10
    #print(digit)
    #num //= 10

#print(3,end=",")
#print(4,end=",")
#print(6,end=",")
#print(9,end="")

#print("Hello \nWorld")

#num=int(input("n:"))
#rev_num=0
#while num!=0:
    #digit=num%10
    #rev_num=rev_num*10 + digit
    #num//=10
#print(rev_num)

#num=int(input("n:"))
#rev_num=0
#num1=num
#while num!=0:
    #digit=num%10
    #rev_num=rev_num*10 + digit
    #num//=10
#if rev_num==num1:
    #print(num1,"is Palindrome")
#else:
    #print(num1,"is not palindrome")

#i=1
#while i<=10:
    #print(i)
    #if i==3:
        #break
    #i+=1

#i=0
#while True:
    #print(i)
    #i+=1

#i=0
#while True:
    #print(i)
    #if i==1000:
        #break
    #i+=1

#num1=int(input("n1:"))
#num2=int(input("n2:"))
#if num1>num2:
    #g=num1
#else:
    #g=num2
#while True:
    #if g%num1==0 and g%num2==0:
        #lcm=g
        #break
    #g+=1
#print("LCM =",lcm)

#for i in range(1,6):
    #print("Hello World")

#i=1
#while i<=5:
    #print("Hello World")
    #i+=1

#for i in range(1,11):
    #print(i)

#for i in range(1,21):
    #if i%2==0:
        #print(i)

#for i in range(1,21):
    #if i%2!=0:
        #print(i)

#sum=0
#for i in range(1,21):
    #if i%2==0:
        #sum=sum+i
#print("sum =",sum)

#n=int(input("n:"))
#for i in range(1,n+1):
    #print(i)

#n=int(input("n:"))
#for i in range(0,n):
    #print(i)

#num=int(input("n:"))
#f=1
#for i in range(1,num+1):
    #f*=i
#print("Factorial =",f)

#num=int(input("n:"))
#for i in range(1,num+1):
    #if num%i==0:
        #print(i)
#for i in range(10,-1,-1):
    #print(i)

#for i in range(-1,-11,-1):
    #print(i)

#count=0
#num=int(input("n:"))
#for i in range(1,num+1):
    #if num%i==0:
        #count+=1
#print("Total Factors =",count)

#count=0
#num=int(input("n:"))
#for i in range(1,num+1):
    #if num%i==0:
        #count+=1
#if count==2:
    #print(num,"is a prime number")
#else:
    #print(num,"is not a prime number")

#num1=int(input("n1:"))
#num2=int(input("n2:"))
#if num1<num2:
   # s=num1
#else:
    #s=num2
#for i in range(1,s+1):
    #if num1%i==0 and num2%i==0:
        #hcf=i
#print("HCF/GCD =",hcf)

#for i in range(1,6):
    #print('*')
    
#for i in range(1,3):
    #for j in range(1,3):
        #print("*")

#for i in range(1,3):
    #for j in range(1,3):
        #print('*',end='')

#for i in range(1,3):
    #for j in range(1,3):
        #print('*',end='')
    #print()

#for i in range(1,6):
    #for j in range(1,6):
        #print('*',end='')
    #print()

#for i in range(1,6):
    #for j in range(1,6):
        #print(j,end='')
    #print()

#for i in range(1,5):
    #for j in range(1,5):
        #print(i,end='')
    #print()

#n=1
#for i in range(1,5):
    #for j in range(1,5):
        #print(n,end='')
    #print()
    #n+=1

#for i in range(1,5):
    #for j in range(1,5):
        #if i%2==0:
            #print('#',end='')
        #else:
            #print('*',end='')
    #print()

#for i in range(1,5):
    #for j in range(1,5):
        #if j%2==0:
            #print('#',end='')
        #else:
            #print('*',end='')
    #print()

#for i in range(1,5):
   #for j in range(0,i):
        #print('*',end='')
    #print()

#for i in range(1,5):
    #for j in range(i):
        #print('*',end='')
    #print()

#for i in range(1,5):
    #for j in range(1,i+1):
        #print('*',end='')
    #print()

#i=1
#while i<5:
    #j=0
    #while j<i:
        #print('*',end='')
        #j+=1
    #print()
    #i+=1

#for i in range(1,5):
    #for j in range(1,i+1):
        #print(j,end='')
    #print()

#for i in range(1,5):
    #for j in range(1,i+1):
        #if i%2==0:
            #print('#',end='')
        #else:
            #print('*',end='')
    #print()

#for i in range(1,5):
    #for j in range(1,i+1):
        #print(i,end='')
    #print()

#n=1
#for i in range(1,5):
    #for j in range(1,i+1):
        #print(n,end='')
        #n+=1
    #print()

#for i in range(1,5):
    #for j in range(0,5-i):
        #print('*',end='')
    #print()

#for i in range(4,0,-1):
    #for j in range(0,i):
        #print('*',end='')
    #print()

#for i in range(1,5):
    #for space in range(0,4-i):
        #print(' ',end='')
    #for star in range(0,i):
        #print('*',end='')
    #print()

#for i in range(1,5):
    #for space in range(0,i-1):
        #print(' ',end='')
    #for star in range(0,5-i):
        #print('*',end='')
    #print()

#for i in range(4,0,-1):
    #for space in range(0,4-i):
        #print(' ',end='')
    #for star in range(0,i):
        #print('*',end='')
    #print()

#for i in range(1,5):
    #for space in range(0,4-i):
        #print(' ',end='')
    #for star in range(0,2*i-1):
        #print('*',end='')
    #print()

#for i in range(1,5):
    #for lstar in range(0,i):
        #print('*',end='')
    #for space in range(0,8-2*i):
        #print(' ',end='')
    #for rstar in range(0,i):
        #print('*',end='')
    #print()

#for i in range(1,5):
    #for space in range(0,i-1):
        #print(' ',end='')
    #for star in range(0,9-2*i):
        #print('*',end='')
    #print()

#for i in range(4,0,-1):
    #for space in range(0,4-i):
        #print(' ',end='')
    #for star in range(0,2*i-1):
        #print('*',end='')
    #print()

#for i in range(1,5):
    #for space in range(0,4-i):
        #print(' ',end='')
    #for star in range(0,2*i-1):
        #print('*',end='')
    #print()
#for i in range(4,0,-1):
    #for space in range(0,4-i):
        #print(' ',end='')
    #for star in range(0,2*i-1):
        #print('*',end='')
    #print()

#s=input("s:")
#if s==s[::-1]:
    #print(s,"is a palindrome")
#else:
    #print(s,"is not a palindrome")

#s=input("s:")
#print(len(s))
#for index in range(0,len(s)):
    #print(s[index])

#s=input("s:")
#for index in range(0,len(s)):
    #print(s[index])

#s='My age is 18'
#count=0
#for char in range(0,len(s)):
    #if s[char] in "0123456789":
        #count+=1
#print("Total Digits =",count)

#s="My age is 18"
#count=0
#for char in range(0,len(s)):
    #if s[char] in " ":
        #count+=1
#print("Total Spaces =",count)

#s="My age is 18"
#count=0
#for char in range(0,len(s)):
    #if s[char]==" " and s[char+1]!=" ":
        #count+=1
#print("Total Words =",count+1)

#s="Hello! My name is Jasleen"
#count=0
#for char in range(0,len(s)):
    #if s[char] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
        #count+=1
#print("Total Special Characters =",count)        

#s="jasleen@gmail.com"
#if len(s)>3:
    #if '@' in s and '.' in s:
        #print("Valid")
    #else:
        #print("Invalid")
#else:
    #print("Invalid")

#s="Hello World"
#s1=s.lower()
#print(s1)

#s="Hello World"
#s2=s.upper()
#print(s2)

#s="Hello World"
#print(s.swapcase())

#s="Hello World"
#print(s.capitalize())

#s="hello world"
#print(s.title())

#s="Hello World"
#print(s.replace("World","Python"))
#print(s.replace("World",","))
#print(s.replace("World",""))

#s="Hello World"
#print(s.count("l"))

#s="Hello World"
#print(s.index("r"))
#print(s.index("l"))

#s="Hello World"
#print(s.find("r"))
#print(s.find("z"))

#s="    Python    "
#print(s.strip())
#print(s.lstrip())
#print(s.rstrip())

#s="Python"
#print(s.islower())
#print(s.isupper())
#print(s.istitle())
#print(s.isalpha())

#s1="abc-1999"
#print(s1.isdigit())
#print(s1.isalnum())

#s1="Hello"
#s2="World"
#s=s1+s2
#print(s)

#s1="Hello"
#s2="World"
#s=s1+" "+s2
#print(s)

#s="Python"
#print(s*5)

#star="*"
#for i in range(1,5):
    #print(star*i)

#star="*"
#for i in range(4,0,-1):
    #print(star*i)

#star="*"
#for i in range(1,5):
    #spacecount=4-i
    #print(" "*spacecount,end="")
    #print(star*i)

#star="*"
#for i in range(4,0,-1):
    #spacecount=4-i
    #print(" "*spacecount,end="")
    #print(star*i)

#for i in range(1,5):
    #spacecount=4-i
    #starcount=2*i-1
    #print(" "*spacecount,end="")
    #print("*"*starcount)

#for i in range(1,5):
    #spacecount=4-i
    #starcount=2*i-1
    #print(" "*spacecount,end="")
    #print("*"*starcount)
#for i in range(3,0,-1):
    #spacecount=4-i
    #starcount=2*i-1
    #print(" "*spacecount,end="")
    #print("*"*starcount)

#for i in range(1,5):
    #starcount=i
    #spacecount=8-2*i
    #print("*"*starcount,end="")
    #print(" "*spacecount,end="")
    #print("*"*starcount)

#list=[10,20,30,40,50,20]
#print(list[2])

#l1=[10,20,30,40,50,20]
#l1[-1]=60
#print(l1)

#l1=[10,20,30,40,50,20]
#l1[-1]+=40
#print(l1)

#l1=[10,20,30,40,50,60]
#print(l1[1:5])
#print(l1[:2])
#print(l1[::2])
#print(l1[::-1])
#print(l1[::-3])

#l1=[10,20,30,40,50,60]
#for i in range(0,len(l1)):
    #print(l1[i])

#student=[1,"Mehak","MBA",95]
#student.append("LSE")
#student.insert(2,"Jasleen")
#student[1]+=" Kaur "
#student[4]=97
#print(student)

#student=[1,"Mehak","MBA",97,"LSE"]
#student.remove("LSE")
#student.pop()
#print(student)

#l=[10,20,30,40,50]
#for i in range(0,len(l)):
    #print(l[i])

#l=[]
#for i in range(10):
    #num=int(input("n:"))
    #l.append(num)
#print(l)

#l=[]
#while len(l)!=10:
    #num=int(input("n:"))
    #if num not in l:
        #l.append(num)
#print(l)

#l=[]
#while len(l)!=10:
    #num=int(input("n:"))
    #if num not in l:
        #l.append(num)
#avg=sum(l)/len(l)
#print("Average =",avg)

#l=[]
#sum_l=0
#while len(l)!=10:
    #num=int(input("n:"))
    #if num not in l:
        #l.append(num)
#for i in range(0,len(l)):
    #sum_l+=l[i]
#avg=sum_l/len(l)
#print("Average =",avg)

#l=[]
#while len(l)!=10:
    #num=int(input("n:"))
    #if num not in l and num<25:
        #l.append(num)
#print(l)

#l=[]
#while len(l)!=10:
    #num=int(input("n:"))
    #if num<25:
        #l.append(num)
#print(l)

#l=[1,5,3,7,6,4,2,8,10,9]
#l.sort()
#print(l)

#l=[1,5,3,7,6,4,2,8,10,9]
#l.sort(reverse=True)
#print(l)

#fruits=["Apple","mango","Grapes","guava","Banana"]
#fruits.sort()
#print(fruits)

#fruits=["Apple","mango","Grapes","guava","Banana"]
#fruits.sort(reverse=True)
#print(fruits)

#l=[]
#sum_l=0
#for i in range(10):
    #num=int(input("n:"))
    #if num not in l:
        #l.append(num)
#print(l)
#avg=sum(l)/len(l)
#print("Average =",avg)
#for i in range(0,len(l)):
    #sum_l+=l[i]
#print("Sum =",sum_l)
#l.sort()
#print(l)
#print("Smallest Number =",l[0])
#print("Largest Number =",l[-1])

#l=[]
#for i in range(10):
    #num=int(input("n:"))
    #if num not in l:
        #l.append(num)
#print(l)
#print("Average =",sum(l)/len(l))
#print("Sum =",sum(l))
#print("Smallest Number =",min(l))
#print("Largest Number =",max(l))

#l1=[31,65,1,13,26]
#l2=[23,30,7,9,26]
#print(l1+l2)

#num=[10,20,30,40,50,20]
#print(num.count(20))

#num=[10,20,30,40,50,20]
#print(num.index(20))

#x=[1,2,3,4,5]
#result=[]
#for i in range(0,len(x)):
    #result.append(x[i]**2)
#print(result)

#x=[1,2,3,4,5]
#result=[x[i]**2 for i in range(0,len(x))]
#print(result)

#x=[10,20,30,50,15,25,20]
#result=[]
#for i in range(0,len(x)):
    #if x[i]<25:
        #result.append(x[i])
#print(result)

#x=[10,20,30,50,15,25,20]
#result=[x[i] for i in range(0,len(x)) if x[i]<25]
#print(result)

#x=[1,2,3,4,5]
#result=[]
#for i in range(0,len(x)):
    #if x[i]%2!=0:
        #result.append('odd')
    #else:
        #result.append('even')
#print(result)

#x=[1,2,3,4,5]
#result=["even" if x[i]%2==0 else "odd" for i in range(0,len(x))]
#print(result)

#t=[10,20,30,40,50]
#print(t[2])
#print(t[-4])
#print(t[1:4])
#print(t[::-1])

#t=(10,20,30,40,50)
#print(t)
#l=list(t)
#l.append(60)
#l.insert(0,0)
#t=tuple(l)
#print(t)

#t=(10,20,30,40,50)
#print(t)
#l=list(t)
#l.remove(30)
#l.pop()
#t=tuple(l)
#print(t)

#d={'roll':1,'name':'Jasleen','class':12,'marks':98}
#print(d['name'])

#d={'roll':1,'name':'Jasleen','class':12,'marks':98}
#d['name']+='Kaur'
#d['class']='BTech'
#print(d)

#d={'roll':1,'name':'Jasleen','class':12,'marks':98}
#d['course']='BTech'
#print(d)

#student={}
#student['name']=input("Enter Name:")
#student['roll']=input("Enter roll number:")
#student['course']=input("Enter course:")
#student['marks']=float(input("Enter marks:"))
#student['father_name']=input("Enter father name:")
#print(student)

#student={}
#name=input("Enter name:")
#roll=int(input("Enter roll number:"))
#course=input("Enter course:")
#marks=float(input("Enter marks:"))
#father_name=input("Enter father name:")
#student['name']=name
#student['roll']=roll
#student['course']=course
#student['marks']=marks
#student['father_name']=father_name
#print(student)

#cars={'Brand':'Ford','Model':'Mustang'}
#cars['year']=2024
#cars['Model']='Icon'
#print(cars)

#cars={'Brand':'Ford','Model':'Mustang'}
#cars.update({'Model':'Icon','type':'Petrol'})
#print(cars)

#cars={'Brand':'Ford','Model':'Mustang','year':2024}
#cars.pop('year')
#print(cars)
#cars.popitem()
#print(cars)
#cars.clear()
#print(cars)

#student={'name':'Asees','roll':10}
#course=input("Enter class:")
#father_name=input("Enter father name:")
#marks=float(input("Enter marks:"))
#student['class']=course
#student['father_name']=father_name
#student['marks']=marks
#print(student)
#student['name']='Aseespreet'
#print(student)
#student.pop('roll')
#serial_number=int(input("Enter serial number:"))
#student['serial_number']=serial_number
#print(student)

#l=[10,20,30,40,50]
#s='Hello'
#for i in range(len(s)):
    #print(s[i])
#for i in range(len(l)):
    #print(l[i])

#l=[10,20,30,40,50]
#s='Hello'
#for element in l:
    #print(element)
#for char in s:
    #print(char)

#students=[
    #{'roll':1,'name':'Aryan','class':'MCA'},
    #{'roll':2,'name':'Harman','class':'12th'},
    #{'roll':3,'name':'Asees','class':'11th'}
    #]
#d={}
#d['roll']=int(input("Enter roll number:"))
#d['name']=input("Enter name:")
#d['class']=input("Enter class:")
#students.append(d)
#for i in students:
    #print(i)
   
#students=[
    #{'roll':1,'name':'Aryan','class':'MCA'},
    #{'roll':2,'name':'Harman','class':'12th'},
    #{'roll':3,'name':'Asees','class':'11th'}
    #]
#roll=int(input("Enter roll number:"))
#for i in students:
    #if i['roll']==roll:
        #print("Found")
        #break
#else:
    #print("Not Found")

#for i in students:
    #print(i)

#students=[
    #{'roll':1,'name':'Aryan','class':'MCA'},
    #{'roll':2,'name':'Harman','class':'12th'},
    #{'roll':3,'name':'Asees','class':'11th'}
    #]
#roll=int(input("Enter roll:"))
#for i in students:
    #if i['roll']==roll:
        #i['roll']=int(input("Enter roll number:"))
        #i['name']=input("Enter name:")
        #i['class']=input("Enter class:")
        #print("Student has been updated")
        #break
#else:
    #print("Not Found")
#for i in students:
    #print(i)

#students=[
    #{'roll':1,'name':'Aryan','class':'MCA'},
    #{'roll':2,'name':'Harman','class':'12th'},
    #{'roll':3,'name':'Asees','class':'11th'}
    #]
#roll=int(input("Enter roll:"))
#for i in students:
    #if i['roll']==roll:
        #students.remove(i)
        #print("Student has been deleted")
        #break
#else:
    #print("Not Found")
#for i in students:
    #print(i)

#students = [
    #{'roll':1, 'name':'Aryan','class':'MCA'},
    #{'roll':2, 'name':'Harman','class':'12th'},
    #{'roll':3, 'name':'Asees','class':'11th'},
    #]

#while True:
    #print("Press 1 to Add new Student ")
    #print("Press 2 to Update an existing Student ")
    #print("Press 3 to Delete an existing Student ")
    #print("Press 4 to Search a Student")
    #print("Press 5 to View All Students")
    #print("Press 0 to exit \n")
    #choice = input("Enter Choice")

    #if choice == '1':
        #d = {}
        #d['roll'] = int(input("Enter Roll Number "))
        #d['name'] = input("Enter Name ")
        #d['class'] = input("Enter Class ")
        #students.append(d)
        #print("Student has been Added \n")
        
    #elif choice == '2':
        #roll = int(input("Enter Roll "))
        #for i in students:
            #if i['roll'] == roll:
                #i['roll'] = int(input("Enter Roll Number "))
                #i['name'] = input("Enter Name ")
                #i['class'] = input("Enter Class ")
                #print("Student has been Updated \n")
                #break
        #else:
            #print("Not Found \n")

    #elif choice == '3':
        #roll = int(input("Enter Roll "))
        #for i in students:
            #if i['roll'] == roll:
                #students.remove(i)
                #print("Student has been Deleted \n")
                #break
        #else:
            #print("Not Found \n")

    #elif choice == '4':
        #roll = int(input("Enter Roll "))
        #for i in students:
            #if i['roll'] == roll:
                #print(i)
                #break
        #else:
            #print("Not Found \n")
   
    #elif choice == '5':
        #for i in students:
            #print(i)
        #print()
   
    #elif choice == '0':
        #print("Thanku for using our app.")
        #break
   
    #else:
        #print("Please Enter valid option\n")

#student=[[1,'Harman','BCA',98],
         #[2,'Asees','12th',98],
         #[3,'Ravneet','12th',95]]
#print(student[0])
#print(student[0][0])
#print(student[1][2])
#print(student[2][3])

#student=[[1,'Harman','BCA',98],
         #[2,'Asees','12th',98],
         #[3,'Ravneet','12th',95]]
#for i in student:
    #print(i)

#student=[[1,'Harman','BCA',98],
         #[2,'Asees','12th',98],
         #[3,'Ravneet','12th',95]]
#for i in student:
    #print(i[1])

#students=[
    #[1,'Harman','BCA',98],
    #[2,'Asees','11th',98],
    #[3,'Ravneet','12th',87]
    #]
#while True:
    #print("Press 1 to add new student")
    #print("Press 2 to update an existing student")
    #print("Press 3 to delete an existing student")
    #print("Press 4 to search a student")
    #print("Press 5 to view all students")
    #print("Press 0 to exit \n")
    #choice=input("Enter choice:")

    #if choice=='1':
        #roll=int(input("Enter roll number:"))
        #name=input("Enter name:")
        #course=input("Enter class:")
        #marks=input("Enter marks:")
        #students.append([roll,name,course,marks])
        #print("Student has been added \n")
        
    #elif choice=='2':
        #roll=int(input("Enter roll number:"))
        #for i in students:
            #if i[0]==roll:
                #i[1]=input("Enter name:")
                #i[2]=input("Enter class:")
                #i[3]=input("Enter marks:")
                #print("Student has been updated \n")
                #break
        #else:
            #print("Student does not exist \n")

    #elif choice=='3':
        #roll=int(input("Enter roll number:"))
        #for i in students:
            #if i[0]==roll:
                #students.remove(i)
                #print("Student has been removed \n")
                #break
        #else:
            #print("Student does not exist \n")

    #elif choice=='4':
        #roll=int(input("Enter roll number:"))
        #for i in students:
            #if i[0]==roll:
                #print(i)
                #print()
                #break
        #else:
            #print("Student does not exist \n")

    #elif choice=='5':
        #for i in students:
            #print(i)
        #print()

    #elif choice=='0':
        #print("Thank You for using our app")
        #break

    #else:
        #print("Please select valid option \n")
        
#def display():
    #print("Hello Python")

#display()
#display()
#display()
#display()

#def addition():
    #n1=int(input("n1:"))
    #n2=int(input("n2:"))
    #print("Sum =",n1+n2)

#addition()

#def factorial():
    #n=int(input("n:"))
    #f=1
    #for i in range(1,n+1):
        #f*=i
    #print("Factorial =",f)

#factorial()

#def prime():
    #n=int(input("n:"))
    #count=0
    #for i in range(1,n+1):
        #if n%i==0:
            #count+=1
    #if count==2:
        #print("Prime")
    #else:
        #print("Not Prime")

#prime()

#def addition(n1,n2):
    #print("Sum =",n1+n2)

#addition(31,65)

#def prime(num):
    #count=0
    #for i in range(1,num+1):
        #if num%i==0:
            #count+=1
    #if count==2:
        #print(num,"is prime")
    #else:
        #print(num,"is not prime")

#prime(10)

#def addition(n1,n2):
    #print(n1+n2)

#addition(n2=65,n1=31)

#def addition(n1=0,n2=0):
    #print(n1+n2)

#addition()

#def addition(n1=0,n2=0):
    #result=n1+n2
    #return result

#answer=addition(31,65)
#print(answer)

#def factorial(num):
    #f=1
    #for i in range(1,num+1):
        #f*=i
    #return f

#result=factorial(7)
#print(result)

#def factors(num):
    #f=[]
    #for i in range(1,num+1):
        #if num%i==0:
            #f.append(i)
    #return f

#list=factors(3)
#print(list)

#def get_factors(num):
    #factors=[]
    #for i in range(1,num+1):
        #if num%i==0:
            #factors.append(i)
    #return factors

#for i in range(2,21):
    #list=get_factors(i)
    #if len(list)==2:
        #print(i,"is prime")
    #else:
        #print(i,"is not prime",list)

#def increment(n1,n2):
    #n1+=10
    #n2+=10
    #return n1,n2

#result=increment(31,65)
#print(result)

#def increment(n1,n2):
    #n1+=10
    #n2+=10
    #return n1,n2

#r1,r2=increment(31,65)
#print(r1)
#print(r2)

#def addition(*n):
    #return sum(n)

#result=addition(31,65,1,13,30,26,7,9,23,74,28,8,3,48)
#print(result)

#def addition(*n):
    #s=0
    #for i in n:
        #s+=i
    #return s

#result=addition(31,65,1,13,30,26,7,9,23)
#print(result)

#def demo(**d):
    #print(d)

#demo(n1=31,n2=65,n3=1,n4=13)

#def vowel_remove(s):
    #new_s=''
    #for i in s:
        #if i not in 'aeiouAEIOU':
            #new_s+=i
    #return new_s

#result=vowel_remove('hello')
#print(result)

#def vowels(s):
    #count=0
    #for i in s:
        #if i in 'aeiouAEIOU':
            #count+=1
    #return count

#result=vowels("Hello World")
#print(result)

#import math

#num=int(input("n:"))
#result=math.sqrt(num)
#print(result)

#import math

#num=int(input("n:"))
#print("Factorial =",math.factorial(num))

#import math

#num=float(input("n:"))
#print(math.ceil(num))
#print(math.floor(num))

#import random

#num=random.randrange(1,21)
#num1=random.randint(1,21)
#print(num)
#print(num1)

#import datetime

#date=datetime.date.today()
#print(date)

#import datetime

#time=datetime.datetime.now()
#print(time)

'''import datetime

dtime=datetime.datetime.now()
print(dtime.time())'''

'''ans=0
def addition(n1,n2):
    global ans
    ans=n1+n2
addition(31,65)
print(ans)'''

'''class Car:
    speed=0

    def display(self):
        print("Current Speed=",self.speed)

    def accelerate(self):
        self.speed+=10

    def brake(self):
        self.speed-=10

obj=Car()
obj.accelerate()
obj.accelerate()
obj.display()
obj.brake()
obj.display()'''

'''class Bank:
    balance=0

    def display(self):
        print("Current Balance=",self.balance)

    def deposit(self):
        amount=int(input("Enter amount to be deposited="))
        self.balance+=amount

    def withdraw(self):
        amount=int(input("Enter amount to be withdrawn="))
        self.balance-=amount

bank=Bank()
bank.display()
bank.deposit()
bank.display()
bank.withdraw()
bank.display()'''

'''class Bank:
    def __init__(self):
        print("Thank You for opening an account")
        self.balance=int(input("Please enter initial balance="))
        self.display()

    def display(self):
        print("Current Balance=",self.balance)

    def deposit(self):
        amount=int(input("Enter amount="))
        self.balance+=amount
        self.display()

    def withdraw(self):
        amount=int(input("Enter amount="))
        self.balance-=amount
        self.display()

obj=Bank()
obj.deposit()
obj.withdraw()'''


'''class Bank:
    def __init__(self,balance):
        print("Thank You for opening an account")
        self.balance=balance
        self.display()

    def display(self):
        print("Current balance=",self.balance)

    def deposit(self):
        amount=int(input("Enter amount="))
        self.balance+=amount
        self.display()

    def withdraw(self):
        amount=int(input("Enter amount="))
        self.balance-=amount
        self.display()

obj=Bank(5000)
obj.deposit()
obj.withdraw()'''

'''class Bank:
    def __init__(self,balance):
        print("Thank You for opening an account")
        self.__balance=balance
        self.display()

    def display(self):
        print("Current Balance=",self.__balance)

    def deposit(self):
        amount=int(input("Enter amount="))
        self.__balance+=amount
        self.display()

    def withdraw(self):
        amount=int(input("Enter amount="))
        self.__balance-=amount
        self.display()

obj=Bank(4000)
obj.deposit()
obj.__balance=28462895
obj.withdraw()'''

'''age=19
s=f"My age is {age}"
print(s)'''
        
'''class StudentsManagementSystem:
    def __init__(self):
        self.students = [
            {'roll':'1', 'name':'Latika','course':'Python'},
            {'roll':'2','name':'Jasleen','course':'Python'}
            ]

        while True:
            print("Press 1 to add a new student")
            print("Press 2 to update existing student")
            print("Press 3 to delete existing student")
            print("Press 4 to search a new student")
            print("Press 5 to view all students")
            print("Press 0 to Exit")
            choice=input("Enter choice:")

            if choice=='1':
                self.addStudent()
            elif choice=='2':
                self.updateStudent()
            elif choice=='3':
                self.deleteStudent()
            elif choice=='4':
                self.searchStudent()
            elif choice=='5':
                self.viewAllStudents()
            elif choice=='6':
                print("\n Thank You")
                break
            else:
                print("\n Please enter correct option \n")

    def addStudent(self):
        d={}
        print()
        d['roll']=input("Enter roll:")
        d['name']=input("Enter name:")
        d['course']=input("Enter course:")
        self.students.append(d)
        print("Student has been added \n")

    def viewAllStudents(self):
        print()
        for i in self.students:
            print(f"{i['roll']}---{i['name']}---{i['course']}")
        print()

    def updateStudent(self):
        print()
        roll=input("Enter roll:")
        for i in self.students:
            if i['roll']==roll:
                name=input(f"Enter Name (Press Enter for {i['name']}):")
                if name!='':
                    i['name']=name
                course=input("Enter course:")
                if course!='':
                    i['course']=course
                print("Student has been updated \n")
                break
            else:
                print("Roll Number does not exist \n")

    def deleteStudent(self):
        roll=input("Enter roll no:")
        for i in self.students:
            if i['roll']==roll:
                self.students.remove(i)
                print("\n Student has been removed \n")
                break
        else:
            print("\n Student does not exists \n")

    def searchStudent(self):
        roll=input("Enter roll:")
        print()
        for i in self.students:
            if i['roll']==roll:
                print(f"{i['roll']}---{i['name']}---{i['course']}")
                break
        else:
            print("Student does not exists")
        print()

obj=StudentsManagementSystem()'''

'''class A:
    def display(self):
        print("This is class A")

class B(A):
    def __init__(self):
        print("Welcome")

obj_A=A()
obj_A.display()'''

'''class A:
    def display(self):
        print("This is class A")

class B(A):
    def __init__(self):
        print("Welcome")

obj_A=A()
obj_A.display()

obj_B=B()'''

'''class A:
    def display(self):
        print("This is class A")

class B(A):
    def __init__(self):
        print("Welcome")

obj_A=A()
obj_A.display()

obj_B=B()
obj_B.display()'''

'''class A:
    def display(self):
        print("This is class A")

class B(A):
    def __init__(self):
        print("Welcome")

    def display(self):
        print("This is class B")

obj_A=A()
obj_A.display()

obj_B=B()
obj_B.display()'''

class A:
    def display(self):
        print("This is class A")

class B(A):
    def __init__(self):
        print("Welcome")

    def display(self):
        super().display()
        print("This is class B")

obj_A=A()
obj_A.display()

obj_B=B()
obj_B.display()


        
                
                

    
