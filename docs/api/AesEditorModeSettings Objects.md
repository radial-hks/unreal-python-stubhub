## AesEditorModeSettings Objects

```python
class AesEditorModeSettings(DeveloperSettings)
```

Aes Editor Mode Settings

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEditorMode
- **File**: AesEditorModeSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angle_snap_threshold`` (float):  [Read-Write]
- ``building_prefab_tables`` (Array[SoftObjectPath]):  [Read-Write]
- ``building_style`` (AesEditorVectorStyle):  [Read-Write] Building Style
- ``building_types`` (Array[str]):  [Read-Write]
- ``camera_speed`` (int32):  [Read-Write]
- ``camera_speed_scalar`` (float):  [Read-Write]
- ``camera_speed_zoom`` (float):  [Read-Write]
- ``coastline_style`` (AesEditorVectorStyle):  [Read-Write] Coastline Style
- ``custom_dom_channels`` (Array[CustomDomChannel]):  [Read-Write]
- ``earth_actor_level_template`` (Map[str, SoftObjectPath]):  [Read-Write] Earth Actor Template
- ``editor_default_pawn`` (SoftClassPath):  [Read-Write]
- ``flow_map_style`` (AesEditorVectorStyle):  [Read-Write] FlowMap Style
- ``game_default_pawn`` (SoftClassPath):  [Read-Write]
- ``guide_line_color`` (Color):  [Read-Write] Guide Line Color
- ``guide_line_length`` (float):  [Read-Write] Guide Line Length
- ``guide_line_thickness`` (float):  [Read-Write] Guide Line Thickness
- ``half_point_hit_size`` (Vector2D):  [Read-Write] Half Point Hit Size
- ``junction_style`` (AesEditorVectorStyle):  [Read-Write] Junction Style
- ``landmark_style`` (AesEditorVectorStyle):  [Read-Write] Landmark Style
- ``mouse_move_detect_delta_time`` (float):  [Read-Write] Vector
- ``road_modify_style`` (AesEditorRoadModifyStyle):  [Read-Write] Road Modify
- ``road_style`` (AesEditorVectorStyle):  [Read-Write] Road Style
- ``show_editing_region`` (bool):  [Read-Write]
- ``splat_map_style`` (AesEditorVectorStyle):  [Read-Write] SplatMap Style
- ``tangent_handle_style`` (AesEditorVectorStyle):  [Read-Write] Road Style
- ``tangent_scale`` (float):  [Read-Write] Tangent Scale
- ``terraforming_style`` (AesEditorVectorStyle):  [Read-Write] Water Style
- ``vegetation_erase_color`` (LinearColor):  [Read-Write] Vegetation Style
- ``vegetation_paint_color`` (LinearColor):  [Read-Write] Vegetation Style
- ``water_style`` (AesEditorVectorStyle):  [Read-Write] Water Style
- ``z_axis_translation_unit`` (float):  [Read-Write] Vector

<a id="unreal.AesEditorModeSettings.angle_snap_threshold"></a>

#### angle\_snap\_threshold

```python
@property
def angle_snap_threshold() -> float
```

(float):  [Read-Only]

<a id="unreal.AesEditorModeSettingsLibrary"></a>