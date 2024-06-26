def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        elif stk and stk[-1] == arr[i]:
            stk.pop(-1)
            i += 1
        elif stk and stk[-1] != arr[i]:
            stk.append(arr[i])
            i += 1
    stk = [-1] if not stk else stk
    return stk