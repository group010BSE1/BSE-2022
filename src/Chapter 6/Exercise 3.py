word = 'banana'
def count(word, a):
    counter = 0
    for letter in word:
        if letter==a:
            counter = counter + 1
    print(counter)
count(word,"a")