#can we have a set with 18(int) and "18"(str) as a value same it?

# yes, we can do becuse 18 and "18".oth are difeerent object

a = set()
a.add(18)
a.add("18")
print(a)