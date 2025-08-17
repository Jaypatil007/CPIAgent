# CPIGent CLI

CPIGent CLI is a powerful, interactive command-line interface for communicating with Google's Gemini large language models and interacting with CPI artifacts.

Built with Python, Typer, and Rich, it provides a beautiful and intuitive user experience directly in your terminal, complete with command autocompletion, syntax highlighting, and Markdown rendering.

## Features

- **Interactive Chat:** Engage in a conversation with the Gemini Pro model.
- **CPI Integration:** Authenticate and interact with CPI packages and artifacts.
- **Rich Output:** Responses are beautifully rendered with support for Markdown, tables, and syntax-highlighted code.
- **Smart Command System:** Use `!` commands to control the CLI without interrupting your conversation.
- **Configuration Management:** Easily manage your API key and model from the terminal or within the chat.

## Getting Started

### Prerequisites

- Python 3.8+
- A Google Gemini API Key. You can get one from [Google AI Studio](https://aistudio.google.com/).
- Access credentials for your CPI instance.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Jaypatil007/CPIAgent.git
    cd CPIAgent/CPIGent-CLI
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

Before running the application, you need to configure two essential files in the `CPIGent-CLI` directory.

1.  **Create the Credentials File (`credentials.json`)**

    This file stores the OAuth details required to connect to your CPI instance. Create a file named `credentials.json` and add the following content, replacing the placeholder values with your actual credentials:

    ```json
    {
      "oauth": {
        "clientid": "YOUR_CPI_CLIENT_ID",
        "clientsecret": "YOUR_CPI_CLIENT_SECRET",
        "tokenurl": "YOUR_CPI_TOKEN_URL",
        "url": "YOUR_CPI_API_BASE_URL"
      }
    }
    ```

2.  **Create the Environment File (`.env`)**

    This file is used to store your Google Gemini API key securely. Create a file named `.env` and add your key:

    ```
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
    ```
    The application will automatically load this key on startup.

## Usage

### Starting a Chat Session

To begin your conversation with the AI, run:
```bash
python main.py chat
```
This launches the interactive prompt. Simply type your question and press Enter.

### In-Chat Commands

In-chat commands give you control over the application without needing to exit. They are always prefixed with `!`.

-   **`!help`**: Displays a list of all available in-chat commands.
-   **`!config show`**: Shows the current model and confirms if the API key is set.
-   **`!config set model <MODEL_NAME>`**: Changes the Gemini model to use (e.g., `gemini-pro`).
-   **`!exit`** or **`!quit`**: Ends the chat session.
