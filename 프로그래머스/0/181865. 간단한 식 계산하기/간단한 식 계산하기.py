def solution(binomial):
    answer = 0
    split_binomial = binomial.split()
    split_binomial[0] = int(split_binomial[0])
    split_binomial[2] = int(split_binomial[2])
    if split_binomial[1] == '+':
        answer = split_binomial[0] + split_binomial[2]
    elif split_binomial[1] == '-':
        answer = split_binomial[0] - split_binomial[2]
    elif split_binomial[1] == '*':
        answer = split_binomial[0] * split_binomial[2]
    return answer