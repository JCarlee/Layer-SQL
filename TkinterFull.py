#Default values in window
#File explorer for file loc

from tkinter import *

master = Tk()

fields = 'File Loc', 'Id', 'Name', 'FullName', 'Bubble Title', 'Category', 'Table Name', 'Table Type', \
         'Data Source', 'Coverage', 'Always Show', 'Update Frequency', 'Records', 'LinkedData1', 'LinkedData2',  'URL',\
         'ServerHandler', 'IsRegional', 'ParentLayer', 'Style', 'DataType', 'Vertex', 'Geography'


def try_input(i):
    if i == '':
        return "NULL"
    elif type(i) is str and i != "NULL":
        return "'" + i + "'"
    else:
        return i

def make_sql():
    Id = try_input(e2.get())
    Name = try_input(str(e3.get()))
    FullName = try_input(str(e4.get()))
    BubbleTitle = try_input(str(e5.get()))
    Category = try_input(str(e6.get()))
    TableName = try_input(e7.get())
    TableType = try_input(str(e8.get()))
    DataSource = try_input(str(e9.get()))
    Coverage = try_input(str(e10.get()))
    AlwaysShow = try_input(e11.get())
    UpdateFrequency = try_input(e12.get())
    Records = try_input(e13.get())
    LinkedData1 = try_input(str(e14.get()))
    LinkedData2 = try_input(str(e15.get()))
    URL = try_input(str(e16.get()))
    ServerHandler = try_input(e17.get())
    IsRegional = try_input(e18.get())
    ParentLayer = try_input(e19.get())
    Style = try_input(str(e20.get()))
    DataType = try_input(str(e21.get()))
    Vertex = try_input(e22.get())
    Geography = try_input(str(e23.get()))
    file = open(e1.get(), 'w')
    file.write("Update [Layer] Set [Sequence] = [Sequence] + 1 Where [Sequence] >= EMPTY;\n\n")

    file.write("Insert into [Layer]([Id], [Sequence], [Name], [FullName], [BubbleTitle], [Category], [TableName], "
               "[TableType], [DataSource], [Coverage], [IsActive], [AlwaysShow], [Searchable], [InceptionDate], "
               "[UpdateFrequency], [Records], [SupportData], [LinkedData1], [LinkedData2], [URL], [ServerHandler], "
               "[ClientHandler], [ClientParameter], [IsRegional], [ParentLayer], [Style], [HighlightStyle], [Range], "
               "[Zoom], [DataType], [LayerType], [BubbleType], [Vertex], [Query], "
               "[Buffer], [Geography])\n\t")

    file.write(
        "Values({0}, EMPTY, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, 1, {9}, 7, GETDATE(), {10}, {11}, 0, {12}, {13}, {14}, "
        "{15}, \'Dynamic\', NULL, {16}, {17}, {18}, NULL, NULL, NULL, {19}, \'Kml\', \'uGRIDD\', {20}, \'Geography\', 30000"
        ", geography::STGeomFromText({21}, 4326));\n".format(
            Id, Name, FullName, BubbleTitle, Category, TableName, TableType, DataSource, Coverage, AlwaysShow,
            UpdateFrequency, Records, LinkedData1, LinkedData2, URL, ServerHandler, IsRegional, ParentLayer, Style,
            DataType, Vertex, Geography))

    file.write('''
    Select * from Layer order by Sequence;

    GO

    ALTER TABLE ''' + e7.get() +
               '\n\tADD CONSTRAINT [PK_' + e7.get() + '''] PRIMARY KEY CLUSTERED ([Id] ASC);

    GO

    CREATE SPATIAL INDEX [Idx_''' + e7.get() + '''_Geo]
        ON ''' + e7.get() + ''' ([Geography])
        USING GEOGRAPHY_GRID
        WITH  (
                GRIDS = (LEVEL_1 = MEDIUM, LEVEL_2 = MEDIUM, LEVEL_3 = MEDIUM, LEVEL_4 = MEDIUM)
              );''')

    file.close()


for i in fields:
    Label(master, text=i).grid(row=fields.index(i))


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
e23 = Entry(master)


e1.grid(row=0, column=1, sticky=W+E)
e1.grid(row=0, column=1, sticky=W+E)
e2.grid(row=1, column=1, sticky=W+E)
e3.grid(row=2, column=1, sticky=W+E)
e4.grid(row=3, column=1, sticky=W+E)
e5.grid(row=4, column=1, sticky=W+E)
e6.grid(row=5, column=1, sticky=W+E)
e7.grid(row=6, column=1, sticky=W+E)
e8.grid(row=7, column=1, sticky=W+E)
e9.grid(row=8, column=1, sticky=W+E)
e10.grid(row=9, column=1, sticky=W+E)
e11.grid(row=10, column=1, sticky=W+E)
e12.grid(row=11, column=1, sticky=W+E)
e13.grid(row=12, column=1, sticky=W+E)
e14.grid(row=13, column=1, sticky=W+E)
e15.grid(row=14, column=1, sticky=W+E)
e16.grid(row=15, column=1, sticky=W+E)
e17.grid(row=16, column=1, sticky=W+E)
e18.grid(row=17, column=1, sticky=W+E)
e19.grid(row=18, column=1, sticky=W+E)
e20.grid(row=19, column=1, sticky=W+E)
e21.grid(row=20, column=1, sticky=W+E)
e22.grid(row=21, column=1, sticky=W+E)
e23.grid(row=22, column=1, sticky=W+E)

Button(master, text='Quit', command=master.quit).grid(row=23, column=0, sticky=W, pady=4)
Button(master, text='Save', command=make_sql).grid(row=23, column=1, sticky=W, pady=4)

master.columnconfigure(1, weight=1)

mainloop()
