## AvaDynamicMeshConverterModifier Objects

```python
class AvaDynamicMeshConverterModifier(AvaGeometryBaseModifier)
```

Ava Dynamic Mesh Converter Modifier

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaDynamicMeshConverterModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_type`` (int32):  [Read-Write] Which components should we take into account for the conversion
- ``filter_actor_classes`` (Set[type(Class)]):  [Read-Write] Actor class to use as filter when gathering actors to convert
- ``filter_actor_mode`` (AvaDynamicMeshConverterModifierFilter):  [Read-Write] Actor filter mode : none, include or exclude specific actor class
- ``hide_converted_mesh`` (bool):  [Read-Write] Change visibility of source mesh once they are converted to dynamic mesh, by default will convert itself so hide converted mesh is true
- ``include_attached_actors`` (bool):  [Read-Write] Checks and convert all attached actors below this actor
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``source_actor_weak`` (Actor):  [Read-Write] What actor should we copy from, by default is self
- ``transform_update_interval`` (float):  [Read-Write] Update interval to compare if a transform has changed in converted components, when value <= 0 then skipped

<a id="unreal.AvaDynamicMeshConverterModifier.set_source_actor"></a>

#### set_source_actor

```python
def set_source_actor(actor: Actor) -> None
```

x.set_source_actor(actor) -> None
Set Source Actor

Args:
    actor (Actor):

<a id="unreal.AvaDynamicMeshConverterModifier.set_include_attached_actors"></a>

#### set_include_attached_actors

```python
def set_include_attached_actors(include: bool) -> None
```

x.set_include_attached_actors(include) -> None
Set Include Attached Actors

Args:
    include (bool):

<a id="unreal.AvaDynamicMeshConverterModifier.set_hide_converted_mesh"></a>

#### set_hide_converted_mesh

```python
def set_hide_converted_mesh(hide: bool) -> None
```

x.set_hide_converted_mesh(hide) -> None
Set Hide Converted Mesh

Args:
    hide (bool):

<a id="unreal.AvaDynamicMeshConverterModifier.set_filter_actor_mode"></a>

#### set_filter_actor_mode

```python
def set_filter_actor_mode(
        filter: AvaDynamicMeshConverterModifierFilter) -> None
```

x.set_filter_actor_mode(filter) -> None
Set Filter Actor Mode

Args:
    filter (AvaDynamicMeshConverterModifierFilter):

<a id="unreal.AvaDynamicMeshConverterModifier.set_filter_actor_classes"></a>

#### set_filter_actor_classes

```python
def set_filter_actor_classes(classes: Set[Class]) -> None
```

x.set_filter_actor_classes(classes) -> None
Set Filter Actor Classes

Args:
    classes (Set[type(Class)]):

<a id="unreal.AvaDynamicMeshConverterModifier.set_component_types"></a>

#### set_component_types

```python
def set_component_types(
        types: Set[AvaDynamicMeshConverterModifierType]) -> None
```

x.set_component_types(types) -> None
Set Component Types

Args:
    types (Set[AvaDynamicMeshConverterModifierType]):

<a id="unreal.AvaDynamicMeshConverterModifier.get_source_actor"></a>

#### get_source_actor

```python
def get_source_actor() -> Actor
```

x.get_source_actor() -> Actor
Get Source Actor

Returns:
    Actor:

<a id="unreal.AvaDynamicMeshConverterModifier.get_include_attached_actors"></a>

#### get_include_attached_actors

```python
def get_include_attached_actors() -> bool
```

x.get_include_attached_actors() -> bool
Get Include Attached Actors

Returns:
    bool:

<a id="unreal.AvaDynamicMeshConverterModifier.get_hide_converted_mesh"></a>

#### get_hide_converted_mesh

```python
def get_hide_converted_mesh() -> bool
```

x.get_hide_converted_mesh() -> bool
Get Hide Converted Mesh

Returns:
    bool:

<a id="unreal.AvaDynamicMeshConverterModifier.get_filter_actor_mode"></a>

#### get_filter_actor_mode

```python
def get_filter_actor_mode() -> AvaDynamicMeshConverterModifierFilter
```

x.get_filter_actor_mode() -> AvaDynamicMeshConverterModifierFilter
Get Filter Actor Mode

Returns:
    AvaDynamicMeshConverterModifierFilter:

<a id="unreal.AvaDynamicMeshConverterModifier.get_filter_actor_classes"></a>

#### get_filter_actor_classes

```python
def get_filter_actor_classes() -> Set[Class]
```

x.get_filter_actor_classes() -> Set[type(Class)]
Get Filter Actor Classes

Returns:
    Set[type(Class)]:

<a id="unreal.AvaDynamicMeshConverterModifier.get_component_types"></a>

#### get_component_types

```python
def get_component_types() -> Set[AvaDynamicMeshConverterModifierType]
```

x.get_component_types() -> Set[AvaDynamicMeshConverterModifierType]
Get Component Types

Returns:
    Set[AvaDynamicMeshConverterModifierType]:

<a id="unreal.AvaExtrudeModifier"></a>