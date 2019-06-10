from bs4 import BeautifulSoup
from urllib.request import urlopen

# we define the variables for our URL sources
BASE_URL = "http://www.indeed.com"
states_URL = "http://www.indeed.com/find-jobs.jsp"
# the lists that will contain our States and Cities
states_URL_list = []
cities_name_list = []


# our function for fetching and creating the states list
def get_state_links(states_URL):
    # get the page source from the states URL page
    html = urlopen(states_URL).read()

    # create the BeautifulSoup object
    soup = BeautifulSoup(html, "lxml")
    # we use a Bs method to find the link section
    states_page = soup.find_all(id="states")
    # then a loop to get all states links
    # and we construct each state link using the relative ones
    for states in states_page:
        links = states.findAll('a')
        for a in links:
            if a.text != '':
                states_URL_list.append(BASE_URL + a['href'])
    # finally we return the States URL list
    return states_URL_list


# the function to get those CITY, STATE names to use in our API
def get_city_names():
    # get the states URL list
    states_URL_list = get_state_links(states_URL)
    # loop through all state pages
    for page in states_URL_list:
        html = urlopen(page).read()
        soup = BeautifulSoup(html, "lxml")
        # use Bs to find the cities relevant HTML elements
        cities_page = soup.find_all('p', attrs={'class': 'city'})
        # loop through each element to get the city URL
        for p in cities_page:
            links = p.findAll('a')
            # open a txt file to store city names
            f = open('‎cities', 'a', encoding='utf8')
            # get each city state link
            for a in links:
                city_state = a['href']
                # parse CITY, STATE names using url string
                if city_state[:5] == '/jobs' or '%' in city_state:
                    f.write(a.text + '\n')
                # parse CITY, STATE and format as needed
                else:
                    city_state = city_state.lstrip('/l-').replace('-', ' ').split(',')
                    city = city_state[0]
                    state_raw = city_state[1]
                    state = ''

                    for char in state_raw:
                        if char.isupper():
                            state += char
                    # join CITY, STATE abbreviation strings
                    location = city + ', ' + state
                    # write them to the file
                    f.write(location + '\n')

    # close file
    f.close()

get_city_names()

