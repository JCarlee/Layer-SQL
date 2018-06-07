from tkinter import filedialog
from tkinter import *

master = Tk()

# List to store field names
field_names = ['Id', 'Name', 'FullName', 'Bubble Title', 'Category', 'Table Name', 'Table Type',
               'Data Source', 'Coverage', 'Always Show', 'Update Frequency', 'Records', 'LinkedData1', 'LinkedData2',
               'URL', 'ServerHandler', 'Client Handler', 'Client Parameter', 'IsRegional', 'ParentLayer', 'Style',
               'DataType', 'LayerType', 'Vertex', 'Geography']


# Verify input from user
def try_input(f):
    if f == '':
        return "NULL"
    elif type(f) is str and f != "NULL":
        return "'" + f + "'"
    else:
        return f


def make_sql_report():
    master.filename = filedialog.asksaveasfilename(defaultextension=".sql",
                                                   filetypes=(("sql", "*.sql"), ("all files", "*.*")))
    fid = try_input(int(e1.get()))
    name = try_input(str(e2.get()))
    full_name = try_input(str(e3.get()))
    bubble_title = try_input(str(e4.get()))
    category = try_input(str(e5.get()))
    table_name = try_input(e6.get())
    table_type = try_input(str(e7.get()))
    data_source = try_input(str(e8.get()))
    coverage = try_input(str(e9.get()))
    always_show = try_input(int(e10.get()))
    update_frequency = try_input(int(e11.get()))
    records = try_input(int(e12.get()))
    linked_data1 = try_input(str(e13.get()))
    linked_data2 = try_input(str(e14.get()))
    url = try_input(str(e15.get()))
    server_handler = try_input(e16.get())
    client_handler = try_input(str(e17.get()))
    client_parameter = try_input(str(e18.get()))
    is_regional = try_input(int(e19.get()))
    parent_layer = try_input(int(e20.get()))
    style = try_input(str(e21.get()))
    data_type = try_input(str(e22.get()))
    layer_type = try_input(str(e23.get()))
    vertex = try_input(int(e24.get()))
    geography = try_input(str(e25.get()))
    csv_true = e26.get()
    input_values = [fid, name, full_name, bubble_title, category, table_name, table_type, data_source, coverage,
                    always_show, update_frequency, records, linked_data1, linked_data2, url, server_handler,
                    client_handler, client_parameter, is_regional, parent_layer, style, data_type, layer_type, vertex,
                    geography]
    sql_file = open(master.filename, 'w')
    sql_file.write("Update [Layer] Set [Sequence] = [Sequence] + 1 Where [Sequence] >= EMPTY;\n\n")

    sql_file.write("Insert into [Layer]([Id], [Sequence], [Name], [FullName], [BubbleTitle], [Category], [TableName], "
                   "[TableType], [DataSource], [Coverage], [IsActive], [AlwaysShow], [Searchable], [InceptionDate], "
                   "[UpdateFrequency], [Records], [SupportData], [LinkedData1], [LinkedData2], [URL], [ServerHandler], "
                   "[ClientHandler], [ClientParameter], [IsRegional], [ParentLayer], [Style], [HighlightStyle], "
                   "[Range], [Zoom], [DataType], [LayerType], [BubbleType], [Vertex], [Query], "
                   "[Buffer], [Geography])\n\t")

    sql_file.write(
        "Values({0}, EMPTY, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, 1, {9}, 7, GETDATE(), {10}, {11}, 0, {12}, {13}, "
        "{14}, {15}, {16}, {17}, {18}, {19}, {20}, NULL, NULL, NULL, {21}, {22}, \'uGRIDD\', {23}, "
        "\'Geography\', 30000 , geography::STGeomFromText({24}, 4326));\n".format(
            fid, name, full_name, bubble_title, category, table_name, table_type, data_source, coverage, always_show,
            update_frequency, records, linked_data1, linked_data2, url, server_handler, client_handler,
            client_parameter, is_regional, parent_layer, style, data_type, layer_type, vertex, geography))
    sql_file.write('\nSelect * from Layer order by Sequence;')

    if table_name != 'NULL':
        sql_file.write('''
    
GO
    
ALTER TABLE ''' + e6.get() + '\n\tADD CONSTRAINT [PK_' + e6.get() + '''] PRIMARY KEY CLUSTERED ([Id] ASC);
    
GO
    
CREATE SPATIAL INDEX [Idx_''' + e6.get() + '''_Geo]
    ON ''' + e6.get() + ''' ([Geography])
    USING GEOGRAPHY_GRID
    WITH  (
            GRIDS = (LEVEL_1 = MEDIUM, LEVEL_2 = MEDIUM, LEVEL_3 = MEDIUM, LEVEL_4 = MEDIUM)
          );''')

    sql_file.close()

    # Create CSV report file
    if csv_true == 1:
        report_file = master.filename.replace('.sql', '.csv')
        csv_file = open(report_file, 'w')
        for a, b in zip(field_names, input_values):
            csv_file.write(str(a) + ',' + str(b) + '\n')
        csv_file.close()


