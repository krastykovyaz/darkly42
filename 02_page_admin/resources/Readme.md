# Admin Page

__http://192.168.99.101/admin/__

## Description
This is a admin page. We nee to input username and password.  

## Form Inputs
For the input data to the form we go to the [robots.txt](#http://192.168.99.101/robots.txt) and we've got a path to the [/whatever](#http://192.168.99.101/whatever/) where I've got htpasswd.

## Flag
In the htpaswd I've got root:437394baff5aa33daa618be47b75cb49. Which means username: root and password qwerty123@ from [MD5](#https://md5.gromweb.com/?md5=437394baff5aa33daa618be47b75cb49). After inputing to the form I've got the next flag d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

## Safety
Do not storage inside the service meta in easy hashing at the same time.
