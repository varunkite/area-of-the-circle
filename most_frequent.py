import operator
test_str = "Mississippi"
all_freq = {}


for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
all_freq = dict( sorted(all_freq.items(), key=operator.itemgetter(1),reverse=True))
print( str(all_freq))
