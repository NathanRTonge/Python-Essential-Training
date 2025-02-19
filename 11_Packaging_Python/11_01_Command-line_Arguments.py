"""
Contains info on command line arguments
"""
from argparse import ArgumentParser

# Creates parser object that can parse the different arguments put in
parser = ArgumentParser()

# Adds the argument 'output' for the filename where the output is going
parser.add_argument('--output', '-o', required = True,
                    help= 'Destination file for output of this '
                          'program')
#-- if full word, - if letter
#--help/-h give info in the help='' string
#required means that the argument must be given for the program to run

# Adds argument 'text' for the text we wish to output
parser.add_argument('--text', '-t', required = True,
                    help= 'Text to write to the file')


args = parser.parse_args()

with open(args.output, 'w') as f: #opens filename in 'w'rite mode
    f.write(args.text + '\n')

print(f'Wrote "{args.text}" to file "{args.output}"') #tells us if program was successful