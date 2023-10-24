set1={"CCE","CSBS","ECE"}
print(set1)            #{'CSBS', 'ECE', 'CCE'}
set1.add("EEE")
print(set1)            #{'CSBS', 'EEE', 'CCE', 'ECE'}
set1.discard("ECE")
print(set1,len(set1))  #{'CSBS', 'EEE', 'CCE'} 3
set2={1,2,3,45}
set3={23,45,567,2}
print(set1|set2,set1.union(set2))
#{1, 2, 3, 'CCE', 'EEE', 45, 'CSBS'} {1, 2, 3, 'CCE', 'EEE', 45, 'CSBS'}
print(set2&set3,set2.intersection(set3))          #{2, 45} {2, 45}
print(set2-set3,set2.difference(set3))            #{1, 3} {1, 3}
print(set2^set3,set2.symmetric_difference(set3))  #{1, 3, 567, 23} {1, 3, 567, 23}
if(set2==set3):
    print("Equal")
else:
    print("Not Equal")  #Not Equal
set4=set3.copy()
print(set4)  #{2, 23, 45, 567}
set4.remove(45)
print(set4)  #{2, 23, 567}
set4.pop()
print(set4)  #{23, 567}
set4.clear()
print(set4)  #set()
