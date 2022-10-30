import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

all_eq_data = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_data:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {
            'title': 'Magnitude',
        },
    },
}]
my_layout = Layout(title='Global Earthquakes')

fig = {
    'data': data,
    'layout': my_layout,
}

offline.plot(fig, filename='global_earthquakes.html')