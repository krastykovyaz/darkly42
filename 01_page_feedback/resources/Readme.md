# Feedback Page
__http://192.168.56.101/?page=feedback__
## Description
This is a feedback page where users can provide feedback. 

## Form Inputs
The readme file needs improvement as the page appears to be poorly written. The form has an input of type "Submit" with an onClick attribute that returns "checkForm()". However, there is no such JavaScript function on the page. When the button is pressed, it generates an error in the Chrome developer tools. In the "Console" section of the developer tools, we can see an error message that says "Uncaught ReferenceError: checkForm is not defined" at line 83. The form element also has an onsubmit attribute that calls "validate_form()", which also seems to be broken. The issue is that in the form, the textarea has a name "mtxtMessage", but in the JavaScript validation function, it is "mtxMessage". This one-character element name misspelling has crippled the JavaScript validation, and as a result, the length of the message is never validated.
Even if the JavaScript was functional and properly checked the lengths of both fields' names and messages, it would still be possible to perform an HTTP post request with empty variables (for example, via curl or Python's requests). While playing with the page, it was discovered that it will only show the flag when the "mtxtMessage" is set to certain values. For instance, testing with a one-character string "a" showed the flag. On the other hand, testing with other characters like "b" did not work, but "c" did. Therefore, a small script was written to test all possible values from 0 to 255.

## Flag
I've got a hash of the flag by rendering the [page](#http://192.168.56.101/?page=feedback). 


## Key Takeaway
To find the correct character that would work in the specific context. To automate the process of finding the correct character, I created a script that would test all possible values from 0 to 255 and output the character that worked. The character set that worked was aceilprst in both uppercase and lowercase, which appears to be an anagram of the word "particles".