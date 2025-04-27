## Variant Objects

```python
class Variant(Object)
```

Variant

**C++ Source:**

- **Plugin**: VariantManagerContent
- **Module**: VariantManagerContent
- **File**: Variant.h

<a id="unreal.Variant.switch_on"></a>

#### switch_on

```python
def switch_on() -> None
```

x.switch_on() -> None
Switch On

<a id="unreal.Variant.set_thumbnail_from_texture"></a>

#### set_thumbnail_from_texture

```python
def set_thumbnail_from_texture(new_thumbnail: Texture2D) -> None
```

x.set_thumbnail_from_texture(new_thumbnail) -> None
Sets the thumbnail to use for this variant. Can receive nullptr to clear it

Args:
    new_thumbnail (Texture2D):

<a id="unreal.Variant.set_thumbnail_from_file"></a>

#### set_thumbnail_from_file

```python
def set_thumbnail_from_file(file_path: str) -> None
```

x.set_thumbnail_from_file(file_path) -> None
Set Thumbnail from File

Args:
    file_path (str):

<a id="unreal.Variant.set_thumbnail_from_editor_viewport"></a>

#### set_thumbnail_from_editor_viewport

```python
def set_thumbnail_from_editor_viewport() -> None
```

x.set_thumbnail_from_editor_viewport() -> None
Sets the thumbnail from the active editor viewport. Doesn't do anything if the Editor is not available

<a id="unreal.Variant.set_thumbnail_from_camera"></a>

#### set_thumbnail_from_camera

```python
def set_thumbnail_from_camera(world_context_object: Object,
                              camera_transform: Transform,
                              fov_degrees: float = 50.000000,
                              min_z: float = 50.000000,
                              gamma: float = 2.200000) -> None
```

x.set_thumbnail_from_camera(world_context_object, camera_transform, fov_degrees=50.000000, min_z=50.000000, gamma=2.200000) -> None
Set Thumbnail from Camera

Args:
    world_context_object (Object): 
    camera_transform (Transform): 
    fov_degrees (float): 
    min_z (float): 
    gamma (float):

<a id="unreal.Variant.set_display_text"></a>

#### set_display_text

```python
def set_display_text(new_display_text: Text) -> None
```

x.set_display_text(new_display_text) -> None
Set Display Text

Args:
    new_display_text (Text):

<a id="unreal.Variant.is_active"></a>

#### is_active

```python
def is_active() -> bool
```

x.is_active() -> bool
Returns true if none of our properties are dirty

Returns:
    bool:

<a id="unreal.Variant.get_thumbnail"></a>

#### get_thumbnail

```python
def get_thumbnail() -> Texture2D
```

x.get_thumbnail() -> Texture2D
Gets the thumbnail currently used for this variant

Returns:
    Texture2D:

<a id="unreal.Variant.get_parent"></a>

#### get_parent

```python
def get_parent() -> VariantSet
```

x.get_parent() -> VariantSet
Get Parent

Returns:
    VariantSet:

<a id="unreal.Variant.get_num_dependencies"></a>

#### get_num_dependencies

```python
def get_num_dependencies() -> int
```

x.get_num_dependencies() -> int32
Get Num Dependencies

Returns:
    int32:

<a id="unreal.Variant.get_num_actors"></a>

#### get_num_actors

```python
def get_num_actors() -> int
```

x.get_num_actors() -> int32
Get Num Actors

Returns:
    int32:

<a id="unreal.Variant.get_display_text"></a>

#### get_display_text

```python
def get_display_text() -> Text
```

x.get_display_text() -> Text
Get Display Text

Returns:
    Text:

<a id="unreal.Variant.get_dependents"></a>

#### get_dependents

```python
def get_dependents(level_variant_sets: LevelVariantSets,
                   only_enabled_dependencies: bool) -> Array[Variant]
```

x.get_dependents(level_variant_sets, only_enabled_dependencies) -> Array[Variant]
Returns all the variants that have this variant as a dependency

Args:
    level_variant_sets (LevelVariantSets): 
    only_enabled_dependencies (bool): 

Returns:
    Array[Variant]:

