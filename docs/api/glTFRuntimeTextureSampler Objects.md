## glTFRuntimeTextureSampler Objects

```python
class glTFRuntimeTextureSampler(StructBase)
```

Gl TFRuntime Texture Sampler

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeParser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``mag_filter`` (TextureFilter):  [Read-Write]
- ``min_filter`` (TextureFilter):  [Read-Write]
- ``tile_x`` (TextureAddress):  [Read-Write]
- ``tile_y`` (TextureAddress):  [Read-Write]
- ``tile_z`` (TextureAddress):  [Read-Write]

<a id="unreal.glTFRuntimeTextureSampler.__init__"></a>

#### \_\_init\_\_

```python
def __init__(tile_x: TextureAddress = TextureAddress.TA_WRAP,
             tile_y: TextureAddress = TextureAddress.TA_WRAP,
             tile_z: TextureAddress = TextureAddress.TA_WRAP,
             min_filter: TextureFilter = TextureFilter.TF_NEAREST,
             mag_filter: TextureFilter = TextureFilter.TF_NEAREST) -> None
```

<a id="unreal.glTFRuntimeTextureSampler.tile_x"></a>

#### tile\_x

```python
@property
def tile_x() -> TextureAddress
```

(TextureAddress):  [Read-Write]

<a id="unreal.glTFRuntimeTextureSampler.tile_x"></a>

#### tile\_x

```python
@tile_x.setter
def tile_x(value: TextureAddress) -> None
```

<a id="unreal.glTFRuntimeTextureSampler.tile_y"></a>

#### tile\_y

```python
@property
def tile_y() -> TextureAddress
```

(TextureAddress):  [Read-Write]

<a id="unreal.glTFRuntimeTextureSampler.tile_y"></a>

#### tile\_y

```python
@tile_y.setter
def tile_y(value: TextureAddress) -> None
```

<a id="unreal.glTFRuntimeTextureSampler.tile_z"></a>

#### tile\_z

```python
@property
def tile_z() -> TextureAddress
```

(TextureAddress):  [Read-Write]

<a id="unreal.glTFRuntimeTextureSampler.tile_z"></a>

#### tile\_z

```python
@tile_z.setter
def tile_z(value: TextureAddress) -> None
```

<a id="unreal.glTFRuntimeTextureSampler.min_filter"></a>

#### min\_filter

```python
@property
def min_filter() -> TextureFilter
```

(TextureFilter):  [Read-Write]

<a id="unreal.glTFRuntimeTextureSampler.min_filter"></a>

#### min\_filter

```python
@min_filter.setter
def min_filter(value: TextureFilter) -> None
```

<a id="unreal.glTFRuntimeTextureSampler.mag_filter"></a>

#### mag\_filter

```python
@property
def mag_filter() -> TextureFilter
```

(TextureFilter):  [Read-Write]

<a id="unreal.glTFRuntimeTextureSampler.mag_filter"></a>

#### mag\_filter

```python
@mag_filter.setter
def mag_filter(value: TextureFilter) -> None
```

<a id="unreal.glTFRuntimeMaterialsConfig"></a>