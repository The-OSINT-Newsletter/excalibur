# Excalibur

Excalibur is a powerful OSINT (Open Source Intelligence) tool designed to assist in the collection and analysis of social media profiles. It checks if a Twitter username is archived and fetches profiles from various social media platforms, including Product Hunt, Medium, and Mastodon.

## Features

- **Twitter Archive Check**: Verify if a Twitter username is archived.
- **Profile Fetching**: Retrieve profiles from Product Hunt, Medium, and Mastodon.
- **User-Friendly CLI**: Easy-to-use command-line interface for quick operations.

## Installation

To install Excalibur, follow these steps:

1. Clone the repository:
```
git clone https://github.com/The-OSINT-Newsletter/excalibur.git
```
2. Navigate to the project directory:
```
cd excalibur
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage

To use Excalibur, run the main script `cli.py` from the command line:
```
python cli.py --u [username]
```

Replace `[username]` with the the username of a Twitter (X) profile.

## License

Excalibur is released under the MIT License.
