import re
fhand = open('regex_sample.txt')
sum = 0

for line in fhand:
        line=line.rstrip()
        numbers = re.findall('[0-9]+',line)
        for number in numbers:
                if number is not None:
                        sum += int(number)
print(sum)               
