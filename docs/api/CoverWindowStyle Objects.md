## CoverWindowStyle Objects

```python
class CoverWindowStyle(StructBase)
```

Cover Window Style

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: WindowAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``offset`` (Vector2D):  [Read-Write]
- ``size`` (Vector2D):  [Read-Write]
- ``url`` (str):  [Read-Write]

<a id="unreal.CoverWindowStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(url: str = "",
             size: Vector2D = [0.000000, 0.000000],
             offset: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.CoverWindowStyle.url"></a>

#### url

```python
@property
def url() -> str
```

(str):  [Read-Write]

<a id="unreal.CoverWindowStyle.url"></a>

#### url

```python
@url.setter
def url(value: str) -> None
```

<a id="unreal.CoverWindowStyle.size"></a>

#### size

```python
@property
def size() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.CoverWindowStyle.size"></a>

#### size

```python
@size.setter
def size(value: Vector2D) -> None
```

<a id="unreal.CoverWindowStyle.offset"></a>

#### offset

```python
@property
def offset() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.CoverWindowStyle.offset"></a>

#### offset

```python
@offset.setter
def offset(value: Vector2D) -> None
```

<a id="unreal.CreateWindowParams"></a>