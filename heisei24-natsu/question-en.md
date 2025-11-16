# University of Tokyo, Creative Informatics, 2012-summer coding test

Make a shooting game to be played by a player alone with following steps:

The shooting game is played on a board with 9 x 15 grid coordinates that are surrounded by A, B, C and D segments (Figure 1). The player moves a gun on the segment C and fires a bullet to a target that moves downward from above. Players compete for a score that is the number of targets shot down by bullets during a game.

The target is thrown from a grid point V on the segment A to a 45 degree lower right direction. The target moves one grid coordinate downward and one grid coordinate horizontally in a unit of time. The reflective index of segments B and D is 1.0 such that the target rebounds with the angle of reflection identical to the angle of incidence. When the target reaches to the segment C, the target becomes lost and the score of the game remains at the same value.

<img alt="Figure 1. The board used in the game" src="pic1.png"/>

<img alt="Figure 2. A snapshot of the board using a character-based presentation" src="pic2.png" title="Figure 2. A snapshot of the board using a character-based presentation"/>

The player moves the gun and fires the gun by pushing the i, j, k or l key of the keyboard. The assignment of keys is as follows. Let’s assume that only one key is pushed at a time.

* i key:
  fires a bullet from the gun. Then the board is updated.

* j key:
  moves the gun on the segment C to one grid position left. Then the board is updated.
  When the gun is at the left-most location of the segment C, the location of the gun is unchanged and the board is updated.

* k key:
  updates the board without any operation to the gun.

* l key:
  moves the gun on the segment C to one grid position right. Then the board is updated.
  When the gun is at the right-most location of the segment C, the location of the gun is unchanged and the board is updated.

---

All key input other than i, j, k or l key is ignored. Note that you can assume that the CR key (Enter key) is pushed just after the i, j, k or l key is pushed.

The method to display the current board can be either a graphical presentation or a character-based presentation. When the board is displayed with characters, "-", "|", "", "/", and " " are used to show segments A, B, C and D and the internal grid points may not be displayed. The location where the target is thrown from the segment A is displayed as "V" and the location of the gun on the segment C is displayed as "X". The location of the target is displayed as "O" and the location of the bullet is displayed as "•". Figure 2 shows a snapshot of the board during a game using the character-based presentation. The method to display the board can be either one of three methods shown below. If the answer uses method 2 or method 3 shown below, additional points will be added to the correct answer.

* Method 1. Character-based presentation where all the board is re-displayed when the board is updated.
* Method 2. Character-based presentation where only the modified location of the board is updated by replacing necessary characters.
* Method 3. Graphical presentation where a bit-map graphical representation of the board is used.

The game begins without a target on the board. When the board is updated and there is no target on the board, a new target is thrown from the V point. After that, the location of the target moves one vertical grid coordinate and one horizontal grid coordinate every time the board is updated.

When the player pushes the i key, a bullet is fired from the gun. After that the bullet moves straight upward one grid coordinate every time the board is updated. When the bullet collides with the target, both the bullet and the target are erased from the board and then one point is added to the score of the game. When the bullet reaches the segment A without colliding to the target, the bullet becomes lost. The player can shoot two bullets for one throw of a target. If the player wants to move the position of the gun, the player pushes the j or l key.

A game-over occurs when the player fails to hit the target and the target becomes lost on the segment C five times. When game-over occurs, the program terminates after showing the score of the game.

(1) Make a program that shows the board excluding any bullet and target.

(2) Make a program that throws a target from the center point of the segment A toward a lower right direction with 45 degree angle, and move the location of the target downward every time the board is updated. When the target reaches the segment C, the target becomes lost. When no target is on the board, a new target is thrown from the center point of the segment A.

(3) Make a program that has a gun on the center point of the segment C. When i key is pushed, a bullet is fired upward from the gun. After that, the bullet goes upward one grid coordinate for each update and the board is re-displayed. In the program, erase the bullet and the target and increase the score of the game by one when they collide with each other.

(4) Modify the program made for (3) to randomize the throw point of target over all the grid points on the segment A with equal probability.

(5) Make a shooting game program in which the gun moves on the segment C when the j key or the l key is pushed and fires a bullet when the i key is pushed.

(6) So far, updating the board and input to the keys are synchronized and the play of the shooting game program is complicated. To modify this program to be more like a real gaming machine, updating the board should be independent from operations to keys by updating the board periodically and the operations for moving and firing the gun are directly controlled by input to keys. Describe the necessary modification to satisfy these requirements on the answer sheet.

(7) Modify the program written so far to periodically update the board every 0.5 seconds without pushing any key, to move the gun one grid coordinate when the j or l key is pushed, and to fire the gun when the i key is pushed.