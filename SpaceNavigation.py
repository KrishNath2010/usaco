# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 09:31:46 2021

@author: Krish Nath
"""

trails=input()
trails=int(trails)
for trail in range(trails):
    cordinates=input()
    cordinates=cordinates.split(' ')
    x_cor=int(cordinates[0])
    y_cor=int(cordinates[1])
    directions=input()
    directions_list=[]
    for x in directions:
        directions_list.append(x)
    directions=directions_list
    num_R=0
    num_U=0
    num_D=0
    num_L=0
    for x in directions:
        if x=='R':
            num_R+=1
        if x=='U':
            num_U+=1
        if x=='D':
            num_D-=1
        if x=='L':
            num_L-=1
    x_true=False
    y_true=False
    if x_cor<0:
        if num_L<=x_cor:
            x_true=True
    else:
        if num_R>=x_cor:
            x_true=True
    if y_cor<0:
        if num_D<=y_cor:
            y_true=True
    else:
        if num_U>=y_cor:
            y_true=True
    if x_true==True and y_true==True:
        print('YES')
    else:
        print('NO')
    
            
        
        
        
        
        