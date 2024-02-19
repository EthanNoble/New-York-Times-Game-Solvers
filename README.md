# Purpose
You can use these suite of tools to solve the many New York Times game! This project is obviously intended to be a fun way to learn more about problem solving with programming and not intended to just aimlessly cheat at these games (what's the point of doing that!?). Eventually I want to write a solver for every NYT game that's possible to solve programmatically!

# Wordle Solver
Under the wordle folder, you can run the wordle_solver.py script with the required -w and -r command line arguments. -w is used to specify the list of words that you have already played on the Wordle board, and -r is used to specify the rule sets (green, yellow, or black) corresponding to each word. An example use case is given below:

## Use Case
Lets say that you just played the first word 'audio' and your Wordle board looks like this:

<img width="314" alt="audio" src="https://github.com/EthanNoble/New-York-Times-Game-Solvers/assets/58098861/78ef2ea6-36c1-4dcd-b554-e49157ac2239">

As you can see D is green and I is yellow. A, U, and O are grey (specified as black in this program). This forms the ruleset 'bbgyb' that you specify to wordle_solver.py with -r:

```python wordle_solver.py -w audio -r bbgyb```

You also specify the word 'audio with -w. Running the above command gives you the following output:

```
Found 57 possible solution words.
Words: {'hidel', 'bidry', 'widen', 'midst', 'eider', 'widdy', 'midis', 'sides', 'hides', 'hided', 'tiddy', 'fidel', 'indin', 'kiddy', 'fidge', 'tided', 'riden', 'bides', 'indri', 'indef', 'rider', 'index', 'indic', 'sidhe', 'ridge', 'sider', 'tides', 'igdyr', 'sidth', 'nides', 'biddy', 'rides', 'indyl', 'nidge', 'wides', 'midge', 'hider', 'sided', 'giddy', 'bidri', 'middy', 'nided', 'midgy', 'mider', 'wider', 'fides', 'cider', 'indiv', 'width', 'indew', 'ridgy', 'bided', 'bider', 'bidet', 'indii', 'vidry', 'sidle'}
```

Every word that was outputted to the console is a valid 5 letter word that conforms to the ruleset specified and is thus a valid next word to play. Keep in mind not every word might be playable if it's not in the NYT's dictionary of playable words.

Let's choose 'cider' from this list of words. This gives us the next board:

<img width="314" alt="cider" src="https://github.com/EthanNoble/New-York-Times-Game-Solvers/assets/58098861/1c10feb7-5847-44fb-8602-9ef76c9198dd">

Great! Let's specify the next ruleset. Remember to keep the previous word and ruleset in the command:

```python wordle_solver.py -w audio cider -r bbgyb bggyy```

As you play more words, you will keep appending new words and rulesets to this command. Running the above command gives us the following output:

```
Found 1 possible solution words.
Words: {'ridge'}
```

And since there is only one word in the entire english dictionary of five-letter words that matches our rulesets, it must be the correct word! Playing 'ridge' wins the game!

<img width="314" alt="ridge" src="https://github.com/EthanNoble/New-York-Times-Game-Solvers/assets/58098861/11524a94-b5ed-4bf1-875d-bc74cecfe52a">
