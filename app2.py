import os
from random import randint

for i in range(1, 365):
    for j in range(randint(1, 10)):  # Simplified loop initialization
        date_string = f"{i} days ago"  # Using f-string for readability
        
        # Append the date_string to 'file.txt'
        with open('file.txt', 'a') as file:
            file.write(date_string + "\n")  # Added newline for better formatting

        # Execute Git commands to create a commit with a specific date
        os.system('git add .')
        os.system(f'git commit --date="{date_string}" -m "commit"')

# Push the commits to the remote repository
os.system('git push -u origin main')
