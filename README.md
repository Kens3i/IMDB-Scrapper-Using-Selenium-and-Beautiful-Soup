
# IMDB SCRAPPER
## A Scraping bot made with the help of Selenium and Beautiful Soup 🤖

![](https://media1.giphy.com/media/U71a32kq0bcVGVOcuF/giphy.gif?cid=790b76110b651b13cdc503fb4421c041d20b6cbaac531763&rid=giphy.gif&ct=s)

## Table of Contents

1.  [Overview](#Overview)
 
2.  [Libraries Used](#Libraries-Used)
3.  [Workflow](#Workflow)
4.  [Screesnshots](#Screesnshots)
5.  [Challenges](#Challenges)

## Overview

This program has 2 parts. The first part is a automation bot made with the help of Selenium which opens a Google Chrome tab and navigates to the IMDB home page. Then it goes to the advanced search and selects different parameters to filter some movies. Then in the 2nd part I developed a web-scrapper which scraps the data of those movies like the title, the year in which it got released, the rating of the movie, etc.


## Libraries-Used

-   `selenium`
-   `time`
-   `bs4`
-   `requests`
-   `pandas`

## Workflow

The following workflow is for the selenium bot.

- **Visiting** https://www.imdb.com/.
- **Cliking** on the "all" button and selecting the "advanced search" button.
- **Cliking** "advanced title search" button.
- **Ticking** on the "feature film" and "tv_movie" in the "mvoie type" section.
- **Writing** the dates so that the filter will select movies realeased from 2000 to 2022.
- **Selecting** the ratings in such a way that the movie should be betweeen a rating of 7.0 and 10.0.
- **Selecting** those movies which are not black and white.
- **Clicking** the submit button
- **Saving** the url to use for scraping.

Finally the following workflow is for scraping the data.
- **Accessing** the url which was saved before using the `requests` library.
- **Scraping** the movie titles, the year of release, the total duration , the genre and the rating of the movie.
- **Converting** the scrapped data to .xlsx file using the `pandas` library.

## Screenshots

- Automation using Selenium

![](https://github.com/Kens3i/IMDB-Scrapper-Using-Selenium-and-Beautiful-Soup/blob/main/Gifs/imdb%20scrapper%20gif%201.gif?raw=true)


- Result After Scrapping Using Beautiful Soup

![](https://github.com/Kens3i/IMDB-Scrapper-Using-Selenium-and-Beautiful-Soup/blob/main/Gifs/imdb%20scrapper%20gif%202.gif?raw=true)


## Challenges

- Had some difficulties selecting the HTML elements so had to use XPath in those cases.
- There were some AttributeErrors so had to use try catch block to overcome it.

### Thankyou For Spending Your Precious Time Going Through This Project!
### If You Find Any Value In This Project Or Gained Something New Please Do Give A ⭐.
