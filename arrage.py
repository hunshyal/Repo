input = [0,1,0,1,0,0,1,1,1,0]

#new_list = [x for x in input if x == 0] + [x for x in input if x == 1]
#print(new_list)

#################
##   OR        ##
#################

new_list = []
for i in input:
  if i == 0:
    new_list.insert(0,i)
  else:
    new_list.append(i)

print(new_list)
print("Adding this to git1")
print("Adding this to git2")
print("Adding this to git3")
print("Adding this to git4")

