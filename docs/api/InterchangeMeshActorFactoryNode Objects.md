## InterchangeMeshActorFactoryNode Objects

```python
class InterchangeMeshActorFactoryNode(InterchangeActorFactoryNode)
```

Interchange Mesh Actor Factory Node

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeMeshActorFactoryNode.h

<a id="unreal.InterchangeMeshActorFactoryNode.set_slot_material_dependency_uid"></a>

#### set_slot_material_dependency_uid

```python
def set_slot_material_dependency_uid(slot_name: str,
                                     material_dependency_uid: str) -> bool
```

x.set_slot_material_dependency_uid(slot_name, material_dependency_uid) -> bool
Add a Material dependency to the specified slot of this object.

Args:
    slot_name (str): 
    material_dependency_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeMeshActorFactoryNode.set_custom_geometric_transform"></a>

#### set_custom_geometric_transform

```python
def set_custom_geometric_transform(attribute_value: Transform) -> bool
```

x.set_custom_geometric_transform(attribute_value) -> bool
Set the geometric offset. Any mesh attached to this scene node will be offset using this transform.

Args:
    attribute_value (Transform): 

Returns:
    bool:

<a id="unreal.InterchangeMeshActorFactoryNode.set_custom_animation_asset_uid_to_play"></a>

#### set_custom_animation_asset_uid_to_play

```python
def set_custom_animation_asset_uid_to_play(attribute_value: str) -> bool
```

x.set_custom_animation_asset_uid_to_play(attribute_value) -> bool
Set the animation asset for this scene node to play. (This is only relevant for SkeletalMeshActors: scene nodes that are instantiating skeletal meshes.)

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeMeshActorFactoryNode.remove_slot_material_dependency_uid"></a>

#### remove_slot_material_dependency_uid

```python
def remove_slot_material_dependency_uid(slot_name: str) -> bool
```

x.remove_slot_material_dependency_uid(slot_name) -> bool
Remove the Material dependency associated with the specified slot name from this object.

Args:
    slot_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMeshActorFactoryNode.get_slot_material_dependency_uid"></a>

#### get_slot_material_dependency_uid

```python
def get_slot_material_dependency_uid(slot_name: str) -> Optional[str]
```

x.get_slot_material_dependency_uid(slot_name) -> str or None
Retrieve the Material dependency for the specified slot of this object.

Args:
    slot_name (str): 

Returns:
    str or None: 

    out_material_dependency (str):

<a id="unreal.InterchangeMeshActorFactoryNode.get_slot_material_dependencies"></a>

#### get_slot_material_dependencies

```python
def get_slot_material_dependencies() -> Map[str, str]
```

x.get_slot_material_dependencies() -> Map[str, str]
Retrieve the correspondence table between slot names and assigned materials for this object.

Returns:
    Map[str, str]: 

    out_material_dependencies (Map[str, str]):

<a id="unreal.InterchangeMeshActorFactoryNode.get_custom_geometric_transform"></a>

#### get_custom_geometric_transform

```python
def get_custom_geometric_transform() -> Optional[Transform]
```

x.get_custom_geometric_transform() -> Transform or None
Get the geometric offset. Any mesh attached to this scene node will be offset using this transform.

Returns:
    Transform or None: 

    attribute_value (Transform):

<a id="unreal.InterchangeMeshActorFactoryNode.get_custom_animation_asset_uid_to_play"></a>

#### get_custom_animation_asset_uid_to_play

```python
def get_custom_animation_asset_uid_to_play() -> Optional[str]
```

x.get_custom_animation_asset_uid_to_play() -> str or None
Get the animation asset set for this scene node to play.

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeMeshFactoryNode"></a>