# debug_log.md
# Author: Jason Nguyen

## Bug 1
Error type: KeyErroe
File + line: week8_buggy.py, line 12
What the error means: Python couldn't find the key because it was misspelled
What I told the duck: I noticed that amount was spelled incorrectly in the first record
What I tried: I checked the records and found the spelling mistake
How I fixed it: I changed 'amout' to 'amount' in the first record

## Bug 2
Error type: TypeError
File + line: week8_buggy.py, line 16
What the error means: Python cannot compare an integer with a string using the greater than operator
How I fixed it: I removed the quotation marks around 1000 so Python would compare two numbers

## After Fixing Both Bugs
Final output: Total: $5150.00 across 3 records
True
Did pytest pass? Yes 

## AI Literacy Reflection
Did I use AI?  No
If yes -- exact prompt I used: ___
What AI explained: ___
What I changed myself: ___
Can I explain every fixed line? Yes 

## What I learned
I learned how to identify errors by reading the traceback and checking my code. I also learned that small mistakes like spelling errors and incorrect data types can prevent a program from running correctly.