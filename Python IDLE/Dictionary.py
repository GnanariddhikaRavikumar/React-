dict1={}
dict2={"Name":"Allwin","Dept":"EEE","Year":1}
print(dict1,dict2,len(dict2))
dict3={("Name","Kavin"),("Rollno",1)}
print(dict3)
dict4={"Name":"Lamborghini","Prize":"3.12Cr","Color":["Red","Yellow","Black"]}
print(dict4,len(dict4),type(dict4))
print(dict4["Color"])
dict4["Model"]="Lamborghini Reveulto"
print(dict4)
dict4["Prize"]="4 Cr"
print(dict4)
print(dict4.keys(),dict4.items())
dict5=dict2.copy()
print(dict5)
dict6={"CCE","CSE","CSBS","EEE"}
keys={'a','e','i','o','u'}
value="Vowels"
vowels=dict.fromkeys(keys,value)
print(vowels)
print(dict2.get("Year"))
dict2["College"]="SECE"
print(dict2)
print(dict2.popitem())
print(dict2)
print(dict2.pop("Year"))
print(dict2.values())
print(dict3)
dict7={"College":"SECE"}
dict2.update(dict7)
print(dict2)
dict3.clear()
print(dict3)
del dict2
print(dict2)
'''OUTPUT:
    {} {'Name': 'Allwin', 'Dept': 'EEE', 'Year': 1} 3
    {('Name', 'Kavin'), ('Rollno', 1)}
    {'Name': 'Lamborghini', 'Prize': '3.12Cr', 'Color': ['Red', 'Yellow', 'Black']} 3 <class 'dict'>
    ['Red', 'Yellow', 'Black']
    {'Name': 'Lamborghini', 'Prize': '3.12Cr', 'Color': ['Red', 'Yellow', 'Black'], 'Model': 'Lamborghini Reveulto'}
    {'Name': 'Lamborghini', 'Prize': '4 Cr', 'Color': ['Red', 'Yellow', 'Black'], 'Model': 'Lamborghini Reveulto'}
    dict_keys(['Name', 'Prize', 'Color', 'Model']) dict_items([('Name', 'Lamborghini'), ('Prize', '4 Cr'), ('Color', ['Red', 'Yellow', 'Black']), ('Model', 'Lamborghini Reveulto')])
    {'Name': 'Allwin', 'Dept': 'EEE', 'Year': 1}
    {'o': 'Vowels', 'u': 'Vowels', 'i': 'Vowels', 'e': 'Vowels', 'a': 'Vowels'}
    1
    {'Name': 'Allwin', 'Dept': 'EEE', 'Year': 1, 'College': 'SECE'}
    ('College', 'SECE')
    {'Name': 'Allwin', 'Dept': 'EEE', 'Year': 1}
    1
    dict_values(['Allwin', 'EEE'])
    {('Name', 'Kavin'), ('Rollno', 1)}
    {'Name': 'Allwin', 'Dept': 'EEE', 'College': 'SECE'}'''
