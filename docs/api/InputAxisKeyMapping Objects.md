## InputAxisKeyMapping Objects

```python
class InputAxisKeyMapping(StructBase)
```

Defines a mapping between an axis and key
see: https://docs.unrealengine.com/latest/INT/Gameplay/Input/index.html

**C++ Source:**

- **Module**: Engine
- **File**: PlayerInput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``axis_name`` (Name):  [Read-Write] Friendly name of axis, e.g "MoveForward"
- ``key`` (Key):  [Read-Write] Key to bind it to.
- ``scale`` (float):  [Read-Write] Multiplier to use for the mapping when accumulating the axis value

<a id="unreal.InputAxisKeyMapping.__init__"></a>

#### __init__

```python
def __init__(axis_name: Name = "None",
             scale: float = 0.000000,
             key: Key = []) -> None
```

<a id="unreal.InputAxisKeyMapping.axis_name"></a>

#### axis_name

```python
@property
def axis_name() -> Name
```

(Name):  [Read-Write] Friendly name of axis, e.g "MoveForward"

<a id="unreal.InputAxisKeyMapping.axis_name"></a>

#### axis_name

```python
@axis_name.setter
def axis_name(value: Name) -> None
```

<a id="unreal.InputAxisKeyMapping.scale"></a>

#### scale

```python
@property
def scale() -> float
```

(float):  [Read-Write] Multiplier to use for the mapping when accumulating the axis value

<a id="unreal.InputAxisKeyMapping.scale"></a>

#### scale

```python
@scale.setter
def scale(value: float) -> None
```

<a id="unreal.InputAxisKeyMapping.key"></a>

#### key

```python
@property
def key() -> Key
```

(Key):  [Read-Write] Key to bind it to.

<a id="unreal.InputAxisKeyMapping.key"></a>

#### key

```python
@key.setter
def key(value: Key) -> None
```

<a id="unreal.InputActionSpeechMapping"></a>