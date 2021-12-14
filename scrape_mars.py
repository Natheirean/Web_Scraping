#Dependancies
from bs4 import BeautifulSoup as bsoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    mars_data_return = {}
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    url = "https://redplanetscience.com/"
    browser.visit(url)
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text
    mars_data_return['news_title']=news_title
    mars_data_return['news_paragraph']=news_p

    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    browser.links.find_by_partial_text('FULL IMAGE').click()
    html = browser.html
    soup = bsoup(html, 'html.parser')
    imgsrc = soup.find('img', class_='fancybox-image').get('src')
    image_path = url+imgsrc
    mars_data_return['feature_image']=image_path

    url = "https://galaxyfacts-mars.com/"
    browser.visit(url)

    html = browser.html
    htmltables = pd.read_html(html)
    mars_data_df = htmltables[1]
    mars_data_df.columns=['Measurement', 'Value']
    mars_html = mars_data_df.to_html()
    mars_html = mars_html.replace('\n','')
    mars_data_return['data_table']=mars_html

    hemisphere_images = []
    url = "https://marshemispheres.com/"
    browser.visit(url)

    browser.links.find_by_partial_text('Cerberus').click()

    html = browser.html
    soup = bsoup(html, 'html.parser')
    hemtitle = soup.find('h2', class_='title').text
    hemimage = soup.find('img', class_='wide-image').get('src')
    hemurl = url + hemimage
    hemisphere = {'title': hemtitle, 'img_url': hemurl }
    hemisphere_images.append(hemisphere)

    browser.visit(url)
    browser.links.find_by_partial_text('Schiaparelli').click()

    html = browser.html
    soup = bsoup(html, 'html.parser')
    hemtitle = soup.find('h2', class_='title').text
    hemimage = soup.find('img', class_='wide-image').get('src')
    hemurl = url + hemimage
    hemisphere = {'title': hemtitle, 'img_url': hemurl }
    hemisphere_images.append(hemisphere)

    browser.visit(url)
    browser.links.find_by_partial_text('Syrtis').click()

    html = browser.html
    soup = bsoup(html, 'html.parser')
    hemtitle = soup.find('h2', class_='title').text
    hemimage = soup.find('img', class_='wide-image').get('src')
    hemurl = url + hemimage
    hemisphere = {'title': hemtitle, 'img_url': hemurl }
    hemisphere_images.append(hemisphere)

    browser.visit(url)
    browser.links.find_by_partial_text('Valles').click()
    html = browser.html
    soup = bsoup(html, 'html.parser')
    hemtitle = soup.find('h2', class_='title').text
    hemimage = soup.find('img', class_='wide-image').get('src')
    hemurl = url + hemimage
    hemisphere = {'title': hemtitle, 'img_url': hemurl }
    hemisphere_images.append(hemisphere)
    browser.quit()

    mars_data_return['hemisphere_imgs']=hemisphere_images

    return mars_data_return