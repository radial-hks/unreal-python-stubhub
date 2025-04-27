## RigUnit_ItemExists Objects

```python
class RigUnit_ItemExists(RigUnit_ItemBase)
```

Returns true or false if a given item exists

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Item.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``exists`` (bool):  [Read-Write]
- ``item`` (RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_ItemExists.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             exists: bool = False) -> None
```

<a id="unreal.RigUnit_ItemExists.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_ItemExists.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_ItemExists.exists"></a>

#### exists

```python
@property
def exists() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_ItemReplace"></a>