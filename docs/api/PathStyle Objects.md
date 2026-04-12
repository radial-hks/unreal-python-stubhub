## PathStyle Objects

```python
class PathStyle(StructBase)
```

Path Style

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: PathAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (str):  [Read-Write]
- ``pass_color`` (str):  [Read-Write]
- ``type`` (str):  [Read-Write]
- ``width`` (float):  [Read-Write]

<a id="unreal.PathStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(type: str = "",
             width: float = 0.000000,
             color: str = "",
             pass_color: str = "") -> None
```

<a id="unreal.PathStyle.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write]

<a id="unreal.PathStyle.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.PathStyle.width"></a>

#### width

```python
@property
def width() -> float
```

(float):  [Read-Write]

<a id="unreal.PathStyle.width"></a>

#### width

```python
@width.setter
def width(value: float) -> None
```

<a id="unreal.PathStyle.color"></a>

#### color

```python
@property
def color() -> str
```

(str):  [Read-Write]

<a id="unreal.PathStyle.color"></a>

#### color

```python
@color.setter
def color(value: str) -> None
```

<a id="unreal.PathStyle.pass_color"></a>

#### pass\_color

```python
@property
def pass_color() -> str
```

(str):  [Read-Write]

<a id="unreal.PathStyle.pass_color"></a>

#### pass\_color

```python
@pass_color.setter
def pass_color(value: str) -> None
```

<a id="unreal.CreatePathParams"></a>