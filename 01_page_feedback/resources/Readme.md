# Feedback Page
__http://192.168.56.101/?page=feedback__
## Description
This is a feedback page where users can provide feedback. 

## Form Inputs
The form has an input of type "Submit" with an onClick attribute that returns "checkForm()". However, there is no such JavaScript function on the page. When the button is pressed, it generates an error in the Firefox developer tools. In the "Console" section of the developer tools, we can see an error message that says "Uncaught ReferenceError: checkForm is not defined" at line 83. The form element also has an onsubmit attribute that calls "validate_form()", which also seems to be broken. The issue is that in the form, the textarea has a name "mtxtMessage", but in the JavaScript validation function, it is "mtxMessage". This one-character element name misspelling has crippled the JavaScript validation, and as a result, the length of the message is never validated.
Even if the JavaScript was functional and properly checked the lengths of both fields' names and messages, it would still be possible to perform an HTTP post request with empty variables (for example, via curl or Python's requests). While playing with the page, it was discovered that it will only show the flag when the "mtxtMessage" is set to certain values. For instance:

```065 41 A
067 43 C
069 45 E
073 49 I
076 4c L
080 50 P
082 52 R
083 53 S
084 54 T
097 61 a
099 63 c
101 65 e
105 69 i
108 6c l
112 70 p
114 72 r
115 73 s
116 74 t```

Therefore, a small script was written to test all possible values from 0 to 127.

## Flag
I've got a hash of the flag by rendering the [page](#http://192.168.56.101/?page=feedback). 


## Key Takeaway
To find the correct character that would work in the specific context. To automate the process of finding the correct character, I created a script that would test all possible values from 0 to 127 and output the character that worked. The character set that worked was aceilprst in both uppercase and lowercase, which appears to be an anagram of the word "particles".