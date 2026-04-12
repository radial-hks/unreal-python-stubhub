## MeshHeatMapTools Objects

```python
class MeshHeatMapTools(BlueprintFunctionLibrary)
```

Mesh Heat Map Tools

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpDataV
- **File**: MeshHeatMapTools.h

<a id="unreal.MeshHeatMapTools.generate_heat_map_mesh"></a>

#### generate\_heat\_map\_mesh

```python
@classmethod
def generate_heat_map_mesh(cls,
                           world_context_object: Object,
                           points: Array[Vector],
                           values: Array[float],
                           mesh_boundary: Array[Vector2D],
                           value_range: Vector2D,
                           mapping_height_range: Vector2D,
                           color_map: Array[LinearColor],
                           grid_spacing: float = 5.000000) -> MeshHeatMapData
```

X.generate_heat_map_mesh(world_context_object, points, values, mesh_boundary, value_range, mapping_height_range, color_map, grid_spacing=5.000000) -> MeshHeatMapData
Generate Heat Map Mesh

Args:
    world_context_object (Object): 
    points (Array[Vector]): 
    values (Array[float]): 
    mesh_boundary (Array[Vector2D]): 
    value_range (Vector2D): 
    mapping_height_range (Vector2D): 
    color_map (Array[LinearColor]): 
    grid_spacing (float): 

Returns:
    MeshHeatMapData:

<a id="unreal.BatchPlaceAssetParams"></a>