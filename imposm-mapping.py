from re import compile, I

from imposm.mapping import (
    Options, Polygons, LineStrings, PseudoArea, GeneralizedTable, FieldType,
    meter_to_mapunit, Bool, Direction, String, WayZOrder, Type, Integer
    )

def zoom_threshold(zoom):
    return meter_to_mapunit(20037508.0 * 2 / (2**(9 + zoom)))

db_conf = Options(
    db='planet_osm',
    host='localhost',
    port=5432,
    user='osm',
    password='',
    sslmode='allow',
    prefix='osm_new_',
    proj='epsg:900913',
)



# WHERE leisure IN ('park', 'water_park', 'marina', 'nature_reserve',
# 	                                   'playground', 'garden', 'common')
# 	                    OR amenity IN ('graveyard')
# 	                    OR landuse IN ('cemetery')
# 	                    OR leisure IN ('sports_centre', 'golf_course', 'stadium',
# 	                                   'track', 'pitch')
# 	                    OR landuse IN ('recreation_ground')
# 	                    OR landuse IN ('forest', 'wood')
# 	                 
# 	                 ORDER BY ST_Area(way) DESC

green_areas = Polygons(
    name = 'green_areas',
    fields = (
        ('area', PseudoArea()),
    ),
    mapping = {
        'leisure': ('park', 'water_park', 'marina', 'nature_reserve', 'playground', 'garden', 'common', 'sports_centre', 'golf_course', 'stadium', 'track', 'pitch'),
        'landuse': ('cemetery', 'park', 'water_park', 'marina', 'nature_reserve', 'playground', 'garden', 'common', 'forest', 'wood'),
        'amenity': ('graveyard')
    }
)

green_areas_z13 = GeneralizedTable(
    name = 'green_areas_z13',
    tolerance = zoom_threshold(13),
    origin = green_areas,
)

green_areas_z10 = GeneralizedTable(
    name = 'green_areas_z10',
    tolerance = zoom_threshold(10),
    origin = green_areas_z13,
)



# WHERE amenity IN ('school', 'college', 'university', 'bus_station',
#                   'ferry_terminal', 'hospital', 'kindergarten',
#                   'place_of_worship', 'public_building', 'townhall')
#    OR landuse IN ('industrial', 'commercial')

grey_areas = Polygons(
    name = 'grey_areas',
    fields = (
        ('area', PseudoArea()),
    ),
    mapping = {
        'amenity': ('school', 'college', 'university', 'bus_station', 'ferry_terminal', 'hospital', 'kindergarten', 'place_of_worship', 'public_building', 'townhall'),
        'landuse': ('industrial', 'commercial')
    }
)

grey_areas_z13 = GeneralizedTable(
    name = 'grey_areas_z13',
    tolerance = zoom_threshold(13),
    origin = grey_areas,
)

grey_areas_z10 = GeneralizedTable(
    name = 'grey_areas_z10',
    tolerance = zoom_threshold(10),
    origin = grey_areas_z13,
)



# WHERE building IS NOT NULL

buildings = Polygons(
    name = 'buildings',
    fields = (
        ('area', PseudoArea()),
    ),
    mapping = {
        'building': ('__any__',)
    }
)

buildings_z13 = GeneralizedTable(
    name = 'buildings_z13',
    tolerance = zoom_threshold(13),
    origin = buildings,
)

buildings_z10 = GeneralizedTable(
    name = 'buildings_z10',
    tolerance = zoom_threshold(10),
    origin = buildings_z13,
)



# WHERE aeroway IS NOT NULL

aeroways = LineStrings(
    name = 'aeroways',
    mapping = {
        'aeroway': ('__any__',)
    }
)

aeroways_z13 = GeneralizedTable(
    name = 'aeroways_z13',
    tolerance = zoom_threshold(13),
    origin = aeroways,
)

aeroways_z10 = GeneralizedTable(
    name = 'aeroways_z10',
    tolerance = zoom_threshold(10),
    origin = aeroways_z13,
)



# WHERE waterway IS NOT NULL

waterways = LineStrings(
    name = 'waterways',
    mapping = {
        'waterway': ('__any__',)
    }
)

waterways_z13 = GeneralizedTable(
    name = 'waterways_z13',
    tolerance = zoom_threshold(13),
    origin = waterways,
)

waterways_z10 = GeneralizedTable(
    name = 'waterways_z10',
    tolerance = zoom_threshold(10),
    origin = waterways_z13,
)



# WHERE "natural" IN ('water', 'bay')
# 	 OR waterway = 'riverbank'
# 	 OR landuse = 'reservoir'

