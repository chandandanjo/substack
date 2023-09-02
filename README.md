# Substack Python API

This Python library provides a simple way to interact with Substack's web services. You can use this library to perform actions such as logging in, managing recovery questions, enabling or disabling two-factor authentication, and retrieving your profile image.


## Usage

Here's an example of how to use this library:

```python
from substack import Substack

# Create a Substack object
substack = Substack()

# Log in using your email and password
result = substack.login_from_mail('your_email@example.com', 'your_password')
print(result)

# OR Log in using a saved cookie file
result = substack.login_from_saved_cookie('cookie.json')
print(result)

# OR Log in using an uploaded cookie
result = substack.login_from_uploaded_cookie('{"your_cookie_data": "here"}')
print(result)

# Retrieve your username
username = substack.user_name()
print(f'Username: {username}')

# Enable recovery questions
substack.enable_recovery_questions()

# Disable recovery questions
substack.disable_recovery_questions()

# Enable two-factor authentication
substack.two_factor_auth()

# Disable two-factor authentication
substack.disable_two_factor_auth()

# Retrieve your profile image URL
profile_image_url = substack.profile_image()
print(f'Profile Image URL: {profile_image_url}')
```

## Documentation

- `login_from_mail(mail, password)`: Log in to Substack using your email and password. Returns 'Connected Successfully' on success, or 'Wrong Credentials' on failure.

- `login_from_saved_cookie(cookie_file_name)`: Log in to Substack using a saved cookie file. Returns 'Connected Successfully' on success, or 'Wrong Cookie' if the cookie is invalid or not found.

- `login_from_uploaded_cookie(cookie_name)`: Log in to Substack using an uploaded cookie. Returns 'Connected Successfully' on success, or 'Wrong Cookie' if the cookie is invalid.

- `save_cookie()`: Save the current session's cookies to a file named 'output.txt'. Returns 'Cookies saved in output.txt file.' on success, or 'No Cookies in the session currently.' if no cookies are available.

- `user_name()`: Retrieve the username associated with the logged-in Substack account.

- `enable_recovery_questions()`: Enable recovery questions for your Substack account. Note that the data provided may vary depending on your specific recovery questions and answers.

- `disable_recovery_questions()`: Disable recovery questions for your Substack account. Note that the data provided may vary depending on your specific recovery questions and answers.

- `two_factor_auth()`: Perform two-factor authentication for your Substack account. You will be prompted to enter a six-digit TOTP (Time-Based One-Time Password).

- `disable_two_factor_auth()`: Disable two-factor authentication for your Substack account. You will be prompted to enter a six-digit TOTP.

- `profile_image()`: Retrieve the URL of your profile image on Substack.

## Disclaimer

Please use this library responsibly and respect Substack's terms of service. Unauthorized access to Substack's services may violate their policies.
