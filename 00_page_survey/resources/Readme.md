# Survey Page
__http://192.168.99.101/?page=survey__
## Description
This is a survey page where users can make choices and provide input. Each row of the "Make your choice" table is an HTML form element. The form action is set to "#" which means it submits to itself, and the form method is set to POST.

## Form Inputs
The form has several inputs:

1. Input name "sujet" (type: hidden): This input has a value range from 2 to 6.
2. Input name "valeur" (type: select): This input has a value range from 1 to 10.

The "valeur" element also has an onchange JavaScript attribute, which automatically submits the form when the value is changed.

## Flag
If a POST request is submitted with the "valeur" value greater than 10, the page will display the flag.

```curl -s 'http://192.168.99.101/index.php?page=survey' --data 'sujet=2&valeur=10'  -o before.html && curl -s 'http://192.168.99.101/index.php?page=survey' --data 'sujet=2&valeur=110'  -o after.html && diff before.html after.html | sed 's/.*flag is \(.*\)<\/h2>.*/\1/' > flag```

## Key Takeaway
The key takeaway from this experience is the importance of data sanitization and validation to prevent potential security vulnerabilities. Whether variables are passed in the URL through a GET request or through a more complex POST request, proper measures should be taken to ensure the accuracy and safety of user data.</br>
In terms of security, this code is attempting to exploit a vulnerability in the survey page. By sending different POST requests with varying values of thevaleur parameter, the code checks if there is any difference in the server's response. The assumption is that if the value of valeur is greater than 10, the flag will be displayed in the response.</br>
However, this approach is not a secure way of extracting the flag, as it relies on the assumption that the flag will always be wrapped in a specific HTML tag structure. Additionally, this code does not handle edge cases or validate/sanitize the user input properly.</br>
To ensure better security, it is crucial to implement proper input validation and sanitization techniques, such as server-side validation and using secure APIs, to prevent potential vulnerabilities like injection attacks or data manipulation.</br>
