# debug_log.md
# Author: Mateus De Mesquita

## Bug 1
Error type: KeyError
File + line: "/Users/demateus/ism3232/module05_functions/week8_buggy.py", line 12
"/Users/demateus/ism3232/module05_functions/week8_buggy.py", line 21
What the error means: It means that the key in the code does not exist.
What I told the duck: I told the duck that for the the def get_total function, the records starting from 0 are to be called and added from amounts.
What I tried: I noticed that in the records not all the amounts had the same key typed the same.
How I fixed it: I fixed the key to match each other.

## Bug 2
Error type: TypeError
File + line: week8_buggy.py, lines 23 and 16
What the error means: The error means that the operation is calling for a type that is separate from the actual type, such as a string when calling for int.
How I fixed it: I went to the line with the error and wrapped it in a int() function.

## After Fixing Both Bugs
Final output: Total: $5150.00 across 3 records
True
Did pytest pass? Yes

## AI Literacy Reflection
Did I use AI? Yes 
If yes -- exact prompt I used: "I am trying to import this package into my test file but I am getting an error because it can not access the file in the parent directory. How do I work around this?"
What AI explained: Python can’t see the parent folder. When pytest runs a file in tests/, it adds tests/ to the path, not module05_functions/. Any of these fixes work: Option A (simplest): run from the parent folder with python -m
What I changed myself: I ran the pytest from the bash u
Can I explain every fixed line? Yes 

## What I learned

The most valuable aspect of this process that I learned was the duck method. Not only did it help me understand how to debug, but it also reinforces my knowledge of functions and how they work too. It also highlights any misunderstanding of the code and forces you to think critically.