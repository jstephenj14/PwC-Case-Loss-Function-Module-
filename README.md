# PwC-Case-Loss-Function-Module-
The purpose of this code is to identify specific segments of a population that exhibit a high loss fraction. The loss fraction
defined for this purpose is calculated as the ratio between total claims and total premiums.

This code module takes in customer level data on the premiums paid and amount claimed by a customer from an insurance company. 
Other indicator variables like deographics are also given as input to this function. Interval variables(like income) are binned before 
the segmentation is performed.

Python code implementing this is available [here](https://github.com/jstephenj14/PwC-Case-Loss-Function-Module-/blob/master/Loss%20Function%20Iteration%20Code.py)

A possible sample output based on the customer's bucketed income, marital status (M or D) and gender (M or F) is reproduced below. The tree displays segments with two numbers:(1) Loss Fraction and (2) Count of customers in the segment

<a href="https://drive.google.com/uc?export=view&id=1M1tDxkXjvkB3RTINHqfetK_0LrqR7dCR"><img src="https://drive.google.com/uc?export=view&id=1M1tDxkXjvkB3RTINHqfetK_0LrqR7dCR" style="width: 500px; max-width: 100%; height: auto" title="WOE Table" /></a>

