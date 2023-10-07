# Password recover Page

__http://192.168.56.101/?page=recover__

## Description
This page for password recovering. 

## Form Outputs
Let's look on the page source exactly to ```</form>``` tag.

```
<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	<input type="submit" name="Submit" value="Submit">
</form>
```
We get the email __webmaster@borntosec.com__.

## Flag
change webmaster@borntosec.com to other one value
In the output we get the flag

## Safety
XSS attact
When it comes to web safety, there are a few important points to consider based on the exercise: </br>
1. Be cautious with password recovery pages: Password recovery pages should be handled with care as they often involve sensitive information. It's crucial to ensure that the page is secure and that any personal data, such as email addresses, are protected.
2. Check the page source: Examining the page source can often reveal important information about a website's functionality or vulnerabilities. In this exercise, checking the page source helped uncover the email address associated with password recovery.
3. Protect personal information: The exercise demonstrates the importance of protecting personal information, such as email addresses. It's crucial to be mindful of who has access to this information and how it is stored or shared.
4. Use secure connections: When interacting with web pages that involve sensitive information, make sure to use secure connections (HTTPS) to protect your data from potential eavesdropping or interception.
5. Implement security measures: As a user, it's important to implement security measures such as strong, unique passwords for different online accounts, enabling two-factor authentication, and regularly updating software and applications to minimize potential security risks.

