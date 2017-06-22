programmer-challenge
==================

This is a program in python to test the ability of a programmer to find the best solution to discover a phrase.

The programmer should make a program with the minimum of requests to find the phrase.
The program should make a POST request in the URL: https://programmerchallenge.herokuapp.com/challenge/run_task/ with a string to find the solution.

### Guide:

CHAR = If return the CHAR in the same position, so you found the right CHAR in the right position
* = Have the CHAR but in the wrong position
? = Don't have de char on the string

Allowed chars:
Letters: A-Z, a-z
Numbers: 0-1
Special chars: '!.,:;#$%&*

### Example:
If the phrase is: "Steve Jobs"

Request    | Response | Explain
------- |  --------- | ---------
aeiou | ?*?*? | "e" and "o" have on the string but in the wrong position
steve | *teve | "s" has only in the "Jobs"
Steve | Steve | That's right so far
Steve bobs | Steve *obs | "b" has only in Jobs
Steve Jobs Jobs | Steve Jobs | The text legth will be in the maximum the len of "Steve Jobs"
Steve Jobs | Steve Jobs | That's GREAT!


### Test:
URL: https://programmerchallenge.herokuapp.com/challenge/run_task/

POST: teste

Try to do a POST in this url with a message

Or just try to acess in your browser:

https://programmerchallenge.herokuapp.com/challenge/run_task/?phrase=gth
