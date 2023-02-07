str =  ("kitten")
i = int(input("Enter the index of character to be removed : "))
new_str =""

for n in range (0,len(str)):
  if n != i:
    new_str = new_str + str[n]

print ("My new string : " + new_str)
    