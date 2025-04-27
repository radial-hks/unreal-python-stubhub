## DMMaterialComponent Objects

```python
class DMMaterialComponent(Object)
```

The base class for all material components. Has a few useful things.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]

<a id="unreal.DMMaterialComponent.component_state"></a>

#### component_state

```python
@property
def component_state() -> DMComponentLifetimeState
```

(DMComponentLifetimeState):  [Read-Only]

<a id="unreal.DMMaterialComponent.component_dirty"></a>

#### component_dirty

```python
@property
def component_dirty() -> bool
```

(bool):  [Read-Only]

<a id="unreal.DMMaterialComponent.editable_properties"></a>

#### editable_properties

```python
@property
def editable_properties() -> Array[Name]
```

(Array[Name]):  [Read-Only]

<a id="unreal.DMMaterialComponent.update"></a>

#### update

```python
def update(source: DMMaterialComponent, update_type: DMUpdateType) -> None
```

x.update(source, update_type) -> None
Event that is triggered when this component, or a sub-component, changes to trigger other updates in the model.

Args:
    source (DMMaterialComponent): 
    update_type (DMUpdateType):

<a id="unreal.DMMaterialComponent.set_component_state"></a>

#### set_component_state

```python
def set_component_state(new_state: DMComponentLifetimeState) -> None
```

x.set_component_state(new_state) -> None
Changes the component state to a new one. Should not be used to set it back to Created.

Args:
    new_state (DMComponentLifetimeState):

<a id="unreal.DMMaterialComponent.is_property_visible"></a>

#### is_property_visible

```python
def is_property_visible(property_: Name) -> bool
```

x.is_property_visible(property_) -> bool
Returns true the given UPROPERTY name is editable.

Args:
    property_ (Name): 

Returns:
    bool:

<a id="unreal.DMMaterialComponent.is_component_valid"></a>

#### is_component_valid

```python
def is_component_valid() -> bool
```

x.is_component_valid() -> bool
Checks object flags and IsValid()

Returns:
    bool:

<a id="unreal.DMMaterialComponent.is_component_removed"></a>

#### is_component_removed

```python
def is_component_removed() -> bool
```

x.is_component_removed() -> bool
Returns true if this component is in the Removed state.

Returns:
    bool:

<a id="unreal.DMMaterialComponent.is_component_created"></a>

#### is_component_created

```python
def is_component_created() -> bool
```

x.is_component_created() -> bool
Returns true if this component is in the original "Created" state and has not been moved onto Added or Removed.

Returns:
    bool:

<a id="unreal.DMMaterialComponent.is_component_added"></a>

#### is_component_added

```python
def is_component_added() -> bool
```

x.is_component_added() -> bool
Returns true if this component is in the Added state.

Returns:
    bool:

<a id="unreal.DMMaterialComponent.has_component_been_removed"></a>

#### has_component_been_removed

```python
def has_component_been_removed() -> bool
```

x.has_component_been_removed() -> bool
Returns true if this component is in the Removed or greater state.

Returns:
    bool:

<a id="unreal.DMMaterialComponent.has_component_been_created"></a>

#### has_component_been_created

```python
def has_component_been_created() -> bool
```

x.has_component_been_created() -> bool
This is a kind of "useless" check, a component has _always_ been created. It's here for completeness.

Returns:
    bool:

<a id="unreal.DMMaterialComponent.has_component_been_added"></a>

#### has_component_been_added

```python
def has_component_been_added() -> bool
```

x.has_component_been_added() -> bool
Returns true if this component is in the Added or greater state.

Returns:
    bool:

<a id="unreal.DMMaterialComponent.get_typed_parent"></a>

#### get_typed_parent

```python
def get_typed_parent(parent_class: Class,
                     allow_subclasses: bool) -> DMMaterialComponent
```

x.get_typed_parent(parent_class, allow_subclasses) -> DMMaterialComponent
Returns the first in the model hierarchy above this component of the given type.

Args:
    parent_class (type(Class)): 
    allow_subclasses (bool): 

Returns:
    DMMaterialComponent:

<a id="unreal.DMMaterialComponent.get_parent_component"></a>

#### get_parent_component

```python
def get_parent_component() -> DMMaterialComponent
```

x.get_parent_component() -> DMMaterialComponent
Returns the component that owns this component in the model hierarchy.

Returns:
    DMMaterialComponent:

<a id="unreal.DMMaterialComponent.get_outer_safe"></a>

#### get_outer_safe

```python
def get_outer_safe() -> Object
```

x.get_outer_safe() -> Object
Does some checks to see whether the out is safe to retrieve and retrieves it.

Returns:
    Object:

<a id="unreal.DMMaterialComponent.get_editable_properties"></a>

#### get_editable_properties

```python
def get_editable_properties() -> Array[Name]
```

x.get_editable_properties() -> Array[Name]
Returns a list of FNames for this component representing editable UPROPERTYs.

Returns:
    Array[Name]:

<a id="unreal.DMMaterialComponent.get_component_state"></a>

#### get_component_state

```python
def get_component_state() -> DMComponentLifetimeState
```

x.get_component_state() -> DMComponentLifetimeState
Get Component State

Returns:
    DMComponentLifetimeState:

<a id="unreal.DMMaterialComponent.get_component_path"></a>

#### get_component_path

```python
def get_component_path() -> str
```

x.get_component_path() -> str
Returns the complete path from the model to this component.

Returns:
    str:

<a id="unreal.DMMaterialComponent.get_component_description"></a>

#### get_component_description

```python
def get_component_description() -> Text
```

x.get_component_description() -> Text
Returns a description of this class/object.

Returns:
    Text:

<a id="unreal.DMMaterialComponent.get_component_by_path"></a>

#### get_component_by_path

```python
def get_component_by_path(path: str) -> DMMaterialComponent
```

x.get_component_by_path(path) -> DMMaterialComponent
Searches the component for a specific component based on a path.

Args:
    path (str): 

Returns:
    DMMaterialComponent:

<a id="unreal.DMMaterialLinkedComponent"></a>