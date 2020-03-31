test_list =[1,2,3,3,3,4,5,5,6,7,8,9]
print ('before=:'+str(test_list)) 
t = [] 
for i in test_list:
    if i in t:
        i='n'
        t.append(i)
    else:
        t.append(i) 
print ('after=:'+str(t))