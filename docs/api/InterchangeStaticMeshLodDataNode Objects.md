## InterchangeStaticMeshLodDataNode Objects

```python
class InterchangeStaticMeshLodDataNode(InterchangeFactoryBaseNode)
```

namespace UE

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeStaticMeshLodDataNode.h

<a id="unreal.InterchangeStaticMeshLodDataNode.set_one_convex_hull_per_ucx"></a>

#### set_one_convex_hull_per_ucx

```python
def set_one_convex_hull_per_ucx(attribute_value: bool) -> bool
```

x.set_one_convex_hull_per_ucx(attribute_value) -> bool
Set One Convex Hull Per UCX

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshLodDataNode.set_import_collision_type"></a>

#### set_import_collision_type

```python
def set_import_collision_type(
        attribute_value: InterchangeMeshCollision) -> bool
```

x.set_import_collision_type(attribute_value) -> bool
Set Import Collision Type

Args:
    attribute_value (InterchangeMeshCollision): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshLodDataNode.set_import_collision"></a>

#### set_import_collision

```python
def set_import_collision(attribute_value: bool) -> bool
```

x.set_import_collision(attribute_value) -> bool
Set Import Collision

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshLodDataNode.remove_sphere_collision_mesh_uid"></a>

#### remove_sphere_collision_mesh_uid

```python
def remove_sphere_collision_mesh_uid(mesh_name: str) -> bool
```

x.remove_sphere_collision_mesh_uid(mesh_name) -> bool
Remove Sphere Collision Mesh Uid

Args:
    mesh_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshLodDataNode.remove_mesh_uid"></a>

#### remove_mesh_uid

```python
def remove_mesh_uid(mesh_name: str) -> bool
```

x.remove_mesh_uid(mesh_name) -> bool
Remove Mesh Uid

Args:
    mesh_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshLodDataNode.remove_convex_collision_mesh_uid"></a>

#### remove_convex_collision_mesh_uid

```python
def remove_convex_collision_mesh_uid(mesh_name: str) -> bool
```

x.remove_convex_collision_mesh_uid(mesh_name) -> bool
Remove Convex Collision Mesh Uid

Args:
    mesh_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshLodDataNode.remove_capsule_collision_mesh_uid"></a>

#### remove_capsule_collision_mesh_uid

```python
def remove_capsule_collision_mesh_uid(mesh_name: str) -> bool
```

x.remove_capsule_collision_mesh_uid(mesh_name) -> bool
Remove Capsule Collision Mesh Uid

Args:
    mesh_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshLodDataNode.remove_box_collision_mesh_uid"></a>

#### remove_box_collision_mesh_uid

```python
def remove_box_collision_mesh_uid(mesh_name: str) -> bool
```

x.remove_box_collision_mesh_uid(mesh_name) -> bool
Remove Box Collision Mesh Uid

Args:
    mesh_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshLodDataNode.remove_all_sphere_collision_meshes"></a>

#### remove_all_sphere_collision_meshes

```python
def remove_all_sphere_collision_meshes() -> bool
```

x.remove_all_sphere_collision_meshes() -> bool
Remove All Sphere Collision Meshes

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshLodDataNode.remove_all_meshes"></a>

#### remove_all_meshes

```python
def remove_all_meshes() -> bool
```

x.remove_all_meshes() -> bool
Remove All Meshes

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshLodDataNode.remove_all_convex_collision_meshes"></a>

#### remove_all_convex_collision_meshes

```python
def remove_all_convex_collision_meshes() -> bool
```

x.remove_all_convex_collision_meshes() -> bool
Remove All Convex Collision Meshes

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshLodDataNode.remove_all_capsule_collision_meshes"></a>

#### remove_all_capsule_collision_meshes

```python
def remove_all_capsule_collision_meshes() -> bool
```

x.remove_all_capsule_collision_meshes() -> bool
Remove All Capsule Collision Meshes

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshLodDataNode.remove_all_box_collision_meshes"></a>

#### remove_all_box_collision_meshes

```python
def remove_all_box_collision_meshes() -> bool
```

x.remove_all_box_collision_meshes() -> bool
Remove All Box Collision Meshes

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshLodDataNode.get_sphere_collision_mesh_uids_count"></a>

#### get_sphere_collision_mesh_uids_count

```python
def get_sphere_collision_mesh_uids_count() -> int
```

x.get_sphere_collision_mesh_uids_count() -> int32
Get Sphere Collision Mesh Uids Count

Returns:
    int32:

<a id="unreal.InterchangeStaticMeshLodDataNode.get_sphere_collision_mesh_uids"></a>

#### get_sphere_collision_mesh_uids

```python
def get_sphere_collision_mesh_uids() -> Array[str]
```

x.get_sphere_collision_mesh_uids() -> Array[str]
Get Sphere Collision Mesh Uids

Returns:
    Array[str]: 

    out_mesh_names (Array[str]):

<a id="unreal.InterchangeStaticMeshLodDataNode.get_one_convex_hull_per_ucx"></a>

#### get_one_convex_hull_per_ucx

```python
def get_one_convex_hull_per_ucx() -> Optional[bool]
```

x.get_one_convex_hull_per_ucx() -> bool or None
Get One Convex Hull Per UCX

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeStaticMeshLodDataNode.get_mesh_uids_count"></a>

