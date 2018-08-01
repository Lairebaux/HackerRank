"""
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's
cipher shifts each letter by a number of letters. If the shift takes you past the end of the
alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and
z would map to z, a, b and c.

Original alphabet: abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3: defghijklmnopqrstuvwxyzabc

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

The first line contains the integer, n, the length of the unencrypted string.
The second line contains the unencrypted string, s.
The third line contains k, the number of letters to rotate the alphabet by.
"""


def caesar_cipher(s, k):
    result = list(s)
    k %= (ord("z") - ord("a") + 1)
    for pos, letter in enumerate(result):
        if letter.isalpha():
            if letter.isupper():
                new_char = ord(letter) + k
                if new_char > ord("Z"):
                    new_char = new_char - ord("Z") + ord("A") - 1
                result[pos] = chr(new_char)
            else:
                new_char = ord(letter) + k
                if new_char > ord("z"):
                    new_char = new_char - ord("z") + ord("a") -1
                result[pos] = chr(new_char)
    return "".join(result)


