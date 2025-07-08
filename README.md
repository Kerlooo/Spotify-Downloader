# Spotify Downloader

A Python-based Spotify music downloader that uses user authentication to download tracks, albums, and playlists with improved reliability and speed.

## Features

- **User Authentication**: Uses your Spotify account credentials to avoid rate limits
- **Multiple Formats**: Support for mp3, flac, ogg, opus, m4a, wav
- **Organized Output**: Automatically organizes downloads by artist and album
- **High Quality**: Configurable bitrate settings for mp3 format
- **Batch Download**: Download entire albums and playlists
- **Saved Songs**: Download your Spotify "Saved Songs" playlist

## Prerequisites

- Python 3.7 or higher
- A Spotify account
- Internet connection

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/Kerlooo/Spotify-Downloader.git
cd Spotify-Downloader
```

### 2. Set up Python environment

#### On Linux/macOS:
```bash
python3 -m venv myenv
source myenv/bin/activate
pip install spotdl
```

#### On Windows:
```bash
python -m venv myenv
myenv\Scripts\activate
pip install spotdl
```

### 3. Run the downloader
```bash
python downloader_auth.py
```
or
```bash
python3 downloader_auth.py
```

## Usage

1. **Start the application**: Run `python downloader_auth.py` / `python3 downloader_auth.py`
2. **Enter Spotify URL**: Provide a track, album, or playlist URL from Spotify
3. **Choose format**: Select your preferred audio format (default: mp3)
4. **Set bitrate** (for mp3): Choose quality (128k, 192k, 320k - default: 320k)
5. **Authenticate**: On first run, you'll be prompted to authenticate with Spotify
6. **Download**: Confirm and wait for the download to complete

### Supported URL Types

- **Track**: `https://open.spotify.com/track/...`
- **Album**: `https://open.spotify.com/album/...`
- **Playlist**: `https://open.spotify.com/playlist/...`
- **Saved Songs**: Use `saved` as the URL to download your saved songs

### Output Structure

Downloads are automatically organized in the following structure:
```
song/
├── Artist Name/
│   └── Album Name/
│       ├── Artist Name - Track 1.mp3
│       ├── Artist Name - Track 2.mp3
│       └── ...
```

## Authentication

This version uses Spotify user authentication to:
- Avoid rate limiting issues
- Download faster and more reliably
- Access your saved songs and private playlists

On first use, you'll be guided through the authentication process:
1. Open the provided link in your browser
2. Log in with your Spotify account
3. Authorize the application
4. Credentials are automatically saved for future use

## Troubleshooting

### Common Issues

**spotdl not found**: Install it with `pip install spotdl`

**Authentication errors**: 
- Ensure you have a valid Spotify account
- Check your internet connection
- Try running the script again

**Rate limiting**: 
- This version uses authentication to minimize rate limits
- If you encounter rate limits, wait a moment and try again

**Invalid URL**: 
- Make sure the URL is from Spotify
- Podcast URLs are not supported
- Ensure the URL is complete and valid

## Legal Notice

This tool is for personal use only. Please respect copyright laws and Spotify's terms of service. Only download music you own or have permission to download.

## Contributing

Feel free to submit issues and enhancement requests!

## Next Updates
- [ ] Create a GUI
- [ ] Better download speed 
- [ ] Fix Rate Limit