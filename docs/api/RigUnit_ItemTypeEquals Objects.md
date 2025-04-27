## RigUnit_ItemTypeEquals Objects

```python
class RigUnit_ItemTypeEquals(RigUnit_ItemBase)
```

Returns true if the two items' types are equal

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Item.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (RigElementKey):  [Read-Write]
- ``b`` (RigElementKey):  [Read-Write]
- ``result`` (bool):  [Read-Write]

<a id="unreal.RigUnit_ItemTypeEquals.__init__"></a>

#### __init__

```python
def __init__(a: RigElementKey = [RigElementType.NONE, "None"],
             b: RigElementKey = [RigElementType.NONE, "None"],
             result: bool = False) -> None
```

<a id="unreal.RigUnit_ItemTypeEquals.a"></a>

#### a

```python
@property
def a() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_ItemTypeEquals.a"></a>

#### a

```python
@a.setter
def a(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_ItemTypeEquals.b"></a>

#### b

```python
@property
def b() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_ItemTypeEquals.b"></a>

#### b

```python
@b.setter
def b(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_ItemTypeEquals.result"></a>

#### result

```python
@property
def result() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_ItemTypeNotEquals"></a>