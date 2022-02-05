# 2048-Game
Here we have created a working replica of 2048 using python and Tkinter.

# Design Principle:

I have used Tkinter for the Graphical user interface. 
We use four moves in the game Left, Right, Up, Down. We will take all the move as left swipe but we will convert it into the various moves using functions; Transpose, Inverse.
We will RIGHT swipe by reversing matrix and performing left Swipe.
We will take UP move by taking transpose then moving left.
We will take DOWN move by taking transpose the moving right.

# Code Walkthrough:

Every step taken in the code is written in comments go through them to understand all the steps.

# Scope of (8 x 8) from (4 x 4)

Intially we can intialize the four tiles randomly with 2 or 4. All the moves can be same as the 4 X 4 only we have to increase the number of rows and columns.
After each move we can add a new tile with 2 or 4 value everytime at the empty cell. We can also set the end number at a higher value.

# End Number as 4096 

We can make a function(in my case **game_over**) where we can check that if any row contains the 4096 then we can display the game over.
