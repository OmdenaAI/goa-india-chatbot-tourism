import scraping_module as sm

# page url
url = 'https://www.planetware.com/india/best-beaches-in-goa-ind-1-30.htm'

# get html content
soup = sm.get_soup(url)

# load all beaches
beaches =soup.find_all('div',{'class':'siteblock'})[1:19]
len(beaches)

#first beach
first_beach = beaches[0]
print(first_beach)

# first beach title
first_title = first_beach.find('h2',{'class':'sitename'}).text
print(first_title)

# description of the first beach
paragraphs = first_beach.find_all('p')
# removing html tags in the text
for p in paragraphs:
    text = p.get_text()
    print(text)

beach_data = []
for beach in beaches:
    beach_name = beach.find('h2', {'class': 'sitename'}).text
    beach_description_tags = beach.find_all('p')
    beach_description = ' '.join([tag.get_text() for tag in beach_description_tags])
    beach_data.append({'beach_name': beach_name, 'beach_description': beach_description})

df = sm.pd.DataFrame(beach_data)

# Create the folder if it doesn't exist
folder_path = 'data'
# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)

# Save the DataFrame as a CSV file in the folder
file_name = 'beach_data.csv'
sm.save_dataframe(df, folder_path, file_name)




