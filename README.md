# substack
Accessing 'substack.com' via requests module python.

### Contains following :
  - main.py : It contains REST API developed using **FastAPI** and deployed via **Uvicorn** to provide web based interaction with the Substack class and it's methods (*only some of them*).
  - substack.py : It contains the main Substack class which is responsible for all the interaction with substack.com via creating a **requests.Session()** object and performing various methods.
      - login_from_mail : This method logs in to user's substack account and accepts two arguments namely email and password. It also saves session cookies for future                             logins, until it expires.
      - login_from_saved_cookie : This methods logs in to user's substack account and accepts a cookie file (obtained from session.cookies.get_dict()) as argument.
      - user_name : Returns username (if logged in).
      - enable_recovery_questions, disable_recovery_questions : Enable and disable recovery questions respectively (recovery questions may vary from user to user).
      - two_factor_auth : Checks if two factor auth is enabled, if enabled asks for six digit TOTP to continue logging in.
      - disable_two_factor_auth : Disables two factor auth (Also requires TOTP).
      - profile_image : Returns profile image url (if logged in).
