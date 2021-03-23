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

### The algorithm (tentative)
We will search for the first group of consecutive seats of the size of the reservation. 
Then we will check that the location meets the safety requirements. 
Once this is done we will update the seating chart and output the reservation to file `output.txt`. 

### Note: Console Output 
`$python --version`
`Python 3.7.3` 

### To-do
1. ~~Implement seating chart~~
2. ~~Construct `Reservation`~~
3. ~~Implement algorithm~~
4. ~~Fix edge cases and fitting~~
