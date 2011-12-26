OSM Solar
=========

Solar is a [Mapnik](http://mapnik.org) rendering style for OpenStreetMap designed
for limited storage applications that require extensive areas of pre-rendered
maps. It’s designed to work with an OpenStreetMap PostGIS database built using
[Osm2pgsql](http://wiki.openstreetmap.org/wiki/Osm2pgsql) and default settings.

Designed in cooperation with [Aaron Huslage](http://twitter.com/huslage) and
[Roger Weeks](http://about.me/rogerweeks) of [Tethr](http://www.tethr.org/),
Solar can be used to create fully-detailed tiles of OSM data at a third of the
filesize of the default Mapnik stylesheet. We use a limited color palette
sampled from [Ethan Schoonover’s Solarized](http://ethanschoonover.com/solarized)
and limit the output to 4-bit color to maximize the compression offered by the
PNG image format.

To use OSM Solar, use [Cascadenik](https://github.com/mapnik/Cascadenik/wiki)
to convert the [layer file](https://github.com/migurski/HighRoad/blob/master/style.mml)
to a Mapnik-compatible `style.xml` file.

High Road is made by Michal Migurski, of [Stamen Design](http://stamen.com).

Details
-------

At distant zoom levels, local and residential streets are omitted. Bold, simple
highways dominate the map, and the visual layering is categorical to clearly
separate each road type. Large towns, parks, and water bodies are named.

![Oakland, z11](https://github.com/migurski/OSM-Solar/raw/master/renders/sanfrancisco-11.jpg)

Deeper in to the map, local streets and highway ramps start to appear. You begin
to see block-scale details and smaller features:

![Oakland, z13](https://github.com/migurski/OSM-Solar/raw/master/renders/sanfrancisco-13.jpg)

At the closest zoom levels, physical layering takes over and you begin to see over-
and underpasses as they exist in the built world along with a full collection of
parks, water bodies, small villages and other OSM features:

![Oakland, z15](https://github.com/migurski/OSM-Solar/raw/master/renders/sanfrancisco-15.jpg)

Elsewhere
---------

A maze of ramps marks the east approach to New York’s
[Lincoln Tunnel](http://maps.google.com/maps?q=new+york+lincoln+tunnel&hl=en&ll=40.757408,-73.996997&spn=0.004575,0.011169&sll=37.0625,-95.677068&sspn=39.099308,58.007813&vpsrc=6&t=h&z=17):

![New York, z16](https://github.com/migurski/OSM-Solar/raw/master/renders/newyork-16.jpg)

A cloverleaf interchange on Moscow’s
[MKAD](http://en.wikipedia.org/wiki/Moscow_Ring_Road):

![Moscow, z14](https://github.com/migurski/OSM-Solar/raw/master/renders/moscow-14.jpg)

London’s dense network of trunk roads, centered on
[the Isle of Dogs](http://www.openstreetmap.org/?lat=51.5058&lon=-0.0111&zoom=12&layers=M):

![London, z12](https://github.com/migurski/OSM-Solar/raw/master/renders/london-12.jpg)
