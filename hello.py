n= 10
d = dict()  
for x in range(1,n+1):
    d[x] = x*x
print(d)
    
def are_anagrams(str1,str2):
    if sorted(str1) == sorted(str2):
        print(f"{str1} and {str2} are not anagrams")
    else:
        print(f"{str1} and {str2} are not anagrams")

        

def reverse_string(str3):

    str3 = list(str3)
    str3.reverse()
    str3 = ''.join(str3)
    print(str3)

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

def unique(integers):
    integers = set(integers) 
    integers = list(integers)
    print (integers)  

def reverse_word(name):
    name = list(name) 
    name.reverse()   
    name =''.join(name)
    print(name)

def reverse(name):
    print(name[::-1])  

def remove_duplicates(str):
    new_str =" "
    for char in str:
        if char in new_str:
            new_str+=char
            return(new_str)
      



    

    
          
  




  
