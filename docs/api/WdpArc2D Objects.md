## WdpArc2D Objects

```python
class WdpArc2D(WdpCurve2D)
```

Wdp Arc 2D

**C++ Source:**

- **Plugin**: WdpCommon
- **Module**: WdpGeometry
- **File**: WdpArc2D.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``end_angle`` (double):  [Read-Write]
- ``inverse`` (bool):  [Read-Write]
- ``origin`` (Vector2D):  [Read-Write]
- ``radius`` (double):  [Read-Write]
- ``start_angle`` (double):  [Read-Write]

<a id="unreal.WdpArc2D.__init__"></a>

#### \_\_init\_\_

```python
def __init__(origin: Vector2D = [0.000000, 0.000000],
             radius: float = 0.000000,
             start_angle: float = 0.000000,
             end_angle: float = 0.000000,
             inverse: bool = False) -> None
```

<a id="unreal.WdpArc2D.origin"></a>

#### origin

```python
@property
def origin() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.WdpArc2D.origin"></a>

#### origin

```python
@origin.setter
def origin(value: Vector2D) -> None
```

<a id="unreal.WdpArc2D.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(double):  [Read-Write]

<a id="unreal.WdpArc2D.radius"></a>

#### radius

```python
@radius.setter
def radius(value: float) -> None
```

<a id="unreal.WdpArc2D.start_angle"></a>

#### start\_angle

```python
@property
def start_angle() -> float
```

(double):  [Read-Write]

<a id="unreal.WdpArc2D.start_angle"></a>

#### start\_angle

```python
@start_angle.setter
def start_angle(value: float) -> None
```

<a id="unreal.WdpArc2D.end_angle"></a>

#### end\_angle

```python
@property
def end_angle() -> float
```

(double):  [Read-Write]

<a id="unreal.WdpArc2D.end_angle"></a>

#### end\_angle

```python
@end_angle.setter
def end_angle(value: float) -> None
```

<a id="unreal.WdpArc2D.inverse"></a>

#### inverse

```python
@property
def inverse() -> bool
```

(bool):  [Read-Write]

<a id="unreal.WdpArc2D.inverse"></a>

#### inverse

```python
@inverse.setter
def inverse(value: bool) -> None
```

<a id="unreal.WdpEllipse2D"></a>