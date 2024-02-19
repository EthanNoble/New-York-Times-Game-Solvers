# Purpose
You can use these suite of tools to solve the many New York Times game! This project is obviously intended to be a fun way to learn more about problem solving with programming and not intended to just aimlessly cheat at these games (what's the point of doing that!?).

# Wordle Solver
Under the wordle folder, you can run the wordle_solver.py script with the required -w and -r command line arguments. -w is used to specify the list of words that you have already played on the Wordle board, and -r is used to specify the rule sets (green, yellow, or black) corresponding to each word. An example use case is given below:

## Use Case
Lets say that you just played the first word 'audio' and your Wordle board looks like this:

<img width="314" alt="audio" src="https://github.com/EthanNoble/New-York-Times-Game-Solvers/assets/58098861/78ef2ea6-36c1-4dcd-b554-e49157ac2239">

As you can see D is green and I is yellow. A, U, and O are grey (specified as black in this program). This forms the ruleset that you specify to wordle_solver.py as 'bbgyb':
'''python wordle_solver.py -w audio -r bbgyb'''
