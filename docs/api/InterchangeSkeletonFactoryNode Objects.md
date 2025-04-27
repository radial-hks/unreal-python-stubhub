## InterchangeSkeletonFactoryNode Objects

```python
class InterchangeSkeletonFactoryNode(InterchangeFactoryBaseNode)
```

Interchange Skeleton Factory Node

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeSkeletonFactoryNode.h

<a id="unreal.InterchangeSkeletonFactoryNode.set_custom_use_time_zero_for_bind_pose"></a>

#### set_custom_use_time_zero_for_bind_pose

```python
def set_custom_use_time_zero_for_bind_pose(attribute_value: bool) -> bool
```

x.set_custom_use_time_zero_for_bind_pose(attribute_value) -> bool
If AttributeValue is true, force this skeleton to use time-zero evaluation instead of its bind pose.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletonFactoryNode.set_custom_skeletal_mesh_factory_node_uid"></a>

#### set_custom_skeletal_mesh_factory_node_uid

```python
def set_custom_skeletal_mesh_factory_node_uid(attribute_value: str) -> bool
```

x.set_custom_skeletal_mesh_factory_node_uid(attribute_value) -> bool
Set Custom Skeletal Mesh Factory Node Uid

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletonFactoryNode.set_custom_root_joint_uid"></a>

#### set_custom_root_joint_uid

```python
def set_custom_root_joint_uid(attribute_value: str) -> bool
```

x.set_custom_root_joint_uid(attribute_value) -> bool
Set Custom Root Joint Uid

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletonFactoryNode.initialize_skeleton_node"></a>

#### initialize_skeleton_node

```python
def initialize_skeleton_node(unique_id: str, display_label: str,
                             asset_class: str) -> None
```

x.initialize_skeleton_node(unique_id, display_label, asset_class) -> None
Initialize node data.
param:: UniqueID - The unique ID for this node.

Args:
    unique_id (str): 
    display_label (str): The name of the node.
    asset_class (str): The class the Skeleton factory will create for this node.

<a id="unreal.InterchangeSkeletonFactoryNode.get_object_class"></a>

#### get_object_class

```python
def get_object_class() -> Class
```

x.get_object_class() -> type(Class)
Get the class this node creates.

Returns:
    type(Class):

<a id="unreal.InterchangeSkeletonFactoryNode.get_custom_use_time_zero_for_bind_pose"></a>

#### get_custom_use_time_zero_for_bind_pose

```python
def get_custom_use_time_zero_for_bind_pose() -> Optional[bool]
```

x.get_custom_use_time_zero_for_bind_pose() -> bool or None
Query whether this skeleton should replace joint transforms with time-zero evaluation instead of bind pose.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeSkeletonFactoryNode.get_custom_skeletal_mesh_factory_node_uid"></a>

#### get_custom_skeletal_mesh_factory_node_uid

```python
def get_custom_skeletal_mesh_factory_node_uid() -> Optional[str]
```

x.get_custom_skeletal_mesh_factory_node_uid() -> str or None
Get Custom Skeletal Mesh Factory Node Uid

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeSkeletonFactoryNode.get_custom_root_joint_uid"></a>

#### get_custom_root_joint_uid

```python
def get_custom_root_joint_uid() -> Optional[str]
```

x.get_custom_root_joint_uid() -> str or None
Return false if the attribute was not set previously.

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeTextureFactoryNode"></a>