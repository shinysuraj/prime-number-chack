def Devide(user):
   for i in range(1,user+1):
      if user%i == 0:
         print(f"{user}/{i}={int(user/i)}")
      else: 
         pass
user1=int(input('\nEnter your number\n'))
if user1>1:
   for x in range(2,user1):
      if user1%2==0:
         print(f"{user1} it is no prime number")
         Devide(user1)
         break
      else:
         print(f"{user1} it is a prime number")
         Devide(user1)
         break

else:
   print(f"{user1} it is not prime number")