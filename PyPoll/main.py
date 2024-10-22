
"""PyPoll Homework."""

# dependencies
import csv
from pathlib import Path

# files to import & export
file_to_load = Path("Resources/election_data.csv")  
file_to_output = Path("analysis/election_analysis.txt") 

# initial variables to track
total_votes = 0
candidates = [] # list of candidates
votes_stockham = 0
votes_degette = 0
votes_doane = 0

# open & read the csv
with open(file_to_load, 'r', encoding='utf-8') as election_data:
    reader = csv.reader(election_data)
    
    # skip the column titles
    header = next(reader)
    
    # loop over all rows
    for row in reader:
        
        # add to the total number of votes
        total_votes += 1 

        # track new candidate names
        if row[2] not in candidates:
            candidates.append(row[2])
            # after looping over all rows, this "candidates" list will return three names - so we'll deal with them individually in the next part.

        # track each candidate's votes
        if row[2] == "Charles Casper Stockham":
            votes_stockham += 1
        elif row[2] == "Diana DeGette":
            votes_degette += 1
        elif row[2] == "Raymon Anthony Doane":
            votes_doane += 1
    
    # track each candidate's percentage of total votes
    percent_stockham = (votes_stockham / total_votes) * 100
    percent_degette = (votes_degette / total_votes) * 100
    percent_doane = (votes_doane / total_votes) * 100

    # find winner of election
    winner = max([votes_degette, votes_doane, votes_stockham])
    if winner == votes_degette:
        winner_name = "Diana DeGette"
    elif winner == votes_stockham:
        winner_name = "Charles Casper Stockham"
    elif winner == votes_doane:
        winner_name = "Raymon Anthony Doane"

# save all this info in the output
output = f"""
        Election Results
        -------------------------
        Total Votes: {total_votes}
        -------------------------
        Charles Casper Stockham: {round(percent_stockham,3)}% ({votes_stockham})
        Diana DeGette: {round(percent_degette,3)}% ({votes_degette})
        Raymon Anthony Doane: {round(percent_doane,3)}% ({votes_doane})
        -------------------------
        Winner: {winner_name}
        -------------------------"""

# print to terminal
print(output)

# output the results in a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

# update the user
print("""

        The above results have been saved in the analysis folder.
        
     """)