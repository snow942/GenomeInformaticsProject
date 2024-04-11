#Ryan Snow
#New Code

file_in = open ('Wolbachia_Genome.txt', 'r')
file_out = open ('RyanSnow_GenomeInformatics.txt', 'w')
#Reads in the Wolbachia Genome and creates an output file

file_out.write ("Ryan Snow \nGenome Informatics Code \n \n")

content = file_in.read ()

LL = []
LL = content.splitlines ()

#print (LL)
seq = ""
seq = seq.join (LL)
#print (len (seq))
#print (seq)
#seq = content.strip ()
#Removes all 'whitespace' from the sequence

#print (seq)

count = -1
cviaII = "CATG"
fatI = "CATG"
out = []
out2 = []
out3 = []

position = 0
position2 = 0
#A placeholder for the position values

while position < len(seq)+ 200:
    position = seq.find(cviaII, position)

    position2 = seq.find(fatI, position2)
    position2 +=1
    #Looks for the position of the restriction enzyme

    if position == -1:
        break

    out.append (position)
    out.append (position2)
    out2.append (position)
    out3.append (position2)
    #Adds position of restriction enzyme to list
    position += 1
    position2 += 1

#seq = seq.replace ('CATG', "|CATG")
#seq = seq.replace ('CATG', "|CATG")    
#print (seq)

x = 0
remake = []
#Placeholder to remake the nucleotide list 'seq'

while x <= len (seq):
    if x in out:
        remake.append ('|')
    #Makes all occurrences of the restriction enzymes |
        
    else:
        remake.append ('-')
    #Makes all other occurrences -
        
    x+=1
    
    #if x == len (seq) or y > len (out):
        #break
    #When the length of the sequence is reached, stop the program

remake.insert (0,0)
#Adds a 0 at the 0 position in the list

new_seq = str(remake)
#Turns the list of - and | into a string

new_seq = new_seq.replace (',', '').replace ('\'','').replace (' ','').replace ('[','').replace (']','')
#Replaces and removes all unwanted instances in the list


a=0
b=0
remake2 = []
#Placeholder to remake the nucleotide list 'seq'

for z in seq:
    if a == int (out2[b]):
        remake2.append ('S')
        b+=1
    #Makes all occurrences of the restriction enzymes |
        
    else:
        remake2.append ('-')
    #Makes all other occurrences -
        
    a+=1
    if a == len (seq) or b == len (out2):
        break
    #When the length of the sequence is reached, stop the program

remake2.insert (0,0)
#Adds a 0 at the 0 position in the list

new_seq2 = str(remake2)
#Turns the list of - and | into a string

new_seq2 = new_seq2.replace (',', '').replace ('\'','').replace (' ','').replace ('[','').replace (']','')
new_seq2 = new_seq2.replace ('S-----','CviaII')
new_seq2 = new_seq2.replace ('-', ' ')
new_seq2 = new_seq2.replace ('S','CviaII')
#Replaces and removes all unwanted instances in the list


j=0
k=0
remake3 = []
#Placeholder to remake the nucleotide list 'seq'

for z in seq:
    if j == int (out3[k]):
        remake3.append ('R')
        k+=1
    #Makes all occurrences of the restriction enzymes |
        
    else:
        remake3.append ('-')
    #Makes all other occurrences -
        
    j+=1
    if j == len (seq) or k == len (out3):
        break
    #When the length of the sequence is reached, stop the program

remake3.insert (0,0)
#Adds a 0 at the 0 position in the list

new_seq3 = str(remake3)
#Turns the list of - and | into a string

new_seq3 = new_seq3.replace (',', '').replace ('\'','').replace (' ','').replace ('[','').replace (']','')
new_seq3 = new_seq3.replace ('R---','FatI')
new_seq3 = new_seq3.replace ('-', ' ')
new_seq3 = new_seq3.replace ('R','FatI')
#Replaces and removes all unwanted instances in the list


start = 1
end = 51
#Start and end of each line (length)
integer = 50
#Placeholder for int line size (How much each line will increase by)

while start <= len (new_seq):
    file_out.write (str(start) + "\t" + new_seq2 [start:end] + "\n")
    file_out.write (str(start) + "\t" + new_seq3 [start:end] + "\n")
    file_out.write (str(start) + "\t" + new_seq [start:end] + "\n")
    print (str(start) + "\t" + new_seq2 [start:end])
    print (str(start) + "\t" + new_seq3 [start:end])
    print (str(start) + "\t" + new_seq [start:end])
    start += integer
    end += integer
#Prints the sequence 50 characters at a time

len_new_seq = len (new_seq) - 1
#Removes the additional length character caused by inserting the 0 at the 0 position

print ("\nThe length of the genome is " + str(len_new_seq) + ".")
file_out.write ("\nThe length of the genome is " + str(len_new_seq) + " base pairs.")
#Prints the length of the genome

out_new = []
for i in out:
    out_new.append(i + 1)
#Adjusts the list of cuts for the 0 added at the 0 position

print ("\n")
print (out_new)
file_out.write ("\n")
file_out.write (str(out_new))
#Prints the list of cuts

file_out.write ("\n \nThere are " + str(len (out_new)) + " possible cuts in the sequence above.")
print ("\n")
print ("There are " + str(len (out_new)) + " possible cuts in the sequence above.")
#Prints the number of cuts

    
file_out.close ()
