from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from pytube import YouTube
import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox


class Song:
    def __init__(self, title, authors, duration, album) -> None:
        self._title = title
        self._authors = authors
        self._duration = duration
        self._album = album

    @property
    def title(self):
        return self._title

    @property
    def authors(self):
        return self._authors

    @property
    def duration(self):
        return self._duration

    @property
    def album(self):
        return self._album

def search_from_spotify_album(url):
    songs = []
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    for element in driver.find_elements(By.XPATH, '//*[@id="main"]/div/div[2]/div[4]/div/div[2]/div[2]/div/main/section/div[4]/div[1]/div[2]/div[2]/div'):
        title = element.find_element(By.XPATH, './div/div/div[2]/div/a/div').text
        authors = []
        for author in element.find_elements(By.XPATH, './div/div/div[2]/div/span'):
            if author.text not in ["E", ", "]:
                authors.append(author.text)
        duration = element.find_element(By.XPATH, './div/div/div[3]/div').text
        album = element.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[4]/div/div[2]/div[2]/div/main/section/div[1]/div[2]/div[2]/span[2]/h1').text
        songs.append(Song(title, authors, duration, album))
    driver.quit()
    return songs

def search_from_spotify_song(url):
    song = None
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)

    title = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[4]/div/div[2]/div[2]/div/main/section/div[1]/div[2]/div[3]/span[2]/h1').text
    author = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[4]/div/div[2]/div[2]/div/main/section/div[1]/div[2]/div[3]/div/div/span/a').text
    duration = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[4]/div/div[2]/div[2]/div/main/section/div[1]/div[2]/div[3]/div/span[6]').text
    album = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[4]/div/div[2]/div[2]/div/main/section/div[1]/div[2]/div[3]/div/span[2]/a').text

    return Song(title, author, duration, album)

def search_song_at_youtube(song):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")
    time.sleep(1)
    search_box = driver.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input')
    search_box.send_keys(song.title, song.authors[0])
    time.sleep(1)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    for song_yt in driver.find_elements(By.XPATH, '//*[@id="contents"]'):
        if (song.title.lower() in song_yt.text.lower()) and song.authors[0].lower() in song_yt.text.lower():
            return song_yt.find_element(By.XPATH, '//*[@id="thumbnail"]').get_attribute("href")
    driver.quit()
    return ""

def download_audio(video_url):
    """Downloads audio from a YouTube video as an MP3 file."""
    download_options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Output filename format
        'ffmpeg_location': "C:\\Program Files\\ffmpeg-master-latest-win64-gpl\\bin"  # Path to ffmpeg
    }
    
    with yt_dlp.YoutubeDL(download_options) as downloader:
        downloader.download([video_url])



def whole_process_album(url):
    raw_songs_from_spotify = search_from_spotify_album(url)
    for song in raw_songs_from_spotify:
        print(song.title, song.authors)
        try:
            download_audio(search_song_at_youtube(song))
        except Exception as e:
            pass

def whole_process_song(url):
    raw_song_from_spotify = search_from_spotify_song(url)
    print(raw_song_from_spotify.title, raw_song_from_spotify.authors)
    try:
        download_audio(search_song_at_youtube(raw_song_from_spotify))
    except Exception as e:
        pass

url_spotify_album = "https://open.spotify.com/album/2d9BCZeAAhiZWPpbX9aPCW?si=8soB9c8vQbuXVPqeNKDaEg"
url_spotify_song = "https://open.spotify.com/track/6d3q0F9VNtdxQUTVlRcet6?si=c881d45710e34596"

def start_download_song():
    url = url_entry.get()  # Get the URL from the Entry widget
    whole_process_song(url)

def start_download_album():
    url = url_entry.get()  # Get the URL from the Entry widget
    whole_process_album(url)

root = tk.Tk()
root.title("Spotify to YouTube MP3 Downloader")
root.geometry("400x250")

tk.Label(root, text="Enter Song or Album URL:").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Corrected Buttons with Lambda Functions
tk.Button(root, text="Download MP3 SONG", command=lambda: start_download_song()).pack()
tk.Button(root, text="Download MP3 ALBUM", command=lambda: start_download_album()).pack()

root.mainloop()