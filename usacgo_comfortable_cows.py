# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 14:29:07 2021

@author: Krish Nath
"""
def is_cow_comfortable(give_data,cow):
    cow_x=cow[0]
    cow_y=cow[1]
    nebors=[(cow_x+1,cow_y),(cow_x,cow_y+1),(cow_x-1,cow_y),(cow_x,cow_y-1)]
    not_in=0
    missing=None
    for a in nebors:
        if not_in>1:
            break
        if a not in give_data:
            not_in+=1
            missing=a
    if not_in==1:
        return True,missing
    else:
        return False,None
answer_list=[]
num_of_cows=int(input())
data_list=[]
for s in range(num_of_cows):
    sample=input()
    sample=sample.split()
    sample_tuple=(int(sample[0]),int(sample[1]))
    data_list.append(sample_tuple)
count=1
use_data=[]
while count<=3 and count<=num_of_cows:
    use_data.append(data_list[count-1])
    count+=1
    answer_list.append(0)
answer=0
for q in range(num_of_cows-3):
    add_index=q+3
    add_tup=data_list[add_index]
    if add_tup in use_data:
        use_data.remove(add_tup)
        answer-=1
    use_data.append(add_tup)
    missing_list=[]
    for e in use_data:
        cow_x=add_tup[0]
        cow_y=add_tup[1]
        nebors=[(cow_x+1,cow_y),(cow_x,cow_y+1),(cow_x-1,cow_y),(cow_x,cow_y-1)]
        #if e in nebors:
        prob,missing=is_cow_comfortable(use_data,e)
        if prob==True:
            use_data.append(missing)
            missing_list.append(missing)
            answer+=1
    while missing_list!=[]:
        for t in missing_list:
            prob,missing=is_cow_comfortable(use_data,t)
            if prob==True:
                use_data.append(missing)
                missing_list.append(missing)
                answer+=1
            missing_list.remove(t)
    answer_list.append(answer)
for m in answer_list:
    print(m)
    
