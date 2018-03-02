# Function to handle user input
from builtins import str


def try_input(i):
    if i == '':
        return "NULLpy"
    elif type(i) is str and i != "NULL":
        return "'" + i + "'"
    else:
        return i


FileLoc = input('File location and name: ')
file = open(FileLoc,'w')

Id = try_input(int(input('Id: ')))
Name = try_input(str(input('Name [TaxOH]: ')))
FullName = try_input(str(input('FullName [Tax Map (Ohio))]: ')))
BubbleTitle = try_input(str(input('BubbleTitle [Ohio Tax Maps]: ')))
Category = try_input(str(input('Category [Public Data]: ')))

TableNameRaw = input('TableName: ')
TableName = try_input(TableNameRaw)

TableType = try_input(str(input('TableType [NULL/Sublayer define]: ')))
DataSource = try_input(str(input('DataSource: ')))
Coverage = try_input(str(input('Coverage: ')))
AlwaysShow = try_input(int(input('AlwaysShow [If restricted 0/1]: ')))
UpdateFrequency = try_input(int(input('UpdateFrequency [12]: ')))
Records = try_input(int(input('Records: ')))
LinkedData1 = try_input(str(input('LinkedData1 [PDF, LAS, Fusion Table]: ')))
LinkedData2 = try_input(str(input('LinkedData2 [PDF, LAS, Fusion Table]: ')))
URL = try_input(str(input('URL: ')))
ServerHandler = try_input(int(input('ServerHandler [6]: ')))
IsRegional = try_input(int(input('IsRegional [0, 1]: ')))
ParentLayer = try_input(int(input('ParentLayer [0, parent id]: ')))
Style = try_input(str(input('Style [Milepost.png]: ')))
DataType = try_input(str(input('DataType [Point]: ')))
Vertex = try_input(int(input('Vertex: ')))
Geography = try_input(str(input('Geography: ')))

file.write(
    "Values({0}, EMPTY, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, 1, {9}, 7, GETDATE(), {10}, {11}, 0, {12}, {13}, {14},"
    "{15}, \'Dynamic\', NULL, {16}, {17}, {18}, 0, 0, {19}, \'Kml\', \'uGRIDD\', {20}, \'Geography\', 30000 , "
    "geography::STGeomFromText({21}, 4326));\n".format(
        Id, Name, FullName, BubbleTitle, Category, TableName, TableType, DataSource, Coverage, AlwaysShow,
        UpdateFrequency, Records, LinkedData1, LinkedData2, URL, ServerHandler, IsRegional, ParentLayer, Style,
        DataType, Vertex, Geography))

file.close()
