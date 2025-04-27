## MovieGraphModifierNode Objects

```python
class MovieGraphModifierNode(MovieGraphSettingNode)
```

A collection node specifies an interface for doing dynamic scene queries for actors in the world. Collections work in tandem with
UMovieGraphModifiers to select which actors the modifiers should be run on.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphModifierNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``modifier_name`` (str):  [Read-Write] The name of this modifier.
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.

<a id="unreal.MovieGraphModifierNode.modifier_name"></a>

#### modifier_name

```python
@property
def modifier_name() -> str
```

(str):  [Read-Write] The name of this modifier.

<a id="unreal.MovieGraphModifierNode.modifier_name"></a>

#### modifier_name

```python
@modifier_name.setter
def modifier_name(value: str) -> None
```

<a id="unreal.MovieGraphModifierNode.set_collection_enabled"></a>

#### set_collection_enabled

```python
def set_collection_enabled(collection_name: Name,
                           is_collection_enabled: bool) -> None
```

x.set_collection_enabled(collection_name, is_collection_enabled) -> None
Sets the enable state (within this modifier) of the collection with the given name. Disabled collections will not be modified by this modifier
node. Collections that are added to the modifier are enabled by default.

Args:
    collection_name (Name): 
    is_collection_enabled (bool):

<a id="unreal.MovieGraphModifierNode.remove_modifier"></a>

#### remove_modifier

```python
def remove_modifier(modifier_type: Class) -> bool
```

x.remove_modifier(modifier_type) -> bool
Removes the modifier of the specified type. Returns true on success, or false if a modifier of the specified type does not exist on the node.

Args:
    modifier_type (type(Class)): 

Returns:
    bool:

<a id="unreal.MovieGraphModifierNode.remove_collection"></a>

#### remove_collection

```python
def remove_collection(collection_name: Name) -> bool
```

x.remove_collection(collection_name) -> bool
Remove a collection identified by the given name. Returns true if the collection was found and removed successfully, else false.

Args:
    collection_name (Name): 

Returns:
    bool:

<a id="unreal.MovieGraphModifierNode.is_collection_enabled"></a>

#### is_collection_enabled

```python
def is_collection_enabled(collection_name: Name) -> bool
```

x.is_collection_enabled(collection_name) -> bool
Gets the enable state (within this modifier) of the collection with the given name.

Args:
    collection_name (Name): 

Returns:
    bool:

<a id="unreal.MovieGraphModifierNode.get_modifiers"></a>

#### get_modifiers

```python
def get_modifiers() -> Array[MovieGraphCollectionModifier]
```

x.get_modifiers() -> Array[MovieGraphCollectionModifier]
Gets all modifiers currently added to the node.

Returns:
    Array[MovieGraphCollectionModifier]:

<a id="unreal.MovieGraphModifierNode.get_modifier"></a>

#### get_modifier

```python
def get_modifier(modifier_type: Class) -> MovieGraphCollectionModifier
```

x.get_modifier(modifier_type) -> MovieGraphCollectionModifier
Gets the modifier of the specified type, or nullptr if one does not exist on this node.

Args:
    modifier_type (type(Class)): 

Returns:
    MovieGraphCollectionModifier:

<a id="unreal.MovieGraphModifierNode.get_collections"></a>

#### get_collections

```python
def get_collections() -> Array[Name]
```

x.get_collections() -> Array[Name]
Gets all collections that will be affected by the modifiers on this node.

Returns:
    Array[Name]:

<a id="unreal.MovieGraphModifierNode.add_modifier"></a>

#### add_modifier

```python
def add_modifier(modifier_type: Class) -> MovieGraphCollectionModifier
```

x.add_modifier(modifier_type) -> MovieGraphCollectionModifier
Adds a new modifier of the specified type. Returns a pointer to the new modifier, or nullptr if a modifier of the specified type already
exists on this node (only one modifier of each type can be added to the node).

Args:
    modifier_type (type(Class)): 

Returns:
    MovieGraphCollectionModifier:

<a id="unreal.MovieGraphModifierNode.add_collection"></a>

#### add_collection

```python
def add_collection(collection_name: Name) -> None
```

x.add_collection(collection_name) -> None
Add a collection identified by the given name which will be affected by the modifiers on this node.

Args:
    collection_name (Name):

<a id="unreal.MovieGraphOutputNode"></a>