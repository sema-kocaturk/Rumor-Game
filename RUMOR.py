# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 00:59:04 2020

@author: user
"""


import random
L1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
L2=[1] # those who know gossip
L3=[]  #number of chats until everyone knows the gossip
L4=[] #200 times the number of chats until everyone knows
t=0 #number of chats until one person knows the gossip
n=0 # a person knows the gossip
r=0 # 20 people knows the gossip
a=0 # t = At least 15 people up to 100 met the requirement once in 200 attempts
b=0 #t = Maximum 2 people up to 10 met the condition b times in 200 attempts
probolity=15/100

while r<=3 :
     if len(L1)==len(L2):
         r=r+1
         L2.clear()
         L2.append(1)
         
         L4.append(L3[-1])
         
         t=0
     if t <=100:
         
         if  len(L2)== 15 or len(L2)== 16 or len(L2)== 17 or len(L2)== 18 or len(L2)== 19 or len(L2)== 20  :
             a=a+1
            
     if t<=10:        
         if len(L2)==1 or len(L2)==2 :
             b=b+1
     rnd=random.randint(1,20)
     rnd_person1=random.choice(L1)
     L1.remove(rnd_person1)
     rnd_person2=random.choice(L1)
     L1.append(rnd_person1)
    
       
     if  rnd_person1 in L2 and  rnd_person2 in L2:
        t=t+1
        
     elif rnd_person1 in L2 or  rnd_person2 in L2:
        
        if rnd_person1 in L2 :
    
          if rnd >=1 and rnd  <=15:
              L2.append(rnd_person2)
              t=t+1
              L3.append(t)           
              n=n+1
             
          else :
               rnd<15 and rnd <=20 
               t=t+1   
               
        elif rnd_person2 in L2:
            
            if rnd >=1 and rnd  <=15:
              L2.append(rnd_person1)
              t=t+1
              L3.append(t)
              n=n+1
              
            else :
               rnd<15 and rnd <=20      
               t=t+1 
               
     else:
            t=t+1
           
            
            
print("average:",sum(L4)/200)    
            
 
print("probability at least 15 people know the humor until the t=100:" , a/200)          
print("Probability that at most 2 people know the humor at time t=10:", b/200)
            
