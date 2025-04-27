## RigUnit_CollectionReplaceItemsArray Objects

```python
class RigUnit_CollectionReplaceItemsArray(RigUnit_CollectionBase)
```

Replaces all names within the item array

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_duplicates`` (bool):  [Read-Write]
- ``items`` (Array[RigElementKey]):  [Read-Write]
- ``new`` (Name):  [Read-Write]
- ``old`` (Name):  [Read-Write]
- ``remove_invalid_items`` (bool):  [Read-Write]
- ``result`` (Array[RigElementKey]):  [Read-Write]

<a id="unreal.RigUnit_CollectionReplaceItemsArray.__init__"></a>

#### __init__

```python
def __init__(items: Array[RigElementKey] = [],
             old: Name = "None",
             new: Name = "None",
             remove_invalid_items: bool = False,
             allow_duplicates: bool = False,
             result: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_CollectionReplaceItemsArray.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Write]

<a id="unreal.RigUnit_CollectionReplaceItemsArray.items"></a>

#### items

```python
@items.setter
def items(value: Array[RigElementKey]) -> None
```

<a id="unreal.RigUnit_CollectionReplaceItemsArray.old"></a>

#### old

```python
@property
def old() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_CollectionReplaceItemsArray.old"></a>

#### old

```python
@old.setter
def old(value: Name) -> None
```

<a id="unreal.RigUnit_CollectionReplaceItemsArray.new"></a>

#### new

```python
@property
def new() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_CollectionReplaceItemsArray.new"></a>

#### new

```python
@new.setter
def new(value: Name) -> None
```

<a id="unreal.RigUnit_CollectionReplaceItemsArray.remove_invalid_items"></a>

#### remove_invalid_items

```python
@property
def remove_invalid_items() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_CollectionReplaceItemsArray.remove_invalid_items"></a>

#### remove_invalid_items

```python
@remove_invalid_items.setter
def remove_invalid_items(value: bool) -> None
```

<a id="unreal.RigUnit_CollectionReplaceItemsArray.allow_duplicates"></a>

#### allow_duplicates

```python
@property
def allow_duplicates() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_CollectionReplaceItemsArray.allow_duplicates"></a>

#### allow_duplicates

```python
@allow_duplicates.setter
def allow_duplicates(value: bool) -> None
```

<a id="unreal.RigUnit_CollectionReplaceItemsArray.result"></a>

#### result

```python
@property
def result() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only]

<a id="unreal.RigUnit_CollectionItems"></a>