<a id="unreal.Variant.get_dependency"></a>

#### get_dependency

```python
def get_dependency(index: int) -> VariantDependency
```

x.get_dependency(index) -> VariantDependency
Get the dependency at index 'Index' by value. Will crash if index is invalid

Args:
    index (int32): 

Returns:
    VariantDependency:

<a id="unreal.Variant.get_actor"></a>

#### get_actor

```python
def get_actor(actor_index: int) -> Actor
```

x.get_actor(actor_index) -> Actor
Get Actor

Args:
    actor_index (int32): 

Returns:
    Actor:

<a id="unreal.Variant.set_dependency"></a>

#### set_dependency

```python
def set_dependency(index: int,
                   dependency: VariantDependency) -> VariantDependency
```

x.set_dependency(index, dependency) -> VariantDependency
Set Dependency

Args:
    index (int32): 
    dependency (VariantDependency): 

Returns:
    VariantDependency: 

    dependency (VariantDependency):

<a id="unreal.Variant.remove_captured_property_by_name"></a>

#### remove_captured_property_by_name

```python
def remove_captured_property_by_name(actor: Actor, property_path: str) -> None
```

x.remove_captured_property_by_name(actor, property_path) -> None
Removes property capture with PropertyPath from Actor's binding within Variant, if it exists

Args:
    actor (Actor): 
    property_path (str):

<a id="unreal.Variant.remove_captured_property"></a>

#### remove_captured_property

```python
def remove_captured_property(actor: Actor, property_: PropertyValue) -> None
```

x.remove_captured_property(actor, property_) -> None
Removes a property capture from an actor binding within Variant, if it exists

Args:
    actor (Actor): 
    property_ (PropertyValue):

<a id="unreal.Variant.remove_actor_binding_by_name"></a>

#### remove_actor_binding_by_name

```python
def remove_actor_binding_by_name(actor_name: str) -> None
```

x.remove_actor_binding_by_name(actor_name) -> None
Looks for an actor binding to an actor with ActorLabel within Variant and removes it, if it exists

Args:
    actor_name (str):

<a id="unreal.Variant.remove_actor_binding"></a>

#### remove_actor_binding

```python
def remove_actor_binding(actor: Actor) -> None
```

x.remove_actor_binding(actor) -> None
Removes an actor binding to Actor from Variant, if it exists

Args:
    actor (Actor):

<a id="unreal.Variant.get_captured_properties"></a>

#### get_captured_properties

```python
def get_captured_properties(actor: Actor) -> Array[PropertyValue]
```

x.get_captured_properties(actor) -> Array[PropertyValue]
Returns which properties have been captured for this actor in Variant

Args:
    actor (Actor): 

Returns:
    Array[PropertyValue]:

<a id="unreal.Variant.delete_dependency"></a>

#### delete_dependency

```python
def delete_dependency(index: int) -> None
```

x.delete_dependency(index) -> None
Delete Dependency

Args:
    index (int32):

<a id="unreal.Variant.capture_property"></a>

#### capture_property

```python
def capture_property(actor: Actor, property_path: str) -> PropertyValue
```

x.capture_property(actor, property_path) -> PropertyValue
Finds the actor binding to Actor within Variant and tries capturing a property with PropertyPath
Returns the captured UPropertyValue if succeeded or nullptr if it failed.

Args:
    actor (Actor): 
    property_path (str): 

Returns:
    PropertyValue:

<a id="unreal.Variant.add_dependency"></a>

#### add_dependency

```python
def add_dependency(
        dependency: VariantDependency) -> Tuple[int, VariantDependency]
```

x.add_dependency(dependency) -> (int32, dependency=VariantDependency)
Add Dependency

Args:
    dependency (VariantDependency): 

Returns:
    VariantDependency: 

    dependency (VariantDependency):

<a id="unreal.Variant.add_actor_binding"></a>

#### add_actor_binding

```python
def add_actor_binding(actor: Actor) -> None
```

x.add_actor_binding(actor) -> None
Binds the Actor to the Variant, internally creating a VariantObjectBinding

Args:
    actor (Actor):

<a id="unreal.VariantSet"></a>