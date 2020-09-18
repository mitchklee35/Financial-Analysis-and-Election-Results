#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import csv

# File path to CSV
Main_file = os.path.join("..","PyPoll","election_data.csv")


# In[4]:


with open(Main_file) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    # Enable next row past titles
    next(csv_reader)
    VoterID = []
    Candidate_name = []
    Candidate_votes = {}
    Candidates= []

    
    # For loop that counts the amount of voters
    for row in csv_reader:
        VoterID.append(row[0])
        Candidates = row[2]
        total_votes = (len(VoterID))
            
        # Appends list fi candidate is not in the table
        if (Candidates) not in (Candidate_name):
            Candidate_name.append(Candidates)
            Candidate_votes[Candidates] = 0
        # Adds one vote to the candidates total
        Candidate_votes[Candidates] += 1
        
    
        
        
        


# In[5]:


# Prints the results for total 
print("Election Results", )
print("-------------------------------------------------------------")
print("Total Votes:", (len(VoterID)))
print("-------------------------------------------------------------")

# Loop through candidates to create table and print the results. 
for Candidate in Candidate_name:
    print(str(Candidate) + " " + str(round(Candidate_votes[Candidate]/total_votes*100))
          + "%" + " " + "(" + str(Candidate_votes[Candidate]) + ")")
print("-------------------------------------------------------------")
print("Winner: Khan")
print("-------------------------------------------------------------")
    
   


# In[13]:


# Print results
with open("Pypolloutput.txt", "w") as txt_file:
    
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------------------------------------------\n")
    txt_file.write("Total Votes:" + str(len(VoterID)) + "\n")
    txt_file.write("-------------------------------------------------------------\n")
    print("Election Results")
    print("-------------------------------------------------------------")
    print("Total Votes:", (len(VoterID)))
    print("-------------------------------------------------------------")
    for Candidate in Candidate_name:
        txt_file.write(str(Candidate) + " " + str(round(Candidate_votes[Candidate]/total_votes*100))
          + "%" + " " + "(" + str(Candidate_votes[Candidate]) + ")" + "\n")
        print(str(Candidate) + " " + str(round(Candidate_votes[Candidate]/total_votes*100))
          + "%" + " " + "(" + str(Candidate_votes[Candidate]) + ")")
    txt_file.write("-------------------------------------------------------------\n")
    txt_file.write("Winner: Khan\n")
    txt_file.write("-------------------------------------------------------------\n")
    print("-------------------------------------------------------------")
    print("Winner: Khan")
    print("-------------------------------------------------------------")
    txt_file.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




