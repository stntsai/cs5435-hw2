# HW2 Short Answers

## Task 2.6

- Reflected XSS vulnerability - Attackers can use a similar attack as the one in Task 2.1 and 2.2 to steal the victim’s credentials. For example, the coin amount or some personal information shown on the user’s profile page. Attackers can use reflected XSS technique to send what has been “seen” on users’ logged in page to arbitrary destinations./

- Stored XSS vulnerability - Any entry point on the profile page could be subject to stored XSS attack. Attackers can insert malicious scripts through any `<input>` tag, “pay” button as an example, using the similar method we used in Task 2.5 to contaminate a user’s page and force them to send coins to any destination once the page is viewed.

## Task 2.8

1. Stored XSS - Malicious scripts were stored directly into the database or server where no sanitation check was performed. When the user visits the compromised website, the script is then executed automatically./
Reflected CSS - The attacker injects malicious code as part of the HTML rendered in a webpage. Only when the user clicks on it, it then becomes effective.

2. When a web server set the Access-Control-Allow-Origin header to “*”, it means that the resource in its origin can be accessed by any origin. In this case, any site can send an XHR request to the site and access the server’s response on behalf of their visitors. In a CSS attack, attackers may easily exfiltrate user credentials using cookies they gain through user’s visit to a malicious website. They don’t even need to think of a way to bypass the header.
