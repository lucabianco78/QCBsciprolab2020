"""exercises/process_fasta.py"""

import argparse

parser = argparse.ArgumentParser(description="Parses a single-entry fasta file and returns some stats.")
parser.add_argument("inputFasta", type = str, help = "The input fasta file")
parser.add_argument("-S", "--search", type = str, default = "", 
                    help="The (optional) string to look for.")





# Reads a fasta file input_file in 
#and returns the tuple (header, sequence)
def read_sequence(input_file):
    sequence = ""
    hdr = ""
    inF = open(input_file)
    for line in inF:
        line = line.strip()
        if not line.startswith(">"):
            sequence += line
        else:
            hdr = line[1:]

    return hdr,sequence


# Gets a sequence seq and returns 
# a dictionary with the counts of all elements.
# This function also prints off the counts (and %)
def count_chars(seq):
    char_dict = dict()
    L = len(seq)
    for c in seq:
        if char_dict.get(c, None) == None:
            char_dict[c] = 0
        char_dict[c] += 1
    
    print("The sequence has length: {}".format(L)) 
    for el in char_dict:
        print("{} is present {} times ({:.2f} %)".format(el, char_dict[el], 100 * char_dict[el]/L))
    
    return char_dict

# Counts how many times search_s is in seq and returns an integer
def count_str(seq, search_s):
    return seq.count(search_s)
   

args = parser.parse_args()

inFasta = args.inputFasta

search_str = args.search


h,s = read_sequence(inFasta)
print(h)
print(s)
cnts = count_chars(s)

if len(search_str) > 0:
    C = count_str(s, search_str)
    print("Sequence '{}' is present {} times ".format(search_str, C))