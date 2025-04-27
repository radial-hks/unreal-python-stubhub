## TextureCropSize Objects

```python
class TextureCropSize(StructBase)
```

Texture Replace Crop Size parameter container

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Base.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``h`` (int32):  [Read-Write] Replace texture crop height, in pixels
- ``w`` (int32):  [Read-Write] Replace texture crop width, in pixels

<a id="unreal.TextureCropSize.__init__"></a>

#### __init__

```python
def __init__(w: int = 0, h: int = 0) -> None
```

<a id="unreal.TextureCropSize.w"></a>

#### w

```python
@property
def w() -> int
```

(int32):  [Read-Write] Replace texture crop width, in pixels

<a id="unreal.TextureCropSize.w"></a>

#### w

```python
@w.setter
def w(value: int) -> None
```

<a id="unreal.TextureCropSize.h"></a>

#### h

```python
@property
def h() -> int
```

(int32):  [Read-Write] Replace texture crop height, in pixels

<a id="unreal.TextureCropSize.h"></a>

#### h

```python
@h.setter
def h(value: int) -> None
```

<a id="unreal.DisplayClusterReplaceTextureCropRectangle"></a>