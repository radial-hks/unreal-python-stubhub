## InterchangePhysicsAssetFactoryNode Objects

```python
class InterchangePhysicsAssetFactoryNode(InterchangeFactoryBaseNode)
```

Interchange Physics Asset Factory Node

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangePhysicsAssetFactoryNode.h

<a id="unreal.InterchangePhysicsAssetFactoryNode.set_custom_skeletal_mesh_uid"></a>

#### set_custom_skeletal_mesh_uid

```python
def set_custom_skeletal_mesh_uid(attribute_value: str) -> bool
```

x.set_custom_skeletal_mesh_uid(attribute_value) -> bool
Set the Skeletal Mesh asset UID used to create the data in the post-pipeline step.

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangePhysicsAssetFactoryNode.initialize_physics_asset_node"></a>

#### initialize_physics_asset_node

```python
def initialize_physics_asset_node(unique_id: str, display_label: str,
                                  asset_class: str) -> None
```

x.initialize_physics_asset_node(unique_id, display_label, asset_class) -> None
Initialize node data.
param:: UniqueID - The unique ID for this node.

Args:
    unique_id (str): 
    display_label (str): The name of the node.
    asset_class (str): The class the Skeleton factory will create for this node.

<a id="unreal.InterchangePhysicsAssetFactoryNode.get_object_class"></a>

#### get_object_class

```python
def get_object_class() -> Class
```

x.get_object_class() -> type(Class)
Get the class this node creates.

Returns:
    type(Class):

<a id="unreal.InterchangePhysicsAssetFactoryNode.get_custom_skeletal_mesh_uid"></a>

#### get_custom_skeletal_mesh_uid

```python
def get_custom_skeletal_mesh_uid() -> Optional[str]
```

x.get_custom_skeletal_mesh_uid() -> str or None
Get the Skeletal Mesh asset UID used to create the data in the post-pipeline step.

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeSceneVariantSetsFactoryNode"></a>