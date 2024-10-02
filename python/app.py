from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Song:
    def __init__(self, title, authors, duration, album) -> None:
        self.title = title,
        self.authors = authors,
        self.duration = duration,
        self.album = album

    def get_title(self):
        return self.title

def search_from_spotify_album(url):
    songs = []
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)

    for element in driver.find_elements(By.XPATH, '//*[@id="main"]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/main/section/div[4]/div[1]/div[2]/div[2]/div'):
        title = element.find_element(By.XPATH, './div/div/div[2]/div/a/div').text
        authors = []
        for author in element.find_elements(By.XPATH, './div/div/div[2]/div/span'):
            if author.text not in ["E", ", "]:
                authors.append(author.text)
        duration = element.find_element(By.XPATH, './div/div/div[3]/div').text
        album = element.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[4]/div[1]/div[2]/div[2]/div/main/section/div[1]/div[3]/div[3]/span[2]/h1').text
        songs.append(Song(title, authors, duration, album))
    driver.quit()
    return songs

def search_song_at_youtube(song):
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")
    time.sleep(2)
    search_box = driver.find_element(By.XPATH, '//*[@id="search"]')
    search_box.send_keys("vegetta")
    # search_box.send_keys(Keys.RETURN)
    # time.sleep(1)
    # for song_yt in driver.find_elements(By.XPATH, '//*[@id="contents"]/ytd-video-renderer'):
    #     if song.title in song_yt.text:
    #         return song_yt.get_attribute("href")
    # driver.quit()
    return ""

def download_link_song(link):
    driver = webdriver.Chrome()
    driver.get("https://mp3-juices.nu/p1aL/")
    time.sleep(1)
    search_box = driver.find_element(By.XPATH, '//*[@id="query"]')
    search_box.send_keys(link)
    search_box.click()
    time.sleep(1)
    search_box.send_keys(Keys.RETURN)
    time.sleep(1)
    download_button = driver.find_element('//*[@id="result_1"]/div[2]/a[1]')
    download_button.click()
    time.sleep(2)
    download_button = driver.find_element('//*[@id="1"]')
    download_button.click()
    time.sleep(5)

# songg = Song(("Sacrificio"), (["Taini"]), ("2:29"), "DATA")
# print(search_song_at_youtube(songg))

download_link_song("https://www.youtube.com/watch?v=kLpH1nSLJSs")