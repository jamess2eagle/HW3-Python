import os
import csv


votes = 0
candidates = []
votecount = {}

#join file
csvpath = os.path.join("election_data.csv")

#read the file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=(','))
    csvheader = next(csvreader)
    #increase vote counts for each row
    for row in csvreader:
        votes += 1
        #update candidates list
        if row[2] not in candidates:
            candidates.append(row[2])
            votecount[row[2]] = 0
        #update the vote counts for each candidate
        for candidate in candidates:
            if row[2] == candidate:
                votecount[row[2]] += 1


#sort by the vote count
sortvotecount = sorted(votecount.items(), key=lambda x: x[1],reverse = True)


print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes}")
print("-------------------------")
for candidate in sortvotecount:
    print(f"{candidate[0]} : {candidate[1] / votes * 100:.3f}% ({candidate[1]})")
print("-------------------------")
print(f"Winner: {sortvotecount[0][0]}")
print("-------------------------")


with open("output.txt", "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {votes}\n")
    file.write("-------------------------\n")
    for candidate in sortvotecount:
        file.write(f"{candidate[0]} : {candidate[1] / votes * 100:.3f}% ({candidate[1]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {sortvotecount[0][0]}\n")
    file.write("-------------------------\n")

