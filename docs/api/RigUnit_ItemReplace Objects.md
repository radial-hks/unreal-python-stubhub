## RigUnit_ItemReplace Objects

```python
class RigUnit_ItemReplace(RigUnit_ItemBase)
```

Replaces the text within the name of the item

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Item.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``item`` (RigElementKey):  [Read-Write]
- ``new`` (Name):  [Read-Write]
- ``old`` (Name):  [Read-Write]
- ``result`` (RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_ItemReplace.__init__"></a>

#### __init__

```python
def __init__(item: RigElementKey = [RigElementType.NONE, "None"],
             old: Name = "None",
             new: Name = "None",
             result: RigElementKey = [RigElementType.NONE, "None"]) -> None
```

<a id="unreal.RigUnit_ItemReplace.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_ItemReplace.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_ItemReplace.old"></a>

#### old

```python
@property
def old() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_ItemReplace.old"></a>

#### old

```python
@old.setter
def old(value: Name) -> None
```

<a id="unreal.RigUnit_ItemReplace.new"></a>

#### new

```python
@property
def new() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_ItemReplace.new"></a>

#### new

```python
@new.setter
def new(value: Name) -> None
```

<a id="unreal.RigUnit_ItemReplace.result"></a>

#### result

```python
@property
def result() -> RigElementKey
```

(RigElementKey):  [Read-Only]

<a id="unreal.RigUnit_ItemEquals"></a>