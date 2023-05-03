global gap_work
global compare_work
# Program to find all possible alignments of a pair of strings when adding
# gaps to the shorter string

# Given:  Two strings of nucleotides
# Find:  All possible alignments when adding gaps to the shorter string


# Function to create a list of all ways one gap can be inserted into
# a string.  The input is a string, the output is a list of strings
# with a gap inserted into all positions of the input string

def insertOneGap(strng,gap_work):
    alignments = []
    for i in range(len(strng)):
        newStrng = strng[0:i] + '-' + strng[i:len(strng)]
        alignments = alignments + [newStrng]
        gap_work = gap_work + 1
    alignments = alignments + [strng + '-']
    return alignments,gap_work
            
# Function to take a set union of a pair of lists
# This is used to eliminate any duplicates in the list when they are combined
def Union(list1, list2):
    for a in list2:
        if a not in list1:
            list1 = list1 + [a]
    return list1


# Function to create all possible alignments of a string with a certain number
# of gaps inserted
def insertAllGaps(strng, gaps,gap_work):
    # List of alignments starts with the initial string
    alignments = [strng]

    # Loop to insert one gap at a time
    for i in range(gaps):

        # Initialize list of new alignments with i gaps in the string
        newAlignments = []

        # For every string in the list of alignments
        for st in alignments:
            # Insert one gap in each alignment in the list
            al,gap_work = insertOneGap(st,gap_work)

            # Add the new alignment to the list of new alignments being created
            newAlignments = Union(newAlignments,al)

        # The alignments list now becomes the new alignments list to now
        # add another gap to each of the alignments in the new list
        alignments = newAlignments
    return alignments,gap_work

# Function to compute the scores for all alignments compared to another string
# Gap score = -1; Match score = 1; Mismatch score = 0
# def computeScores(st, alignments):
#     return scores

#   Make a list that goes through the alighments and if char[i] = char2[i] scores +2
#   If char[i] != char2[i] scores -2
#   If char2[i] == '-' score -1

#for str in alignments:
#           for char in st:

# for char in st:
           # for str in alignments:

                
def computeScores(st,alignments,compare_work):
    scores = []
    p = 0
    for str in alignments:
        score = 0
        j = 0
        for char in str:
            if st[j] == char:
                score = score + 2
            if char == '-':
                score = score - 1
            elif st[j] != char:
                score = score - 2
            j = j + 1
            compare_work = compare_work + 1
        if p == 0:
            highest = 0
            highest = score
        if score > highest:
            highest = score
        scores.append(score)
        p = p + 1
    return scores, highest, compare_work

# Function to print all of the alignments along with the score for
# each alignment

def printResults(st, alignments,scores,highest,compare_work,gap_work):
    print("There are ", len(alignments), " alignments")
    print('The following alignments are optimal:')
    for i in range(len(alignments)):
        if scores[i] == highest:
            print(st)
            print(alignments[i])
            print('Score = ',scores[i])
            print(" ")

    print('Amount of work done (gaps): ' , gap_work)
    print('Amount of work done (comparisons): ', compare_work)
    return
        
# Main function
def main():
    gap_work = 0
    compare_work = 0
    # Get the two strings to align
    str1 = input("Enter string 1: ")
    str2 = input("Enter string 2: ")


    # Compute alignments adding gaps to the shorter string
    if len(str1) > len(str2):
        longStr = str1
        shortStr = str2
    else:
        longStr = str2
        shortStr = str1
    
    alignments,gap_work = insertAllGaps(shortStr,len(longStr)-len(shortStr),gap_work)
    scores,highest,compare_work = computeScores(longStr,alignments,compare_work)
    printResults(longStr,alignments,scores,highest,compare_work,gap_work)
