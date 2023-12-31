# -*- coding: utf-8 -*-
"""Bootcamp_Assignment_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gwYYTas7QEf27ntDfvktnR7kVVoZr9BB
"""

#Display Fibonacci Series upto 10 terms

def Fib(n):
	if n<= 0:
		print("ERROR!!!")
	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return Fib(n-1)+Fib(n-2)

print(Fib(10))

#Display numbers at the odd indices of a list

l=[1,2,3,4,5,6,7,8,9,10]

for i in range(0,10):
  if(i%2!=0):
    print(l[i])

#Print a list in reverse order

l=[1,2,3,4,5,6,7,8,9,10]
n=9
while(n>=0):
  print(l[n])
  n=n-1

#Your task is to count the number of different words in this text
#	string = """
#	ChatGPT has created this text to provide tips on creating interesting paragraphs.
#	First, start with a clear topic sentence that introduces the main idea.
#	Then, support the topic sentence with specific details, examples, and evidence.
#	Vary the sentence length and structure to keep the reader engaged.
#	Finally, end with a strong concluding sentence that summarizes the main points.
#	Remember, practice makes perfect!
#	"""

string="ChatGPT has created this text to provide tips on creating interesting paragraphs. First, start with a clear topic sentence that introduces the main idea. Then, support the topic sentence with specific details, examples, and evidence. Vary the sentence length and structure to keep the reader engaged. Finally, end with a strong concluding sentence that summarizes the main points. Remember, practice makes perfect!"
count=0
length=len(string)
for i in range(0,length):
  if(string[i]==" "):
    count=count+1

print(count+1)

#Write a function that takes a word as an argument and returns the number of vowels in the word
def vowels(word):
  length=len(word)
  count=0
  for i in range(0,length):
    if(word[i]=="a"):
      count=count+1
    elif(word[i]=="e"):
      count=count+1
    elif(word[i]=="i"):
      count=count+1
    elif(word[i]=="o"):
      count=count+1
    elif(word[i]=="u"):
      count=count+1
  return(count)

vowels("Anukriti")

#Iterate through the following list of animals and print each one in all caps.
#animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']

animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']

for i in range(0,5):
  print(animals[i].upper())

#Iterate from 1 to 15, printing whether the number is odd or even

for i in range(1,16):
  if(i%2==0):
    print(i,"=> Even")
  else:
    print(i,"=> Odd")

#Take two integers as input from user and return the sum

a=input()
b=input()
print(int(a)+int(b))