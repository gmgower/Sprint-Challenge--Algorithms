'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

# U
input(s): one string
output: count how many times ***th*** occurs, case sensitve / return integer
requirements: use recursion of n

# P
1. find base case edge case less than 2  stop recursing
2. if the first 2 letters are 'th', it add 1
3. if it doesn't match then it move on

'''
def count_th(word):    
    # TBC
    # find base case edge case less than 2  stop recursing
    if len(word) < 2:
        return 0
    if word[0:2] == 'th': # firt 2 letter match add 1 and recurse through word removing indices
        return count_th(word[1:]) + 1
    else: # doesn't match recurse remove [0] index
        return count_th(word[1:])

print(count_th("yuithth"))
 
