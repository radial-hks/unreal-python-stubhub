## DisplayClusterConfigurationPostRender_Override Objects

```python
class DisplayClusterConfigurationPostRender_Override(StructBase)
```

Display Cluster Configuration Post Render Override

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_PostRender.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_replace`` (bool):  [Read-Write] Disable default render, and resolve SourceTexture to viewport
- ``should_use_texture_region`` (bool):  [Read-Write] Set to True to crop the texture for the inner frustum as specified below.
- ``source_texture`` (Texture):  [Read-Write] Texture to use in place of the inner frustum.
- ``texture_region`` (DisplayClusterReplaceTextureCropRectangle):  [Read-Write] Texture Crop

<a id="unreal.DisplayClusterConfigurationPostRender_Override.__init__"></a>

#### __init__

```python
def __init__(
    allow_replace: bool = False,
    source_texture: Texture = None,
    should_use_texture_region: bool = False,
    texture_region: DisplayClusterReplaceTextureCropRectangle = [[0, 0],
                                                                 [0, 0]]
) -> None
```

<a id="unreal.DisplayClusterConfigurationPostRender_Override.allow_replace"></a>

#### allow_replace

```python
@property
def allow_replace() -> bool
```

(bool):  [Read-Write] Disable default render, and resolve SourceTexture to viewport

<a id="unreal.DisplayClusterConfigurationPostRender_Override.allow_replace"></a>

#### allow_replace

```python
@allow_replace.setter
def allow_replace(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationPostRender_Override.source_texture"></a>

#### source_texture

```python
@property
def source_texture() -> Texture
```

(Texture):  [Read-Write] Texture to use in place of the inner frustum.

<a id="unreal.DisplayClusterConfigurationPostRender_Override.source_texture"></a>

#### source_texture

```python
@source_texture.setter
def source_texture(value: Texture) -> None
```

<a id="unreal.DisplayClusterConfigurationPostRender_Override.should_use_texture_region"></a>

#### should_use_texture_region

```python
@property
def should_use_texture_region() -> bool
```

(bool):  [Read-Write] Set to True to crop the texture for the inner frustum as specified below.

<a id="unreal.DisplayClusterConfigurationPostRender_Override.should_use_texture_region"></a>

#### should_use_texture_region

```python
@should_use_texture_region.setter
def should_use_texture_region(value: bool) -> None
```

<a id="unreal.DisplayClusterConfigurationPostRender_Override.texture_region"></a>

#### texture_region

```python
@property
def texture_region() -> DisplayClusterReplaceTextureCropRectangle
```

(DisplayClusterReplaceTextureCropRectangle):  [Read-Write] Texture Crop

<a id="unreal.DisplayClusterConfigurationPostRender_Override.texture_region"></a>

#### texture_region

```python
@texture_region.setter
def texture_region(value: DisplayClusterReplaceTextureCropRectangle) -> None
```

<a id="unreal.DisplayClusterConfigurationICVFX_ChromakeyMarkers"></a>