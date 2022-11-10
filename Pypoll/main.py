import csv

input_file = '/Users/sandhyaranidatla/Desktop/NU-VIRT-DATA-PT-10-2022-U-LOLC/repositories/python-challenge/Pypoll/Resources/election_data.csv'

# CSV file has 3 columns: 'Voter ID', "County", "Candidate"
# Initialising empty lists to be used later on
election_list = []
candidates_list = []
# Open csv file in default read mode with context manager
with open(input_file, newline="", encoding="utf-8") as election:

    # Store the contents of budget_data.csv in a variable
    reader = csv.DictReader(election, delimiter=",")

    for row in reader:
        election_list.append(row)

    # Getting the list of candidates who received votes
    for vote in range(len(election_list)):
        for key in election_list[vote]:
            candidates_list.append(election_list[vote]['Candidate'])

# Getting the unique and sorted list
unique_candidates = sorted(list(set(candidates_list)))

candidate_1_votes = 0
candidate_2_votes = 0
candidate_3_votes = 0

# Looping through the list of dictionaries, and plus one vote if matches the candidate
for vote in election_list:
    if vote['Candidate'] == unique_candidates[0]:
        candidate_1_votes += 1
    elif vote['Candidate'] == unique_candidates[1]:
        candidate_2_votes += 1
    else:
        candidate_3_votes += 1

# Creating a final dictionary of candidate with votes.
final_dict = {unique_candidates[0]: candidate_1_votes, unique_candidates[1]: candidate_2_votes, unique_candidates[2]: candidate_3_votes}

# Print statements
print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(election_list)}")
print("-------------------------")
print(f"{unique_candidates[0]}: {round(candidate_1_votes / len(election_list) * 100, 3)}% ({candidate_1_votes})")
print(f"{unique_candidates[1]}: {round(candidate_2_votes / len(election_list) * 100, 3)}% ({candidate_2_votes})")
print(f"{unique_candidates[2]}: {round(candidate_3_votes / len(election_list) * 100, 3)}% ({candidate_3_votes})")
print("-------------------------")
print(f"Winner: {max(final_dict, key=final_dict.get)}")
print("-------------------------")

# Output files
output_file = "/Users/sandhyaranidatla/Desktop/NU-VIRT-DATA-PT-10-2022-U-LOLC/repositories/python-challenge/Pypoll/analysis/output1.txt"

with open(output_file, "w") as file:
    # Write methods to print to Election_Summary
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {len(election_list)}\n")
    file.write("-------------------------\n")
    file.write(f"{unique_candidates[0]}: {round(candidate_1_votes / len(election_list) * 100, 3)}% ({candidate_1_votes})\n")
    file.write(f"{unique_candidates[1]}: {round(candidate_2_votes / len(election_list) * 100, 3)}% ({candidate_2_votes})\n")
    file.write(f"{unique_candidates[2]}: {round(candidate_3_votes / len(election_list) * 100, 3)}% ({candidate_3_votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {max(final_dict, key=final_dict.get)}\n")
    file.write("-------------------------\n")
