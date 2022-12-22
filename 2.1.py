#a
given_str = "Python is a case sensitive language"
print (len(given_str))
#b
rev_given_str = given_str [::-1]
print (rev_given_str)
#c
new_str = slice (given_str[10:26])
print (new_str)
#d
replaced_str = given_str.replace("a case sensitive", "object oriented")
print (replaced_str)
#e
index_a = given_str.index("a")
print (index_a)
#f
white_spc_rem = given_str.replace(" ","")
print (white_spc_rem)
