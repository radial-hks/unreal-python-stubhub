## RasterStyle Objects

```python
class RasterStyle(StructBase)
```

Raster Style

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: RasterAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gradient_setting`` (Array[str]):  [Read-Write]
- ``path`` (str):  [Read-Write]
- ``type`` (str):  [Read-Write]

<a id="unreal.RasterStyle.__init__"></a>

#### \_\_init\_\_

```python
def __init__(path: str = "",
             type: str = "",
             gradient_setting: Array[str] = []) -> None
```

<a id="unreal.RasterStyle.path"></a>

#### path

```python
@property
def path() -> str
```

(str):  [Read-Write]

<a id="unreal.RasterStyle.path"></a>

#### path

```python
@path.setter
def path(value: str) -> None
```

<a id="unreal.RasterStyle.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write]

<a id="unreal.RasterStyle.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.RasterStyle.gradient_setting"></a>

#### gradient\_setting

```python
@property
def gradient_setting() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.RasterStyle.gradient_setting"></a>

#### gradient\_setting

```python
@gradient_setting.setter
def gradient_setting(value: Array[str]) -> None
```

<a id="unreal.CreateRasterParams"></a>