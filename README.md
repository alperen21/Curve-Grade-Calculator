# Curve Grade Calculator

  After I took an introductory course in probability / statistics in my university since I now had learned about normal distribution and curve grades I realized that I now can approximate my rank in the class and could approximate my letter grade given that the instructor provides us with standard deviation, mean and class population. It occured to me that I could use some libraries in Python to utilitze this into a script so I wrote the code for automating the calculations.

## Math

  Curve class can do two calculations, approximating your rank within the class and calculating the letter grade for the individual coursework/exam (the algorithm assumes that the given coursework makes up 100% of your final / cumulative score). For approximation of the place you are at within the class:

  Let's say you got 78% in class that has the mean 37.07, standard deviation 23.2, highest grade is 91 and the lowest grade is 0 and that particular class has 102 students. Then, if the random variable X indicates the score of another student, the probability of that student scoring higher than you would be:
  
  <a href="https://www.codecogs.com/eqnedit.php?latex=P(&space;78&space;<&space;x&space;<&space;91&space;|&space;0&space;<&space;x&space;<&space;91)&space;=&space;P&space;(&space;\frac{78-37}{23.2}&space;<&space;z&space;<&space;\frac{91-37}{23.2}&space;|&space;\frac{0-37}{23.2}&space;<&space;z&space;<&space;\frac{91-37}{23.2})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(&space;78&space;<&space;x&space;<&space;91&space;|&space;0&space;<&space;x&space;<&space;91)&space;=&space;P&space;(&space;\frac{78-37}{23.2}&space;<&space;z&space;<&space;\frac{91-37}{23.2}&space;|&space;\frac{0-37}{23.2}&space;<&space;z&space;<&space;\frac{91-37}{23.2})" title="P( 78 < x < 91 | 0 < x < 91) = P ( \frac{78-37}{23.2} < z < \frac{91-37}{23.2} | \frac{0-37}{23.2} < z < \frac{91-37}{23.2})" /></a>
  
  Which is equal to: 
  
  <a href="https://www.codecogs.com/eqnedit.php?latex=P(&space;1.76&space;<&space;z&space;<&space;2.32&space;|&space;-1,59&space;<&space;z&space;<&space;2.32)&space;=&space;\frac{Table(2.32)-Table(1.76)}{Table(2.32)-Table(-1.59)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(&space;1.76&space;<&space;z&space;<&space;2.32&space;|&space;-1,59&space;<&space;z&space;<&space;2.32)&space;=&space;\frac{Table(2.32)-Table(1.76)}{Table(2.32)-Table(-1.59)}" title="P( 1.76 < z < 2.32 | -1,59 < z < 2.32) = \frac{Table(2.32)-Table(1.76)}{Table(2.32)-Table(-1.59)}" /></a>
  
  I used Scipy library to calculate normal probabilities. table_grade corresponds to Table(1.76), table_min corresponds to Table(-1.59) and table_max corresponds to Table(2.32). If statements are there to also take into account that the normalized grade may fall on the left or the right side of the 0 point of Gaussian curve, which depends on whether your grade is higher or lower than the mean.
  
  This probability is then multiplied with the total number of students in the class to approximate your place in the ranking of the class. For example in this case the output of rank() is 4 which means that you got the 4th highest grade in the whole class.
  
  For the letter grades, a dictionary data structure is used. This dictionary (grade_boundaries) is initialized within initialization of the class itself accordingly to boolean values "default" and "plus_minus" which are set to true by default. If plus_minus is set to true, the class assumes that the instructor is using the grade system like A, A-, B+, B, B- and so on. If its set to false the class will switch to AA, BA, BB grading system. If default is set to true, the grade scale will be divided equally and if not grades list will be used to determine which percentages correspond to which letter grades. For example, A:10 means that only 10% of the class will get an A; if the corresponding A- is set to 15 then someone who falls between 15%-10% will get an A- and so on.
