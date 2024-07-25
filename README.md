# dialogue-generator
Text Generator
==============

This is a Streamlit app that generates text based on a trigram model trained on Sherlock Holmes stories.

Features:
- Text generation using a trigram model
- Dynamic user interface with Streamlit
- Customizable input text and output length

Installation:
1. Ensure you have Python 3.7+ installed on your system.
2. Clone this repository or download the project files.
3. Install the required packages by running:
   pip install streamlit

Usage:
1. Make sure the 'sherlock.txt' file is in the same directory as 'app.py' and 'text_generator.py'.
2. Open a terminal or command prompt in the project directory.
3. Run the Streamlit app with the command:
   streamlit run app.py
4. Your default web browser should open automatically to the app. If not, go to http://localhost:8501 in your browser.
5. Enter your starting text (at least two words) in the input field.
6. Use the slider to select the number of words you want to generate.
7. Click the "Generate Text" button to see the result.

Files:
- app.py: The main Streamlit application
- text_generator.py: Core functionality for text generation
- sherlock.txt: Training data (Sherlock Holmes stories)

How it works:
The app uses a trigram model trained on Sherlock Holmes stories. It generates text by predicting the next word based on the previous two words. If a particular word combination is not found in the training data, it randomly selects a word from the vocabulary.

Troubleshooting:
- If you encounter a "file not found" error, ensure that 'sherlock.txt' is in the same directory as 'app.py'.
- Make sure all required packages are installed.

Contributing:
Contributions are welcome! Feel free to submit pull requests or open issues for bugs and feature requests.

License:
This project is open source and available under the MIT License.

