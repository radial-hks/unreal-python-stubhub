## InterchangeLevelFactoryNode Objects

```python
class InterchangeLevelFactoryNode(InterchangeFactoryBaseNode)
```

Interchange Level Factory Node

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeLevelFactoryNode.h

<a id="unreal.InterchangeLevelFactoryNode.set_custom_should_create_level"></a>

#### set_custom_should_create_level

```python
def set_custom_should_create_level(attribute_value: bool) -> bool
```

x.set_custom_should_create_level(attribute_value) -> bool
Set actors bounding box.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeLevelFactoryNode.set_custom_scene_import_asset_factory_node_uid"></a>

#### set_custom_scene_import_asset_factory_node_uid

```python
def set_custom_scene_import_asset_factory_node_uid(
        attribute_value: str) -> bool
```

x.set_custom_scene_import_asset_factory_node_uid(attribute_value) -> bool
Set the actor factory node unique id that hold the re-import data.

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeLevelFactoryNode.set_custom_create_world_partition_level"></a>

#### set_custom_create_world_partition_level

```python
def set_custom_create_world_partition_level(attribute_value: bool) -> bool
```

x.set_custom_create_world_partition_level(attribute_value) -> bool
If true, created world partition level.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeLevelFactoryNode.remove_custom_actor_factory_node_uid"></a>

#### remove_custom_actor_factory_node_uid

```python
def remove_custom_actor_factory_node_uid(actor_factory_node_uid: str) -> bool
```

x.remove_custom_actor_factory_node_uid(actor_factory_node_uid) -> bool
Remove one actor factory node unique id from this object.

Args:
    actor_factory_node_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeLevelFactoryNode.get_object_class"></a>

#### get_object_class

```python
def get_object_class() -> Class
```

x.get_object_class() -> type(Class)
Get the class this node want to create

Returns:
    type(Class):

<a id="unreal.InterchangeLevelFactoryNode.get_custom_should_create_level"></a>

#### get_custom_should_create_level

```python
def get_custom_should_create_level() -> Optional[bool]
```

x.get_custom_should_create_level() -> bool or None
Get actors bounding box.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeLevelFactoryNode.get_custom_scene_import_asset_factory_node_uid"></a>

#### get_custom_scene_import_asset_factory_node_uid

```python
def get_custom_scene_import_asset_factory_node_uid() -> Optional[str]
```

x.get_custom_scene_import_asset_factory_node_uid() -> str or None
Get the actor factory node unique id that hold the re-import data.

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeLevelFactoryNode.get_custom_create_world_partition_level"></a>

#### get_custom_create_world_partition_level

```python
def get_custom_create_world_partition_level() -> Optional[bool]
```

x.get_custom_create_world_partition_level() -> bool or None
If true, created world partition level.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeLevelFactoryNode.get_custom_actor_factory_node_uids"></a>

#### get_custom_actor_factory_node_uids

```python
def get_custom_actor_factory_node_uids() -> Array[str]
```

x.get_custom_actor_factory_node_uids() -> Array[str]
This function allow to retrieve all actor factory node unique id for this object.

Returns:
    Array[str]: 

    out_actor_factory_node_uids (Array[str]):

<a id="unreal.InterchangeLevelFactoryNode.get_custom_actor_factory_node_uid_count"></a>

#### get_custom_actor_factory_node_uid_count

```python
def get_custom_actor_factory_node_uid_count() -> int
```

x.get_custom_actor_factory_node_uid_count() -> int32
This function allow to retrieve the number of track dependencies for this object.

Returns:
    int32:

<a id="unreal.InterchangeLevelFactoryNode.get_custom_actor_factory_node_uid"></a>

#### get_custom_actor_factory_node_uid

```python
def get_custom_actor_factory_node_uid(index: int) -> str
```

x.get_custom_actor_factory_node_uid(index) -> str
This function allow to retrieve one actor factory node unique id for this object.

Args:
    index (int32): 

Returns:
    str: 

    out_actor_factory_node_uid (str):

<a id="unreal.InterchangeLevelFactoryNode.add_custom_actor_factory_node_uid"></a>

#### add_custom_actor_factory_node_uid

```python
def add_custom_actor_factory_node_uid(actor_factory_node_uid: str) -> bool
```

x.add_custom_actor_factory_node_uid(actor_factory_node_uid) -> bool
Add one actor factory node unique id to this object.

Args:
    actor_factory_node_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeLevelInstanceActorFactoryNode"></a>