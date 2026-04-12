## RasterOverlayRendererOptions Objects

```python
class RasterOverlayRendererOptions(StructBase)
```

This struct is passed through the raster overlay options and is used when
`prepareRasterInLoadThread` is called.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumRasterOverlay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``filter`` (TextureFilter):  [Read-Write]
- ``group`` (TextureGroup):  [Read-Write]
- ``use_mipmaps`` (bool):  [Read-Write]

<a id="unreal.RasterOverlayRendererOptions.__init__"></a>

#### \_\_init\_\_

```python
def __init__(filter: TextureFilter = TextureFilter.TF_NEAREST,
             group: TextureGroup = TextureGroup.TEXTUREGROUP_WORLD,
             use_mipmaps: bool = False) -> None
```

<a id="unreal.RasterOverlayRendererOptions.filter"></a>

#### filter

```python
@property
def filter() -> TextureFilter
```

(TextureFilter):  [Read-Write]

<a id="unreal.RasterOverlayRendererOptions.filter"></a>

#### filter

```python
@filter.setter
def filter(value: TextureFilter) -> None
```

<a id="unreal.RasterOverlayRendererOptions.group"></a>

#### group

```python
@property
def group() -> TextureGroup
```

(TextureGroup):  [Read-Write]

<a id="unreal.RasterOverlayRendererOptions.group"></a>

#### group

```python
@group.setter
def group(value: TextureGroup) -> None
```

<a id="unreal.RasterOverlayRendererOptions.use_mipmaps"></a>

#### use\_mipmaps

```python
@property
def use_mipmaps() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RasterOverlayRendererOptions.use_mipmaps"></a>

#### use\_mipmaps

```python
@use_mipmaps.setter
def use_mipmaps(value: bool) -> None
```

<a id="unreal.CesiumRasterOverlayLoadFailureDetails"></a>