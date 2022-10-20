nestedlist = [ [1, 2, 3, 4], ["Ten", "Twenty", "Thirty"], [1.1,  1.0E1, 1+2j, 20.55, 3.142]]
flatlist=[element for sublist in nestedlist for element in sublist]
print(flatlist)



Test_list = [1, 2, 3, 4, 5]
New_list = Test_list.copy()
New_list.reverse()

print("Original List: ", Test_list)  # Output: [1,2,3,4,5]
print("Reversed List: ", New_list)  # Output: [5,4,3,2,1]
