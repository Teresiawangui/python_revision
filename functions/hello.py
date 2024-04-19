n= 10
d = dict()  
for x in range(1,n+1):
    d[x] = x*x
print(d)
 #8.create a program that takes two strings as input and checks if one is an anagram of the other.e.g("listen","silent")   
def are_anagrams(str1,str2):
    if sorted(str1) == sorted(str2):
        print(f"{str1} and {str2} are anagrams")
    else:
        print(f"{str1} and {str2} are not anagrams")

#10.create a program that takes a string as input and counts the number of vowels in it.
def vowel_count(str):
    count = 0
    vowels = set("a,e,i,o,u,A,E,I,O,U")    
    for alphabet in str:
        if alphabet in vowels:
            count +=1
    print(count)

def my_vowels(name,vowels):
    count = sum(name.count(vowel)for vowel in vowels)
    print(count)
#5.write a program that takes a list of integers as input and removes all duplicates numbers, returning a list with unique numbers only.
def unique():
    integers = [3,5,8,9,6,4,8,5,3]
    new_integers = set(integers) 
    current_integers = list(new_integers)
    print (current_integers)
#2.write a program that takes a string as input and outputs the string reversed.
def reverse_word(name):
    name = list(name) 
    name.reverse()   
    name =''.join(name)
    my_string =(name)
    print(my_string)

def reverse(name):
    print(name[::-1])  

 #1.create program that takes two sorted arrays as input and merges them into a single sorted array.       
def merging_array(arr1,arr2):
    merged_array=sorted(arr1) +sorted(arr2)
    wholeSorted = sorted(merged_array)
    print(wholeSorted)
#4.write a program that takes a list of integers as input and outputs the list in sorted descending order.
def sortDescending():
    integers = [9,4,7,2,1,8]
    integers.sort(reverse=True)
    print(integers)

#3.write a program that takes a string as input and removes all duplicate characters, maintaining the original order. 
def remove_duplicates(word):
    word = set(word)
    word = sorted(word)
    print(word)













  
      


    

    
          
  




  
