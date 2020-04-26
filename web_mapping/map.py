import folium
import pandas


data=pandas.read_csv("Volcanoes.txt")
lat=data["LAT"]
lon=data["LON"]
elev=data["ELEV"]
lon=list(lon)
lat=list(lat)

def color_genarator(elevation):
    if(elevation < 1000):
        return ("green")
    elif 1000<=elevation<3000:
        return("orange")
    else:
        return("red")

#Base map
map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")

# Creating the second layer by adding feature group of pointers and adding that to the base map.
fgv=folium.FeatureGroup(name="My map of Volcanoes")

for la,lt,el in zip(lat,lon,elev):
    # fg.add_child(folium.Marker(location=[la,lt],popup=str(el)+ " m", icon=folium.Icon(color=color_genarator(el))))
    fgv.add_child(folium.CircleMarker(location=[la, lt], radius=10,popup=str(el) + " m",
                                     icon=folium.Icon(color=color_genarator(el))))

fgp=folium.FeatureGroup(name="My map of Population")

#Creating third layer by adding feature group of colored polygon layer to the base map
fgp.add_child(folium.GeoJson(data=open("world.json",'r',encoding='utf-8-sig').read(),
                            style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
                            else 'orange' if 10000000 <= x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())
map.save("Map.html")