## WdpLine2D Objects

```python
class WdpLine2D(WdpCurve2D)
```

Wdp Line 2D

**C++ Source:**

- **Plugin**: WdpCommon
- **Module**: WdpGeometry
- **File**: WdpLine2D.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``end_point`` (Vector2D):  [Read-Write]
- ``start_point`` (Vector2D):  [Read-Write]

<a id="unreal.WdpLine2D.__init__"></a>

#### \_\_init\_\_

```python
def __init__(start_point: Vector2D = [0.000000, 0.000000],
             end_point: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.WdpLine2D.start_point"></a>

#### start\_point

```python
@property
def start_point() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WdpLine2D.start_point"></a>

#### start\_point

```python
@start_point.setter
def start_point(value: Vector2D) -> None
```

<a id="unreal.WdpLine2D.end_point"></a>

#### end\_point

```python
@property
def end_point() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WdpLine2D.end_point"></a>

#### end\_point

```python
@end_point.setter
def end_point(value: Vector2D) -> None
```

<a id="unreal.WdpPolyline"></a>