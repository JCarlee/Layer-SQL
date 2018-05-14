# Ask if REST Query or Tile Export


def ask_user():
    client_type = input('Type 1 for REST Query. Type 2 for Tile Export')
    valid_type = False
    while valid_type is False:
        if client_type == 1:
            valid_type = True
            rest_query()
        elif client_type == 2:
            valid_type = True
            tile_export()
        else:
            print('Please provide a valid response')


def rest_query():
    rest_ugridd = []
    rest_field = []
    rest_type = []
    # Ask for URL ending in /query
    url = input('URL ending in /query: ')

    # Ask for geometry type (Polygon, Line, Point)
    geom_type = input('Geometry type: ')

    # Ask for Title field
    title = input('Title field: ')

    # Ask for uGRIDD Field Names until user types STOP
    i = ''
    rest_ugridd_str = ''
    while i != 'STOP':
        i = input('Enter uGRIDD Bubble Field Names, type STOP when done: ')
        rest_ugridd.append(i)
        rest_ugridd_str = '","'.join(rest_ugridd)

    # Ask for field name and type based on list length
    for x, y in range(0, len(rest_ugridd)):
        a = input('Enter REST Field Name for' + rest_ugridd[x] + ': ')
        b = input('Enter REST Field definition (atr, link) for ' + rest_ugridd[y] + ': ')
        rest_field.append(a)
        rest_type.append(b)
    rest_field_str = ''
    prev = None
    for a, b in rest_field, rest_type:
        if prev is not None:
            rest_field_str.append('"' + b + ':' + a + '",')
        else:
            rest_field_str.append('"' + b + ':' + a + '"')
        prev = a
    # Ask for style string
    style = input('Style (#000000",0.8,2,"#005CE6",0.35): ')

    # Return final string
    return '["{0}?inSR=4326&outSR=4326&spatialRel=esriSpatialRelIntersects&f=json&returnGeometry=true&outFields=*&' \
           'distance=#distance#&units=esriSRUnit_Meter&supportsQueryWithDistance=true&geometryType=#geometryType#&' \
           'geometry=#geometry#","Polygon","atr:{1}",["{2}"],["]'.format(url, title, rest_ugridd_str)


def tile_export():
    tile_ugridd = []
    tile_field = []
    tile_type = []
    # Ask for Name (VirginiaArcGIS)
    # Ask for geometry type
    # Ask for unique ID field
    # Ask for bounding box
    # Ask for url ending in /export
    # Ask for url ending in /query
    # Ask for Title
    # Ask for uGRIDD Field Names until user types STOP
    # Ask for field name and type based on list length
    pass
