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

signup_form_header = '''
    <DOCTYPE! html>
    <meta charset="UTF-8">
    <html>
        <head>
            <title>Signup Page</title>
        </head>
        <body>
            <h2 style="text-align:center">Signup Form</h2>
 '''
signup_form_footer = '''
        </body>
        <footer></footer>
    </html>
 '''

class SignupHandler(webapp2.RequestHandler):
    def get(self):
        signup_form_body = '''
            <form style="display: flex; flex-direction: column; align-items: flex-end;max-width:60%">
                <label>
                    Username:
                    <input type="text" name="username">
                </label>

                <label>
                    Password:
                    <input type="password" name="password">
                </label>

                <label>
                    Verify Password:
                    <input type="password" name="verify_password">
                </label>

                <label>
                    Email(optional):
                    <input type="email" name="email">
                </label>

                <label>
                    <input type="submit">
                </label>
            </form>
         '''
        content = signup_form_header + signup_form_body + signup_form_footer
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/signup', SignupHandler)
], debug=True)
