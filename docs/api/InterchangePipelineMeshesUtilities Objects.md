## InterchangePipelineMeshesUtilities Objects

```python
class InterchangePipelineMeshesUtilities(Object)
```

Interchange Pipeline Meshes Utilities

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangePipelines
- **File**: InterchangePipelineMeshesUtilities.h

<a id="unreal.InterchangePipelineMeshesUtilities.set_context"></a>

#### set_context

```python
def set_context(context: InterchangePipelineMeshesUtilitiesContext) -> None
```

x.set_context(context) -> None
Set Context

Args:
    context (InterchangePipelineMeshesUtilitiesContext):

<a id="unreal.InterchangePipelineMeshesUtilities.is_valid_mesh_instance_uid"></a>

#### is_valid_mesh_instance_uid

```python
def is_valid_mesh_instance_uid(mesh_instance_uid: str) -> bool
```

x.is_valid_mesh_instance_uid(mesh_instance_uid) -> bool
Return true if there is an existing FInterchangeMeshInstance that matches the MeshInstanceUid key.

Args:
    mesh_instance_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangePipelineMeshesUtilities.is_valid_mesh_geometry_uid"></a>

#### is_valid_mesh_geometry_uid

```python
def is_valid_mesh_geometry_uid(mesh_geometry_uid: str) -> bool
```

x.is_valid_mesh_geometry_uid(mesh_geometry_uid) -> bool
Return true if there is an existing FInterchangeMeshGeometry that matches the MeshInstanceUid key.

Args:
    mesh_geometry_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangePipelineMeshesUtilities.get_mesh_instance_skeleton_root_uid"></a>

#### get_mesh_instance_skeleton_root_uid

```python
def get_mesh_instance_skeleton_root_uid(mesh_instance_uid: str) -> str
```

x.get_mesh_instance_skeleton_root_uid(mesh_instance_uid) -> str
Return the skeleton root node UID. This is the UID for a UInterchangeSceneNode that has a "Joint" specialized type.
Return an empty string if the MeshInstanceUid parameter points to nothing.

Args:
    mesh_instance_uid (str): 

Returns:
    str:

<a id="unreal.InterchangePipelineMeshesUtilities.get_mesh_instance_by_uid"></a>

#### get_mesh_instance_by_uid

```python
def get_mesh_instance_by_uid(
        mesh_instance_uid: str) -> InterchangeMeshInstance
```

x.get_mesh_instance_by_uid(mesh_instance_uid) -> InterchangeMeshInstance
Get the instanced mesh from the unique ID.

Args:
    mesh_instance_uid (str): 

Returns:
    InterchangeMeshInstance:

<a id="unreal.InterchangePipelineMeshesUtilities.get_mesh_geometry_skeleton_root_uid"></a>

#### get_mesh_geometry_skeleton_root_uid

```python
def get_mesh_geometry_skeleton_root_uid(mesh_geometry_uid: str) -> str
```

x.get_mesh_geometry_skeleton_root_uid(mesh_geometry_uid) -> str
Return the skeleton root node UID. This is the UID for a UInterchangeSceneNode that has a "Joint" specialized type.
Return an empty string if the MeshGeometryUid parameter points to nothing.

Args:
    mesh_geometry_uid (str): 

Returns:
    str:

<a id="unreal.InterchangePipelineMeshesUtilities.get_mesh_geometry_by_uid"></a>

#### get_mesh_geometry_by_uid

```python
def get_mesh_geometry_by_uid(
        mesh_geometry_uid: str) -> InterchangeMeshGeometry
```

x.get_mesh_geometry_by_uid(mesh_geometry_uid) -> InterchangeMeshGeometry
Get the geometry mesh from the unique ID.

Args:
    mesh_geometry_uid (str): 

Returns:
    InterchangeMeshGeometry:

<a id="unreal.InterchangePipelineMeshesUtilities.get_all_static_mesh_instance"></a>

#### get_all_static_mesh_instance

```python
def get_all_static_mesh_instance() -> Array[str]
```

x.get_all_static_mesh_instance() -> Array[str]
Get the unique IDs of all static mesh instances.

