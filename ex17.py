#ex17 more files

#import 2 more packages
from sys import argv
from os.path import exists

# set 2 variables to argv arguement
script, from_file, to_file = argv

#display what following code is doing
print(f"Copying from {from_file} to {to_file}.")

# we could do these two on one line, too. How?
#Open old file from ex16_sample 
ex16_txt = open(from_file)
indata = ex16_txt.read()

# display the outcome (use f formatted variable is easier)
print(f"The input file is {len(indata)} bytes long")

# display output outcome
print(f"Does the output exist? {exists(to_file)}")

# display some options
print("Ready, hit RETURN to continue, CTRL-C to abort." )
input()

#create a file
output = open(to_file, 'w')
output.write(indata)

#display the process
print("Alright, all done!")

output.close()
ex16_txt.close()


