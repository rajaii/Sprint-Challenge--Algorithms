'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    txt = word.split('th')
    if len(txt) != 0:
        return
    return txt.count('th')

    
    


#break to array
#set base case
#set counter var
#count occurrences of th in array in counter
#return count
