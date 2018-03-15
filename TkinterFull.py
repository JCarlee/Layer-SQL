# Default values in window

from tkinter import filedialog
from tkinter import *

master = Tk()

# List to store field names
field_names = ['Id', 'Name', 'FullName', 'Bubble Title', 'Category', 'Table Name', 'Table Type',
               'Data Source', 'Coverage', 'Always Show', 'Update Frequency', 'Records', 'LinkedData1', 'LinkedData2',
               'URL', 'ServerHandler', 'IsRegional', 'ParentLayer', 'Style', 'DataType', 'Vertex', 'Geography']


# Verify input from user
def try_input(f):
    if f == '':
        return "NULL"
    elif type(f) is str and f != "NULL":
        return "'" + f + "'"
    else:
        return f


# Write all inputs to the .sql file and report csv
def make_sql():
    master.filename = filedialog.asksaveasfilename(defaultextension=".sql",
                                                   filetypes=(("sql", "*.sql"), ("all files", "*.*")))
    fid = try_input(e1.get())
    name = try_input(str(e2.get()))
    full_name = try_input(str(e3.get()))
    bubble_title = try_input(str(e4.get()))
    category = try_input(str(e5.get()))
    table_name = try_input(e6.get())
    table_type = try_input(str(e7.get()))
    data_source = try_input(str(e8.get()))
    coverage = try_input(str(e9.get()))
    always_show = try_input(e10.get())
    update_frequency = try_input(e11.get())
    records = try_input(e12.get())
    linked_data1 = try_input(str(e13.get()))
    linked_data2 = try_input(str(e14.get()))
    url = try_input(str(e15.get()))
    server_handler = try_input(e16.get())
    is_regional = try_input(e17.get())
    parent_layer = try_input(e18.get())
    style = try_input(str(e19.get()))
    data_type = try_input(str(e20.get()))
    vertex = try_input(e21.get())
    geography = try_input(str(e22.get()))
    input_values = [fid, name, full_name, bubble_title, category, table_name, table_type, data_source, coverage,
                    always_show, update_frequency, records, linked_data1, linked_data2, url, server_handler,
                    is_regional, parent_layer, style, data_type, vertex, geography]
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
        "{14}, {15}, \'Dynamic\', NULL, {16}, {17}, {18}, NULL, NULL, NULL, {19}, \'Kml\', \'uGRIDD\', {20}, "
        "\'Geography\', 30000 , geography::STGeomFromText({21}, 4326));\n".format(
            fid, name, full_name, bubble_title, category, table_name, table_type, data_source, coverage, always_show,
            update_frequency, records, linked_data1, linked_data2, url, server_handler, is_regional, parent_layer,
            style, data_type, vertex, geography))

    sql_file.write('''
    Select * from Layer order by Sequence;

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
    report_file = master.filename.replace('.sql', '.csv')
    csv_file = open(report_file, 'w')
    for a, b in zip(field_names, input_values):
        csv_file.write(a + ',' + b + '\n')
    csv_file.close()


# Create labels
for i in field_names:
    Label(master, text=i).grid(row=field_names.index(i))


# Define values from entries
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)
e9 = Entry(master)
e10 = Entry(master)
e11 = Entry(master)
e12 = Entry(master)
e13 = Entry(master)
e14 = Entry(master)
e15 = Entry(master)
e16 = Entry(master)
e17 = Entry(master)
e18 = Entry(master)
e19 = Entry(master)
e20 = Entry(master)
e21 = Entry(master)
e22 = Entry(master)

# Create tkinter rows
e1.grid(row=0, column=1, sticky=W + E)
e2.grid(row=1, column=1, sticky=W + E)
e3.grid(row=2, column=1, sticky=W + E)
e4.grid(row=3, column=1, sticky=W + E)
e5.grid(row=4, column=1, sticky=W + E)
e6.grid(row=5, column=1, sticky=W + E)
e7.grid(row=6, column=1, sticky=W + E)
e8.grid(row=7, column=1, sticky=W + E)
e9.grid(row=8, column=1, sticky=W + E)
e10.grid(row=9, column=1, sticky=W + E)
e11.grid(row=10, column=1, sticky=W + E)
e12.grid(row=11, column=1, sticky=W + E)
e13.grid(row=12, column=1, sticky=W + E)
e14.grid(row=13, column=1, sticky=W + E)
e15.grid(row=14, column=1, sticky=W + E)
e16.grid(row=15, column=1, sticky=W + E)
e17.grid(row=16, column=1, sticky=W + E)
e18.grid(row=17, column=1, sticky=W + E)
e19.grid(row=18, column=1, sticky=W + E)
e20.grid(row=19, column=1, sticky=W + E)
e21.grid(row=20, column=1, sticky=W + E)
e22.grid(row=21, column=1, sticky=W + E)

# Create Quit and Save buttons
Button(master, text='Quit', command=master.quit).grid(row=22, column=0, sticky=W, pady=4)
Button(master, text='Save', command=make_sql).grid(row=22, column=1, sticky=W, pady=4)

# Ensure text boxes expand with window
master.columnconfigure(1, weight=1)

mainloop()
