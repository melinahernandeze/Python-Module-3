import os
import csv

output_path = os.path.join("PyPoll","Resources","election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}


with open(output_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Reading the first row (header)
    header = next(csvreader)

    
    # Iterate through each row in the CSV file
    for row in csvreader:
# Count total votes
        total_votes += 1

# Extract candidate name from the row
        candidate_name = row[2]

# Update candidate's votes count
        candidates[candidate_name] = candidates.get(candidate_name, 0) + 1


# Print the Election Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Iterate through candidates and calculate percentage of votes
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

    # Update the winner if needed
    if votes > winner["votes"]:
        winner["name"] = candidate
        winner["votes"] = votes

print("-------------------------")
print(f"Winner: {winner['name']}")
print("-------------------------")

