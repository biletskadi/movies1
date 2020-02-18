import folium
import pandas
from geopy.geocoders import Nominatim
import geopy.distance


def distance(location1, location2):
    """
    function returns distance between two tuples of coordinates
    """
    return geopy.distance.vincenty(location1, location2).km


def location(locations):
    """
    function returns latitude and longitude from location name
    """
    geo = Nominatim(user_agent="main.py")
    location1 = geo.geocode(locations)
    return location1.latitude, location1.longitude


def movies(year, filename):
    """
    function returns list with movie name, year, location and tuple of latitude and longitude
    from year and filename
    """
    data = pandas.read_csv(filename, error_bad_lines=False)
    movie = data['movie']
    years = data['year']
    locations = data['location']
    movie_lst = set()
    for j in range(len(movie)):
        try:
            if int(years[j]) == year and locations[j] != 'NO DATA':
                movie_lst.add((movie[j], years[j], locations[j], location(locations[j])))
        except AttributeError:
            pass
        except ValueError:
            pass
    return movie_lst


if __name__ == '__main__':
    lst = []
    year1 = int(input("Enter a year of the movie: "))
    latitude = float(input("Enter your latitude: "))
    longitude = float(input("Enter your longitude: "))
    print('Map is generating...')
    print('Please wait...')
    loc = (latitude, longitude)
    x = movies(year1, 'loc.csv')
    for i in x:
        lst.append((distance(loc, i[3]), i[0], i[3], i[2]))
    new_lst = sorted(lst[:5])
    m = folium.Map(location=[latitude, longitude], zoom_start=11)
    fg = folium.FeatureGroup(name='Point')
    fg.add_child(folium.Marker([latitude, longitude], popup='my_point', tooltip='me'))
    hg = folium.FeatureGroup(name='Films filmed nearby')
    for i in range(len(new_lst)):
        tooltip = str(lst[i][3])
        hg.add_child(folium.Marker([new_lst[i][2][0], new_lst[i][2][1]], popup=new_lst[i][1], tooltip=tooltip))
    pg = folium.FeatureGroup(name='Seven wonders of the Ancient world')
    pg.add_child(folium.CircleMarker([29.979167, 31.134167], popup='Great Pyramid of Giza', tooltip=1))
    pg.add_child(folium.CircleMarker([32.5355, 44.4275], popup='Hanging gardens of Babylon', tooltip=2))
    pg.add_child(folium.CircleMarker([37.637861, 21.63], popup='Statue of Zeus at Olympia', tooltip=3))
    pg.add_child(folium.CircleMarker([37.949722, 27.363889], popup='Temple of Artemis at Ephesus', tooltip=4))
    pg.add_child(folium.CircleMarker([37.037942, 27.424097], popup='Mausoleum at Halicarnassus', tooltip=5))
    pg.add_child(folium.CircleMarker([36.451111, 28.227778], popup='Colossus of Rhodes', tooltip=6))
    pg.add_child(folium.CircleMarker([31.214167, 29.885], popup='Lighthouse of Alexandria', tooltip=7))
    m.add_child(fg)
    m.add_child(hg)
    m.add_child(pg)
    m.add_child(folium.LayerControl())
    m.save("movies_map.html")
    print('Finished. Please have look at the map movies_map.html')