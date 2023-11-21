# Project Name: Weekly Track Roundup Songs Database

## Overview

This project is designed to create a database of links to songs featured in the video series "Weekly Track Roundup" by @theneedledrop channel on YouTube (https://www.youtube.com/@theneedledrop).
It does so by scraping the links of songs using Youtube Data API v3 from the description of the videos featured in the "Weekly Track Roundup" playlist. The gathered information is then stored in a database. 
To access Youtube Data API v3 it's required to create a project, enable the API and create a developer key (https://console.cloud.google.com/). Instructions can be found at https://developers.google.com/youtube/v3/getting-started
Additionally, there is a module that creates a YouTube playlist with youtube links extracted from the database. In the future, links from other sources (spotify,itunes,etc.) in the database will either be converted to youtube links or be displayed in a custom html page.

## Getting Started

### Prerequisites

Before running the project, make sure you have the following installed:

- Python 3.x
- Pip (Python package installer)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/JosePereira96/MusicDB.git
```

2. Navigate to the project directory:

```bash
cd MusicDB
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Configuration

1. Open the `config.ini` file.

2. Update the following parameters:

   - `user`: Replace with the user that connects to the database created previously.
   - `password`: Replace with the user's password.
   - `dbName`: Specify the name of the database previously created.
   - `developerKey`: Specify the developer key previously created.

## Usage

1. Run the scraper to gather information from the YouTube channel:

```bash
python fantanoScrapper.py
```

2. The scraper will populate the specified database with information such as videoID, URL and other relevant details.

3. Run the playlist creator to generate a YouTube playlist and open a web browser page:

```bash
python playlist.py
```

4. The playlist creator will use the information from the database to create a new unnamed playlist and automatically update the database to change the field "watched".

## Database Schema

The database will have a table named `links` with the following columns:

- `linkID` (auto-incremented)
- `ownerID` (ID of video which the song is featured)
- `url` (URL of the song)
- `watched` (describes if the user has listened to that song. updates when song is featured in a playlist)

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and suggestions are highly appreciated.


## Acknowledgments

- Thanks to the developers of the YouTube API and other dependencies used in this project.
- Special thanks to the open-source community for their valuable contributions.

Happy coding!