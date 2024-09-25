#permutations of a given string
# Write perm and fact where fact calculates the factorial.


#factorial
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)   



#permutations
def perm(word):
    answer = []
    if len(word) == 0:
        return[ '' ]
    
    for i in range(len(word)):
        letter = word[i]
        remaining =  word[:i] + word[i+1:]
        #print(f'letter: {letter}, rem: {remaining}')

        a = perm(remaining)

        for w in a:
            answer = answer + [w + letter]
    return answer

#print(perm('dog'))

# test
assert sorted(perm("hat")) == sorted(['hat', 'aht', 'ath', 'hta', 'tha', 'tah']), "First assert fails."
assert len(perm("race")) == fact(len("race")), "Second assert fails."
assert len(perm("whatever")) == 40320, "Third assert failed."
print ("All assertions passed without a problem")