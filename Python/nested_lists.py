# # nested list

# # for _ in range(int(input())):
# name = ["sanna","kiran","jyoti","vikram","vinay"]
# score= [30,20,30,40,45]
# output=list(map(list,(zip(name,(map(float,score))))))
# sorted_ouput=sorted(output, key=lambda x:(x[1],x[0]))
# final_ouput=sorted_ouput[1:]
# print(final_ouput)
# dict1={}
# for name, score in final_ouput:
#     if score in dict1:
#         dict1[score].append(name)
        
#     else:
#         dict1[score]= [name]
    
# second_last_output=(list(dict1.values())[0])
# print(second_last_output)



if __name__ == '__main__':
    
    records = []
    scores = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        scores.append(score)
        records.append([name, score])
        
    scores.sort()
    for i in range(1, len(scores)):
        if scores[i] > scores[i-1]:
            sec_min = scores[i]
            break
        
    result = []
    for record in records:
        if record[1] == sec_min:
            result.append(record[0])
            
    result.sort()
    for name in result:
        print(name)
            
        