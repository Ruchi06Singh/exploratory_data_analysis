from tkinter import Widget
import streamlit as st

from time import time
from bs4 import BeautifulSoup
import requests

from streamlit_option_menu import option_menu

st.set_page_config(page_title="My Webpage", layout="wide")



# ---Header Sec---
st.title("Scrapy")
st.subheader("your own job scraper")
st.write("---")

# ---intro---
name = st.text_input("Enter your name")
st.write("We are glad to have you here", name)
st.write("---")

# ---user input---
familiar_skill = st.text_input("Enter a familiar skill")
unfamiliar_skill = st.text_input("Enter an unfamiliar skill ( if no un-familiar skills insert space/- )")

st.write('##')
st.write("filtering out jobs that fits you right")

def times_here():

    times = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords='+ familiar_skill).text
    # st.write(html_comtent)

    soup_times = BeautifulSoup(times,'lxml')
    # st.write(soup)

    jobs_times = soup_times.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for job_times in jobs_times:
        
        tcompany_name = job_times.find('h3', class_='joblist-comp-name').text.replace("\n","").replace("  ","")
        skills = job_times.find('span', class_='srp-skills').text.replace("\n","").replace("  ","")
        try:
            location = job_times.ul.find_all('li')[1].span.text
        except:
            location = job_times.ul.find_all('li')[2].span.text
        limk = job_times.header.h2.a['href']

        if unfamiliar_skill not in skills:
            # st.write(published_date)
            st.write(tcompany_name)
            st.write(skills)
            st.write(location)
            st.write(limk)
            st.write('---')


def shine_here():

    shine = requests.get('https://www.shine.com/job-search/'+ familiar_skill).text
    soup_shine = BeautifulSoup(shine,'lxml')

    jobs_shines = soup_shine.find_all('div', class_='jobCard_jobCard__jjUmu white-box-border jobCard')
    jobs_active_shines = soup_shine.find_all('div', class_='jobCard_jobCard__jjUmu active white-box-border jobCard')

    for job_shine in (jobs_active_shines+jobs_shines):

        scompany_name = job_shine.find('div', class_='jobCard_jobCard_cName__mYnow').text
        role = job_shine.find('h2', itemprop='name').text
        city = job_shine.find('div', class_='jobCard_jobCard_lists__fdnsc').div.text
        info = job_shine.find('meta', itemprop='url')['content']

        st.write(scompany_name)
        st.write(role)
        st.write(city)
        st.write(info)
        st.write('---')

def jooble_here():

    url_jooble = 'https://in.jooble.org/SearchResult?p=5&ukw='+familiar_skill#+'developer'

    jooble = requests.get(url_jooble).text
    jooble_soup = BeautifulSoup(jooble,'lxml')

    cards = jooble_soup.find_all('article', class_='FxQpvm yKsady')

    for card in cards:
        try:
            comp = card.section.find('div', class_='_15xYk4').div.div.div.p.text
            post = card.header.h2.a.text
            loc = card.section.find('div', class_='_15xYk4').div.find('div', class_='fAH3JV _2fd0Bh _1HYDQk _1BK4fr').div.text
            infoo = card.header.h2.a['href']

            st.write(comp)
            st.write(post)
            st.write(loc)
            st.write(infoo)
            st.write("---")

        except:
            st.write("for more job opportunities go to-", url_jooble)

def freshers_here():
    html_fresher = requests.get('https://www.freshersworld.com/jobs/jobsearch/'+familiar_skill).text
    soup_fresher = BeautifulSoup(html_fresher,'lxml')

    card_list = soup_fresher.find_all('div', class_='col-md-12 col-lg-12 col-xs-12 padding-none job-container jobs-on-hover top_space')

    for card in card_list:
        # print(card)
        comps = card.find('div', class_='col-md-12 col-lg-12 col-xs-12').find('div', class_='col-md-12 col-xs-12 col-lg-12').find('div', class_='col-md-12 col-xs-12 col-lg-12 padding-none left_move_up').a.h3.text
        role = card.find('div', class_='col-md-12 col-lg-12 col-xs-12').find('div', class_='col-md-12 col-xs-12 col-lg-12').find('div', class_='col-md-12 col-xs-12 col-lg-12 padding-none left_move_up').div.text
        qual = card.find('div', class_='col-md-12 col-lg-12 col-xs-12').find('div', class_='col-md-12 col-xs-12 col-lg-12').find('div', class_='col-md-12 col-xs-12 col-lg-12 padding-none left_move_up').find('div', class_='qualification-block').find('span', class_='qualifications display-block modal-open').find_all('span')
        place = card.find('div', class_='col-md-12 col-xs-12 col-lg-12 view-apply-container').div.div.find('span', class_='job-location display-block modal-open').a.text
        info = card.find('div', class_='col-md-12 col-lg-12 col-xs-12').find('div', class_='col-md-12 col-xs-12 col-lg-12').find('div', class_='col-md-12 col-xs-12 col-lg-12 padding-none left_move_up').a['href']
        
        st.write(comps)
        st.write(role)
        for i in qual:
            st.write(i.text)
        
        st.write(info)
        st.write('---')

selected = option_menu(
    menu_title="",
    options=["timesjobs","shine","jooble","freshersworld"],
    orientation="horizontal"
    #icons = [""]
)

if selected == "timesjobs":
    st.subheader(f"you have selected {selected}")
    times_here()
if selected == "shine":
    st.subheader(f"you have selected {selected}")
    shine_here()
if selected == "jooble":
    st.subheader(f"you have selected {selected}")
    jooble_here()
if selected == "freshersworld":
    st.subheader(f"you have selected {selected}")
    freshers_here()


hidden_menu_style = """
    <style>
    #MainMenu {visibility : hidden;}
    footer {visibility : hidden;}
    </style>
    """

st.markdown(hidden_menu_style, unsafe_allow_html=True)
