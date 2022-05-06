import os
import csv

#locate the source data file
electiondata = os.path.join("Resources", "election_data.csv")
#
# Variables to store  candidate and respective votes and %
# We know there are only 4 candidates in this election and their names
#
TotalVotes=0
Candidate1="Khan"
Candidate2="Correy"
Candidate3="Li"
Candidate4="O'Tooley"
Candidate1_VotesCnt=0
Candidate3_VotesCnt=0
Candidate2_VotesCnt=0
Candidate4_VotesCnt=0
InformalVotes=0
WinningVoteCnt=0
Winner=""
Candidate1_percentage =0.000
Candidate2_percentage =0.000
Candidate3_percentage =0.000
Candidate4_percentage =0.000

# Use encoding for Windows
with open(electiondata, newline='\n', encoding='utf-8') as csvfile:
    #
    #Loop through every row of data skipping the first line which is the header
    #
    header=next (csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        #Count all votes as we go along
        TotalVotes=TotalVotes+1
        #
        #Tally up the votes for each candidate who we know beforehand
        #
        if row[2]   == Candidate1:
            Candidate1_VotesCnt = Candidate1_VotesCnt + 1
        elif row[2] ==Candidate2:
            Candidate2_VotesCnt = Candidate2_VotesCnt + 1
        elif row[2] == Candidate3:
            Candidate3_VotesCnt = Candidate3_VotesCnt + 1
        elif row[2] == Candidate4:
            Candidate4_VotesCnt = Candidate4_VotesCnt + 1
        else:
            InformalVotes=InformalVotes+1
    #
    #Now see who got the most votes and hence the winner
    #
    if Candidate1_VotesCnt > WinningVoteCnt:
      Winner=Candidate1
      WinningVoteCnt=Candidate1_VotesCnt
    if Candidate2_VotesCnt > WinningVoteCnt:
      Winner=Candidate2
      WinningVoteCn2=Candidate2_VotesCnt
    if Candidate3_VotesCnt > WinningVoteCnt:
      Winner=Candidate3
      WinningVoteCnt=Candidate3_VotesCnt
    if Candidate4_VotesCnt > WinningVoteCnt:
      Winner=Candidate4
      WinningVoteCnt=Candidate4_VotesCnt

    Candidate1_percentage = round(Candidate1_VotesCnt/TotalVotes*100,3)
    Candidate2_percentage = round(Candidate2_VotesCnt/TotalVotes*100,3)
    Candidate3_percentage = round(Candidate3_VotesCnt/TotalVotes*100,3)
    Candidate4_percentage = round(Candidate4_VotesCnt/TotalVotes*100,3)
    

#output the  results to the console

# Write the header row
    print ("")
    print ("Election Results" )
    print ("------------------------" )
    print ("Total Votes: " + str(TotalVotes) )    
    print ("------------------------" )
    print (Candidate1 +":     " +  str(Candidate1_percentage)+"% (" + str(Candidate1_VotesCnt)+")" )
    print (Candidate2 +":   " +  str(Candidate2_percentage)+"% (" + str(Candidate2_VotesCnt)+")" )
    print (Candidate3 +":       " +  str(Candidate3_percentage)+"% (" + str(Candidate3_VotesCnt)+")" )
    print (Candidate4 +": " +  str(Candidate4_percentage)+"% (" + str(Candidate4_VotesCnt)+")" )
    print ("-----------------------" )
    print ("Winner is " + Winner )
    print ("-----------------------" )  
    #
    #print ("Check if there are any votes for none of the 4 known candidates.")
    #print ("Check on Total Votes for all 4 candidates counted (must equal Total Votes above): " + str(Candidate1_VotesCnt + Candidate3_VotesCnt + Candidate2_VotesCnt + Candidate4_VotesCnt))   
    #print ("Informal Votes " + str(InformalVotes)) 
    #print ("Check on % Votes for 4 known candidates must equal 100.00% :     " + str(Candidate4_percentage + Candidate3_percentage + Candidate1_percentage + Candidate2_percentage)) 
#  Set variable for output file
output_file = os.path.join("analysis","ElectionResults.txt")

# #  Open the output file
newline="\n"
with open(output_file, "w") as datafile:
    # Write the header row
    datafile.write ("")
    datafile.write ("Election Results"+newline)
    datafile.write ("------------------------"+newline)
    datafile.write ("Total Votes: " + str(TotalVotes)+newline)    
    #datafile.write ("Check on Total Votes: " + str(Candidate1_VotesCnt + Candidate3_VotesCnt + Candidate2_VotesCnt + Candidate4_VotesCnt))   
    #datafile.write ("Check on % Votes:     " + str(Candidate4_percentage + Candidate3_percentage + Candidate1_percentage + Candidate2_percentage)) 
    datafile.write ("------------------------"+newline)
    datafile.write (Candidate1 +":     " +  str(Candidate1_percentage)+"% (" + str(Candidate1_VotesCnt)+")"+newline)
    datafile.write (Candidate2 +":   " +  str(Candidate2_percentage)+"% (" + str(Candidate2_VotesCnt)+")"+newline)
    datafile.write (Candidate3 +":       " +  str(Candidate3_percentage)+"% (" + str(Candidate3_VotesCnt)+")"+newline)
    datafile.write (Candidate4 +": " +  str(Candidate4_percentage)+"% ("+  str(Candidate4_VotesCnt)+")"+newline)
    datafile.write ("-----------------------"+newline)
    datafile.write ("Winner is " + Winner + newline)
    datafile.write ("-----------------------"+newline)  
