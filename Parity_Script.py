# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Parity_Script.py
# Created on: 2020-04-06 14:07:24.00000
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

Road_Centerlines_In = arcpy.GetParameterAsText(0)

# Local variables:

Road_Centerlines_Layer = "Road_Centerlines_Layer"

# Process: Make Feature Layer
arcpy.MakeFeatureLayer_management(Road_Centerlines_In, Road_Centerlines_Layer)

# Process: Select Layer By Attribute
arcpy.SelectLayerByAttribute_management(Road_Centerlines_Layer, "NEW_SELECTION", "fromaddr_l <> 0 and toaddr_l <> 0 AND MOD (\"fromaddr_l \",  2) = 1 and MOD (\"toaddr_l\",  2) = 1")

# Process: Calculate Field
arcpy.CalculateField_management(Road_Centerlines_Layer, "parity_l", "\"O\"", "VB", "")

# Process: Select Layer By Attribute (2)
arcpy.SelectLayerByAttribute_management(Road_Centerlines_Layer, "NEW_SELECTION", "fromaddr_r <> 0 and toaddr_r <> 0 AND MOD (\"fromaddr_r \",  2) = 1 and MOD (\"toaddr_r\",  2) = 1")
# Process: Calculate Field (2)
arcpy.CalculateField_management(Road_Centerlines_Layer, "parity_r", "\"O\"", "VB", "")

# Process: Select Layer By Attribute (3)
arcpy.SelectLayerByAttribute_management(Road_Centerlines_Layer, "NEW_SELECTION", "fromaddr_l <> 0 and toaddr_l <> 0 AND MOD (\"fromaddr_l \",  2) = 0 and MOD (\"toaddr_l\",  2) = 0")

# Process: Calculate Field (3)
arcpy.CalculateField_management(Road_Centerlines_Layer, "parity_l", "\"E\"", "VB", "")

# Process: Select Layer By Attribute (4)
arcpy.SelectLayerByAttribute_management(Road_Centerlines_Layer, "NEW_SELECTION", "fromaddr_r <> 0 and toaddr_r <> 0 AND MOD (\"fromaddr_r \",  2) = 0 and MOD (\"toaddr_r\",  2) = 0")

# Process: Calculate Field (4)
arcpy.CalculateField_management(Road_Centerlines_Layer, "parity_r", "\"E\"", "VB", "")

# Process: Select Layer By Attribute (5)
arcpy.SelectLayerByAttribute_management(Road_Centerlines_Layer, "NEW_SELECTION", "fromaddr_l = 0 AND toaddr_l = 0")

# Process: Calculate Field (5)
arcpy.CalculateField_management(Road_Centerlines_Layer, "parity_l", "\"Z\"", "VB", "")

# Process: Select Layer By Attribute (6)
arcpy.SelectLayerByAttribute_management(Road_Centerlines_Layer, "NEW_SELECTION", "fromaddr_r = 0 AND toaddr_r = 0")

# Process: Calculate Field (6)
arcpy.CalculateField_management(Road_Centerlines_Layer, "parity_r", "\"Z\"", "VB", "")

# Process: Select Layer By Attribute (7)
arcpy.SelectLayerByAttribute_management(Road_Centerlines_Layer, "NEW_SELECTION", "MOD (\"toaddr_l\",  2) = 0 AND MOD (\"fromaddr_l \",  2) = 1")

# Process: Calculate Field (7)
arcpy.CalculateField_management(Road_Centerlines_Layer, "parity_l", "\"B\"", "VB", "")

# Process: Select Layer By Attribute (8)
arcpy.SelectLayerByAttribute_management(Road_Centerlines_Layer, "NEW_SELECTION", "MOD (\"toaddr_l\",  2) = 1 AND MOD (\"fromaddr_l \",  2) = 0")

# Process: Calculate Field (8)
arcpy.CalculateField_management(Road_Centerlines_Layer, "parity_l", "\"B\"", "VB", "")

# Process: Select Layer By Attribute (9)
arcpy.SelectLayerByAttribute_management(Road_Centerlines_Layer, "NEW_SELECTION", "MOD (\"toaddr_r\",  2) = 0 AND MOD (\"fromaddr_r \",  2) = 1")

# Process: Calculate Field (9)
arcpy.CalculateField_management(Road_Centerlines_Layer, "parity_r", "\"B\"", "VB", "")

# Process: Select Layer By Attribute (10)
arcpy.SelectLayerByAttribute_management(Road_Centerlines_Layer, "NEW_SELECTION", "MOD (\"toaddr_r\",  2) = 1 AND MOD (\"fromaddr_r \",  2) = 0")

# Process: Calculate Field (10)
arcpy.CalculateField_management(Road_Centerlines_Layer, "parity_r", "\"B\"", "VB", "")

