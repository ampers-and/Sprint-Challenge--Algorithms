'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC
    # iterative -
    #  start at 0, stop at len-2, find t, if h is next - +1
    def count_helper(word, count=0):
        # base case
        if len(word) <= 1:
            return count
        # recursion
        if word[0] == 't' and word[1] == 'h':
            count += 1

        return count_helper(word[1:], count)

    return count_helper(word)
