import unittest
class TestLogin(unittest.TestCase):
   def test_login_success(self):
       # Test login success
       self.assertEqual(login('admin', 'admin'), 'Login success')

   def test_login_failure(self):
       # Test login failure
       self.assertEqual(login('admin', 'wrong_password'), 'Login failed')
def login(username, password):
   # Login function
   if username == 'admin' and password == 'admin':
       return 'Login success'
   else:
       return 'Login failed'
if __name__ == '__main__':
   unittest.main()