water_areas = Polygons(
    name = 'water_areas',
    fields = (
        ('area', PseudoArea()),
    ),
    mapping = {
        'natural': ('water', 'bay'),
        'waterway': ('riverbank',),
        'landuse': ('reservoir',)
    }
)

water_areas_z13 = GeneralizedTable(
    name = 'water_areas_z13',
    tolerance = zoom_threshold(13),
    origin = water_areas,
)

water_areas_z10 = GeneralizedTable(
    name = 'water_areas_z10',
    tolerance = zoom_threshold(10),
    origin = water_areas_z13,
)



class Link (Bool):
    """ Boolean for whether the segment of highway is a link or not.
    """
    column_type = "VARCHAR(3)"

    def value(self, val, osm_elem):
        if osm_elem.tags.get('highway', '').endswith('_link'):
            return 'yes'
        else:
            return 'no'

class ExplicitLayer (FieldType):
    """ Map layer tag to explicit physical layering.

        Higher numbers = higher up in the air.
    """
    column_type = "FLOAT"
    
    def value(self, val, osm_elem):
        try:
            return float(osm_elem.tags.get('layer', 0))
        except ValueError:
            return 0

class HighwayClassification (FieldType):
    """ Map highway tags to one of: minor_road, major_road, highway.
    
        Subclasses override self.classes with per-zoom dictionaries.
    """
    column_type = "VARCHAR(16)"
    classes = dict()
    other = 'minor_road'
    
    def value(self, val, osm_elem):
        kind = osm_elem.tags.get('highway', '')
        return self.classes.get(kind, self.other)

class HighwayPriority (FieldType):
    """ Map highway and railway tags to rendering priority.
        
        Lower numbers = more important.
        
        Subclasses override self.priority with per-zoom dictionaries.
    """
    column_type = "SMALLINT"
    priority = dict()
    
    def value(self, val, osm_elem):
        kind = osm_elem.tags.get('highway', '')
        return self.priority.get(kind, 99)

class NameAbbreviation (FieldType):
    """ Map typical U.S. road names to abbreviated versions, e.g. "St" for "Street".
    """
    column_type = 'VARCHAR(255)'

    patterns = (
        (compile(r'\b(ave)nue$', I),     r'\1'),
        (compile(r'\b(b)oulevard$', I),  r'\1lvd'),
        (compile(r'\b(e)xpressway$', I), r'\1xpwy'),
        (compile(r'\b(h)ighway$', I),    r'\1wy'),
        (compile(r'\b(p)arkway$', I),    r'\1kwy'),
        (compile(r'\b(c)ourt$', I),      r'\1t'),
        (compile(r'\b(dr)ive$', I),      r'\1'),
        (compile(r'\b(pl)ace$', I),      r'\1'),
        (compile(r'\b(l)ane$', I),       r'\1n'),
        (compile(r'\b(r)oad$', I),       r'\1d'),
        (compile(r'\b(st)reet$', I),     r'\1'),
        (compile(r'\b(tr)ail$', I),      r'\1'),
        (compile(r'\b(w)ay$', I),        r'\1y'),
    )
    
    def value(self, val, osm_elem):
        name = osm_elem.tags.get('name', '')
        
        for (pattern, repl) in self.patterns:
            if pattern.search(name):
                return pattern.sub(repl, name)
        
        return name

class ConstantInteger (FieldType):
    """ 
    """
    column_type = 'SMALLINT'
    
    def __init__(self, constant, *args, **kwargs):
        self.constant = constant
        FieldType.__init__(self, *args, **kwargs)
    
    def value(self, val, osm_elem):
        return self.constant

class ConstantVarchar255 (ConstantInteger):
    column_type = 'VARCHAR(255)'

class Roads (LineStrings):
    with_type_field=False
    fields = (
        ('name_abbr', NameAbbreviation()),
        ('highway', Type()),
      # ('tunnel', Bool()),
      # ('bridge', Bool()),
        ('oneway', Direction()),
        ('is_link', Link()),
        ('ref', String()),
        ('layer', ExplicitLayer()),
    )



# WHERE highway IN ('motorway', 'motorway_link')
#    OR highway IN ('trunk', 'trunk_link', 'primary', 'primary_link', 'secondary', 'secondary_link', 'tertiary', 'tertiary_link')
#    OR highway IN ('residential', 'unclassified', 'road', 'unclassified', 'service', 'minor')
#    OR highway IN ('footpath', 'track', 'footway', 'steps', 'pedestrian', 'path', 'cycleway')
# ...
# WHERE railway IN ('rail', 'tram', 'light_rail', 'narrow_guage', 'monorail')

