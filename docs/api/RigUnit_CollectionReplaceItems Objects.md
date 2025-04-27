## RigUnit_CollectionReplaceItems Objects

```python
class RigUnit_CollectionReplaceItems(RigUnit_CollectionBase)
```

Replaces all names within the collection

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_duplicates`` (bool):  [Read-Write]
- ``collection`` (RigElementKeyCollection):  [Read-Write]
- ``items`` (RigElementKeyCollection):  [Read-Write]
- ``new`` (Name):  [Read-Write]
- ``old`` (Name):  [Read-Write]
- ``remove_invalid_items`` (bool):  [Read-Write]

<a id="unreal.RigUnit_CollectionReplaceItems.__init__"></a>

#### __init__

```python
def __init__(items: RigElementKeyCollection = [[]],
             old: Name = "None",
             new: Name = "None",
             remove_invalid_items: bool = False,
             allow_duplicates: bool = False,
             collection: RigElementKeyCollection = [[]]) -> None
```

<a id="unreal.RigUnit_CollectionReplaceItems.items"></a>

#### items

```python
@property
def items() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write]

<a id="unreal.RigUnit_CollectionReplaceItems.items"></a>

#### items

```python
@items.setter
def items(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_CollectionReplaceItems.old"></a>

#### old

```python
@property
def old() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_CollectionReplaceItems.old"></a>

#### old

```python
@old.setter
def old(value: Name) -> None
```

<a id="unreal.RigUnit_CollectionReplaceItems.new"></a>

#### new

```python
@property
def new() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_CollectionReplaceItems.new"></a>

#### new

```python
@new.setter
def new(value: Name) -> None
```

<a id="unreal.RigUnit_CollectionReplaceItems.remove_invalid_items"></a>

#### remove_invalid_items

```python
@property
def remove_invalid_items() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_CollectionReplaceItems.remove_invalid_items"></a>

#### remove_invalid_items

```python
@remove_invalid_items.setter
def remove_invalid_items(value: bool) -> None
```

<a id="unreal.RigUnit_CollectionReplaceItems.allow_duplicates"></a>

#### allow_duplicates

```python
@property
def allow_duplicates() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_CollectionReplaceItems.allow_duplicates"></a>

#### allow_duplicates

```python
@allow_duplicates.setter
def allow_duplicates(value: bool) -> None
```

<a id="unreal.RigUnit_CollectionReplaceItems.collection"></a>

#### collection

```python
@property
def collection() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Only]

<a id="unreal.RigUnit_CollectionReplaceItemsArray"></a>