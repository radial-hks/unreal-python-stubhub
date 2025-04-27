## RigUnit_CollectionUnion Objects

```python
class RigUnit_CollectionUnion(RigUnit_CollectionBase)
```

Returns the union of two provided collections
(the combination of all items from both A and B).

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (RigElementKeyCollection):  [Read-Write]
- ``allow_duplicates`` (bool):  [Read-Write]
- ``b`` (RigElementKeyCollection):  [Read-Write]
- ``collection`` (RigElementKeyCollection):  [Read-Write]

<a id="unreal.RigUnit_CollectionUnion.__init__"></a>

#### __init__

```python
def __init__(a: RigElementKeyCollection = [[]],
             b: RigElementKeyCollection = [[]],
             allow_duplicates: bool = False,
             collection: RigElementKeyCollection = [[]]) -> None
```

<a id="unreal.RigUnit_CollectionUnion.a"></a>

#### a

```python
@property
def a() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write]

<a id="unreal.RigUnit_CollectionUnion.a"></a>

#### a

```python
@a.setter
def a(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_CollectionUnion.b"></a>

#### b

```python
@property
def b() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write]

<a id="unreal.RigUnit_CollectionUnion.b"></a>

#### b

```python
@b.setter
def b(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_CollectionUnion.allow_duplicates"></a>

#### allow_duplicates

```python
@property
def allow_duplicates() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RigUnit_CollectionUnion.allow_duplicates"></a>

#### allow_duplicates

```python
@allow_duplicates.setter
def allow_duplicates(value: bool) -> None
```

<a id="unreal.RigUnit_CollectionUnion.collection"></a>

#### collection

```python
@property
def collection() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Only]

<a id="unreal.RigUnit_CollectionIntersection"></a>