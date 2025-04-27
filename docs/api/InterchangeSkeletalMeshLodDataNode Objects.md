## InterchangeSkeletalMeshLodDataNode Objects

```python
class InterchangeSkeletalMeshLodDataNode(InterchangeFactoryBaseNode)
```

ns UE

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeSkeletalMeshLodDataNode.h

<a id="unreal.InterchangeSkeletalMeshLodDataNode.set_custom_skeleton_uid"></a>

#### set_custom_skeleton_uid

```python
def set_custom_skeleton_uid(attribute_value: str) -> bool
```

x.set_custom_skeleton_uid(attribute_value) -> bool
Set the LOD skeletal mesh factory skeleton reference. Return false if the attribute could not be set.

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalMeshLodDataNode.remove_mesh_uid"></a>

#### remove_mesh_uid

```python
def remove_mesh_uid(mesh_name: str) -> bool
```

x.remove_mesh_uid(mesh_name) -> bool
Remove a mesh geometry used to create this LOD geometry. A mesh UID can represent either a scene node or a mesh node. If it is a scene node, the mesh factory bakes the geometry payload with the global transform of the scene node.

Args:
    mesh_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletalMeshLodDataNode.remove_all_meshes"></a>

#### remove_all_meshes

```python
def remove_all_meshes() -> bool
```

x.remove_all_meshes() -> bool
Remove all mesh geometry used to create this LOD geometry. A mesh UID can represent either a scene node or a mesh node. If it is a scene node, the mesh factory bakes the geometry payload with the global transform of the scene node.

Returns:
    bool:

<a id="unreal.InterchangeSkeletalMeshLodDataNode.get_mesh_uids_count"></a>

#### get_mesh_uids_count

```python
def get_mesh_uids_count() -> int
```

x.get_mesh_uids_count() -> int32
Return the number of mesh geometries this LOD will be made from. A mesh UID can represent either a scene node or a mesh node. If it is a scene node, the mesh factory bakes the geometry payload with the global transform of the scene node.

Returns:
    int32:

<a id="unreal.InterchangeSkeletalMeshLodDataNode.get_mesh_uids"></a>

#### get_mesh_uids

```python
def get_mesh_uids() -> Array[str]
```

x.get_mesh_uids() -> Array[str]
Query all mesh geometry this LOD will be made from. A mesh UID can represent either a scene node or a mesh node. If it is a scene node, the mesh factory bakes the geometry payload with the global transform of the scene node.

Returns:
    Array[str]: 

    out_mesh_names (Array[str]):

<a id="unreal.InterchangeSkeletalMeshLodDataNode.get_custom_skeleton_uid"></a>

#### get_custom_skeleton_uid

```python
def get_custom_skeleton_uid() -> Optional[str]
```

x.get_custom_skeleton_uid() -> str or None
Query the LOD skeletal mesh factory skeleton reference. Return false if the attribute was not set.

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeSkeletalMeshLodDataNode.add_mesh_uid"></a>

#### add_mesh_uid

```python
def add_mesh_uid(mesh_name: str) -> bool
```

x.add_mesh_uid(mesh_name) -> bool
Add a mesh geometry used to create this LOD geometry. A mesh UID can represent either a scene node or a mesh node. If it is a scene node, the mesh factory bakes the geometry payload with the global transform of the scene node.

Args:
    mesh_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeStaticMeshFactoryNode"></a>