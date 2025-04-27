## NamedVector Objects

```python
class NamedVector(StructBase)
```

A named float

**C++ Source:**

- **Module**: Engine
- **File**: AnimationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write]
- ``value`` (Vector):  [Read-Write]

<a id="unreal.NamedVector.__init__"></a>

#### __init__

```python
def __init__(value: Vector = [0.000000, 0.000000, 0.000000],
             name: Name = "None") -> None
```

<a id="unreal.NamedVector.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.NamedVector.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.NamedVector.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.NamedVector.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.NamedColor"></a>