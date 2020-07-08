#First Script

gene_sequence = open("geneSequence.txt", "r")

#set nucleotide vars to 0
a=0;
t=0;
g=0;
c=0;

#skip the first line in the file
gene_sequence.readline()

for line in gene_sequence:
    line = line.lower()
    for char in line:
        if char == "a":
            a+=1
        if char == "t":
            t+=1
        if char == "g":
            g+=1
        if char == "c":
            c+=1

print "numer of a's: " +str(a)
print "numer of t's: " +str(t)
print "numer of g's: " +str(g)
print "numer of c's: " +str(c)

# 0. = cpnvert to floting point
gc= (g+c+0.) / (a+t+c+g+ 0.)

print "GC content: " + str(gc)
