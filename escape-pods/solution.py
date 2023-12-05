def solution(entrances, exits, path):
    # Expaned matrix and super source/target
    def broaden(entrance,exit,map): 
        for i in range(len(map)):
            map[i].append(0)
            map[i].insert(0,0)
        source=[0 for i in range(len(map[0]))]
        for i in entrance:
            source[i+1]=sum(map[i])

        sink=[0 for i in range(len(map[0]))]
        for i in exit:
            k=[j for h in range(len(map)) for j in [map[h][i+1]]]
            map[i][len(map[i])-1]=sum(k)

        map.insert(0,source)
        map.append(sink)
        return(map)

    # Breadth-first search
    def bfs(P):
        X=[]
        for i in range(len(P)):
            for j in range(len(P)):
                if P[i][j]!=0:X.append([i,j])

        output=[-1 for i in range(len(P))]
        position=[i for i in range(len(P))]

        x0=position.index(0)
        y=[0]
        for i in range(len(X)):
            if X[i][0]==x0 and output[X[i][1]]<0:
                output[X[i][1]]=position[X[i][0]]
                y.append(X[i][1])

        j=0
        # stop condition - while y scan all nodes

        while not (max(y)==(len(P)) or j>=len(y)):
            x0=position.index(y[j])
            for i in range(len(X)):
                if X[i][0]==x0 and output[X[i][1]]<0:
                    output[X[i][1]]=position[X[i][0]]
                    y.append(X[i][1])
            j=j+1

        answer=[]
        x1=max(position)

        while x1>0:
            answer.insert(0,[output[x1],x1])
            x1=output[x1]

        return(answer)

    # Edmonds-Karp algorithm
    count=0
    PATH=broaden(entrance=entrances,exit=exits,map=path)

    position=bfs(PATH)
    verify=[i for j in position for i in j]
    flow=[PATH[i[0]][i[1]] for i in position]
    for i in position:
        PATH[i[0]][i[1]]=PATH[i[0]][i[1]]-min(flow)
        PATH[i[1]][i[0]]=PATH[i[1]][i[0]]+min(flow) #residual capacity
    count=count+min(flow)

    while min(verify)>=0:
        position=bfs(PATH)
        verify=[i for j in position for i in j]
        flow=[PATH[i[0]][i[1]] for i in position]
        for i in position:
            PATH[i[0]][i[1]]=PATH[i[0]][i[1]]-min(flow)
            
            #augmenting path

            PATH[i[1]][i[0]]=PATH[i[1]][i[0]]+min(flow) 
        count=count+min(flow)

    return(count)


if __name__ == "__main__":
    entrances = [0, 1]
    exits = [4, 5]

    path =[
        [0, 0, 4, 6, 0, 0],
        [0, 0, 5, 2, 0, 0],
        [0, 0, 0, 0, 4, 4],
        [0, 0, 0, 0, 6, 6],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
        ]

    print(solution(entrances,exits,path))

    entrances = [0]
    exits = [3]
    path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
    print(solution(entrances,exits,path))