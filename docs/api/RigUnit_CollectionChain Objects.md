## RigUnit_CollectionChain Objects

```python
class RigUnit_CollectionChain(RigUnit_CollectionBase)
```

Creates a collection based on a first and last item within a chain.
Chains can refer to bone chains or chains within a control hierarchy.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collection`` (RigElementKeyCollection):  [Read-Write]
- ``first_item`` (RigElementKey):  [Read-Write]
- ``last_item`` (RigElementKey):  [Read-Write]
- ``reverse`` (bool):  [Read-Write]

<a id="unreal.RigUnit_CollectionChain.__init__"></a>

#### __init__

```python
def __init__(first_item: RigElementKey = [RigElementType.NONE, "None"],
             last_item: RigElementKey = [RigElementType.NONE, "None"],
             reverse: bool = False,
             collection: RigElementKeyCollection = [[]]) -> None
```

<a id="unreal.RigUnit_CollectionChain.first_item"></a>

#### first_item

```python
@property
def first_item() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_CollectionChain.first_item"></a>

#### first_item

```python
@first_item.setter
def first_item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_CollectionChain.last_item"></a>

#### last_item

```python
@property
def last_item() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_CollectionChain.last_item"></a>

#### last_item

```python
@last_item.setter
def last_item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_CollectionChain.reverse"></a>

#### reverse

```python
@property
def reverse() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_CollectionChain.reverse"></a>

#### reverse

```python
@reverse.setter
def reverse(value: bool) -> None
```

<a id="unreal.RigUnit_CollectionChain.collection"></a>

#### collection

```python
@property
def collection() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Only]

<a id="unreal.RigUnit_CollectionChainArray"></a>