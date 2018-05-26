


def mars_exploration(s):
    pos = 0
    count = 0
    while pos < len(s):
        if s[pos] != "S":
            count += 1
        if s[pos + 1] != "O":
            count += 1
        if s[pos + 2] != "S":
            count +=1
        pos += 3
    return count
