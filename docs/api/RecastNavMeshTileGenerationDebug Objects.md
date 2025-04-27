## RecastNavMeshTileGenerationDebug Objects

```python
class RecastNavMeshTileGenerationDebug(StructBase)
```

Recast Nav Mesh Tile Generation Debug

**C++ Source:**

- **Module**: NavigationSystem
- **File**: RecastNavMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collision_geometry`` (bool):  [Read-Write] Display the collision used for the navmesh rasterization.
  Note: The visualization is affected by the DrawOffset of the RecastNavmesh owner
- ``compact_heightfield`` (bool):  [Read-Write]
- ``compact_heightfield_distances`` (bool):  [Read-Write]
- ``compact_heightfield_eroded`` (bool):  [Read-Write]
- ``compact_heightfield_regions`` (bool):  [Read-Write]
- ``enabled`` (bool):  [Read-Write] If set, the selected internal debug data will be kept during tile generation to be displayed with the navmesh.
- ``generate_debug_tile_only`` (bool):  [Read-Write] If set, the generator will only generate the tile selected to debug (set in TileCoordinate).
- ``height_field_layers`` (bool):  [Read-Write]
- ``height_field_render_mode`` (HeightFieldRenderMode):  [Read-Write]
- ``heightfield_bounds`` (bool):  [Read-Write]
- ``heightfield_from_rasterization`` (bool):  [Read-Write]
- ``heightfield_post_height_filtering`` (bool):  [Read-Write]
- ``heightfield_post_inclusion_bounds_filtering`` (bool):  [Read-Write]
- ``link_generation_debug_flags`` (uint16):  [Read-Write]
- ``link_generation_selected_edge`` (int32):  [Read-Write] Using -1 as no selected edge.
- ``skip_contour_simplification`` (bool):  [Read-Write] If set, the contour simplification step will be skipped. Beware that enabling this changes the way navmesh will generate when Tile Generation Debug is enabled.
- ``tile_cache_contours`` (bool):  [Read-Write]
- ``tile_cache_detail_mesh`` (bool):  [Read-Write]
- ``tile_cache_layer_areas`` (bool):  [Read-Write]
- ``tile_cache_layer_regions`` (bool):  [Read-Write]
- ``tile_cache_poly_mesh`` (bool):  [Read-Write]
- ``tile_coordinate`` (IntVector):  [Read-Write] Selected tile coordinate, only this tile will have it's internal data kept.
  Tip: displaying the navmesh using 'Draw Tile Labels' show tile coordinates.

<a id="unreal.RecastNavMeshTileGenerationDebug.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NavMeshResolutionParam"></a>