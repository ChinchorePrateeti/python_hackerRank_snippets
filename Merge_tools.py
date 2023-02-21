def merge_the_tools(string, k):
    # inding length of string and substring
    length_of_string = len(string) 
    for index in range(0, length_of_string, k):
        #set method returns the unique values
        substring = list(set(string[index:index+k]))
        #converting list to string again
        substring ="".join(substring)
        print(substring)
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
