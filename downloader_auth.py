import os
import subprocess
import sys
import time

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
    
    # Set output format to organize by artist and album
    output_dir = os.path.join("song", "{artist}", "{album}")
    output_template = os.path.join("song", "{artist}", "{album}", "{artist} - {title}.{output-ext}")
    os.makedirs("song", exist_ok=True)
    output_option = ["--output", output_template]
    
    # Options to handle rate limits with authentication
    auth_options = [
        "--user-auth",        # Enable user authentication
        "--max-retries", "5", # Reduce retries because auth requires fewer
        "--threads", "4"      # Increase threads because auth allows it
    ]
    
    print("\nDownload summary:")
    print(f"- Spotify URL: {spotify_url}")
    print(f"- Output directory: {output_dir}")
    print(f"- Format: {format_choice}")
    if format_choice == "mp3":
        print(f"- Bitrate: {bitrate}")
    print("- Authentication: enabled (user account)")
    print("- Rate limit handling: improved with user auth")
    
    print("\nIMPORTANT: If this is your first time using authentication:")
    print("   1. You will be asked to open a link in your browser")
    print("   2. Log in with your Spotify account")
    print("   3. Authorize the application")
    print("   4. Credentials will be saved automatically")
    
    confirm = input("\nStart download? (y/n): ").lower()
    if confirm != "y":
        print("Download canceled.")
        return False
    
    print("\nStarting download with user authentication...")
    print("Note: This will be much faster and more reliable than the non-auth version.")
    
    try:
        command = ["spotdl", spotify_url] + format_option + bitrate_option + output_option + auth_options
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
        
        for line in process.stdout:
            print(line, end='')
            # With authentication, rate limits should be much less frequent
            if "rate/request limit" in line:
                print("\nRate limit detected (rare with authentication). Waiting...")
                time.sleep(1)
        
        process.wait()
        
        if process.returncode == 0:
            print("\nDownload completed successfully!")
            print("Pro tip: Now that you have configured authentication, you can use this program")
            print("to download your 'Saved Songs' using 'saved' as the URL!")
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
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Spotify Downloader - Authentication Version")
    print("=" * 50)
    print("This version uses your Spotify account authentication")
    print("to avoid rate limit issues and download faster.")
    print("=" * 50)
    
    download_track()

if __name__ == "__main__":
    main() 