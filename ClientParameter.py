import time


# Ask type of 3rd party layer
def ask_user():
    client_type = input('Type 1 for REST Query. Type 2 for Tile Export: ')
    if client_type == '1':
        print(rest_query())
    elif client_type == '2':
        print(tile_export())
    else:
        pass


def get_geom_type():
    while True:
        geom_type = input('Geometry type: ')
        geom_type = geom_type.capitalize()
        if geom_type != 'Point' and geom_type != 'Polygon' and geom_type != 'Line':
            print('Geometry type is not valid, please enter again.')
            time.sleep(1)
        else:
            break
    return geom_type


def style_f(geom_style):
    style = ''
    while style == '':
        geom_type = geom_style
        if geom_type == 'Polygon':
            style = input('Style ("#000000",0.8,2,"#005CE6",0.35): ')
            return style
        elif geom_type == 'Point':
            style = input('Style (/Images/MapIcon/Bridge.png): ')
            return style
        elif geom_type == 'Line':
            style = input('Style (Line): ')
            return style
        else:
            print('Geometry type is not valid')
            get_geom_type()


def fields_f():
    i = ''
    ugridd_field = []
    field_type = []
    rest_field = []
    ugridd_field_str = ''
    while i != 'STOP':
        i = input('Enter uGRIDD Bubble Field Names, type STOP when done: ')
        if i == 'STOP':
            break
        ugridd_field.append(i)
        ugridd_field_str = '","'.join(ugridd_field)

    # Ask for field name and type based on list length
    for x in range(0, len(ugridd_field)):
        a = input('Enter Tile Field Name for ' + ugridd_field[x] + ': ')
        b = input('Enter Tile Field definition (atr, link) for ' + ugridd_field[x] + ': ')
        rest_field.append(a)
        field_type.append(b)

    rest_field_str = ''
    prev = 1
    for a, b in zip(rest_field, field_type):
        if prev != len(rest_field):
            rest_field_str = rest_field_str + '"' + b + ':' + a + '",'
        else:
            rest_field_str = rest_field_str + '"' + b + ':' + a + '"'
        prev += 1
    return [ugridd_field_str, rest_field_str]


# Function for rest query
def rest_query():
    # Ask for URL ending in /query
    url = input('URL ending in /query: ')

    # Ask for geometry type (Polygon, Line, Point)
    geom_type_out = get_geom_type()

    # Ask for Title field
    title = input('Title field: ')

    # Ask for uGRIDD Field Names until user types STOP
    fields = fields_f()

    # Ask for style string
    style = style_f(geom_type_out)

    # Return final string
    return '["{0}?inSR=4326&outSR=4326&spatialRel=esriSpatialRelIntersects&f=json&returnGeometry=true&outFields=*&' \
           'distance=#distance#&units=esriSRUnit_Meter&supportsQueryWithDistance=true&geometryType=#geometryType#&' \
           'geometry=#geometry#","{1}","atr:{2}",["{3}"],[{4}],[{5}]]'.format(url, geom_type_out, title,
                                                                              fields[0], fields[1], style)


# Function for tile export
def tile_export():
    # Ask for Name (VirginiaArcGIS)
    name = input('Name (VirginiaArcGIS): ')

    # Ask for geometry type
    geom_type_out = get_geom_type()

    # Ask for unique ID field
    unique_id = input('Unique ID field name: ')

    # Ask for bounding box
    west = input('West: ')
    south = input('South: ')
    east = input('East: ')
    north = input('North: ')

    # Ask for url ending in /export
    export_url = input('URL ending in /export: ')

    # Ask for url ending in /query
    query_url = input('URL ending in /query: ')

    # Ask for Title
    title = input('Title field: ')

    # Ask for uGRIDD Field Names until user types STOP
    fields = fields_f()
    fields1 = fields[0]
    fields2 = fields[1]

    # Ask for style string
    style = style_f(geom_type_out)

    return '["{0}", "{1}", false, "{2}", [{3}, {4}, {5}, {6}], 4 "{7}","{8}","atr:{9}",["{10}"],[{11}],[{12}]]'.format(
        name, geom_type_out, unique_id, west, south, east, north, export_url, query_url, title, fields1, fields2,
        style)


ask_user()
