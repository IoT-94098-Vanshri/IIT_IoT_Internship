data=input("Enter any string:")
#full string
print("1.full string:",data[:])
#first 5 characters
print("2.first 5 characters:",data[0:5])
#last 3 characters
print("3.last 3 characters:",data[-3:])
#characters from index 2 to 6
print("4.characters from index 2 to 6:",data[2:7])
#reversed string
print("5.reversed string:",data[::-1])
#every second char
print("6.every second char:",data[::2])
#slice from index 3 to end
print("7.slice from index 3 to end:",data[3:])
#slice from start to index 4
print("7.slice from start to index 4:",data[:5])
#negative indexing demo
print("9.negative indexing demo:",data[-5:-1])
#reverse any alternate char
print("10.reverse any alternate char:",data[::-2])


