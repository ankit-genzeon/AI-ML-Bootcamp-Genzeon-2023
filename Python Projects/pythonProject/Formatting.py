a=(int(input("enter number")))
print(a)

b= input("enter a string")
print(b)

#string formats
name = "genzeon"
language = "python"
c= "trainees"

print(c, "are learning", language, "programming at", name)

#format
print("{} are learning {} programming at {}".format(c,language,name))
print("{0} are learning {1} programming at {2}".format(c,language,name))

#placeholder
print("%s are learning %s programming at %s"%(c,language,name))
