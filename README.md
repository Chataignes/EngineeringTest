# EngineeringTest

## Solution1 is implemented in python 3.8.6
- Place solution1.py in the "Engineering Test Files" folder
- Run `python3 solution1.py` in terminal or use any IDE(such as pycharm)
- "Combined.csv" will be generated in the same location
- Wasn't sure if the result file needs to be sorted in IP address. If that's the case I would read the files and store value into a dictionary where {key = IP : value = Env}, sort with the key and write values back to output file.
 
## Solution 2
- Run `npm install request, nedb` in terminal
- Run `node solution2.js`
- The public API gets a random person's information record each time we call the script and print out the full name that got added to the database. It will also show the existing people's full name in the database.
- The database will be stored in `db/info.db`

