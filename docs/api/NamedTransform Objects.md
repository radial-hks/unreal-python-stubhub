## NamedTransform Objects

```python
class NamedTransform(StructBase)
```

A named transform

**C++ Source:**

- **Module**: Engine
- **File**: AnimationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write]
- ``value`` (Transform):  [Read-Write]

<a id="unreal.NamedTransform.__init__"></a>

#### __init__

```python
def __init__(value: Transform = [[0.000000, 0.000000, 0.000000],
                                 [-0.000000, 0.000000, 0.000000],
                                 [1.000000, 1.000000, 1.000000]],
             name: Name = "None") -> None
```

<a id="unreal.NamedTransform.value"></a>

#### value

```python
@property
def value() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.NamedTransform.value"></a>

#### value

```python
@value.setter
def value(value: Transform) -> None
```

<a id="unreal.NamedTransform.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.NamedTransform.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.LocalSpacePose"></a>