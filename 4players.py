#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 10:15:40 2021

@author: viri
"""
print('')
print('This program gives one of the best choices for the first player A, the other one can be obtained by symmetry analysis')
print('The following notation is used in the result')
print('Xa: position chosen by A')
print('Xb: position chosen by B')
print('Xc: position chosen by C')
print('Xd: position chosen by D')
print('Pa: probability that the random number resuls closer to A')
print('Pb: probability that the random number resuls closer to B')
print('Pc: probability that the random number resuls closer to C')
print('Pd: probability that the random number resuls closer to D')

print('')

############################################################################################
#import numpy as np

#fhC = open("salidaC.txt", 'w')
#fhD = open("salidaD.txt", 'w')

NN = input("We will discretise the interval, please enter an integer number of subintervals (greater than 30) ", )
N = int(NN)
#initialazing dictionaries
choices=dict()
prob_inter=dict()

#initializing arrays
bestA=[]
finalA=[]
bestB=[]
finalB=[]
bestC=[]
finalC=[]
bestD=[]


#Initializing probability variables
PA=0
pa=0

##################AUXILIAR FUNCTION ############
def get_key(dic,z): #function defined to fetch key from value
    for key, value in dic.items():
         if z == value:
             return key
 
    return "the key doesn't exist"
################### PROGRAM #################
for A in range(N):
    PB=0

    for B in range(N):
      
        if A==B:
           B=A+1.e-10 #To avoid player B taking exactly the same value that player A.
        
        PC=0
        for C in range(N):
            
            if A==C:
                C=A+1.e-10 #To avoid player C taking exactly the same value that player A.
                
            if B==C:
                C=B+1.e-10 #To avoid player C taking exactly the same value that player B.
            
            
            PD=0                   
            for D in range(N):
                if A==D:
                    D=A+1.e-10 #To avoid player C taking exactly the same value that player A.
                    
                if B==D:
                    D=B+1.e-10 #To avoid player C taking exactly the same value that player B.
                
                if C==D:
                    D=C+1.e-10 #To avoid player C taking exactly the same value that player B.
                             
                choices["A"]=A
                choices["B"]=B
                choices["C"]=C
                choices["D"]=D
               
                X=list(choices.values()) # make a list from values in the dcitionary.
                X.sort()
                P1=(X[0]+X[1])/(2*N)     # Probability for the player that choose the smallest value.
                P2=(X[2]-X[0])/(2*N)     # Probability for the player that choose the next value.
                P3=(X[3]-X[1])/(2*N)     # Probability for the player that choose the next value.
                P4=(N-(X[3]+X[2])/2)/(N) # Probability for the player that choose the last value.
                         
                prob_inter[get_key(choices,X[0])]=P1 #Associate the probability with the player in the first position.
                prob_inter[get_key(choices,X[1])]=P2 #Associate the probability with the player in the second position.
                prob_inter[get_key(choices,X[2])]=P3 #Associate the probability with the player in the third position.
                prob_inter[get_key(choices,X[3])]=P4 #Associate the probability with the player in the fourth position.
                PAi = prob_inter['A']
                PBi = prob_inter['B']
                PCi = prob_inter['C']
                PDi = prob_inter['D']
                if PD < PDi:             #choose the best option for D for each choice of A, B and C.
                    PA1 = PAi
                    PB1 = PBi
                    PC1 = PCi
                    PD  = PDi
                    Dmax=D
                    tup = [A/N,B/N,C/N,Dmax/N,PAi,PBi,PCi,PD]
                    #np.savetxt(fh, tup)
                    #print(tup)
                    
            bestD.append(tup)            #bestD is a two dim array with the best choices for D, given A, B and C.
           

nc=len(bestD)
  
for i in range(N*N):                   #Take the best option for C and D, for each choices of A and B.
    pc=0
    for j in range(i*(N),(i+1)*N):
        if pc<bestD[j][6]:
            bestC=bestD[j] 
            pc=bestD[j][6]
    finalC.append(bestC)             #finalC is a two dim array with the best choices of C and D, given A and B.


for i in range(N):                   #Take the best option for B, C and D, for each choice of A.
    pb=0
    
    for j in range(i*(N),(i+1)*(N)):
        if pb < finalC[j][5]:
            bestB=finalC[j] 
            pb=finalC[j][5]
        
    finalB.append(bestB)

for j in range(N):                  #Select the best option for A, asumming that B, C and D will do the same.
    if pa<finalB[j][4]:
        bestA=finalB[j]             #Store final results for the best option for A.
        pa=finalB[j][4]

print('')
print('The final result is:')
print('X_a =',bestA[0],' Xb =', bestA[1],' X_c =', bestA[2],' X_d =', bestA[3], ' P_a =', bestA[4],' P_b =', bestA[5],' P_c =', bestA[6], ' P_d =', bestA[7])
print('')            
