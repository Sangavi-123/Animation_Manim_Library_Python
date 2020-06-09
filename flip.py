n=5
p=4

#dummy variables
count1=0
count2=0
i=1

#loop construct
while True:
  
  # flipping from forward
  val1=i+2
  if val1<=p:
    count1=count1+1
  else:
    break
  
  # flipping from backward
  val2=n-2
  if val2>=p:
    count2=count2+1
  else:
    break
  
#checking which is the least
if count1<count2:
  print(count1)
else:
  print(count2)