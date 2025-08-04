import re
from email_validator import validate_email, EmailNotValidError

emails = ["john@example.com", "hello@domain.org", "@@@.com", "user@website?com", "invalid@.com"]

#  .+	Matches at least one character before @ (username)
#  @	Literal @ character
#  .+	Matches at least one character after @ (domain name)
#  \.	Matches a literal . (dot)
#  com	Ensures the domain ends with "com"

for email in emails:
    if re.search(r".+@.+\.com", email):
        print(f"{email} is Valid!")
    else:
        print(f"{email} is Invalid!")
        
print("-----------------")
def is_valid_email(email: str) -> bool:
    try:
        # Validate email format
        valid = validate_email(email, check_deliverability=False)
        
        # Extract domain and ensure it ends with '.com'
        if valid.normalized.split('@')[-1].endswith('.com'):
            return True
        else:
            return False
    except EmailNotValidError:
        return False

for email in emails:
    print(f"{email} {'is Valid!' if is_valid_email(email) else 'is Invalid!'}")