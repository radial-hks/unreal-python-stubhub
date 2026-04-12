## CompassDisplay Objects

```python
class CompassDisplay(StructBase)
```

Compass Display

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: CompassAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``anchors`` (str):  [Read-Write]
- ``position`` (Vector2D):  [Read-Write]
- ``size`` (int32):  [Read-Write]

<a id="unreal.CompassDisplay.__init__"></a>

#### \_\_init\_\_

```python
def __init__(position: Vector2D = [0.000000, 0.000000],
             size: int = 0,
             anchors: str = "") -> None
```

<a id="unreal.CompassDisplay.position"></a>

#### position

```python
@property
def position() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.CompassDisplay.position"></a>

#### position

```python
@position.setter
def position(value: Vector2D) -> None
```

<a id="unreal.CompassDisplay.size"></a>

#### size

```python
@property
def size() -> int
```

(int32):  [Read-Write]

<a id="unreal.CompassDisplay.size"></a>

#### size

```python
@size.setter
def size(value: int) -> None
```

<a id="unreal.CompassDisplay.anchors"></a>

#### anchors

```python
@property
def anchors() -> str
```

(str):  [Read-Write]

<a id="unreal.CompassDisplay.anchors"></a>

#### anchors

```python
@anchors.setter
def anchors(value: str) -> None
```

<a id="unreal.StartCompassParams"></a>