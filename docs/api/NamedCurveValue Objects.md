## NamedCurveValue Objects

```python
class NamedCurveValue(StructBase)
```

Name/value pair for retrieving curve values

**C++ Source:**

- **Module**: Engine
- **File**: CurveSourceInterface.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Write] The name of the curve
- ``value`` (float):  [Read-Write] The value of the curve

<a id="unreal.NamedCurveValue.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None", value: float = 0.000000) -> None
```

<a id="unreal.NamedCurveValue.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] The name of the curve

<a id="unreal.NamedCurveValue.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.NamedCurveValue.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Write] The value of the curve

<a id="unreal.NamedCurveValue.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.InputClampConstants"></a>