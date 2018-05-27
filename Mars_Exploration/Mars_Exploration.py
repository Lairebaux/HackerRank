"""Letters in some of the SOS messages are altered by cosmic radiation during transmission.
Given the signal received by Earth as a string, , determine how many letters of Sami's SOS
have been changed by radiation."""


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