class HighwayPriorityZ15 (HighwayPriority):
    priority = dict(motorway=0,
                    trunk=2, primary=3, secondary=4, tertiary=5,
                    motorway_link=6, trunk_link=6, primary_link=6, secondary_link=6, tertiary_link=6,
                    residential=7, unclassified=7, road=7,
                    service=8, minor=8)

class HighwayClassificationZ15 (HighwayClassification):
    classes = dict(motorway='highway', motorway_link='highway',
                   trunk='major_road', trunk_link='major_road',
                   primary='major_road', primary_link='major_road',
                   secondary='major_road', secondary_link='major_road',
                   tertiary='major_road', tertiary_link='major_road',
                   footpath='path', track='path', footway='path', steps='path',
                   pedestrian='path', path='path', cycleway='path')

roads_z15plus = Roads(
    name = 'roads_z15plus',
    mapping = {
        'highway': ('motorway', 'motorway_link', 'trunk', 'trunk_link',
                    'primary', 'primary_link', 'secondary', 'secondary_link', 'tertiary',
                    'residential', 'unclassified', 'road', 'unclassified', '__any__'),
    },
    fields = Roads.fields + (
        ('priority', HighwayPriorityZ15()),
        ('kind', HighwayClassificationZ15()),
    )
)

rails_z15plus = Roads(
    name = 'rails_z15plus',
    mapping = {
        'railway': ('rail', 'tram', 'light_rail', 'narrow_guage', 'monorail', 'subway'),
    },
    fields = Roads.fields + (
        ('priority', ConstantInteger(1)),
        ('kind', ConstantVarchar255('rail')),
    )
)



# WHERE highway IN ('motorway', 'motorway_link')
#    OR highway IN ('trunk', 'trunk_link', 'primary', 'primary_link', 'secondary', 'secondary_link', 'tertiary', 'tertiary_link')
#    OR highway IN ('residential', 'unclassified', 'road', 'minor')
#    OR railway IN ('rail')

class HighwayPriorityZ14 (HighwayPriority):
    priority = dict(motorway=0, trunk=1, primary=2, secondary=3, tertiary=4,
                    motorway_link=5, trunk_link=5, primary_link=5, secondary_link=5, tertiary_link=5,
                    residential=6, unclassified=6, road=6, minor=6)

class HighwayGroupingZ14 (FieldType):
    """ Lower numbers = more important
    """
    column_type = "SMALLINT"
    
    def value(self, val, osm_elem):
        priority = dict(motorway=0, trunk=0, motorway_link=0, trunk_link=0)

        kind = osm_elem.tags.get('highway', '')
        return priority.get(kind, 99)

class HighwayClassificationZ14 (HighwayClassification):
    classes = dict(motorway='highway', motorway_link='highway',
                   trunk='major_road', trunk_link='major_road',
                   primary='major_road', primary_link='major_road',
                   secondary='major_road', secondary_link='major_road',
                   tertiary='major_road', tertiary_link='major_road',
                   residential='minor_road', unclassified='minor_road',
                   road='minor_road', minor='minor_road',
                   rail='rail')
    other = 'unknown'

roads_z14_raw = Roads(
    name = 'roads_z14_raw',
    mapping = {
        'highway': ('motorway', 'motorway_link', 'trunk', 'trunk_link',
                    'primary', 'primary_link', 'secondary', 'secondary_link', 'tertiary', 'tertiary_link',
                    'residential', 'unclassified', 'road', 'unclassified'),
    },
    fields = Roads.fields + (
        ('priority', HighwayPriorityZ14()),
        ('grouping', HighwayGroupingZ14()),
        ('kind', HighwayClassificationZ14()),
    )
)

roads_z14 = GeneralizedTable(
    name = 'roads_z14',
    tolerance = zoom_threshold(14),
    origin = roads_z14_raw,
)

rails_z14_raw = Roads(
    name = 'rails_z14_raw',
    mapping = {
        'railway': ('rail', 'subway'),
    },
    fields = Roads.fields + (
        ('priority', ConstantInteger(7)),
        ('grouping', ConstantInteger(99)),
        ('kind', ConstantVarchar255('rail')),
    )
)

rails_z14 = GeneralizedTable(
    name = 'rails_z14',
    tolerance = zoom_threshold(14),
    origin = rails_z14_raw,
)

# WHERE highway IN ('motorway', 'motorway_link')
#    OR highway IN ('trunk', 'trunk_link', 'primary', 'primary_link', 'secondary', 'secondary_link', 'tertiary', 'tertiary_link')
#    OR highway IN ('residential', 'unclassified', 'road', 'minor')
#    OR railway IN ('rail')

