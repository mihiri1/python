#wordslen
word = "Blue Sky"
x = len(word)
print(x)

#dividepara
paragraph = "Hello Guys " \
            "What's up " \
            "Good Morning " \
            "Have a nice day"
print(paragraph)

#dividepara2
paragraph1 = """ Group No 01 
              Malsha 
              Mihiri  
              Tharindu """
print(paragraph1)


#wordspaces
word1 = "Super"
word2 = "Man"

print(word1 + word2)
print(word1 + " " + word2)
print(word1, word2)

#lettrnum
word3 = "white kite"
a = word3[1]

print(a)
#OR
print(word3[1])

print(word3[0:5])
print(word3[-4:10])
print(word3[:5])
print(word3[6:])

#rstrip
word4 = "Java  "
print(len(word4))
y = word4.rstrip()
print(len(y))

#lstrip
word5 = "  Java"
print(len(word5))
x = word5.lstrip()
print(len(x))

#strip
word6 = "............Java.........."
print(len(word6))
z = word6.strip(".")
print(len(z))

#startswith

word7 = "Python"
word8 = "Python Programming"
word9 = "Java"
word10 = "Java Programming"

print(word7.startswith("P"))
print(word8.startswith("P"))
print(word9.startswith("P"))
print(word10.startswith("P"))

#endswith

print(word7.endswith("n"))
print(word8.endswith("n"))
print(word9.endswith("a"))
print(word10.endswith("a"))