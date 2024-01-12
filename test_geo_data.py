# Imports
import geopandas as gpd
import pyodbc

gdf = gpd.read_file("C:\\Users\\mereja\\Downloads\\ERGW1000\\ERGW1000_v1\\shp\\ergw1000_gwerg__v11_poly.shp")
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'ARTCOM\MSSQLSERVER2017' 
database = 'Test' 
username = 'ConnectDB' 
password = 'mPmI9W97wbmKmAw' 
table_name = 'gdf_ergw1000_gwerg__v11_poly'
schema_name = 'dbo'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# Connect to database using a context manager Geom_Col

cursor = cnxn.cursor()
# Insert Dataframe into SQL Server:
for index, row in gdf.iterrows():
     
     #print(row.geometry)
     #print("-----------          --------")
     #print(str("""INSERT INTO dbo.gdf_ergw1000_gwerg__v11_poly (erg_id,gestein_id,Shape_STAr,Shape_STLe,Geom_Col) values({0},{1},{2},{3},geometry::STGeomFromText('{4}',0))""").format(row.erg_id, row.gestein_id, row.Shape_STAr,row.Shape_STLe,row.geometry))
     sql = str("""INSERT INTO dbo.gdf_ergw1000_gwerg__v11_poly (erg_id,gestein_id,Shape_STAr,Shape_STLe,Geom_Col) values({0},{1},{2},{3},geometry::STGeomFromText('{4}',0))""").format(row.erg_id, row.gestein_id, row.Shape_STAr,row.Shape_STLe,row.geometry)
     cursor.execute(sql)
cnxn.commit()
cursor.close()

