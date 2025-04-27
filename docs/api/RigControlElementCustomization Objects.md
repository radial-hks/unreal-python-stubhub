## RigControlElementCustomization Objects

```python
class RigControlElementCustomization(StructBase)
```

Rig Control Element Customization

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyElements.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``available_spaces`` (Array[RigElementKey]):  [Read-Write]
- ``removed_spaces`` (Array[RigElementKey]):  [Read-Write]

<a id="unreal.RigControlElementCustomization.__init__"></a>

#### __init__

```python
def __init__(available_spaces: Array[RigElementKey] = [],
             removed_spaces: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigControlElementCustomization.available_spaces"></a>

#### available_spaces

```python
@property
def available_spaces() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only]

<a id="unreal.RigControlElementCustomization.removed_spaces"></a>

#### removed_spaces

```python
@property
def removed_spaces() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only]

<a id="unreal.RigControlValue"></a>