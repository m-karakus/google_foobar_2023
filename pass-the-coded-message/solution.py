def to_int(l):
    if not l:
        return 0
    res =  int("".join([str(d) for d in l]))
    return res

def solution(l):
    l = sorted(l, reverse=True)
    n = len(l)
    s = sum(l)
    if s % 3 == 0:
        # already divisible by 3 : use all digits
        return to_int(l)
    elif s % 3 == 1:
        # check backward if there is a digit that is 1 mod 3
        i = n - 1
        while i >= 0:
            if l[i] % 3 == 1:
                return to_int(l[:i] + l[i+1:])
            i -= 1
        # there must be two digits that each of them is 2 mod 3
        i = n - 1
        while i >= 0:
            if l[i] % 3 == 2:
                break
            i -= 1
        j = i - 1
        while j >= 0:
            if l[j] % 3 == 2:
                break
            j -= 1
        return to_int(l[:j] + l[j+1:i] + l[i+1:])
    else:
        # check backward if there is a digit that is 2 mod 3
        i = n - 1
        while i >= 0:
            if l[i] % 3 == 2:
                return to_int(l[:i] + l[i+1:])
            i -= 1
        # there must be two digits that each of them is 1 mod 3
        i = n - 1
        while i >= 0:
            if l[i] % 3 == 1:
                break
            i -= 1
        j = i - 1
        while j >= 0:
            if l[j] % 3 == 1:
                break
            j -= 1
        return to_int(l[:j] + l[j+1:i] + l[i+1:])


if __name__ == "__main__":
    print(solution([3, 1, 4, 1]))
    print(solution([3, 1, 4, 1, 5, 9]))
    print(solution([]))
    print(solution([9, 9, 9, 9]))