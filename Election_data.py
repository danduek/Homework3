import csv
import os
import collections

pollDataCSV = os.path.join (".","Resources","election_data.csv")

with open(pollDataCSV, "r", encoding="UTF-8", newline="\n") as data:
    csvData = csv.reader(data,delimiter=",")
    ignore_headers = next(csvData)

    total_votes = 0
    votes_by_cand = []
    candidate_votes = {}

    for row in csvData:
        total_votes += 1

        name = row[2]
        if name in candidate_votes:
            candidate_votes[name] += 1
        else:
         candidate_votes[name] = 1
vote_counts = '\n'
for key in candidate_votes.keys():
    percent_of_total = (candidate_votes[key] / total_votes) * 100
    percent_of_total = round( percent_of_total, 3 )
    vote_counts += f'   {key}: {percent_of_total}% ({candidate_votes[key]}) \n'
    votes_by_cand.append(candidate_votes[key])

max_votes = max(votes_by_cand)
max_index = votes_by_cand.index(max_votes)
candidate_names = list(candidate_votes.#keys())
winner = candidate_names[max_index]

    report = f'''
        Election Results
    ____________________________
    Total Votes: {total_votes}
    ____________________________
    {vote_counts}
    ____________________________
    Winner: {winner}
    ____________________________
'''

#file1 = open(PyPollReport.txt","W") #write mode
#file1.write(report)
#file1.close()

print(report)
