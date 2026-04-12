## CoverRealTimeVideoStyle Objects

```python
class CoverRealTimeVideoStyle(StructBase)
```

Cover Real Time Video Style

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: RealTimeVideoParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bokeh`` (float):  [Read-Write]
- ``corner_shift`` (Array[Vector2D]):  [Read-Write]
- ``offset`` (Vector2D):  [Read-Write]
- ``resolution`` (Vector2D):  [Read-Write]
- ``url`` (str):  [Read-Write]

<a id="unreal.CoverRealTimeVideoStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(url: str = "",
             resolution: Vector2D = [0.000000, 0.000000],
             offset: Vector2D = [0.000000, 0.000000],
             bokeh: float = 0.000000,
             corner_shift: Array[Vector2D] = []) -> None
```

<a id="unreal.CoverRealTimeVideoStyle.url"></a>

#### url

```python
@property
def url() -> str
```

(str):  [Read-Write]

<a id="unreal.CoverRealTimeVideoStyle.url"></a>

#### url

```python
@url.setter
def url(value: str) -> None
```

<a id="unreal.CoverRealTimeVideoStyle.resolution"></a>

#### resolution

```python
@property
def resolution() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.CoverRealTimeVideoStyle.resolution"></a>

#### resolution

```python
@resolution.setter
def resolution(value: Vector2D) -> None
```

<a id="unreal.CoverRealTimeVideoStyle.offset"></a>

#### offset

```python
@property
def offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.CoverRealTimeVideoStyle.offset"></a>

#### offset

```python
@offset.setter
def offset(value: Vector2D) -> None
```

<a id="unreal.CoverRealTimeVideoStyle.bokeh"></a>

#### bokeh

```python
@property
def bokeh() -> float
```

(float):  [Read-Write]

<a id="unreal.CoverRealTimeVideoStyle.bokeh"></a>

#### bokeh

```python
@bokeh.setter
def bokeh(value: float) -> None
```

<a id="unreal.CoverRealTimeVideoStyle.corner_shift"></a>

#### corner\_shift

```python
@property
def corner_shift() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.CoverRealTimeVideoStyle.corner_shift"></a>

#### corner\_shift

```python
@corner_shift.setter
def corner_shift(value: Array[Vector2D]) -> None
```

<a id="unreal.CreateRealTimeVideoParams"></a>