# config/settins.py

class LoginDetectionSettings:
    LOGN_INPUTS = [
        # ... (previous login inputs)
        'data-cy="password-input"',  # Another custom password input
        'id="user"',  # User ID input
        'id="login-form"',  # Login form identifier
        'data-test="login-btn"',  # Test-specific login button
        'data-qa="login-field"',  # Quality assurance login field
        'data-hook="password-input"',  # Password input hook
        'data-test-id="submit-button"',  # Test-specific submit button
        'id="user-login"',  # User login identifier
        'data-login="true"',  # Data attribute for login
        'name="login-email"',  # Login email input
        'data-test-id="login-form"',  # Test-specific login form
        'data-locator="login"',  # Data locator for login
        'data-selector="login-input"',  # Data selector for login input
        'data-key="login-input"',  # Data key for login input
        'class="login-element"',  # Class-based login element
        'data-input="user"',  # Data input for user
        'data-testid="login-password"',  # Test-specific login password input
        'data-automation-id="login-field"',  # Automation ID for login field
        'data-login="username"',  # Data attribute for username input
    ]


class SQLInjectionSettings:
    PAYLOADS = [
        # ... (previous payloads)
        "' OR 1=1 --",  # Another simple payload
        "' UNION SELECT NULL, user, password FROM users--",  # Retrieve user and password
        # ... (more payloads)
    ]

class RegexPatternSettings:
    ERRORS = {
        "MySQL": (
            # ... (MySQL error patterns)
        ),
        "PostgreSQL": (
            # ... (PostgreSQL error patterns)
        ),
        "Microsoft SQL Server": (
            # ... (Microsoft SQL Server error patterns)
        ),
        "Oracle": (
            # ... (Oracle error patterns)
        ),
        "IBM DB2": (
            # ... (IBM DB2 error patterns)
        ),
        "SQLite": (
            # ... (SQLite error patterns)
        ),
        "Informix": (
            # ... (Informix error patterns)
        ),
        "Sybase": (
            # ... (Sybase error patterns)
        )
    }
