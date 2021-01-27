# Curve Grade Calculator

  After I took an introductory course in probability / statistics in my university since I now had learned about normal distribution and curve grades I realized that I now can approximate my rank in the class and could approximate my letter grade given that the instructor provides us with standard deviation, mean and class population. It occured to me that I could use some libraries in Python to utilitze this into a script so I wrote the code for automating the calculations.

## Math

  Curve class can do two calculations, approximating your rank within the class and calculating the letter grade for the individual coursework/exam (the algorithm assumes that the given coursework makes up 100% of your final / cumulative score). For approximation of the place you are at within the class:

  Let's say you got 78% in class that has the mean 37.07, standard deviation 23.2 and that particular class has 102 students. Then, if the random variable X indicates the score of another student, the probability of that student scoring higher than you would be:
  
  <img src="https://latex.codecogs.com/svg.latex?P(X>78)" title="P(X>78)" style="background-color: white;" />
  
  In order to utilize the normal approximation in this you would need to first normalize the random variable:
  
  <img src="https://latex.codecogs.com/svg.latex?P((X-\mu)/\sigma&space;>&space;(78-\mu)/\sigma)" title="P((X-\mu)/\sigma > (78-\mu)/\sigma)" />
  
  For this case mu would be 37.07 and sigma would be 23.2
  
 <img src="https://latex.codecogs.com/svg.latex?P((X-37.07)/23.2&space;>&space;(78-37.07)/23.2)&space;=&space;P(Z&space;>&space;1,764)" title="P((X-37.07)/23.2 > (78-37.07)/23.2) = P(Z > 1,764)" />
  
