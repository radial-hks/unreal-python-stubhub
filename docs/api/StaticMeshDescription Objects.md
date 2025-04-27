## StaticMeshDescription Objects

```python
class StaticMeshDescription(MeshDescriptionBase)
```

A wrapper for MeshDescription, customized for static meshes

**C++ Source:**

- **Module**: StaticMeshDescription
- **File**: StaticMeshDescription.h

<a id="unreal.StaticMeshDescription.set_vertex_instance_uv"></a>

#### set_vertex_instance_uv

```python
def set_vertex_instance_uv(vertex_instance_id: VertexInstanceID,
                           uv: Vector2D,
                           uv_index: int = 0) -> None
```

x.set_vertex_instance_uv(vertex_instance_id, uv, uv_index=0) -> None
Set Vertex Instance UV

Args:
    vertex_instance_id (VertexInstanceID): 
    uv (Vector2D): 
    uv_index (int32):

<a id="unreal.StaticMeshDescription.set_polygon_group_material_slot_name"></a>

#### set_polygon_group_material_slot_name

```python
def set_polygon_group_material_slot_name(polygon_group_id: PolygonGroupID,
                                         slot_name: Name) -> None
```

x.set_polygon_group_material_slot_name(polygon_group_id, slot_name) -> None
Set Polygon Group Material Slot Name

Args:
    polygon_group_id (PolygonGroupID): 
    slot_name (Name):

<a id="unreal.StaticMeshDescription.get_vertex_instance_uv"></a>

#### get_vertex_instance_uv

```python
def get_vertex_instance_uv(vertex_instance_id: VertexInstanceID,
                           uv_index: int = 0) -> Vector2D
```

x.get_vertex_instance_uv(vertex_instance_id, uv_index=0) -> Vector2D
Get Vertex Instance UV

Args:
    vertex_instance_id (VertexInstanceID): 
    uv_index (int32): 

Returns:
    Vector2D:

<a id="unreal.StaticMeshDescription.create_cube"></a>

#### create_cube

```python
def create_cube(
    center: Vector, half_extents: Vector, polygon_group: PolygonGroupID
) -> Tuple[PolygonID, PolygonID, PolygonID, PolygonID, PolygonID, PolygonID]
```

x.create_cube(center, half_extents, polygon_group) -> (polygon_id_plus_x=PolygonID, polygon_id_minus_x=PolygonID, polygon_id_plus_y=PolygonID, polygon_id_minus_y=PolygonID, polygon_id_plus_z=PolygonID, polygon_id_minus_z=PolygonID)
Create Cube

Args:
    center (Vector): 
    half_extents (Vector): 
    polygon_group (PolygonGroupID): 

Returns:
    tuple: 

    polygon_id_plus_x (PolygonID): 

    polygon_id_minus_x (PolygonID): 

    polygon_id_plus_y (PolygonID): 

    polygon_id_minus_y (PolygonID): 

    polygon_id_plus_z (PolygonID): 

    polygon_id_minus_z (PolygonID):

<a id="unreal.SkeletalMeshDescription"></a>