#upper(upper case)
data="hello World"
print(data.upper())
#lower(lower case)
data="HELLO WORLD"
print(data.lower())
#title(first letter capital)
data="hello World"
print(data.title())
#strip(remove spaces from start and end)
data=" hello world "
print(data.strip())
#replace(replace part of string)
data="I love python"
print(data.replace("python","java"))
#split(convert string to list)
data="rose,lili,jasmine"
print(data.split(","))
#join(convert list to string)
data="rose","lili","jasmine"
print(",".join(data))
#startswith(check beginning)
data="hello world"
print(data.startswith("hello"))
#endswith(check ending)
data="hello world"
print(data.endswith("hello"))
#find(find index of substring)
data="I love python"
print(data.find("love"))
#count(count occurance)
data="samruddhee"
print(data.count("e"))
#isalpha(only alphabets)
data="hello"
print(data.isalpha())
#isdigit(only digits)
data="12345"
print(data.isdigit())
