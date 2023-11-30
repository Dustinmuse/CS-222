'''
User Story 1: User Registration
As a new user, I want to be able to register for a new account using email and password

User Story 2: Login
As a registered user, I want to be able to log in to my account using email and password

User Story 3: Password Reset
As a user, who forgot their password, I want to ba able to request a password reset
'''

import unittest
#from User import UserManagement  #if usermanagemnt was defined in another class
class TestUserManagement(unittest.TestCase):
    def test_registration(self):
        userManager = UserManagment() #make object of usermanagemnt
        result = userManager.register("a@b.com", "password")
        self.assertTrue(result)
    def test_login(self):
        userManager = UserManagment()  # make object of usermanagemnt
        userManager.register("a@b.com", "password")
        result = userManager.login("a@b.com", "password")
        self.assertTrue(result) #user was able to log in
    def test_password_reset_request(self):
        userManager = UserManagment()  # make object of usermanagemnt
        result = userManager.request_password_reset("a@b.com")
        self.assertTrue(result)
    def test_password_reset(self):
        userManager = UserManagment()  # make object of usermanagemnt
        userManager.register("a@b.com", "password")
        reset_token = userManager.request_password_reset("a@b.com")
        result = userManager.reset_password("a@b.com", reset_token, "newPassword")
        self.assertTrue(result)
