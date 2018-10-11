Instructions on how to run the analysis:

1) Make sure you have Matplotlib installed on your computer

2) Click on “Run Module.” 
	
**For countWords.py, the user will be prompted to choose an analysis of the top 20 most frequently used words and their frequencies
 for either bush_all.txt or obama_all.txt in the Python shell. You may choose one and then the other after, and if you type in an invalid
 word, you will be prompted to choose again.
 
**For visualizeText.py, it will run the main function of countWords.py again unless you comment out the “main()” at the end. The 2 graphs
 of our analyses will then be displayed.

3) If you only want to check Part 2 of the project (visualizing our analyses), comment out the very last line (i.e. “main()”) of countWords.py and 
then click “Run Module” with the file visualizeText.py open.



We were able to accomplish the tasks we planned to achieve in the proposal, but we did a couple of things differently than we proposed. 
Instead of writing the two functions sortForObama(dBush, dObama) and sortForBush(dBush, dObama) separately, we combined them using one
function with the help of Ordered Dictionary. We manipulated the different parts of the top 20 dictionaries at the same time in one function
instead of two to reduce the runtime a little bit. 



Reflection:
 Through this experience, we have all learned about working on a project in a group that requires all members to be active. To successfully
 create our program, we had to break up the process into smaller parts and solve each problem step-by-step. For example, we used helper functions 
to count frequencies. We found that working as a group rather than alone is far more effective because we all have different strengths and ways 
of solving problems that help us get through hard tasks. The hardest part about our program was creating the frequency graphs. None of us knew 
exactly how to create different types of graphs so that required a lot of research. There were a lot of different ways to make graphs and we did 
not know which way was the correct one. We now know how to create bar graphs and no-fill stack step graphs. If we had more time, we would try to
 figure out an easier way to count the frequencies for the regions to reduce the runtime.
