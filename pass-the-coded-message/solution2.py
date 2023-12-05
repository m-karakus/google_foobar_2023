def solution(l):

    # Don't modify existing list object
    bucket = l[:]
    
    # Remainder Class:
    state = sum(bucket)%3 

    while state > 0 and bucket:

        # Transition between remainder classes by removing numbers
        if state == 1:
            to_remove = set(bucket) & {1, 4, 7}
            if not to_remove:
                to_remove = set(bucket) & {2, 5, 8}
        elif state == 2:
            to_remove = set(bucket) & {2, 5, 8}
            if not to_remove:
                to_remove = set(bucket) & {1, 4, 7}

        # Remove min and move to new remainder class
        bucket.remove(min(to_remove))
        state = sum(bucket) % 3
 
    # Calculate maximal number from bucket
    sorted_list = sorted(bucket)[::-1]
    number = ''.join(str(x) for x in sorted_list)
    return int(number) if number else 0

print(solution([3, 1, 4, 1]))
print(solution([3, 1, 4, 1, 5, 9]))
print(solution([]))
print(solution([9, 9, 9, 9]))