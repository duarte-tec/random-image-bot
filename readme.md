# Random Image Bot

This Python script automates posting random images to Twitter using the Tweepy library. The bot selects a random image from a specified folder, checks if a tweet has been made recently, and posts the image along with the file name as text.

## Table of Contents

- [Configuration](#configuration)
- [Features](#features)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [File Structure](#file-structure)

---

## Configuration <a name="configuration"></a>

Before running the bot, make sure to configure your Twitter API keys in the script:

```python
bearer_token = ''
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
```

Replace the empty strings with your actual Twitter API key values.

## Features <a name="features"></a>

- **Random Selection:** Randomly selects an image file from a specified folder.
- **Tweet Timing:** Ensures tweets are spaced out to comply with Twitter API rate limits.
- **State Tracking:** Keeps track of the timestamp of the last tweet to avoid rapid postings.

## Dependencies <a name="dependencies"></a>

The following Python libraries are required:

- `tweepy`: For interacting with the Twitter API.
- `os`: For file and directory operations.
- `random`: For random selection of files and folders.
- `time`: For time-related operations.
- `datetime`: For working with dates and times.

Make sure these libraries are installed using pip:

```bash
pip install tweepy
```

## Usage <a name="usage"></a>

1. **Clone the Repository:** Clone the repository or download the Python script.

2. **Install Dependencies:** Install the necessary dependencies as mentioned above.

3. **Configure Twitter API Keys:** Replace the empty fields in the script with your actual Twitter API keys.

4. **Set Up Folders:** Define the paths to the folders where your images are stored. Update the `folders` list with appropriate paths:

   ```python
   folders = [
       './path/to/your/folders/'
   ]
   ```

5. **Run the Script:** Execute the Python script:

   ```bash
   python main.py
   ```

6. **Continuous Execution:** The script runs continuously and posts a tweet approximately once an hour, depending on the configured wait intervals.

## File Structure <a name="file-structure"></a>

- `main.py`: The main Python script.
- `savestate.txt`: A text file used to store the timestamp of the last tweet to prevent rapid postings.
