import json
import sys
import os
from typing import List, Dict

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models import User
from src.validators import validate_user_data

def load_users_from_json(filepath: str) -> List[User]:
    """
    Loads user data from a JSON file.
    Skips invalid entries and prints warnings.
    """
    valid_users = []
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: File not found at {filepath}")
        return []
    except json.JSONDecodeError:
        print(f"ERROR: Invalid JSON in {filepath}")
        return []
    
    if not isinstance(data, list):
        print("ERROR: JSON root must be a list of users.")
        return []
    
    for idx, item in enumerate(data):
        is_valid, errors = validate_user_data(item)
        if is_valid:
            try:
                user = User.from_dict(item)
                valid_users.append(user)
            except Exception as e:
                print(f"WARNING: Could not parse user at index {idx}: {e}")
        else:
            print(f"WARNING: User at index {idx} failed validation: {', '.join(errors)}")
    
    return valid_users

def filter_users_by_age(users: List[User], min_age: int, max_age: int) -> List[User]:
    """Return users within the age range (inclusive)."""
    return [u for u in users if min_age <= u.age <= max_age]

def sort_users_by_name(users: List[User]) -> List[User]:
    """Return a new list sorted alphabetically by name."""
    return sorted(users, key=lambda u: u.name.lower())

def generate_summary(users: List[User]) -> Dict:
    """
    Generate a summary dictionary with counts and average age.
    """
    if not users:
        return {"total": 0, "average_age": 0.0, "cities": {}}
    
    total = len(users)
    avg_age = sum(u.age for u in users) / total
    cities = {}
    for u in users:
        if u.city:
            cities[u.city] = cities.get(u.city, 0) + 1
    
    return {
        "total": total,
        "average_age": round(avg_age, 2),
        "cities": cities
    }