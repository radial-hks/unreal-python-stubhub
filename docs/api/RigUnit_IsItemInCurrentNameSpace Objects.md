## RigUnit_IsItemInCurrentNameSpace Objects

```python
class RigUnit_IsItemInCurrentNameSpace(RigUnit_RigModulesBase)
```

Returns true if the given item has been created by this module,
which means that the item's namespace is the module namespace.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_RigModules.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``item`` (RigElementKey):  [Read-Write] * The key of the item to return the namespace for
- ``result`` (bool):  [Read-Write] * True if the item is in this namespace / owned by this module.

<a id="unreal.RigUnit_IsItemInCurrentNameSpace.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             result: bool = False) -> None
```

<a id="unreal.RigUnit_IsItemInCurrentNameSpace.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write] * The key of the item to return the namespace for

<a id="unreal.RigUnit_IsItemInCurrentNameSpace.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_IsItemInCurrentNameSpace.result"></a>

#### result

```python
@property
def result() -> bool
```

(bool):  [Read-Only] * True if the item is in this namespace / owned by this module.

<a id="unreal.RigUnit_GetItemsInNameSpace"></a>