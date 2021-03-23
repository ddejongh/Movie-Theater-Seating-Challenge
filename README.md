# Movie Theater Seating Challenge

### Overview
In this project, we will implement an algorithm that assigns seats to fulfill reservation requests. 
The movie theater has a seating arrangement of 10 rows of 20 seats. 

We must maximize customer safety and satisfaction in alignment with the following requirements:
- There must be a buffer of three seats in between reservations 
- There must be a buffer of at least one row in between reservations 

### Assumptions
We will make the following assumptions:
- Customers have no row preference
- A diagonal distance of one row is sufficient spacing
- End of rows are enough for empty spaces 
- Reservation list is static 
- Input files do not need error handling 
- Reservations are limited to available spaces in the theater  

### The Algorithm (tentative)
After initial planning, we will be implementing a first fit method. 
We will search for the first group of consecutive seats of the size of the reservation. 
Then we will check that the location meets the safety requirements. 
Once this is done we will update the seating chart and output the reservation to file `output.txt`. 

### Note: Console Output 
`$python --version`
`Python 3.7.3` 

### Execution Instructions 
- Run: `python3 movies.py [input-file-path]`
- OR: `python movies.py [input-file-path]`

### To-do
1. ~~Implement seating chart~~
2. ~~Construct `Reservation`~~
3. ~~Implement algorithm~~
4. Fix skip cases 

### Future plans
1. Implement backtracking to ensure optimal fit 
2. Refactor functions for readability and modularity 
3. Maximize customer satisfaction by removing row preference assumption
4. Add preference seating 