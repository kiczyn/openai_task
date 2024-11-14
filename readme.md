# HTML AI Generator Recruitment Task
This is a Python program that generates an HTML file from a text file using the OpenAI API.

## How It Works
1. Downloads the text file from [this link](https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt),
2. Retrieves the API key from the `.env` file,
3. Creates an API request,
4. Saves the API response to an HTML file.

# Installation

Requires [Python](https://www.python.org/) to run.

1. Create a `.env` file and add `OPENAI_API_KEY=<your API key>` to it,
2. Run:
   ```
   pip install -r requirements.txt
   ```
3. Run:
   ```
   python openapp.py
   ```