#sorry just for lower case
x=input("please enter your word:")
a="abcdefghijklmnopqrstuvwxyzabc"
def Caesarcipher(x):
  b=""
  for i in x:
    for j in range(0,len(a)-3):
      if i==a[j]:
        c=a[j+3]
        b=b+c
      else:
        j=j+1
  return(b)
def DCaesarcipher(x):
  b=""
  for i in x:
    for j in range(1,len(a)-3):
      if i==a[-j]:
        c=a[-j-3]
        b=b+c
      else:
        j=j+1
  return(b)
y=int(input("please enter your method,enter 1 forCaesar cipher & enter 2 for Pig Pen:"))
z=int(input("Enter you operation,enter 1 for encrypt or  2 for decrypt:"))
if (y==1) and (z==1):
  print(Caesarcipher(x))
elif (y==1) and (z==2):
  print(DCaesarcipher(x))
else:
  print("PigPen")