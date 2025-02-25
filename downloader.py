import os
import subprocess
import sys

def check_spotdl_installation():
    try:
        subprocess.run(["spotdl", "--version"], capture_output=True)
        return True
    except FileNotFoundError:
        return False

def download_track():
    spotify_url = input("\nEnter the Spotify URL (track/album/playlist): ")
    if not spotify_url.strip() or "spotify.com" not in spotify_url or "spotify.com/show" in spotify_url:
        print("Invalid URL.")
        return False
    
    print("\nAvailable formats: mp3, flac, ogg, opus, m4a, wav")
    format_choice = input("Select format (default: mp3): ").lower() or "mp3"
    format_option = ["--format", format_choice]

    bitrate_option = []
    if format_choice == "mp3":
        bitrate = input("Bitrate quality (128k, 192k, 320k - default: 320k): ") or "320k"
        bitrate_option = ["--bitrate", bitrate]
    
    output_dir = "song"
    os.makedirs(output_dir, exist_ok=True)
    output_option = ["--output", output_dir]
    
    print("\nDownload summary:")
    print(f"- Spotify URL: {spotify_url}")
    print(f"- Output directory: {output_dir}")
    print(f"- Format: {format_choice}")
    if format_choice == "mp3":
        print(f"- Bitrate: {bitrate}")
    
    confirm = input("\nStart download? (y/n): ").lower()
    if confirm != "y":
        print("Download canceled.")
        return False
    
    print("\nStarting download...")
    try:
        command = ["spotdl", spotify_url] + format_option + bitrate_option + output_option
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
        
        for line in process.stdout:
            print(line, end='')
        
        process.wait()
        
        if process.returncode == 0:
            print("\nDownload completed successfully!")
        else:
            print(f"\nDownload finished with an error (code: {process.returncode})")
        
        return process.returncode == 0
    except Exception as e:
        print(f"Error during download execution: {e}")
        return False

def main():
    if not check_spotdl_installation():
        print("spotdl is not installed. Install it with 'pip install spotdl'")
        return
    
    download_track()

if __name__ == "__main__":
    main()