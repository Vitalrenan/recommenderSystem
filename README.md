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
```bash
git clone https://github.com/Vitalrenan/recommenderSystem.git
cd recommenderSystem```

2. Create and activate a virtual environment (optional but recommended):
python3 -m venv env
source env/bin/activate # On Windows, use `env\Scripts\activate`
3. Install the required dependencies:
pip install -r requirements.txt
Usage
To run the recommender system application locally:
python app.py
This will start the application, and you can interact with the recommender system as per the implemented interface.
Data Ingestion
The ingestion/ directory contains scripts responsible for data ingestion and preprocessing. To ingest and preprocess data:
1. Place your raw data files into the data/ directory.
2. Run the appropriate ingestion script:
python ingestion/your_ingestion_script.py
Replace your_ingestion_script.py with the actual script name.
Model Training
Training the recommender model involves:
1. Preparing the data using the ingestion scripts.
2. Running the training module located in the recommender/ directory:
python recommender/train_model.py
Ensure that the training script name matches the actual file in the directory.
Evaluation
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
• Option 1: Set as an Environment Variable
• Before launching Jupyter Notebook, set the OPENAI_API_KEY environment variable in your terminal:
export OPENAI_API_KEY='your-api-key' # On Unix/macOS
set OPENAI_API_KEY='your-api-key' # On Windows
• Then, start Jupyter Notebook:
jupyter notebook
• Option 2: Use a .env File
• Install the python-dotenv package:
pip install python-dotenv
• Create a .env file in the root directory of the project and add your API key:
OPENAI_API_KEY=your-api-key
• In your notebooks, load the environment variables:
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
• Option 3: Set Within the Notebook (Less Secure)
• Directly assign the API key in a notebook cell:
import openai
openai.api_key = 'your-api-key'
• Caution: This method exposes your API key within the notebook and is not recommended for shared environments.
Important: Keep your API key secure and avoid exposing it in public repositories or shared environments.
Contributing
Contributions are welcome! If you’d like to contribute:
1. Fork the repository.
2. Create a new branch:
git checkout -b feature/your_feature_name
3. Make your changes and commit them:
git commit -m "Add your message here"
4. Push to the branch:
git push origin feature/your_feature_name
5. Open a pull request detailing your changes.
License
This project is licensed under the MIT License. See the LICENSE file for more details.
**Notes:**
- Replace `'your-api-key'` with your actual OpenAI API key.
- Ensure that the script names (`your_ingestion_script.py`, `train_model.py`) match the actual filenames in your repository.
- Update any placeholders with specific information relevant to your project.
- Consider adding sections such as "Background," "Features," or "Acknowledgments" as needed
