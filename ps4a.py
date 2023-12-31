# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) <= 1:
        return sequence
    else:
        sequence_list = []
        first = sequence[0]
        second = sequence[1:]

        subsequence = get_permutations(second)
        for seq in subsequence:
            for index in range(len(seq) + 1):
                new_sequence = seq[0:index] + first + seq[index:len(seq) + 1]
                sequence_list.append(new_sequence)


        return sequence_list



#    return sequence_list


if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    print (get_permutations('ab'))
    print (get_permutations('tor'))
    print (get_permutations('bust'))

