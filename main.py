#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re
import cgi

signup_form_header = '''
    <DOCTYPE! html>
    <meta charset="UTF-8">
    <html>
        <head>
            <title>Signup Page</title>
        </head>
        <body style = "background: linear-gradient(to bottom, rgba(252,255,244,1) 0%,rgba(223,229,215,1) 40%,rgba(179,190,173,1) 100%);">
            <h2 style="text-align:center">Signup Form</h2>
 '''

signup_form_body = '''
    <form  action="/signup"
           method="post"
           style="display: flex; flex-direction: column; align-items: flex-center">
     <table style="margin: 0 0 auto 40%;">
        <tr>
            <td>
                <label for='username'>Username</label>
            </td>
            <td>
                <input type='text'
                       name = 'username' {username_val} required>
            </td>
            <td>
                <span style='color:red;'>{username_error}</span>
            </td>
        </tr>
        <tr>
            <td>
                <label for='password'> Password </label>
            </td>
            <td>
                <input type='password' name='password' required>
            </td>
            <td>
                <span style='color:red'>{password_error}</span>
            </td>
        </tr>
        <tr>
            <td>
                <label for='verify_password'>Verify Password</label>
            </td>
            <td>
                <input type='password' name='verify_password' required>
            </td>
            <td>
                <span style='color:red'>{verify_password_error}</span>
            </td>
        </tr>
        <tr>
            <td>
                <label for='email'>Email(Optional)</label>
            </td>
            <td>
                <input type='email' name='email' {email_val}>
            </td>
            <td>
                <span style='color:red'>{email_error}</span>
            </td>
        </tr>
        <tr>
            <td>
            </td>
            <td>
                <input type="submit">
            </td>
        </tr>
    </table>
</form>'''



signup_form_footer = '''
        </body>
        <footer></footer>
    </html>
 '''

# Compiled regex
username_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
password_re = re.compile(r"^.{3,20}$")
email_re = re.compile(r"^[\S]+@[\S]+.[\S]+$")

class IndexPageHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect('/signup')


class SignupHandler(webapp2.RequestHandler):
    def get(self):

        signup_body = signup_form_body.format(username_error = "",
                                              password_error = "",
                                              username_val = "",
                                              email_val = "",
                                              verify_password_error = "",
                                              email_error = "")

        content = signup_form_header + signup_body + signup_form_footer
        self.response.write(content)

    def post(self):
        # init error variables
        username_error = ""
        password_error = ""
        verify_password_error = ""
        email_error = ""

        # get data from posted from
        username = cgi.escape(self.request.get("username"),quote=True)
        password = cgi.escape(self.request.get("password"),quote=True)
        password_verify = cgi.escape(self.request.get("verify_password"),quote=True)
        email = cgi.escape(self.request.get("email"), quote=True)


        if (not username.strip() or not username_re.match(username)):
            username_error = "That's not a valid username!"
        if not password_re.match(password):
            password_error = "Password must be 3 to 20 characters long!"
        if password_verify != password:
            verify_password_error = "Passwords do not match!"
        if email.strip():
            if not email_re.match(email):
                email_error = "That's not a valid email address!"

        if (not username_error and not password_error and not verify_password_error and not email_error):
            self.redirect("/welcome?username=" + username)
        else:
            signup_body = signup_form_body.format(username_val = "value=" + username.strip(),
                                                  email_val = "value=" + email,
                                                  username_error = username_error,
                                                  password_error = password_error,
                                                  verify_password_error = verify_password_error,
                                                  email_error = email_error)
            content = signup_form_header + signup_body + signup_form_footer
            self.response.write(content)


class WelcomePageHandler(webapp2.RequestHandler):
    def get(self):
        welcome_header = '''
            <DOCTYPE! html>
            <meta charset="UTF-8">
            <html>
                <head>
                    <title>Welcome Page</title>
                </head>
                <body style = "background: linear-gradient(to bottom, rgba(252,255,244,1) 0%,rgba(223,229,215,1) 40%,rgba(179,190,173,1) 100%);">

         '''

        username = self.request.get('username');
        content = welcome_header + "<h2>Welcome user {} !</h2>".format(username) + signup_form_footer
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', IndexPageHandler),
    ('/signup', SignupHandler),
    ('/welcome', WelcomePageHandler),
], debug=True)
