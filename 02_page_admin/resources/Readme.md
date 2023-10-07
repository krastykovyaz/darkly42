# Admin Page

__http://192.168.56.101/admin/__

## Description
This is a admin page. We need to input username and password.  

## Form Inputs
We used for brute forsing git clone https://github.com/maurosoria/dirsearch.git
then comand to catch folders ```python3 dirsearch.py -u http://192.168.56.101```
```
Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11715

Output: /mnt/nfs/homes/lnoisome/Desktop/darkly/02_page_admin/resources/dirsearch/reports/http_192.168.56.101/_23-10-07_21-53-35.txt

Target: http://192.168.56.101/

[21:53:35] Starting: 
[21:53:36] 301 -  193B  - /js  ->  http://192.168.56.101/js/
[21:54:15] 301 -  193B  - /admin  ->  http://192.168.56.101/admin/
[21:54:17] 200 -    1KB - /admin/
[21:54:18] 200 -    1KB - /admin/index.php
[21:54:46] 301 -  193B  - /audio  ->  http://192.168.56.101/audio/
[21:55:07] 301 -  193B  - /css  ->  http://192.168.56.101/css/
[21:55:18] 301 -  193B  - /errors  ->  http://192.168.56.101/errors/
[21:55:19] 200 -  967B  - /errors/
[21:55:22] 200 -    1KB - /favicon.ico
[21:55:24] 301 -  193B  - /fonts  ->  http://192.168.56.101/fonts/
[21:55:33] 301 -  193B  - /images  ->  http://192.168.56.101/images/
[21:55:33] 200 -  967B  - /images/
[21:55:34] 200 -  967B  - /includes/
[21:55:34] 301 -  193B  - /includes  ->  http://192.168.56.101/includes/
[21:55:40] 200 -  967B  - /js/
[21:56:22] 200 -   53B  - /robots.txt

Task Completed
```
For the input data to the form we go to the [robots.txt](#http://192.168.56.101/robots.txt) and we've got a path to the [/whatever](#http://192.168.56.101/whatever/) where I've got htpasswd.

## Flag
In the htpaswd I've got root:437394baff5aa33daa618be47b75cb49. Which means username: root and password qwerty123@ from [MD5](#https://md5.gromweb.com/?md5=437394baff5aa33daa618be47b75cb49). After inputing to the admin form We've got the next flag.

## Safety
Do not storage inside the service meta in easy hashing at the same time.
