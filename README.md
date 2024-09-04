# Project Name

## Project Overview
This project focuses on building a predictive model to forecast energy consumption for a commercial building using historical data. Key tasks include data preprocessing, feature engineering, and evaluating machine learning models like Linear Regression and Gradient Boosting. The goal is to select the best-performing model based on appropriate metrics, with clear documentation of the thought process throughout the project​.

## Setup Instructions
_TODO: Add setup instructions here._

## Usage
Jupyter Notebooks are in the "notebooks" directory: (1) Basic Exploratory Analysis, (2) Feature Engineering, (3) Model Building. The Project Structure is a placeholder for future deployment.

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

### 7. Feature Engineering: Based on Time and Chemical Engineering

This section details the various feature engineering techniques applied to enhance the predictive power of the model.

#### 1. Dimensionless Numbers
- **Temperature-Humidity Index (THI)**: A simple index that combines temperature and humidity to assess overall "thermal comfort" levels. It serves as a proxy for outdoor conditions, which can influence energy consumption.
- **Enthalpy**: The total heat content calculated from temperature and humidity, using psychrometric equations. Enthalpy provides a more physically meaningful feature for energy consumption prediction.

#### 2. Relative Humidity
- **Relative Humidity (%)**: A critical factor for HVAC systems, as it affects both cooling and heating loads by reflecting the moisture content in the air.

#### 3. Dew Point
- **Dew Point Temperature**: Calculated from temperature and relative humidity, dew point indicates the temperature at which air becomes saturated with moisture. This feature influences cooling requirements.

#### 4. Lagging Variables
- **Lagged Temperature and Humidity**: Lagged versions of temperature and humidity readings (e.g., t-1, t-2, ..., t-5) capture delayed effects of outdoor conditions on indoor energy consumption.
- **Rolling Averages**: Calculated over various time windows (e.g., 1 hour, 3 hours, 6 hours) to smooth the data and capture underlying trends.
- **Exponential Moving Averages (EMA)**: EMA gives more weight to recent readings while still considering past data, allowing for a dynamic smoothing effect.

#### 5. Rate of Change
- **Rate of Change**: The first derivative of temperature and humidity, which captures how quickly outdoor conditions change. Rapid changes may have a different impact on energy consumption compared to gradual changes.

#### 6. Interaction Features
- **Temperature × Humidity**: Interaction terms that capture non-linear effects influencing energy consumption.
- **Temperature² and Humidity²**: Squared terms to model potential non-linear relationships between these features and energy consumption.

#### 7. Psychrometric Properties
- **Wet-Bulb Temperature**: Calculated using psychrometric charts, wet-bulb temperature is essential for HVAC design and operation.
- **Specific Humidity**: A measure of water vapor content in the air, offering a more stable feature compared to relative humidity.

#### 8. Time-Based Features
- **Time of Day**: Energy consumption may follow diurnal patterns, so features like the hour of the day are included.
- **Day of Week/Weekend Indicator**: Differentiating between weekdays and weekends to account for variations in energy consumption.

#### 9. Cumulative Features
- **Cumulative Degree Days**: Heating degree days (HDD) and cooling degree days (CDD) are accumulated over time to capture overall heating or cooling demand leading up to each time point.

## Additional Sections
_TODO: Add any other important sections here._
