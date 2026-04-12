## MiniMapDisplay Objects

```python
class MiniMapDisplay(StructBase)
```

Mini Map Display

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: MiniMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``anchors`` (str):  [Read-Write]
- ``position`` (Vector2D):  [Read-Write]
- ``size`` (int32):  [Read-Write]

<a id="unreal.MiniMapDisplay.__init__"></a>

#### \_\_init\_\_

```python
def __init__(position: Vector2D = [0.000000, 0.000000],
             size: int = 0,
             anchors: str = "") -> None
```

<a id="unreal.MiniMapDisplay.position"></a>

#### position

```python
@property
def position() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.MiniMapDisplay.position"></a>

#### position

```python
@position.setter
def position(value: Vector2D) -> None
```

<a id="unreal.MiniMapDisplay.size"></a>

#### size

```python
@property
def size() -> int
```

(int32):  [Read-Write]

<a id="unreal.MiniMapDisplay.size"></a>

#### size

```python
@size.setter
def size(value: int) -> None
```

<a id="unreal.MiniMapDisplay.anchors"></a>

#### anchors

```python
@property
def anchors() -> str
```

(str):  [Read-Write]

<a id="unreal.MiniMapDisplay.anchors"></a>

#### anchors

```python
@anchors.setter
def anchors(value: str) -> None
```

<a id="unreal.StartMiniMapParams"></a>