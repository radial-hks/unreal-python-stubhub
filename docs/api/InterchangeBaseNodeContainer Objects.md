## InterchangeBaseNodeContainer Objects

```python
class InterchangeBaseNodeContainer(Object)
```

The Interchange UInterchangeBaseNode graph is a format used to feed factories and writers when they import, reimport, and
export an asset or scene.

This container holds a flat list of all nodes that have been translated from the source data.
Translators fill this container, and the import/export managers read it to execute the import/export process.

**C++ Source:**

- **Module**: InterchangeCore
- **File**: InterchangeBaseNodeContainer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``nodes`` (Map[str, InterchangeBaseNode]):  [Read-Only] Flat List of the nodes. Since the nodes are variable size, we store a pointer.

<a id="unreal.InterchangeBaseNodeContainer.set_node_parent_uid"></a>

#### set_node_parent_uid

```python
def set_node_parent_uid(node_unique_id: str, new_parent_node_uid: str) -> bool
```

x.set_node_parent_uid(node_unique_id, new_parent_node_uid) -> bool
Set the ParentUid of the node.

Args:
    node_unique_id (str): 
    new_parent_node_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeBaseNodeContainer.save_to_file"></a>

#### save_to_file

```python
def save_to_file(filename: str) -> None
```

x.save_to_file(filename) -> None
Serialize the node container into the specified file.

Args:
    filename (str):

<a id="unreal.InterchangeBaseNodeContainer.reset_children_cache"></a>

#### reset_children_cache

```python
def reset_children_cache() -> None
```

x.reset_children_cache() -> None
Reset the cache of children UIDs.

<a id="unreal.InterchangeBaseNodeContainer.reset"></a>

#### reset

```python
def reset() -> None
```

x.reset() -> None
Empty the container.

<a id="unreal.InterchangeBaseNodeContainer.replace_node"></a>

#### replace_node

```python
def replace_node(node_unique_id: str,
                 new_node: InterchangeFactoryBaseNode) -> None
```

x.replace_node(node_unique_id, new_node) -> None
Replace Node

Args:
    node_unique_id (str): 
    new_node (InterchangeFactoryBaseNode):

<a id="unreal.InterchangeBaseNodeContainer.load_from_file"></a>

#### load_from_file

```python
def load_from_file(filename: str) -> None
```

x.load_from_file(filename) -> None
Serialize the node container from the specified file.

Args:
    filename (str):

<a id="unreal.InterchangeBaseNodeContainer.is_node_uid_valid"></a>

#### is_node_uid_valid

```python
def is_node_uid_valid(node_unique_id: str) -> bool
```

x.is_node_uid_valid(node_unique_id) -> bool
Return true if the node unique ID exists in the container.

Args:
    node_unique_id (str): 

Returns:
    bool:

<a id="unreal.InterchangeBaseNodeContainer.get_roots"></a>

#### get_roots

```python
def get_roots() -> Array[str]
```

x.get_roots() -> Array[str]
Return all nodes that do not have any parent.

Returns:
    Array[str]: 

    root_nodes (Array[str]):

<a id="unreal.InterchangeBaseNodeContainer.get_nodes"></a>

#### get_nodes

```python
def get_nodes(class_node: Class) -> Array[str]
```

x.get_nodes(class_node) -> Array[str]
Return all nodes that are of the ClassNode type.

Args:
    class_node (type(Class)): 

Returns:
    Array[str]: 

    out_nodes (Array[str]):

<a id="unreal.InterchangeBaseNodeContainer.get_node_children_uids"></a>

#### get_node_children_uids

```python
def get_node_children_uids(node_unique_id: str) -> Array[str]
```

x.get_node_children_uids(node_unique_id) -> Array[str]
Get the UIDs of all the node's children.

Args:
    node_unique_id (str): 

Returns:
    Array[str]:

<a id="unreal.InterchangeBaseNodeContainer.get_node_children_count"></a>

#### get_node_children_count

```python
def get_node_children_count(node_unique_id: str) -> int
```

x.get_node_children_count(node_unique_id) -> int32
Get the number of children the node has.

Args:
    node_unique_id (str): 

Returns:
    int32:

<a id="unreal.InterchangeBaseNodeContainer.get_node_children"></a>

#### get_node_children

```python
def get_node_children(node_unique_id: str,
                      child_index: int) -> InterchangeBaseNode
```

x.get_node_children(node_unique_id, child_index) -> InterchangeBaseNode
Get the nth const child of the node

Args:
    node_unique_id (str): 
    child_index (int32): 

Returns:
    InterchangeBaseNode:

<a id="unreal.InterchangeBaseNodeContainer.get_node"></a>

#### get_node

```python
def get_node(node_unique_id: str) -> InterchangeBaseNode
```

x.get_node(node_unique_id) -> InterchangeBaseNode
Get a node pointer. Once added to the container, nodes are considered const.

Args:
    node_unique_id (str): 

Returns:
    InterchangeBaseNode:

<a id="unreal.InterchangeBaseNodeContainer.get_is_ancestor"></a>

#### get_is_ancestor

```python
def get_is_ancestor(node_unique_id: str, ancestor_uid: str) -> bool
```

x.get_is_ancestor(node_unique_id, ancestor_uid) -> bool
Checks if ParentNodeUID is an ancestor.

Args:
    node_unique_id (str): 
    ancestor_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeBaseNodeContainer.get_factory_node"></a>

#### get_factory_node

```python
def get_factory_node(node_unique_id: str) -> InterchangeFactoryBaseNode
```

x.get_factory_node(node_unique_id) -> InterchangeFactoryBaseNode
Get a factory node pointer.

Args:
    node_unique_id (str): 

Returns:
    InterchangeFactoryBaseNode:

<a id="unreal.InterchangeBaseNodeContainer.compute_children_cache"></a>

#### compute_children_cache

```python
def compute_children_cache() -> None
```

x.compute_children_cache() -> None
Fill the cache of children UIDs to optimize the GetNodeChildrenUids call.

<a id="unreal.InterchangeBaseNodeContainer.add_node"></a>

#### add_node

```python
def add_node(node: InterchangeBaseNode) -> str
```

x.add_node(node) -> str
Add a node to the container. The node is added into a TMap.
return:: return the node unique ID of the added item. If the node already exist it will return the existing ID. Return InvalidNodeUid if the node cannot be added.

Args:
    node (InterchangeBaseNode): a pointer on the node you want to add

Returns:
    str:

<a id="unreal.InterchangeFactoryBaseNode"></a>