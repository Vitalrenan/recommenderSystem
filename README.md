# Recommender System
This project implements a recommender system designed to provide personalized recommendations based on user data. The system leverages various data processing and machine learning techniques to analyze user preferences and suggest relevant items.
**Live Demo:** The project is deployed and accessible at [https://renanvital-aieng.streamlit.app/](https://renanvital-aieng.streamlit.app/)
## Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Ingestion](#data-ingestion)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Setting Up OpenAI API Key](#setting-up-openai-api-key)
- [Contributing](#contributing)
- [License](#license)
## Project Structure
The repository is organized as follows:
- `data/`: Contains datasets and related resources.
- `ingestion/`: Scripts and modules for data ingestion and preprocessing.
- `notebooks/`: Jupyter notebooks for experimentation and analysis.
- `recommender/`: Core modules implementing the recommender algorithms.
- `app.py`: Main application script to run the recommender system.
- `requirements.txt`: Lists the Python dependencies required for the project.
## Installation
To set up the project locally, follow these steps:
1. **Clone the repository:**
```
git clone https://github.com/Vitalrenan/recommenderSystem.git
cd recommenderSystem
```
2. Create and activate a virtual environment (optional but recommended):
```
python3 -m venv env
source env/bin/activate # On Windows, use `env\Scripts\activate`
```
4. Install the required dependencies:
```
pip install -r requirements.txt
```
Usage
To run the recommender system application locally:
```
python app.py
```
This will start the application, and you can interact with the recommender system as per the implemented interface.
##Data Ingestion
The ingestion/ directory contains scripts responsible for data ingestion and preprocessing. To ingest and preprocess data:
1. Place your raw data files into the data/ directory.
2. Run the appropriate ingestion script:
```
python ingestion/your_ingestion_script.py
```
Replace your_ingestion_script.py with the actual script name.
##Model Training
Training the recommender model involves:
1. Preparing the data using the ingestion scripts.
2. Running the training module located in the recommender/ directory:
```
python recommender/train_model.py
```
Ensure that the training script name matches the actual file in the directory.
##Evaluation
To evaluate the performance of the trained recommender model:
1. Use the evaluation scripts provided in the notebooks/ directory. These Jupyter notebooks contain code to assess model accuracy, precision, recall, and other relevant metrics.
2. Launch Jupyter Notebook:
jupyter notebook
3. Open the desired notebook and follow the instructions to evaluate the model.
Setting Up OpenAI API Key
Some notebooks in this project require access to the OpenAI API. To run these notebooks, you’ll need to set up your OpenAI API key:
1. Obtain an API Key:
• Sign up or log in to your OpenAI account.
• Navigate to the API section to generate a new API key.
2. Set the API Key in Your Environment:

• Directly assign the API key in a notebook cell:
import openai
openai.api_key = 'your-api-key'
• Caution: This method exposes your API key within the notebook and is not recommended for shared environments.
Important: Keep your API key secure and avoid exposing it in public repositories or shared environments.

##License
This project is licensed under the MIT License. See the LICENSE file for more details.

