# cook your dish here
total_input=int(input())
for _ in range(total_input):
    n,e=map(int,input().split())
    g={n:[]}
    for i in range(1,n):
        g[i]=[i+1]
        print(i,i+1)
        e-=1
    end=3
    while e>0:
        for i in range(1,end):
            
            if g[i][-1]<end:
                g[i].append(end)
                print(i,end)
                e-=1
                if e==0:break

        end+=1
    
