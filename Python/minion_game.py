def minion_game(string):
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']

    stu_score = 0
    kev_score = 0

    for i in range(len(string)):
        
        if string[i] in vowels:
            kev_score += len(string) -i
        else:
            stu_score += len(string) -i
    
    if stu_score > kev_score:
        print(f"Stuart {stu_score}")
    elif kev_score > stu_score:
        print(f"Kevin {kev_score}")
    else:
        print(f"Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)



# def Stuart(str_x, indx):
    
#     a = []
    
#     for i in range(indx, len(str_x)):
#         sub_str = str_x[indx:i+1]
#         a.append(sub_str)

#     return a
    

# def Kevin(str_x, indx):
    
#     b = [] 
    
#     for i in range(indx, len(str_x)):
#         sub_str = str_x[indx:i+1]
#         b.append(sub_str)

#     return b

# def minion_game(string):
#     # your code goes here
#     vowels = ['A', 'E', 'I', 'O', 'U']

#     stu = []
#     kev = []

#     for i in range(len(string)):
        
#         if string[i] in vowels:
#             b = Kevin(string, i)
#             kev.append(b)
#         else:
#             a = Stuart(string, i)
#             stu.append(a)

    
#     stu_dict = {}
#     kev_dict = {}

#     for sub_set in stu:
#         for j in range(len(sub_set)):
#             if sub_set[j] not in stu_dict:
#                 stu_dict[sub_set[j]] = 1
#             else:
#                 stu_dict[sub_set[j]] += 1
        
#     for sub_set in kev:
#         for j in range(len(sub_set)):
#             if sub_set[j] not in kev_dict:
#                 kev_dict[sub_set[j]] = 1
#             else:
#                 kev_dict[sub_set[j]] += 1

#     print(stu)
#     print(kev)

#     stu_score = sum(stu_dict.values())
#     kev_score = sum(kev_dict.values())
    
#     if stu_score > kev_score:
#         print(f"Stuart {stu_score}")
#     elif kev_score > stu_score:
#         print(f"Kevin {kev_score}")
#     else:
#         print(f"Draw")

# if __name__ == '__main__':
#     s = input()
#     minion_game(s)