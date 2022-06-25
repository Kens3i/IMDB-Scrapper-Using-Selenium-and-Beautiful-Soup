#Developed By Kens

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select

driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.imdb.com/")
time.sleep(2)

#clicking the all button
dropdown= driver.find_element_by_id("iconContext-arrow-drop-down")
dropdown.click()
time.sleep(1)
#advanced search
element= driver.find_element_by_link_text("Advanced Search")
element.click()
time.sleep(1)

#clciking the advanced title search
adv= driver.find_element_by_link_text("Advanced Title Search")
adv.click()
time.sleep(1)

#selecting the movie types
feature_film=driver.find_element_by_id("title_type-1")
feature_film.click()

tv_movie=driver.find_element_by_id("title_type-2")
tv_movie.click()

#writing the dates
min_date=driver.find_element_by_name("release_date-min")
min_date.click()
min_date.send_keys("2000")

max_date=driver.find_element_by_name("release_date-max")
max_date.click()
max_date.send_keys("2022")

#selecting the ratings
rating_min=driver.find_element_by_name("user_rating-min")
rating_min.click()
dropdown2=Select(rating_min)
dropdown2.select_by_visible_text("7.0")

rating_max=driver.find_element_by_name("user_rating-max")
rating_max.click()
dropdown3=Select(rating_max)
dropdown3.select_by_visible_text("10")

#selecting that the movie should not be black and white
colour = driver.find_element_by_id("colors-1")
colour.click()

#selecting the language should be english
language=driver.find_element_by_name("languages")
dropdown4=Select(language)
dropdown4.select_by_visible_text("English")

#selecting the information to be displayed on 1 page
results_count=driver.find_element_by_id("search-count")
results_count.click()
dropdown5=Select(results_count)
dropdown5.select_by_visible_text("250 per page")

#clicking the submit button
submit= driver.find_element_by_xpath('//*[@id="main"]/p[3]/button')
submit.click()

#storing the current url
current_url=driver.current_url

#################################################################

#CODE FOR BS4
from bs4 import BeautifulSoup
import requests

#accessing the url
response = requests.get(current_url)

#soup object
soup=BeautifulSoup(response.content,"html.parser")

#results items (starting point)
list_items= soup.find_all("div",{"class":"lister-item-content"})

#data we need to extract

titles=[]
years=[]
durations=[]
genres=[]
ratings=[]

for item in list_items:
    # movie title
    titles.append(item.find("h3").find('a').get_text())

    # year
    years.append(item.find("span", {"class": "lister-item-year text-muted unbold"}).get_text().replace("(", "").replace(")", ""))

    # duration
    # used try and catch to omit the AttributeError as some durations are not present
    try:
        temp=item.find("span", {"class": "runtime"}).get_text()
        durations.append(temp)
    except AttributeError:
        durations.append("NA")

    # genre
    genres.append(item.find("span", {"class": "genre"}).get_text().strip().replace("\n",""))

    # rating
    ratings.append(float(item.find("div", {"class": "inline-block ratings-imdb-rating"}).strong.get_text()))

#Converting the scrapped data into an .xlsx file
import pandas as pd

imdb_df=pd.DataFrame({"Movie Title":titles, "Year":years, "Duration":durations, "Genre/Genres":genres, "Rating":ratings})

imdb_df.to_excel("imdb_data.xlsx", index=False)

#Subscribe to Learn with Kens :)