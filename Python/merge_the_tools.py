def merge_the_tools(string, k):
    # your code goes here

    index = -1
    result = []

    for i in range(len(string)):
        if i % k == 0:
            tracker = {}
            result.append("")
            index += 1

        if string[i] not in tracker:
            tracker[string[i]] = 1
            result[index] += string[i]

    for i in result:
        print(i)    

# def merge_the_tools(string, k):
#     # your code goes here
    
#     frac = int(len(string)/k)
#     result = []
#     indx = 0

#     for _ in range(frac):
#         temp = []
#         for i in range(k):
#             if string[indx] not in temp:
#                 temp.append(string[indx])
#             indx += 1
        
#         temp_str = ""   
#         for i in temp:
#             temp_str = temp_str + i
#         result.append(temp_str)

#     for i in result:
#             print(i) 

    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)