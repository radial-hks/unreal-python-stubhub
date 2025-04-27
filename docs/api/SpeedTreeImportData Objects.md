## SpeedTreeImportData Objects

```python
class SpeedTreeImportData(AssetImportData)
```

Speed Tree Import Data

**C++ Source:**

- **Plugin**: SpeedTreeImporter
- **Module**: SpeedTreeImporter
- **File**: SpeedTreeImportData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``import_geometry_type`` (ImportGeometryType):  [Read-Write] Choose whether to import as a 3D asset, billboard or both
- ``include_branch_seam_smoothing`` (bool):  [Read-Write]
- ``include_collision`` (bool):  [Read-Write]
- ``include_color_adjustment`` (bool):  [Read-Write]
- ``include_detail_map_check`` (bool):  [Read-Write]
- ``include_normal_map_check`` (bool):  [Read-Write]
- ``include_smooth_lod_check`` (bool):  [Read-Write]
- ``include_specular_map_check`` (bool):  [Read-Write]
- ``include_speed_tree_ao`` (bool):  [Read-Write]
- ``include_subsurface`` (bool):  [Read-Write]
- ``include_vertex_processing_check`` (bool):  [Read-Write]
- ``include_wind_check`` (bool):  [Read-Write]
- ``lod_type`` (ImportLODType):  [Read-Write] Choose whether painted foliage or individual actor
- ``make_materials_check`` (bool):  [Read-Write]
- ``source_data`` (AssetImportInfo):  [Read-Only] Source file data describing the files that were used to import this asset.
- ``tree_scale`` (float):  [Read-Write] Specify the tree scale

<a id="unreal.WidgetPreview"></a>