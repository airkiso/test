from django.shortcuts import render
import folium
from folium.plugins import FastMarkerCluster
from App.models import locations
# Create your views here.
def index(request):
    stations=locations.objects.all()
    m=folium.Map(location=[41.5025,-72.699997], zoom_start=9)
    for station in stations:
        coordinates= (station.latitude,station.longitude)
        folium.Marker(coordinates,popup=station.station_name).add_to(m)
    '''latitudes=[station.latitude for station in stations]
    longitudes=[station.longitude for station in stations]
    FastMarkerCluster(data=zip(latitudes,longitudes)).add_to(m)
    '''
    context = {'map':m._repr_html_()}
    return render(request, 'index.html', context)
# Create your views here.
