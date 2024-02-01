file1 = str(input("Enter the first file name you want to compare: ")) #asking the first file name from user to compare
file2 = str(input("Enter the second file name you want to compare: ")) #asking the second file name from user to compare

with open(file1 +".txt", "r") as readFile1: #using with ensures that the file is properly closes after its suite finishes. as assignes the value to the object.
    content1 = [line.strip() for line in readFile1.readlines()] 
    # use readlines() read the entire file and return a list of strings, each string is line from the file.
    #when reading lines using readlines() each line include newline character \n at the end.
    #line.strip() used to remove these trailing newline characters.
    #assigned the reading value to content1 variable. 

    
with open(file2 + ".txt","r") as readFile2:
    content2 = [line.strip() for line in readFile2.readlines()]
#do the same thing for other file.

difference_found = False
#created boolean flag to print the result1 just one time. Because of its inside the loop whenever the statement find another differences the result1 printed.
#set the value to false and when its true we will say print the result1.   
    
for i in range(min(len(content1),len(content2))): #define the loop range according to smallest length of content
    if content1[i] != content2[i]: #started to scan line by line and try to find which line is not equal to other one.
       difference_found = True 
       with open("report/difContent.txt","a") as different_result: 
           #when if statement finds differences between the lines it creates new txt file and append the text.
           #used "a" method because we want to add the differences whenever it finds. If we use "w" only writes the last differences.
           
           result1 = f"line{i+1} {file1}.txt :{content1[i]}\nline{i+1} {file2}.txt :{content2[i]}" #when the if find differences it shows that which line and what is the differences.
           print(result1) 
           different_result.write(result1) #writing the result1 into created txt file.
           break #when the differences found break is executed else block is skipped.
else : #used for-else statement because I want to see the result2 one time I dont want to put into if loop.
    with open("report/sameContent.txt","w") as same_result:
        result2 = f"{file1}.txt and {file2}.txt has same context"
        print(result2)
        same_result.write(result2)
           

if difference_found:
    print(f"{file1}.txt and {file2}.txt not has the same context")  
         
#boolen flag going to print the statement 1 time when the condition is met


