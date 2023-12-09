# COMP-1510-202330-Lab-07

Every program needs a README.md

This is written in markdown. Read about markdown here: [markdowncheatsheet](https://www.markdownguide.org/cheat-sheet/)

## Your name:

Xinli Wang

## Your student number:

A01358184

## Your GitHub username:

ShirleyXW

## Any important comments you'd like to make about your work:

Element required show up(only one or two of each element were selected to fill in the following table  ):

| Element name             | Line                       |
|--------------------------|----------------------------|
| Save player data         | sync_users_data.py         |
| List Comprehension       | game.py 91                 |
| Dictionary Comprehension | map.py 283                 |
| if_statements            | game.py 188, 274, 317, etc |
| while_loop               | game.py 642                |
| for_loop                 | game.py 89                 |
| for_loop                 | map.py 167                 |
| membership               | game.py 363                |
| range                    | map.py 167                 |
| itertools.count()        | game.py 87                 |
| random                   | game.py 92                 |


## Game Description:

***Welcome to the Adventure Classroom: The Quest for Super Teaching!***

Embark on an educational journey through a mysterious map filled with challenges and classes. As a teacher seeking to
become a Super Teacher, you'll navigate through classrooms, teach classes, and answer questions to gain experience. 
The ultimate goal is to reach the boss room and achieve the prestigious title of `Super Teacher`.

Your teacher's success depends on your strategic movement, intelligence, and the ability to answer questions correctly. 
Classes may proceed automatically, but your choices impact your teacher's progress. Level up by accumulating experience 
points, and don't forget to check your teacher's information regularly.

Navigate through the map, teach classes, and face the boss room challenge. Will you become the ultimate Super Teacher,
or will your journey end prematurely? The Adventure Classroom awaits!

Good luck on your quest for Super Teaching!


### User Manual:

1.  Starting the Game:
    -   Run the Python script `game.py` to start the game.
    -   You will be prompted to load an existing teacher or create a new one.
        Gamer name is case-sensitive. Make sure the name of character keeps consistent. 
        Otherwise, a new character will be created

2.  Game Interface:

    Use the following commands during the game:
    -   Movement: `n` (north), `s` (south), `e` (east), `w` (west)
    -   Start Class: `x`
    -   Answer Question: `a`, `b`, `c`, or `d`
    -   Check Character Info: `i`
    -   View Map: `m`
    -   Exit Game: `q`

3. Objective:
    -   Explore the map, teach classes, and answer questions to gain experience.
    -   Level up by accumulating experience points.
    -   Reach the boss room and become a Super Teacher.

4.  Classes:
    -   Enter classrooms (`x`) to start a class.
    -   Classes may proceed automatically based on your teacher's intelligence.
    -   If not, answer a question to complete the class.

5.  Questions:
    -   Questions are multiple-choice (A, B, C, or D).
    -   Answer correctly to gain experience.
    -   Incorrect answers result in health loss.

6.  Character Information:
    -   Check your teacher's health, level, intelligence, and experience using `i`.

7.  Map:
    -   View the map and your current location using `m`.
    -   See your location `(▀n▀)/` in the map.

8.  Exiting the Game:
    -   Exit the game using `q`.
    -   Your progress is saved automatically.

9.  Game Over:
    -   The game ends if your health reaches zero.
    -   Each teacher (username) has only one opportunity.
        If unsuccessful, restart the script to begin a new teaching adventure with a different teacher name.

Notes:
- Additional bonus on central garden `location:(2,2)` when gamer first visits.
