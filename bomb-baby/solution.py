def solution(M, F):
    x = int(M)
    y = int(F)
    
    generation = 0

    while x > 1 or y > 1:
        
        if x == 1 or y == 1:
            if x > y:
                x -= y
            elif x < y:
                y -= x
            else:
                x -= y
            generation +=1
        else:
            if x > y:
                generation += x // y
                x %= y
            elif x < y:
                generation += y // x
                y %= x
            else:
                x -= y
        
        if x == 0 or y == 0:
            break
        
    if x == 1 and y == 1:
        return str(generation)
    else:
        return 'impossible'
    

if __name__ == "__main__":
    print(solution(4, 7))
    print(solution(2, 1))