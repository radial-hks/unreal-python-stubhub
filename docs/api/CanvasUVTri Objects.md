## CanvasUVTri Objects

```python
class CanvasUVTri(StructBase)
```

Simple 2d triangle with UVs

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``v0_color`` (LinearColor):  [Read-Write] Color of first vertex
- ``v0_pos`` (Vector2D):  [Read-Write] Position of first vertex
- ``v0_uv`` (Vector2D):  [Read-Write] UV of first vertex
- ``v1_color`` (LinearColor):  [Read-Write] Color of second vertex
- ``v1_pos`` (Vector2D):  [Read-Write] Position of second vertex
- ``v1_uv`` (Vector2D):  [Read-Write] UV of second vertex
- ``v2_color`` (LinearColor):  [Read-Write] Color of third vertex
- ``v2_pos`` (Vector2D):  [Read-Write] Position of third vertex
- ``v2_uv`` (Vector2D):  [Read-Write] UV of third vertex

<a id="unreal.CanvasUVTri.__init__"></a>

#### __init__

```python
def __init__(
        v0_pos: Vector2D = [0.000000, 0.000000],
        v0_uv: Vector2D = [0.000000, 0.000000],
        v0_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
        v1_pos: Vector2D = [0.000000, 0.000000],
        v1_uv: Vector2D = [0.000000, 0.000000],
        v1_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
        v2_pos: Vector2D = [0.000000, 0.000000],
        v2_uv: Vector2D = [0.000000, 0.000000],
        v2_color: LinearColor = [0.000000, 0.000000, 0.000000,
                                 0.000000]) -> None
```

<a id="unreal.CanvasUVTri.v0_pos"></a>

#### v0_pos

```python
@property
def v0_pos() -> Vector2D
```

(Vector2D):  [Read-Write] Position of first vertex

<a id="unreal.CanvasUVTri.v0_pos"></a>

#### v0_pos

```python
@v0_pos.setter
def v0_pos(value: Vector2D) -> None
```

<a id="unreal.CanvasUVTri.v0_uv"></a>

#### v0_uv

```python
@property
def v0_uv() -> Vector2D
```

(Vector2D):  [Read-Write] UV of first vertex

<a id="unreal.CanvasUVTri.v0_uv"></a>

#### v0_uv

```python
@v0_uv.setter
def v0_uv(value: Vector2D) -> None
```

<a id="unreal.CanvasUVTri.v0_color"></a>

#### v0_color

```python
@property
def v0_color() -> LinearColor
```

(LinearColor):  [Read-Write] Color of first vertex

<a id="unreal.CanvasUVTri.v0_color"></a>

#### v0_color

```python
@v0_color.setter
def v0_color(value: LinearColor) -> None
```

<a id="unreal.CanvasUVTri.v1_pos"></a>

#### v1_pos

```python
@property
def v1_pos() -> Vector2D
```

(Vector2D):  [Read-Write] Position of second vertex

<a id="unreal.CanvasUVTri.v1_pos"></a>

#### v1_pos

```python
@v1_pos.setter
def v1_pos(value: Vector2D) -> None
```

<a id="unreal.CanvasUVTri.v1_uv"></a>

#### v1_uv

```python
@property
def v1_uv() -> Vector2D
```

(Vector2D):  [Read-Write] UV of second vertex

<a id="unreal.CanvasUVTri.v1_uv"></a>

#### v1_uv

```python
@v1_uv.setter
def v1_uv(value: Vector2D) -> None
```

<a id="unreal.CanvasUVTri.v1_color"></a>

#### v1_color

```python
@property
def v1_color() -> LinearColor
```

(LinearColor):  [Read-Write] Color of second vertex

<a id="unreal.CanvasUVTri.v1_color"></a>

#### v1_color

```python
@v1_color.setter
def v1_color(value: LinearColor) -> None
```

<a id="unreal.CanvasUVTri.v2_pos"></a>

#### v2_pos

```python
@property
def v2_pos() -> Vector2D
```

(Vector2D):  [Read-Write] Position of third vertex

<a id="unreal.CanvasUVTri.v2_pos"></a>

#### v2_pos

```python
@v2_pos.setter
def v2_pos(value: Vector2D) -> None
```

<a id="unreal.CanvasUVTri.v2_uv"></a>

#### v2_uv

```python
@property
def v2_uv() -> Vector2D
```

(Vector2D):  [Read-Write] UV of third vertex

<a id="unreal.CanvasUVTri.v2_uv"></a>

#### v2_uv

```python
@v2_uv.setter
def v2_uv(value: Vector2D) -> None
```

<a id="unreal.CanvasUVTri.v2_color"></a>

#### v2_color

```python
@property
def v2_color() -> LinearColor
```

(LinearColor):  [Read-Write] Color of third vertex

<a id="unreal.CanvasUVTri.v2_color"></a>

#### v2_color

```python
@v2_color.setter
def v2_color(value: LinearColor) -> None
```

<a id="unreal.ExponentialHeightFogData"></a>