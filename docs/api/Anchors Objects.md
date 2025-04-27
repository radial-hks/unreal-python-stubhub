## Anchors Objects

```python
class Anchors(StructBase)
```

Describes how a widget is anchored.

**C++ Source:**

- **Module**: Slate
- **File**: Anchors.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``maximum`` (Vector2D):  [Read-Write] Holds the maximum anchors, right + bottom.
- ``minimum`` (Vector2D):  [Read-Write] Holds the minimum anchors, left + top.

<a id="unreal.Anchors.__init__"></a>

#### __init__

```python
def __init__(minimum: Vector2D = [0.000000, 0.000000],
             maximum: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.Anchors.minimum"></a>

#### minimum

```python
@property
def minimum() -> Vector2D
```

(Vector2D):  [Read-Write] Holds the minimum anchors, left + top.

<a id="unreal.Anchors.minimum"></a>

#### minimum

```python
@minimum.setter
def minimum(value: Vector2D) -> None
```

<a id="unreal.Anchors.maximum"></a>

#### maximum

```python
@property
def maximum() -> Vector2D
```

(Vector2D):  [Read-Write] Holds the maximum anchors, right + bottom.

<a id="unreal.Anchors.maximum"></a>

#### maximum

```python
@maximum.setter
def maximum(value: Vector2D) -> None
```

<a id="unreal.TypedElementList"></a>