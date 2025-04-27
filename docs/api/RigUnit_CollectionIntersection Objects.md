## RigUnit_CollectionIntersection Objects

```python
class RigUnit_CollectionIntersection(RigUnit_CollectionBase)
```

Returns the intersection of two provided collections
(the items present in both A and B).

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Collection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (RigElementKeyCollection):  [Read-Write]
- ``b`` (RigElementKeyCollection):  [Read-Write]
- ``collection`` (RigElementKeyCollection):  [Read-Write]

<a id="unreal.RigUnit_CollectionIntersection.__init__"></a>

#### __init__

```python
def __init__(a: RigElementKeyCollection = [[]],
             b: RigElementKeyCollection = [[]],
             collection: RigElementKeyCollection = [[]]) -> None
```

<a id="unreal.RigUnit_CollectionIntersection.a"></a>

#### a

```python
@property
def a() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write]

<a id="unreal.RigUnit_CollectionIntersection.a"></a>

#### a

```python
@a.setter
def a(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_CollectionIntersection.b"></a>

#### b

```python
@property
def b() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write]

<a id="unreal.RigUnit_CollectionIntersection.b"></a>

#### b

```python
@b.setter
def b(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_CollectionIntersection.collection"></a>

#### collection

```python
@property
def collection() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Only]

<a id="unreal.RigUnit_CollectionDifference"></a>