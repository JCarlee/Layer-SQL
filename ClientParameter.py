# Ask type of 3rd party layer
def ask_user():
    client_type = input('Type 1 for REST Query. Type 2 for Tile Export: ')
    if client_type == '1':
        print(rest_query())
    elif client_type == '2':
        print(tile_export())
    else:
        pass


# Function for rest query
def rest_query():
    rest_ugridd = []
    rest_field = []
    rest_type = []
    # Ask for URL ending in /query
    url = input('URL ending in /query: ')

    # Ask for geometry type (Polygon, Line, Point)
    def get_geom_type():
        geom_type = input('Geometry type: ')
        geom_type = geom_type.capitalize()
        return geom_type

    geom_type_out = get_geom_type()

    # Ask for Title field
    title = input('Title field: ')

    # Ask for uGRIDD Field Names until user types STOP
    i = ''
    rest_ugridd_str = ''
    while i != 'STOP':
        i = input('Enter uGRIDD Bubble Field Names, type STOP when done: ')
        if i == 'STOP':
            break
        rest_ugridd.append(i)
        rest_ugridd_str = '","'.join(rest_ugridd)
    # Ask for field name and type based on list length
    for x in range(0, len(rest_ugridd)):
        a = input('Enter REST Field Name for ' + rest_ugridd[x] + ': ')
        b = input('Enter REST Field definition (atr, link) for ' + rest_ugridd[x] + ': ')
        rest_field.append(a)
        rest_type.append(b)

    rest_field_str = ''
    prev = 1
    for a, b in zip(rest_field, rest_type):
        if prev != len(rest_field):
            rest_field_str = rest_field_str + '"' + b + ':' + a + '",'
        else:
            rest_field_str = rest_field_str + '"' + b + ':' + a + '"'
        prev += 1

    # Ask for style string
    style = ''
    while style == '':
        if geom_type_out == 'Polygon':
            style = input('Style (#000000",0.8,2,"#005CE6",0.35): ')
        elif geom_type_out == 'Point':
            style = input('Style (/Images/MapIcon/Bridge.png): ')
        elif geom_type_out == 'Line':
            style = input('Style (Line): ')
        else:
            print('Geometry type is not valid')
            geom_type_out = get_geom_type()

    # Return final string
    return '["{0}?inSR=4326&outSR=4326&spatialRel=esriSpatialRelIntersects&f=json&returnGeometry=true&outFields=*&' \
           'distance=#distance#&units=esriSRUnit_Meter&supportsQueryWithDistance=true&geometryType=#geometryType#&' \
           'geometry=#geometry#","{1}","atr:{2}",["{3}"],[{4}],[{5}]]'.format(url, geom_type_out, title,
                                                                              rest_ugridd_str, rest_field_str, style)


def tile_export():
    tile_ugridd = []
    tile_field = []
    tile_type = []
    # Ask for Name (VirginiaArcGIS)
    name = input('Name (VirginiaArcGIS): ')

    # Ask for geometry type
    def get_geom_type():
        geom_type = input('Geometry type: ')
        geom_type = geom_type.capitalize()
        return geom_type

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
    i = ''
    tile_ugridd_str = ''
    while i != 'STOP':
        i = input('Enter uGRIDD Bubble Field Names, type STOP when done: ')
        if i == 'STOP':
            break
        tile_ugridd.append(i)
        tile_ugridd_str = '","'.join(tile_ugridd)

    # Ask for field name and type based on list length
    for x in range(0, len(tile_ugridd)):
        a = input('Enter Tile Field Name for ' + tile_ugridd[x] + ': ')
        b = input('Enter Tile Field definition (atr, link) for ' + tile_ugridd[x] + ': ')
        tile_field.append(a)
        tile_type.append(b)

    tile_field_str = ''
    prev = 1
    for a, b in zip(tile_field, tile_type):
        if prev != len(tile_field):
            tile_field_str = tile_field_str + '"' + b + ':' + a + '",'
        else:
            tile_field_str = tile_field_str + '"' + b + ':' + a + '"'
        prev += 1

    # Ask for style string
    style = ''
    while style == '':
        if geom_type_out == 'Polygon':
            style = input('Style ("#000000",0.8,2,"#005CE6",0.35): ')
        elif geom_type_out == 'Point':
            style = input('Style (/Images/MapIcon/Bridge.png): ')
        elif geom_type_out == 'Line':
            style = input('Style (Line): ')
        else:
            print('Geometry type is not valid')
            geom_type_out = get_geom_type()

    return '["{0}", "{1}", false, "{2}", [{3}, {4}, {5}, {6}], 4 "{7}","{8}","atr:{9}",["{10}"],[{11}],[{12}]]'.format(
        name, geom_type_out, unique_id, west, south, east, north, export_url, query_url, title, tile_ugridd_str,
        tile_field_str, style)


ask_user()
