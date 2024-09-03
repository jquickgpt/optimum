import os

# Directory and file structure
project_structure = {
    "config": ["config.yaml", "config_prod.yaml"],
    "src": {
        "data": {
            "__init__.py": [],
            "load_data.py": [],
            "split_data.py": [],
            "transformers.py": [],
        },
        "features": ["__init__.py", "build_features.py"],
        "models": ["__init__.py", "train.py", "evaluate.py", "predict.py"],
        "pipeline": ["__init__.py", "pipeline.py"],
        "utils": ["__init__.py", "logging.py", "metrics.py"],
    },
    "data": {
        "raw": [".gitkeep"],
        "processed": [".gitkeep"],
    },
    "notebooks": [".gitkeep"],
    "tests": ["test_data.py", "test_model.py", "test_pipeline.py"],
    "docs": ["index.md", "usage_guide.md"],
    "scripts": [".gitkeep"],
    "models": [".gitkeep"],
    "docker": ["Dockerfile"],
    "mlflow": ["mlflow_tracking.py"],
    "fastapi": ["app.py", "routes.py"],
    "infra": [".gitkeep"],
    "ci": [".gitkeep"],
}

# Function to create directories and files


def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, list):  # It's a list of files
            os.makedirs(path, exist_ok=True)
            for file_name in content:
                with open(os.path.join(path, file_name), 'w') as f:
                    pass  # Create empty file
        elif isinstance(content, dict):  # It's a sub-directory structure
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            os.makedirs(path, exist_ok=True)  # Create directory


# Create the project structure in the current directory
current_directory = os.getcwd()
create_structure(current_directory, project_structure)

# Create the README.md file
readme_content = """# Project Name

## Project Overview
_TODO: Add project overview here._

## Setup Instructions
_TODO: Add setup instructions here._

## Usage
_TODO: Add usage instructions here._

## Project Structure

### 1. Project Root Directory
- **README.md**: Project overview, setup instructions, and usage.
- **requirements.txt**: List of Python dependencies.
- **.gitignore**: Files and directories to be ignored by Git.
- **config/**: Configuration files (e.g., YAML, JSON) for different environments (development, production, etc.).
  - `config.yaml`
  - `config_prod.yaml`
- **src/**: Source code for the project.
- **data/**: Folder for datasets and raw data.
  - `raw/`
  - `processed/`
- **notebooks/**: Jupyter notebooks for experimentation and exploratory data analysis.
- **tests/**: Unit and integration tests.
- **docs/**: Project documentation.
- **scripts/**: Utility scripts for tasks like data processing or model deployment.
- **models/**: Saved model files.
- **docker/**: Docker-related files.
- **ci/**: Continuous Integration scripts and configurations (e.g., for GitHub Actions, Jenkins).

### 2. `src/` Directory Structure
- **data/**: Data handling and preprocessing.
  - `__init__.py`
  - `load_data.py`: Functions to load and preprocess data.
  - `split_data.py`: Functions to split data into training, validation, and test sets.
  - `transformers.py`: Custom data transformers and feature engineering.
- **features/**: Feature engineering code.
  - `__init__.py`
  - `build_features.py`: Functions for feature creation.
- **models/**: Model building and training scripts.
  - `__init__.py`
  - `train.py`: Code to train models.
  - `evaluate.py`: Functions to evaluate model performance.
  - `predict.py`: Functions to make predictions using the trained model.
- **pipeline/**: End-to-end pipeline scripts.
  - `__init__.py`
  - `pipeline.py`: Code to define and run the machine learning pipeline.
- **utils/**: Utility functions and helpers.
  - `__init__.py`
  - `logging.py`: Functions to set up and handle logging.
  - `metrics.py`: Custom metrics and evaluation functions.

### 3. Deployment
- **docker/**: Docker files for containerization.
  - `Dockerfile`: Docker configuration.
- **mlflow/**: MLflow tracking for experiment logging and model versioning.
  - `mlflow_tracking.py`: MLflow setup and logging scripts.
- **fastapi/**: FastAPI setup for deploying the model as a REST API.
  - `app.py`: Main application script.
  - `routes.py`: API route definitions.
- **infra/**: Infrastructure as Code (IaC) for cloud deployment.
  - `terraform/` or `cloudformation/`: Scripts to set up cloud infrastructure (e.g., AWS, Azure).

### 4. Testing
- **tests/**: Testing scripts for unit tests, integration tests, and end-to-end tests.
  - `test_data.py`: Tests for data loading and processing.
  - `test_model.py`: Tests for model training and prediction.
  - `test_pipeline.py`: Tests for the entire ML pipeline.

### 5. Continuous Integration/Continuous Deployment (CI/CD)
- **ci/**: Configuration for CI/CD.
  - `github_actions/`: GitHub Actions workflows.
  - `jenkins/`: Jenkins pipeline scripts.
  - `pre-commit-config.yaml`: Pre-commit hooks for code linting and formatting.

### 6. Documentation
- **docs/**: Detailed project documentation, API documentation, and guides.
  - `index.md`: Main documentation file.
  - `api/`: Auto-generated API docs (e.g., from FastAPI).
  - `usage_guide.md`: Instructions on how to use the model and API.

## Additional Sections
_TODO: Add any other important sections here._
"""

# Write the README.md file
with open(os.path.join(current_directory, "README.md"), "w") as f:
    f.write(readme_content)

print(f"Project structure has been created in the root directory.")
