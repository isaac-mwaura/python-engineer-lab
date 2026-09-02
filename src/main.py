import sys
import os
import argparse

# Add the parent directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.processors import load_users_from_json, sort_users_by_name, generate_summary

def main():
    parser = argparse.ArgumentParser(description="User Data Processor")
    parser.add_argument(
        "--file", 
        type=str, 
        required=True,
        help="Path to the JSON file containing user data."
    )
    parser.add_argument(
        "--sort", 
        action="store_true",
        help="Sort the output users by name."
    )
    parser.add_argument(
        "--summary", 
        action="store_true",
        help="Display a summary (total, average age, cities) instead of user list."
    )
    
    args = parser.parse_args()
    
    # Load data
    users = load_users_from_json(args.file)
    if not users:
        print("No valid users to process. Exiting.")
        sys.exit(1)
    
    # Apply sort if requested
    if args.sort:
        users = sort_users_by_name(users)
    
    # Output
    if args.summary:
        summary = generate_summary(users)
        print("=== SUMMARY ===")
        print(f"Total Users: {summary['total']}")
        print(f"Average Age: {summary['average_age']}")
        print("Cities: ", summary['cities'])
    else:
        print("=== USERS ===")
        for user in users:
            city_str = user.city if user.city else "Not specified"
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}, Age: {user.age}, City: {city_str}")

if __name__ == "__main__":
    main()