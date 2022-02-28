str= 'X-DSPAM-Confidence: 0.8475'
a =str.find(' ')
numbers = float(str[a:])
print(numbers)