import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.validators import validate_email, validate_age, validate_user_data

class TestValidators(unittest.TestCase):
    
    def test_validate_email_valid(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertTrue(validate_email("user.name+tag@domain.co.uk"))
    
    def test_validate_email_invalid(self):
        self.assertFalse(validate_email("test@"))
        self.assertFalse(validate_email("test.com"))
        self.assertFalse(validate_email(12345))
    
    def test_validate_age_valid(self):
        self.assertTrue(validate_age(25))
        self.assertTrue(validate_age(0))
        self.assertTrue(validate_age(120))
    
    def test_validate_age_invalid(self):
        self.assertFalse(validate_age(-5))
        self.assertFalse(validate_age(150))
        self.assertFalse(validate_age("twenty"))
    
    def test_validate_user_data_complete_valid(self):
        data = {"id": 1, "name": "Isaac", "email": "isaac@mail.com", "age": 30}
        valid, errors = validate_user_data(data)
        self.assertTrue(valid)
        self.assertEqual(errors, [])
    
    def test_validate_user_data_missing_fields(self):
        data = {"id": 1, "email": "isaac@mail.com"}
        valid, errors = validate_user_data(data)
        self.assertFalse(valid)
        self.assertIn("Missing or empty 'name' field.", errors)
        self.assertIn("Missing 'age' field.", errors)
    
    def test_validate_user_data_invalid_email(self):
        data = {"id": 1, "name": "Isaac", "email": "notanemail", "age": 30}
        valid, errors = validate_user_data(data)
        self.assertFalse(valid)
        self.assertTrue(any("Invalid email format" in err for err in errors))

if __name__ == "__main__":
    unittest.main()