#### get_mesh_uids_count

```python
def get_mesh_uids_count() -> int
```

x.get_mesh_uids_count() -> int32
Mesh UIDs can be either a scene node or a mesh node UID. If it is a scene node, the mesh factory bakes the geometry payload with the global transform of the scene node.

Returns:
    int32:

<a id="unreal.InterchangeStaticMeshLodDataNode.get_mesh_uids"></a>

#### get_mesh_uids

```python
def get_mesh_uids() -> Array[str]
```

x.get_mesh_uids() -> Array[str]
Get Mesh Uids

Returns:
    Array[str]: 

    out_mesh_names (Array[str]):

<a id="unreal.InterchangeStaticMeshLodDataNode.get_import_collision_type"></a>

#### get_import_collision_type

```python
def get_import_collision_type() -> Optional[InterchangeMeshCollision]
```

x.get_import_collision_type() -> InterchangeMeshCollision or None
Get Import Collision Type

Returns:
    InterchangeMeshCollision or None: 

    attribute_value (InterchangeMeshCollision):

<a id="unreal.InterchangeStaticMeshLodDataNode.get_import_collision"></a>

#### get_import_collision

```python
def get_import_collision() -> Optional[bool]
```

x.get_import_collision() -> bool or None
Get Import Collision

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeStaticMeshLodDataNode.get_convex_collision_mesh_uids_count"></a>

#### get_convex_collision_mesh_uids_count

```python
def get_convex_collision_mesh_uids_count() -> int
```

x.get_convex_collision_mesh_uids_count() -> int32
Get Convex Collision Mesh Uids Count

Returns:
    int32:

<a id="unreal.InterchangeStaticMeshLodDataNode.get_convex_collision_mesh_uids"></a>

#### get_convex_collision_mesh_uids

```python
def get_convex_collision_mesh_uids() -> Array[str]
```

x.get_convex_collision_mesh_uids() -> Array[str]
Get Convex Collision Mesh Uids

Returns:
    Array[str]: 

    out_mesh_names (Array[str]):

<a id="unreal.InterchangeStaticMeshLodDataNode.get_capsule_collision_mesh_uids_count"></a>

#### get_capsule_collision_mesh_uids_count

```python
def get_capsule_collision_mesh_uids_count() -> int
```

x.get_capsule_collision_mesh_uids_count() -> int32
Get Capsule Collision Mesh Uids Count

Returns:
    int32:

<a id="unreal.InterchangeStaticMeshLodDataNode.get_capsule_collision_mesh_uids"></a>

#### get_capsule_collision_mesh_uids

```python
def get_capsule_collision_mesh_uids() -> Array[str]
```

x.get_capsule_collision_mesh_uids() -> Array[str]
Get Capsule Collision Mesh Uids

Returns:
    Array[str]: 

    out_mesh_names (Array[str]):

<a id="unreal.InterchangeStaticMeshLodDataNode.get_box_collision_mesh_uids_count"></a>

#### get_box_collision_mesh_uids_count

```python
def get_box_collision_mesh_uids_count() -> int
```

x.get_box_collision_mesh_uids_count() -> int32
Get Box Collision Mesh Uids Count

Returns:
    int32:

<a id="unreal.InterchangeStaticMeshLodDataNode.get_box_collision_mesh_uids"></a>

#### get_box_collision_mesh_uids

```python
def get_box_collision_mesh_uids() -> Array[str]
```

x.get_box_collision_mesh_uids() -> Array[str]
Get Box Collision Mesh Uids

Returns:
    Array[str]: 

    out_mesh_names (Array[str]):

<a id="unreal.InterchangeStaticMeshLodDataNode.add_sphere_collision_mesh_uid"></a>

#### add_sphere_collision_mesh_uid

```python
def add_sphere_collision_mesh_uid(mesh_name: str) -> bool
```

x.add_sphere_collision_mesh_uid(mesh_name) -> bool
Add Sphere Collision Mesh Uid

Args:
    mesh_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshLodDataNode.add_mesh_uid"></a>

#### add_mesh_uid

```python
def add_mesh_uid(mesh_name: str) -> bool
```

x.add_mesh_uid(mesh_name) -> bool
Add Mesh Uid

Args:
    mesh_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshLodDataNode.add_convex_collision_mesh_uid"></a>

#### add_convex_collision_mesh_uid

```python
def add_convex_collision_mesh_uid(mesh_name: str) -> bool
```

x.add_convex_collision_mesh_uid(mesh_name) -> bool
Add Convex Collision Mesh Uid

Args:
    mesh_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshLodDataNode.add_capsule_collision_mesh_uid"></a>

#### add_capsule_collision_mesh_uid

```python
def add_capsule_collision_mesh_uid(mesh_name: str) -> bool
```

x.add_capsule_collision_mesh_uid(mesh_name) -> bool
Add Capsule Collision Mesh Uid

Args:
    mesh_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshLodDataNode.add_box_collision_mesh_uid"></a>

#### add_box_collision_mesh_uid

```python
def add_box_collision_mesh_uid(mesh_name: str) -> bool
```

x.add_box_collision_mesh_uid(mesh_name) -> bool
Add Box Collision Mesh Uid

Args:
    mesh_name (str): 

Returns:
    bool:

<a id="unreal.UsdAssetCache2"></a>