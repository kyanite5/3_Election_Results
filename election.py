import os
import csv

csvpath = "election_data.csv"

# open csv file
with open(csvpath, encoding="utf8", newline='') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
   csvhand = csv.reader(csvfile, delimiter=',')
   csv_header = next(csvfile)
   # print(f"CSV Header: {csv_header}")

   # declarations
   voter = [] # list of voter IDs
   candidate = [] # list of candidate names
   count = int() # total number of votes
   count = 0
   percents = [] # repository for calculating percentages of total votes
   d = {} # dictionary with vote totals per candidate

   for row in csvhand:
   # Add voter ID
       voter.append(row[0])
       count = count + 1
   # Add Candidate
       candidate.append(row[2])
   # Get number of votes per candidate ("histogram") and determine the max
   for cand in candidate:
       d[cand] = d.get(cand,0) + 1
       winnum = max(d.values())
       for k, v in d.items():
           if v == winnum:
              winner = k
  # if you don't care about the brackets use print statement below instead of 2nd for
  # print([k for k, v in d.items() if v == winner])

  # Calculate percentages of vote and save to list percents
   for x in d.values():
       pct = (100*x)/count
       pct = round(pct,3)
       percents.append(pct)
   # Create lists of candidates and tallies that is indexable
   cands = list(d.keys())
   tallies = list(d.values())

# Print results to terminal
print("Election Results")
print("-------------------------")
print("Total Votes: ", count)
print("-------------------------")
print(cands[0], ":", percents[0], "%", "(", tallies[0], ")")
print(cands[1], ":", percents[1], "%", "(", tallies[1], ")")
print(cands[2], ":", percents[2], "%", "(", tallies[2], ")")
print(cands[3], ":", percents[3], "%", "(", tallies[3], ")")
print("-------------------------")
print("Winner: ", winner)

# print to text file
import sys

sys.stdout = open('output_poll.txt','w')
print("Election Results")
print("-------------------------")
print("Total Votes: ", count)
print("-------------------------")
print(cands[0], ":", percents[0], "%", "(", tallies[0], ")")
print(cands[1], ":", percents[1], "%", "(", tallies[1], ")")
print(cands[2], ":", percents[2], "%", "(", tallies[2], ")")
print(cands[3], ":", percents[3], "%", "(", tallies[3], ")")
print("-------------------------")
print("Winner: ", winner)
