# Clean up script to undo the styling changes

from arcgis.gis import *
import os

url = 'https://liy.esrichina.com/portal'
admin_username = 'arcgis'
admin_password = 'Super123'


print("Cleaning up portal style")

try:
    #create a GIS connection
    city_gis = GIS(url, admin_username, admin_password, verify_cert=False)
    print("    Connected to the ArcGIS Enterprise")

    #reset the background file
    city_gis.admin.ux.set_background(background_file=None, is_built_in=False)
    print("    reset Background")

    city_gis.admin.ux.set_banner('banner-2',True)
    print("    reset Banner")

    city_gis.admin.ux.name="ArcGIS Enterprise"
    city_gis.admin.ux.description = ""
    city_gis.admin.ux.description_visibility="false"
    print("    reset name and description")

    city_gis.admin.ux.set_logo(None)

except Exception as style_ex:
    print(str(style_ex))