class HighwayPriorityZ13 (HighwayPriority):
    priority = dict(motorway=0, motorway_link=1, trunk=2, primary=2, secondary=2, tertiary=2,
                    trunk_link=3, primary_link=3, secondary_link=3, tertiary_link=3,
                    residential=4, unclassified=4, road=4)

class HighwayClassificationZ13 (HighwayClassification):
    classes = dict(motorway='highway', motorway_link='highway',
                   trunk='major_road', trunk_link='major_road',
                   primary='major_road', primary_link='major_road',
                   secondary='major_road', secondary_link='major_road',
                   tertiary='major_road', tertiary_link='major_road')

roads_z13_raw = Roads(
    name = 'roads_z13_raw',
    mapping = {
        'highway': ('motorway', 'motorway_link', 'trunk', 'trunk_link',
                    'primary', 'primary_link', 'secondary', 'secondary_link', 'tertiary', 'tertiary_link',
                    'residential', 'unclassified', 'road', 'unclassified'),
    },
    fields = Roads.fields + (
        ('priority', HighwayPriorityZ13()),
        ('kind', HighwayClassificationZ13()),
    )
)

roads_z13 = GeneralizedTable(
    name = 'roads_z13',
    tolerance = zoom_threshold(13),
    origin = roads_z13_raw,
)

rails_z13_raw = Roads(
    name = 'rails_z13_raw',
    mapping = {
        'railway': ('rail', ),
    },
    fields = Roads.fields + (
        ('priority', ConstantInteger(99)),
        ('kind', ConstantVarchar255('rail')),
    )
)

rails_z13 = GeneralizedTable(
    name = 'rails_z13',
    tolerance = zoom_threshold(13),
    origin = rails_z13_raw,
)



# WHERE highway IN ('motorway', 'motorway_link')
#    OR highway IN ('trunk', 'trunk_link', 'secondary', 'primary')
#    OR highway IN ('tertiary', 'residential', 'unclassified', 'road', 'unclassified')

class HighwayPriorityZ12 (HighwayPriority):
    priority = dict(motorway=0, trunk=1, primary=1, secondary=1,
                    tertiary=2, residential=2, unclassified=2, road=2,
                    motorway_link=3, trunk_link=3)

class HighwayClassificationZ12 (HighwayClassification):
    classes = dict(motorway='highway', motorway_link='highway',
                   trunk='major_road', trunk_link='major_road',
                   primary='major_road', secondary='major_road')

roads_z12_raw = Roads(
    name = 'roads_z12_raw',
    mapping = {
        'highway': ('motorway', 'motorway_link', 'trunk', 'trunk_link',
                    'secondary', 'primary', 'tertiary', 'residential',
                    'unclassified', 'road', 'unclassified'),
    },
    fields = Roads.fields + (
        ('priority', HighwayPriorityZ12()),
        ('kind', HighwayClassificationZ12()),
    )
)

roads_z12 = GeneralizedTable(
    name = 'roads_z12',
    tolerance = zoom_threshold(12),
    origin = roads_z12_raw,
)



# WHERE highway IN ('motorway')
#    OR highway IN ('trunk', 'primary')
#    OR highway IN ('secondary', 'tertiary')

class HighwayPriorityZ11 (HighwayPriority):
    priority = dict(motorway=0, trunk=1, primary=1, secondary=2, tertiary=2)

class HighwayClassificationZ11 (HighwayClassification):
    classes = dict(motorway='highway', trunk='major_road', primary='major_road')

roads_z11_raw = Roads(
    name = 'roads_z11_raw',
    mapping = {
        'highway': ('motorway', 'trunk', 'primary', 'secondary', 'tertiary'),
    },
    fields = Roads.fields + (
        ('priority', HighwayPriorityZ11()),
        ('kind', HighwayClassificationZ11()),
    )
)

roads_z11 = GeneralizedTable(
    name = 'roads_z11',
    tolerance = zoom_threshold(11),
    origin = roads_z11_raw,
)



# WHERE highway IN ('motorway')
#    OR highway IN ('trunk', 'primary')
#    OR highway IN ('secondary')

roads_z10_raw = Roads(
    name = 'roads_z10_raw',
    mapping = {
        'highway': ('motorway', 'trunk', 'primary', 'secondary'),
    },
    fields = Roads.fields + (
        ('priority', HighwayPriorityZ11()),
        ('kind', HighwayClassificationZ11()),
    )
)

roads_z10 = GeneralizedTable(
    name = 'roads_z10',
    tolerance = zoom_threshold(10),
    origin = roads_z10_raw,
)
