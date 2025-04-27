## RigUnit_CollectionLoop Objects

```python
class RigUnit_CollectionLoop(RigUnit_CollectionBaseMutable)
```

Given a collection of items, execute iteratively across all items in a given collection

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``collection`` (RigElementKeyCollection):  [Read-Write]
- ``completed`` (ControlRigExecuteContext):  [Read-Write]
- ``count`` (int32):  [Read-Write]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``index`` (int32):  [Read-Write]
- ``item`` (RigElementKey):  [Read-Write]
- ``ratio`` (float):  [Read-Write] Ranging from 0.0 (first item) and 1.0 (last item)
  This is useful to drive a consecutive node with a
  curve or an ease to distribute a value.

<a id="unreal.RigUnit_CollectionLoop.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             collection: RigElementKeyCollection = [[]],
             item: RigElementKey = [RigElementType.NONE, "None"],
             index: int = 0,
             count: int = 0,
             ratio: float = 0.000000,
             completed: ControlRigExecuteContext = []) -> None
```

<a id="unreal.RigUnit_CollectionLoop.collection"></a>

#### collection

```python
@property
def collection() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write]

<a id="unreal.RigUnit_CollectionLoop.collection"></a>

#### collection

```python
@collection.setter
def collection(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_CollectionLoop.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Only]

<a id="unreal.RigUnit_CollectionLoop.index"></a>

#### index

```python
@property
def index() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigUnit_CollectionLoop.count"></a>

#### count

```python
@property
def count() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigUnit_CollectionLoop.ratio"></a>

#### ratio

```python
@property
def ratio() -> float
```

(float):  [Read-Only] Ranging from 0.0 (first item) and 1.0 (last item)
This is useful to drive a consecutive node with a
curve or an ease to distribute a value.

<a id="unreal.RigUnit_CollectionLoop.completed"></a>

#### completed

```python
@property
def completed() -> ControlRigExecuteContext
```

(ControlRigExecuteContext):  [Read-Only]

<a id="unreal.RigUnit_CollectionAddItem"></a>