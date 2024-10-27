
friends = {'Bob', 'Rolf', 'Anne'}
abroad = {'Bob', 'Anne'}

local = friends.difference(abroad)
print(local)

abroad_friends = abroad.difference(friends)
print(abroad_friends)

all_friends = local.union(abroad)

# ----

art = {'Bob', 'Rolf', 'Jen', 'Charlie'}
science = {'Bob', 'Jen', 'Adam', 'Anne'}

both = art.intersection(science)
print(both)

