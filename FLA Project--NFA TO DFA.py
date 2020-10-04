#Python program to convert a TO DFA
#BY RA1811028010010
#   RA1811028010011
#   RA1811028010012
import pandas as pd
a = {}                                 
n = int(input("Number of states: "))            
t = int(input("Number of transitions: "))       
for i in range(n):  
    state = input("Name of State: ")            
    a[state] = {}                          
    for j in range(t):
        path = input("Path : ")               
        print("Enter end state ".format(state,path))
        b = [x for x in input().split()] 
        a[state][path] = b     
print("\na:\n")
print(a)                                    
print("\na table:")
c = pd.DataFrame(a)
print(c.transpose())
print("Enter final state of a: ")s
d = [x for x in input().split()]               
e = []                          
dfa = {}                                    
f = list(list(a.keys())[0])               
g = list(a[f[0]].keys())    
dfa[f[0]] = {}                       
for y in range(t):
    h = "".join(a[f[0]][g[y]])   
    dfa[f[0]][g[y]] = h          
    if h not in f:                        
        e.append(h)                 
        f.append(h)                     
while len(e) != 0:                    
    dfa[e[0]] = {}                    
    for _ in range(len(e[0])):
        for i in range(len(g)):
            temp = []                              
            for j in range(len(e[0])):
                temp += a[e[0][j]][g[i]] 
            s = ""
            s = s.join(temp)                      
            if s not in f:                  
                e.append(s)            
                f.append(s)                 
            dfa[e[0]][g[i]] = s  
       
    e.remove(e[0])    

print("\nDFA: \n")    
print(dfa)                                        
print("\n DFA table: ")
i = pd.DataFrame(dfa)
print(i.transpose())

l = list(dfa.keys())
m = []
for x in l:
    for i in x:
        if i in d:
            m.append(x)
            break
        
print("\nFinal states: ",m)    