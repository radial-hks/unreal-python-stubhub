## DisplayClusterReplaceTextureCropRectangle Objects

```python
class DisplayClusterReplaceTextureCropRectangle(StructBase)
```

Texture Replace Crop parameters container

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Base.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``origin`` (TextureCropOrigin):  [Read-Write] Texture Crop Origin
- ``size`` (TextureCropSize):  [Read-Write] Texture Crop Size

<a id="unreal.DisplayClusterReplaceTextureCropRectangle.__init__"></a>

#### __init__

```python
def __init__(origin: TextureCropOrigin = [0, 0],
             size: TextureCropSize = [0, 0]) -> None
```

<a id="unreal.DisplayClusterReplaceTextureCropRectangle.origin"></a>

#### origin

```python
@property
def origin() -> TextureCropOrigin
```

(TextureCropOrigin):  [Read-Write] Texture Crop Origin

<a id="unreal.DisplayClusterReplaceTextureCropRectangle.origin"></a>

#### origin

```python
@origin.setter
def origin(value: TextureCropOrigin) -> None
```

<a id="unreal.DisplayClusterReplaceTextureCropRectangle.size"></a>

#### size

```python
@property
def size() -> TextureCropSize
```

(TextureCropSize):  [Read-Write] Texture Crop Size

<a id="unreal.DisplayClusterReplaceTextureCropRectangle.size"></a>

#### size

```python
@size.setter
def size(value: TextureCropSize) -> None
```

<a id="unreal.DisplayClusterConfigurationRectangle"></a>