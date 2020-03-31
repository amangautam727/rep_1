from collections import Counter
test_str='cars bikes arcs steer'
test_str=test_str.split(' ')
print('after splitting=:'+str(test_str))
for t in range(0,len(test_str)):
    test_str[t]=''.join(sorted(test_str[t]))
    Dic=Counter(test_str)   
print('max subset anagram =:'+str(max(Dic.values())))
print('after shorting=:'+str(test_str)) 
