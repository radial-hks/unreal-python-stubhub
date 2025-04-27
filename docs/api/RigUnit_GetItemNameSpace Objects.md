## RigUnit_GetItemNameSpace Objects

```python
class RigUnit_GetItemNameSpace(RigUnit_RigModulesBase)
```

Returns the namespace of a given item. This may be an empty string if the item doesn't have a namespace.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_RigModules.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``has_name_space`` (bool):  [Read-Write] * True if the item has a valid namespace
- ``item`` (RigElementKey):  [Read-Write] * The key of the item to return the namespace for
- ``name_space`` (str):  [Read-Write] * The namespace of the item

<a id="unreal.RigUnit_GetItemNameSpace.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             has_name_space: bool = False,
             name_space: str = "") -> None
```

<a id="unreal.RigUnit_GetItemNameSpace.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] * The key of the item to return the namespace for

<a id="unreal.RigUnit_GetItemNameSpace.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_GetItemNameSpace.has_name_space"></a>

#### has_name_space

```python
@property
def has_name_space() -> bool
```

(bool):  [Read-Only] * True if the item has a valid namespace

<a id="unreal.RigUnit_GetItemNameSpace.name_space"></a>

#### name_space

```python
@property
def name_space() -> str
```

(str):  [Read-Only] * The namespace of the item

<a id="unreal.RigUnit_IsItemInCurrentNameSpace"></a>