Returns:
    Array[str]: 

    mesh_instance_uids (Array[str]):

<a id="unreal.InterchangePipelineMeshesUtilities.get_all_static_mesh_geometry"></a>

#### get_all_static_mesh_geometry

```python
def get_all_static_mesh_geometry() -> Array[str]
```

x.get_all_static_mesh_geometry() -> Array[str]
Get the unique IDs of all static mesh geometry.

Returns:
    Array[str]: 

    mesh_geometry_uids (Array[str]):

<a id="unreal.InterchangePipelineMeshesUtilities.get_all_skinned_mesh_instance"></a>

#### get_all_skinned_mesh_instance

```python
def get_all_skinned_mesh_instance() -> Array[str]
```

x.get_all_skinned_mesh_instance() -> Array[str]
Get the unique IDs of all skinned mesh instances.

Returns:
    Array[str]: 

    mesh_instance_uids (Array[str]):

<a id="unreal.InterchangePipelineMeshesUtilities.get_all_skinned_mesh_geometry"></a>

#### get_all_skinned_mesh_geometry

```python
def get_all_skinned_mesh_geometry() -> Array[str]
```

x.get_all_skinned_mesh_geometry() -> Array[str]
Get the unique IDs of all skinned mesh geometry.

Returns:
    Array[str]: 

    mesh_geometry_uids (Array[str]):

<a id="unreal.InterchangePipelineMeshesUtilities.get_all_mesh_instance_uids_using_mesh_geometry_uid"></a>

#### get_all_mesh_instance_uids_using_mesh_geometry_uid

```python
def get_all_mesh_instance_uids_using_mesh_geometry_uid(
        mesh_geometry_uid: str) -> Array[str]
```

x.get_all_mesh_instance_uids_using_mesh_geometry_uid(mesh_geometry_uid) -> Array[str]
Get all instanced mesh UIDs that use the mesh geometry unique ID.

Args:
    mesh_geometry_uid (str): 

Returns:
    Array[str]: 

    mesh_instance_uids (Array[str]):

<a id="unreal.InterchangePipelineMeshesUtilities.get_all_mesh_instance_uids"></a>

#### get_all_mesh_instance_uids

```python
def get_all_mesh_instance_uids() -> Array[str]
```

x.get_all_mesh_instance_uids() -> Array[str]
Get the unique IDs of all mesh instances.

Returns:
    Array[str]: 

    mesh_instance_uids (Array[str]):

<a id="unreal.InterchangePipelineMeshesUtilities.get_all_mesh_geometry_not_instanced"></a>

#### get_all_mesh_geometry_not_instanced

```python
def get_all_mesh_geometry_not_instanced() -> Array[str]
```

x.get_all_mesh_geometry_not_instanced() -> Array[str]
Get the unique IDs of all non-instanced mesh geometry.

Returns:
    Array[str]: 

    mesh_geometry_uids (Array[str]):

<a id="unreal.InterchangePipelineMeshesUtilities.get_all_mesh_geometry"></a>

#### get_all_mesh_geometry

```python
def get_all_mesh_geometry() -> Array[str]
```

x.get_all_mesh_geometry() -> Array[str]
Get the unique IDs of all mesh geometry.

Returns:
    Array[str]: 

    mesh_geometry_uids (Array[str]):

<a id="unreal.InterchangePipelineMeshesUtilities.create_interchange_pipeline_meshes_utilities"></a>

#### create_interchange_pipeline_meshes_utilities

```python
@classmethod
def create_interchange_pipeline_meshes_utilities(
    cls, base_node_container: InterchangeBaseNodeContainer
) -> InterchangePipelineMeshesUtilities
```

X.create_interchange_pipeline_meshes_utilities(base_node_container) -> InterchangePipelineMeshesUtilities
Create an instance of UInterchangePipelineMeshesUtilities.

Args:
    base_node_container (InterchangeBaseNodeContainer): 

Returns:
    InterchangePipelineMeshesUtilities:

<a id="unreal.ImgMediaPlaybackComponent"></a>