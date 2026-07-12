# AlmaShines Signup Automation
Replace the generated email address with an accessible test email account to receive the OTP for manual verification (in test_signup.py) .

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)

## Project Structure

```text
.
├── pages/
│   └── signup.py
├── tests/
│   └── test_signup.py
├── conftest.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## Automated Test Cases

The following scenarios are automated:

- Existing user login flow
- New user signup flow
- Invalid email validation
- User details entry
- Role selection
- Year of Joining selection
- Year of Graduation selection
- Acceptance of Terms and Conditions

## Manual Test Cases

The following scenarios were tested manually:

- OTP verification
- Invalid OTP
- OTP resend
- OTP expiry
- Browser back/refresh behavior during signup

## Notes

1. A unique email address is generated for every signup test to avoid conflicts with existing accounts.
2. OTP verification is performed manually because the OTP is sent to the registered email address and no test mailbox or API was available.
3. The automation covers the required signup flow only. The optional profile completion steps after registration are outside the scope of this project.

## Setup

Clone the repository.

```text
git clone <repository-url>
cd <repository-name>
```

Create a virtual environment.

```text
uv venv
```

Activate the virtual environment.

Windows

```text
.venv\Scripts\activate
```

Install the dependencies.

```text
uv sync
```

## Run

Run all tests:

```text
pytest tests/
```
```text
pytest tests/test_signup.py
```

If the signup flow requires manual OTP entry:

```text
pytest -s tests/test_signup.py
```

