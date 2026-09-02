import re
from typing import Dict, List, Tuple

def validate_email(email: str) -> bool:
    """
    Validate email format using basic regex.
    Returns True if valid, False otherwise.
    """
    if not isinstance(email, str):
        return False
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def validate_age(age: int) -> bool:
    """
    Validate age is a reasonable integer (0 to 120).
    """
    if not isinstance(age, int):
        return False
    return 0 <= age <= 120

def validate_user_data(user_data: Dict) -> Tuple[bool, List[str]]:
    """
    Validates a user dictionary.
    Returns (is_valid, list_of_error_messages).
    """
    errors = []
    
    # Check required fields
    if "id" not in user_data:
        errors.append("Missing 'id' field.")
    if "name" not in user_data or not str(user_data["name"]).strip():
        errors.append("Missing or empty 'name' field.")
    if "email" not in user_data:
        errors.append("Missing 'email' field.")
    if "age" not in user_data:
        errors.append("Missing 'age' field.")
    
    # If we have email, validate format
    if "email" in user_data and user_data["email"]:
        if not validate_email(user_data["email"]):
            errors.append(f"Invalid email format: {user_data['email']}")
    
    # If we have age, validate range
    if "age" in user_data and user_data["age"] is not None:
        try:
            age_val = int(user_data["age"])
            if not validate_age(age_val):
                errors.append(f"Age out of range (0-120): {age_val}")
        except (ValueError, TypeError):
            errors.append(f"Age must be an integer, got: {user_data['age']}")
    
    return len(errors) == 0, errors