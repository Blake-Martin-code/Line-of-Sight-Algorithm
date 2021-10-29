# Line-of-Sight-Algorithm
This program determines which buildings are in the sunlight/shade. 

The objective of PA1 is to implement three different algorithms to solve a line of sight problem. As discussed in lecture, given:

  image - A 2D N×N array of floating point numbers (in meters) representing a terrain.
  h - The horizontal distance between adjacent points
  angle - The Sun's angle of elevation

The algorithms must return a 2D N×N boolean array where:
  An entry [i,j] is True if the point [i,j] in the terrain is in the shade
  An entry [i,j] is False if the point [i,j] in the terrain is in the sunlight
  
 Key Notes:
  In this program the sun is always due west. 
  The only functions I wrote are the Naive, earlyexit and fast functions
    These are the 3 main algorithms that actually determine what buildings are in the shade or not
  0's indicate that the building is in the sun while * indicate the building is in the shade

