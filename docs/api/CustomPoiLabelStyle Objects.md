## CustomPoiLabelStyle Objects

```python
class CustomPoiLabelStyle(StructBase)
```

Custom Poi Label Style

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: CustomPoiEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``background`` (Array[str]):  [Read-Write]
- ``height`` (int32):  [Read-Write]
- ``offset`` (Vector2D):  [Read-Write]
- ``visible`` (int32):  [Read-Write]
- ``width`` (int32):  [Read-Write]
- ``z_index`` (int32):  [Read-Write]

<a id="unreal.CustomPoiLabelStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(width: int = 0,
             height: int = 0,
             visible: int = 0,
             offset: Vector2D = [0.000000, 0.000000],
             z_index: int = 0,
             background: Array[str] = []) -> None
```

<a id="unreal.CustomPoiLabelStyle.width"></a>

#### width

```python
@property
def width() -> int
```

(int32):  [Read-Write]

<a id="unreal.CustomPoiLabelStyle.width"></a>

#### width

```python
@width.setter
def width(value: int) -> None
```

<a id="unreal.CustomPoiLabelStyle.height"></a>

#### height

```python
@property
def height() -> int
```

(int32):  [Read-Write]

<a id="unreal.CustomPoiLabelStyle.height"></a>

#### height

```python
@height.setter
def height(value: int) -> None
```

<a id="unreal.CustomPoiLabelStyle.visible"></a>

#### visible

```python
@property
def visible() -> int
```

(int32):  [Read-Write]

<a id="unreal.CustomPoiLabelStyle.visible"></a>

#### visible

```python
@visible.setter
def visible(value: int) -> None
```

<a id="unreal.CustomPoiLabelStyle.offset"></a>

#### offset

```python
@property
def offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.CustomPoiLabelStyle.offset"></a>

#### offset

```python
@offset.setter
def offset(value: Vector2D) -> None
```

<a id="unreal.CustomPoiLabelStyle.z_index"></a>

#### z\_index

```python
@property
def z_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.CustomPoiLabelStyle.z_index"></a>

#### z\_index

```python
@z_index.setter
def z_index(value: int) -> None
```

<a id="unreal.CustomPoiLabelStyle.background"></a>

#### background

```python
@property
def background() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.CustomPoiLabelStyle.background"></a>

#### background

```python
@background.setter
def background(value: Array[str]) -> None
```

<a id="unreal.CustomPoiLabelContentStyle"></a>