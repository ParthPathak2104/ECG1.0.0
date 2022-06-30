# testString=input("Enter a string: ")

# stringCounter=0 #counts the length of longest non capital alphabetic string
# longestStringCount=0 #length of longest string
# longestString=""
# string=""

# for element in testString:
    
#     #any time string counter is greater than longeststringcounter it will replace the longest string 
#     #any time a break/capital letter / number is encountered string counter becomes 0 and string becomes empty

import re

testString=input("Enter a string: ")

#splits the string on numbers ,capital letters and white spaces 
seperatedArray=re.split("[0-9]|[A-Z]|\s",testString)  

#returns the max string in array according to length of string
longestString=max(seperatedArray,key=len)  
print(longestString)
#*****************************************************
# lenArray=[]
# for item in seperatedArray:
#     lenArray.append(len(item))

# longestStringSize=max(lenArray)
# longestStringIndex=lenArray.index(longestStringSize)

# print(seperatedArray[longestStringIndex])
