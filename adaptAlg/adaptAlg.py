"""
adaptAlg.py
---------
Owen Chen
---------
Adaptive Algorithm module for learning analytics. Machine learning concepts to maximize learning retention
efficency

Algorithm:
1. Split into smallest possible items. 
2. E-Factor of 2.5 initialized to all variables. 
3. OF Matrix and E-Factor categories. Algorithm:
        OF(1,EF) = 4
        for n > 1 OF(n, EF) := EF

        Where OF(n, EF) - optimal factor for n-th repitition  and EF 
4. OF Matrix to determine inter-repetition intervals. 
        I(n, EF) = OF( n, EF) * I(n-1, EF)
        ... Code Onbline
5. Assess quality of repetition responses in 0-5 scale
6. Modify E-factor According to formula
7. After each rep, modify relevant entry of OF matrix. 
8. if quality respobse is lower than 3 start repetition for the item from the beginning with no E-factor change
9. Repeat all items under four in quality assement.


"""

