# operations and numbers 
# connor ter stege 
# 5 nov 25 

###  Version 1
    # create an algorithm to gather data to find the most popular bubble tea place around us
    # choices are: 
    # ask the user for their favorite bubble tea place
    # store the responses in a list
    # give a raw score for each place
    # give scores as percentages based on the number of responses for each place

def vote_listed_choices():     
    choices = ["A. Coco", "B. Chatime", "C. Bubble waffle", "D. gong cha"] 
    print("Vote for your favorite bubble tea place from the following list:")
    print("Give the letter of your choice: ")
    for choice in choices: # its simpler this way imo 
        print(choice)
    votes = []
    for i in range(10):
        vote = input(f"User {i+1}, enter your choice: ").upper().strip(".!?/,';:") 
        votes.append(vote)
    tally = {choice[0]: 0 for choice in choices} 
    for vote in votes:
        if vote in tally:
            tally[vote] += 1
    total_votes = len(votes)
    print("\nResults:") 
    for choice in choices:
        letter = choice[0]
        count = tally[letter]
        percentage = (count / total_votes) * 100
        print(f"{choice}: {count} votes ({percentage:.2f}%)") 

vote_listed_choices()
    
### Version 2
    # ask the user what their favorite bubble tea place is
    # add their response to a list
    # give raw scores for each place
    # gve scores as percentages based on the number of responses for each place

def main(): 
    pass 

if __name__ == "__main__":
    main()


 
