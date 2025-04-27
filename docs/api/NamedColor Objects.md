## NamedColor Objects

```python
class NamedColor(StructBase)
```

A named color

**C++ Source:**

- **Module**: Engine
- **File**: AnimationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write]
- ``value`` (Color):  [Read-Write]

<a id="unreal.NamedColor.__init__"></a>

#### __init__

```python
def __init__(value: Color = [0, 0, 0, 0], name: Name = "None") -> None
```

<a id="unreal.NamedColor.value"></a>

#### value

```python
@property
def value() -> Color
```

(Color):  [Read-Write]

<a id="unreal.NamedColor.value"></a>

#### value

```python
@value.setter
def value(value: Color) -> None
```

<a id="unreal.NamedColor.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.NamedColor.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.NamedTransform"></a>