## IntRect Objects

```python
class IntRect(StructBase)
```

An integer rectangle in 2D space.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\IntRect.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max`` (IntPoint):  [Read-Write]
- ``min`` (IntPoint):  [Read-Write]

<a id="unreal.IntRect.__init__"></a>

#### __init__

```python
def __init__(min: IntPoint = [0, 0], max: IntPoint = [0, 0]) -> None
```

<a id="unreal.IntRect.min"></a>

#### min

```python
@property
def min() -> IntPoint
```

(IntPoint):  [Read-Write]

<a id="unreal.IntRect.min"></a>

#### min

```python
@min.setter
def min(value: IntPoint) -> None
```

<a id="unreal.IntRect.max"></a>

#### max

```python
@property
def max() -> IntPoint
```

(IntPoint):  [Read-Write]

<a id="unreal.IntRect.max"></a>

#### max

```python
@max.setter
def max(value: IntPoint) -> None
```

<a id="unreal.IntVector"></a>