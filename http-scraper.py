import requests
from bs4 import BeautifulSoup

url = 'https://www.dndbeyond.com/characters/77046543'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    container_element = soup.find('div', class_='container') #ct-health-summary__hp-number ct-health-summary__hp-number--dark-mode
    if container_element:
        characterApp_element = container_element.find('div', attrs={'name':'character-app'})
        if characterApp_element:
            characterToolTarget_element = characterApp_element.find('div', id='character-tools-target')
            if characterToolTarget_element:
                #It was going SO well until this point oiwjduoadiad
                characterSheet_element = characterToolTarget_element.find('div', class_='ct-character-sheet')
                if characterSheet_element:
                    print("YIPPEE")
        # hp_text = hp_element.text.strip()
        # print(f"Current HP: {hp_text}")
    else:
        print("HP element not found on the page.")

else:
    print('Failed to retrieve data from D&D Beyond', response.status_code)
