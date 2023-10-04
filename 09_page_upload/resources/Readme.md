# Upload files Page

__http://192.168.56.101/?page=upload__

## Description
This page for uploading documents. 

## Form Outputs
I have upload image and get the output ```/tmp/avatar.jpg succesfully uploaded.```.

## Flag
When we launch the python script we get the next flag.
```
python3 upload.py | grep flag
```

## Safety
Based on the provided Python script and the observations made during the exercise, here are some key points regarding web security:</br>
1. File type validation: The observation that the page only accepts JPEG images indicates that there is some form of file type validation in place. This is a positive security measure to prevent potentially malicious file types from being uploaded. However, it's important to note that file type validation should be implemented server-side and not solely rely on client-side checks.
2. File name validation: The exercise mentions that the filename provided in the script is not valid in UNIX environments due to the / character. This observation highlights the importance of validating and sanitizing user-provided file names. Allowing special characters or not properly handling them can lead to potential security vulnerabilities, such as directory traversal attacks.
3. Content-type mismatch: The script demonstrates that even though the content-type is set to "image/jpeg," the uploaded file's actual contents don't match the specified content-type. This indicates a weakness in the server's validation, as it allows files with arbitrary content to be uploaded. Ideally, the server should properly validate the file's content to ensure it matches the specified content-type.
4. Cross-Site Scripting (XSS) vulnerability: The initial script you provided demonstrates an XSS vulnerability by injecting a script tag into the uploaded file's name. While this vulnerability does not seem directly related to the file upload itself, it is still a potential security issue that should be addressed to prevent attackers from injecting malicious scripts into the website.
5. Flag leakage: The presence of the flag in the server's response can be considered a security oversight. Sensitive information, such as flags or credentials, should be properly protected and not exposed in server responses. This prevents unauthorized access or leakage.
