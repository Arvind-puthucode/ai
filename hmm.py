Sequence="GGCACTGAA"

startH=0.5
startT=0.5

transition=[0.5,0.4,0.5,0.6]

h_dict={"A":0.2,"C":0.3,"G":0.3,"T":0.2}
t_dict={"A":0.3,"C":0.2,"G":0.2,"T":0.3}

Answer=[]
Answer1=[]
for i in range(0,2):
    temp=[]
    for j in range(0,9):
        temp.append(0)
    Answer.append(temp)
    Answer1.append(temp)
    
Answer[0][0]=startT * h_dict[Sequence[0]]
Answer[1][0]=startH * t_dict[Sequence[0]]

Answer1[0][0]=startT * h_dict[Sequence[0]]
Answer1[1][0]=startH * t_dict[Sequence[0]]

for i in range(1,len(Sequence)):
    Answer[0][i]=Answer[0][i-1]*transition[2]*h_dict[Sequence[i]]+Answer[1][i-1]*transition[1]*h_dict[Sequence[i]]
    Answer[1][i]=Answer[1][i-1]*transition[3]*t_dict[Sequence[i]]+Answer[0][i-1]*transition[0]*t_dict[Sequence[i]]
    
for i in range(0,len(Sequence)):
    print("The total probability after Generating letter no ",i+1," is ",Answer[0][i]+Answer[1][i])


if(Answer1[0][0]>Answer1[1][0]):
    print("H",end="")
else:
    print("L",end="")
        
for i in range(1,len(Sequence)):
    Answer1[0][i]=h_dict[Sequence[i]]* max(Answer[0][i-1]*transition[2],Answer[1][i-1]*transition[1])
    Answer1[1][i]=t_dict[Sequence[i]]* max(Answer[1][i-1]*transition[3],Answer[0][i-1]*transition[0])
    if(Answer1[0][i]>Answer1[1][i]):
        print("H",end="")
    else:
        print("L",end="")