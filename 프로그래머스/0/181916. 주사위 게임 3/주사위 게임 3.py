def solution(a, b, c, d):
    answer = 0
    data = [a, b, c, d]
    data.sort()
    if data[0] == data[1] and data[2] == data[3] and data[0] == data[2]:
        answer = 1111 * data[0]
    elif data[0] == data[1] and data[1] == data[2]:
        answer = (10 * data[0] + data[3]) * (10 * data[0] + data[3])
    elif data[1] == data[2] and data[2] == data[3]:
        answer = (10 * data[3] + data[0]) * (10 * data[3] + data[0])
    elif data[0] == data[1] and data[2] == data[3] and data[0] != data[2]:
        answer = (data[0] + data[3]) * abs(data[0] - data[3])
    elif data[0] == data[1]:
        answer = data[2] * data[3]
    elif data[1] == data[2]:
        answer = data[0] * data[3]
    elif data[2] == data[3]:
        answer = data[0] * data[1]
    elif data[0] != data[1] and data[1] != data[2] and data[2] != data[3]:
        answer = data[0]
    return answer