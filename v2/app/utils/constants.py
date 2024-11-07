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