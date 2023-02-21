def merge_the_tools(string, k):
    # inding length of string and substring
    length_of_string = len(string) 
    length_of_substring = int(length_of_string/k)
    for index in range(0, length_of_string, length_of_substring):
        #set method returns the unique values
        substring = list(set(string[index:index+length_of_substring]))
        #converting list to string again
        substring ="".join(substring)
        print(substring)
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
