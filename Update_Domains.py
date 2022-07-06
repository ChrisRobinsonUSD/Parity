# -*- coding: cp1252 -*-
#-------------------------------------------------------------------------------
# Name:         Calculate_Domains.py
# Purpose:      Calculates Domains for Importing Data into DataMark VEP Schema
#               
# Author:       Chris Robinson
#
# Created:      03/18/2019
# Updated:      
#-------------------------------------------------------------------------------

import arcpy
import csv


fc = 'C:/Working/NG911/ng911_gis_data.gdb/Roads_Test'
lookuptable = "C:/Working/NG911/LookupTable.csv"

fc_fields = ['road_type_1','road_type_abr']
      
with arcpy.da.UpdateCursor(fc, fc_fields) as cursor:
    for row in cursor:
        val = str(row[0])
        with open(lookuptable, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for col in reader:
                p = [col[0]]
                if val in p:
                    row[1]=col[1]
                    cursor.updateRow(row)
       
