## RigUnit_CollectionChainArray Objects

```python
class RigUnit_CollectionChainArray(RigUnit_CollectionBase)
```

Creates an item array based on a first and last item within a chain.
Chains can refer to bone chains or chains within a control hierarchy.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``first_item`` (RigElementKey):  [Read-Write]
- ``items`` (Array[RigElementKey]):  [Read-Write]
- ``last_item`` (RigElementKey):  [Read-Write]
- ``reverse`` (bool):  [Read-Write]

<a id="unreal.RigUnit_CollectionChainArray.__init__"></a>

#### __init__

```python
def __init__(first_item: RigElementKey = [RigElementType.NONE, "None"],
             last_item: RigElementKey = [RigElementType.NONE, "None"],
             reverse: bool = False,
             items: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_CollectionChainArray.first_item"></a>

#### first_item

```python
@property
def first_item() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_CollectionChainArray.first_item"></a>

#### first_item

```python
@first_item.setter
def first_item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_CollectionChainArray.last_item"></a>

#### last_item

```python
@property
def last_item() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_CollectionChainArray.last_item"></a>

#### last_item

```python
@last_item.setter
def last_item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_CollectionChainArray.reverse"></a>

#### reverse

```python
@property
def reverse() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_CollectionChainArray.reverse"></a>

#### reverse

```python
@reverse.setter
def reverse(value: bool) -> None
```

<a id="unreal.RigUnit_CollectionChainArray.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only]

<a id="unreal.RigUnit_CollectionNameSearch"></a>