# Create labels
for i in field_names:
    Label(master, text=i).grid(row=field_names.index(i))

# Define values from entries
e1 = Entry(master)  # Id
e1.insert(END, '000')

e2 = Entry(master)  # Name
e2.insert(END, '**MileTX**')

e3 = Entry(master)  # FullName
e3.insert(END, '**Milepost (TX)**')

e4 = Entry(master)  # Bubble Title
e4.insert(END, '**Texas Milepost**')

e5 = Entry(master)  # Catgegory
e5.insert(END, 'Public Data')

e6 = Entry(master)  # Table Name
e6.insert(END, '**Milepost_TX**')

e7 = Entry(master)  # Table Type
e7.insert(END, '**Sublayer/NULL**')

e8 = Entry(master)  # Data Source
e8.insert(END, '**TXDOT**')

e9 = Entry(master)  # Coverage
e9.insert(END, '**Texas**')

e10 = Entry(master)  # Always Show
e10.insert(END, '1')

e11 = Entry(master)  # Update Frequency
e11.insert(END, '12')

e12 = Entry(master)  # Records
e12.insert(END, '100')

e13 = Entry(master)  # LinkedData1
e13.insert(END, '**PDF**')

e14 = Entry(master)  # Linkeddata2
e14.insert(END, 'NULL')

e15 = Entry(master)  # URL
e15.insert(END, 'NULL')

e16 = Entry(master)  # ServerHandler
e16.insert(END, '**6/NULL**')

e17 = Entry(master)  # ClientHandler
e17.insert(END, '**Dynamic/ArcGISRest**')

e18 = Entry(master)  # ClientParameter

e19 = Entry(master)  # IsRegional
e19.insert(END, '1')

e20 = Entry(master)  # ParentLayer
e20.insert(END, '0')

e21 = Entry(master)  # Style
e21.insert(END, '**Milepost.png**')

e22 = Entry(master)  # DataType
e22.insert(END, '**Point**')

e23 = Entry(master) # LayerType
e23.insert(END, 'LayerType (Kml, Tile, Vector)')

e24 = Entry(master)  # Vertex
e24.insert(END, '0')

e25 = Entry(master)  # Geography

e26 = IntVar()
Checkbutton(master, text="Create CSV Report", variable=e26).grid(row=26, sticky=W + E)

# Create tkinter rows
e_list = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23, e24,
          e25]

for i in e_list:
    i.grid(row=e_list.index(i), column=1, sticky=W + E)

# Create Save button
Button(master, text='Save', command=make_sql_report).grid(row=26, column=1, sticky=W+E, pady=4, padx=10)
# Button(master, text='Save', command=make_sql_report).grid(row=25, column=0, sticky=W+E, pady=4, padx=10)

# Ensure text boxes expand with window
master.columnconfigure(1, weight=1)

mainloop()
