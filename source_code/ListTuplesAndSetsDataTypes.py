# List, Tuples and Sets

# List -   List is Muitable Data type.
# List supports ordered
# List accepts duplicate values

courses = ["History", "Math", "Physics", "Compsci"]
nums = [3,4,5,8, 2,1,6,7]

# Empty Lists
empty_list = []
empty_list = list()

#empty tuple
empty_tuple = ()
empty_tuple = tuple()

# empty sets
empty_set = set()

print("We use index method to know index number of list item: ", courses.index("physics".capitalize()))
print("To access list item by using index value: ", courses[1])
print("To access list item by using slicing: ", courses[:2])
print("To access list item by using slicing: ", courses[-3:-1])
courses.append("Art")
print("We use append method to Add an item to the end of the list, courses.append('Art'): ",courses)
courses.insert(3,"Chemistry")
print("we use insert method to insert an item to the specific location, courses.insert(3,'Chemistry'): ",courses)
print("we use extend method to add other list item in the end of list: courses.extend(courses1)")
print("We use pop method to remove last item in list item:courses.pop(): ",courses.pop())
print("if we pass index value to the pop method it remove that specific item: courses.pop(): ", courses.pop(0))
courses.remove("Compsci")
print("we use remove method to remove specific item by passing the item_name: courses.remove(): ",courses)
courses.reverse()
print("we use reverse method to view list items in reverse order: cours es.reverse(): ",courses)
courses.sort()
print("sort list items we used sort method: courses.sort(): ",courses)
courses.sort(reverse = True)
print(courses)
sorted_list = sorted(courses)
print("we use sorted functions with out altering original list: sorted_list = sorted(courses)",sorted_list)
print("original List: ",courses)
print("To convert list into string we use join function: ' '.join(courses)", ' '.join(courses))


print("We use max function to get the max value from the list: max(nums)", max(nums))
print("We use min function to get the min value from the list: min(nums)", min(nums))
print("we use sum function to sum the items: ", sum(nums))

# tuple is immutable data-type
# unlike tuple not support insertion and deletion of an element. because of immutability
# tuples support count, index methods
# tuples support ordered

courses = ("History", "Math", "Physics", "Compsci")
print(courses.count("Math"))
print(courses.index("Compsci"))


# set is mutable data-type
# sets data is not ordered
# sets are not allowed duplicate values
# sets are not support index concept

cs_courses = {"History", "Math", "Physics", "Compsci"}
art_courses = {"History", "Math", "Art", "Design"}

# intersection - &
# union - |
# difference - -
common_courses_in_cs_art_group = cs_courses & art_courses
print("Intersection is a method is used to get the common elements in both sets: ",common_courses_in_cs_art_group)
merge_both_sets = cs_courses | art_courses
print("Union method is used to combine both set data with and not allowing duplicate data: ", merge_both_sets)
difference_return_not_existed_content_in_set2 = cs_courses - art_courses
print("difference_return_not_existed_content_in_set2: ",difference_return_not_existed_content_in_set2)
