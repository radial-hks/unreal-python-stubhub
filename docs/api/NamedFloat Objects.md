## NamedFloat Objects

```python
class NamedFloat(StructBase)
```

A named float

**C++ Source:**

- **Module**: Engine
- **File**: AnimationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write]
- ``value`` (float):  [Read-Write]

<a id="unreal.NamedFloat.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000, name: Name = "None") -> None
```

<a id="unreal.NamedFloat.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write]

<a id="unreal.NamedFloat.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.NamedFloat.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.NamedFloat.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.NamedVector"></a>