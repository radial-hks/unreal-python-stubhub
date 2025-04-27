## BaseComponentReference Objects

```python
class BaseComponentReference(StructBase)
```

Base class for the hard/soft component reference structs

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_property`` (Name):  [Read-Write] Name of component to use. If this is not specified the reference refers to the root component.
- ``path_to_component`` (str):  [Read-Write] Path to the component from its owner actor

<a id="unreal.BaseComponentReference.__init__"></a>

#### __init__

```python
def __init__(component_property: Name = "None") -> None
```

<a id="unreal.BaseComponentReference.component_property"></a>

#### component_property

```python
@property
def component_property() -> Name
```

(Name):  [Read-Write] Name of component to use. If this is not specified the reference refers to the root component.

<a id="unreal.BaseComponentReference.component_property"></a>

#### component_property

```python
@component_property.setter
def component_property(value: Name) -> None
```

<a id="unreal.SoftComponentReference"></a>