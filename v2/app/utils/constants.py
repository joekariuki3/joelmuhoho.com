class PasswordConstants:
    MIN_PASSWORD_LENGTH = 3
    MAX_PASSWORD_LENGTH = 32
    PASSWORD_REQUIRED_MESSAGE = "Password is required"
    PASSWORD_ERROR_MESSAGE = "Password must be at least {MIN_PASSWORD_LENGTH} characters long."
    CONFIRM_PASSWORD_ERROR_MESSAGE = "Passwords do not match"
    CONFIRM_PASSWORD_REQUIRED_MESSAGE = "Confirm password is required"

class EmailConstants:
    EMAIL_REQUIRED_MESSAGE = "Please enter your email address."
    EMAIL_ERROR_MESSAGE = "Please enter a valid email address."

class NameConstants:
    FIRST_NAME_REQUIRED_MESSAGE = "Please enter your first name."
    LAST_NAME_REQUIRED_MESSAGE = "Please enter your last name."

    USERNAME_REQUIRED_MESSAGE = "Please enter your username."
    USERNAME_PLACEHOLDER = "Username"

class ProjectConstants:
    TITLE = {"ADD": "Add Project", "EDIT": "Edit Project"}
    PROJECT_NAME_REQUIRED_MESSAGE = "Project Name/Title is required."
    PROJECT_NAME_PLACEHOLDER = "Project Name or Title"

    PROJECT_DESCRIPTION_REQUIRED_MESSAGE = "Project description is required."
    PROJECT_DESCRIPTION_PLACEHOLDER = "Project Description"

    PROJECT_CATEGORY_REQUIRED_MESSAGE = "Project category is required."
    PROJECT_CATEGORY_PLACEHOLDER = "Please select a category for your project."

    PROJECT_IMAGE_URL_PLACEHOLDER = "Project Image URL"

    PROJECT_DEMO_URL_PLACEHOLDER = "Project Demo URL"

    PROJECT_GITHUB_URL_PLACEHOLDER = "Project GitHub URL"

class CategoryConstants:
    TITLE = {"ADD": "Add Category", "EDIT": "Edit Category"}
    CATEGORY_NAME_REQUIRED_MESSAGE = "Category name is required."
    CATEGORY_NAME_PLACEHOLDER = "Category Name"

class RoleConstants:
    ROOT = "root"
    DEFAULT = "default"
    ADMIN = "admin"
    USER = "user"
    ROLES = [ADMIN, USER]

    TITLE = {"ADD": "Add Role", "EDIT": "Edit Role"}
    ROLE_REQUIRED_MESSAGE = "Role name is required."
    ROLE_PLACEHOLDER = "Role Name"
    ROOT_USER_REQUIRED_MESSAGE = "ROOT user details not provided in .env file, ROOT_FIRST_NAME, ROOT_LAST_NAME, ROOT_EMAIL, ROOT_PASSWORD are required"

class RegistrationConstants:
    TITLE = {"ADD": "Add User", "EDIT": "Edit User"}
    PROFESSION_PLACEHOLDER = "Profession"
    BIO_PLACEHOLDER = "Bio"
    GITHUB_URL_PLACEHOLDER = "GitHub URL"
    LINKEDIN_URL_PLACEHOLDER = "LinkedIn URL"
    TWITTER_URL_PLACEHOLDER = "Twitter URL"
    PROFILE_IMAGE_URL_PLACEHOLDER = "Profile Image URL"