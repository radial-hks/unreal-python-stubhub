## RigUnit_GetItemShortName Objects

```python
class RigUnit_GetItemShortName(RigUnit_RigModulesBase)
```

Returns the short name of the given item (without the namespace)

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_RigModules.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``item`` (RigElementKey):  [Read-Write] * The key of the item to return the short name for
- ``short_name`` (Name):  [Read-Write] * The short name of the item (without the namespace)

<a id="unreal.RigUnit_GetItemShortName.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             short_name: Name = "None") -> None
```

<a id="unreal.RigUnit_GetItemShortName.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] * The key of the item to return the short name for

<a id="unreal.RigUnit_GetItemShortName.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_GetItemShortName.short_name"></a>

#### short_name

```python
@property
def short_name() -> Name
```

(Name):  [Read-Only] * The short name of the item (without the namespace)

<a id="unreal.RigUnit_GetItemNameSpace"></a>