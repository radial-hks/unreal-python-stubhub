## glTFRuntimeImagesConfig Objects

```python
class glTFRuntimeImagesConfig(StructBase)
```

Gl TFRuntime Images Config

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeParser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``compress_mips`` (bool):  [Read-Write]
- ``compression`` (TextureCompressionSettings):  [Read-Write]
- ``force_hdr`` (bool):  [Read-Write]
- ``group`` (TextureGroup):  [Read-Write]
- ``lod_bias`` (int32):  [Read-Write]
- ``max_height`` (int32):  [Read-Write]
- ``max_width`` (int32):  [Read-Write]
- ``srgb`` (bool):  [Read-Write]
- ``streaming`` (bool):  [Read-Write]
- ``vertical_flip`` (bool):  [Read-Write]

<a id="unreal.glTFRuntimeImagesConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        compression: TextureCompressionSettings = TextureCompressionSettings.
    TC_DEFAULT,
        group: TextureGroup = TextureGroup.TEXTUREGROUP_WORLD,
        srgb: bool = False,
        max_width: int = 0,
        max_height: int = 0,
        vertical_flip: bool = False,
        force_hdr: bool = False,
        compress_mips: bool = False,
        streaming: bool = False,
        lod_bias: int = 0) -> None
```

<a id="unreal.glTFRuntimeImagesConfig.compression"></a>

#### compression

```python
@property
def compression() -> TextureCompressionSettings
```

(TextureCompressionSettings):  [Read-Write]

<a id="unreal.glTFRuntimeImagesConfig.compression"></a>

#### compression

```python
@compression.setter
def compression(value: TextureCompressionSettings) -> None
```

<a id="unreal.glTFRuntimeImagesConfig.group"></a>

#### group

```python
@property
def group() -> TextureGroup
```

(TextureGroup):  [Read-Write]

<a id="unreal.glTFRuntimeImagesConfig.group"></a>

#### group

```python
@group.setter
def group(value: TextureGroup) -> None
```

<a id="unreal.glTFRuntimeImagesConfig.srgb"></a>

#### srgb

```python
@property
def srgb() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeImagesConfig.srgb"></a>

#### srgb

```python
@srgb.setter
def srgb(value: bool) -> None
```

<a id="unreal.glTFRuntimeImagesConfig.max_width"></a>

#### max\_width

```python
@property
def max_width() -> int
```

(int32):  [Read-Write]

<a id="unreal.glTFRuntimeImagesConfig.max_width"></a>

#### max\_width

```python
@max_width.setter
def max_width(value: int) -> None
```

<a id="unreal.glTFRuntimeImagesConfig.max_height"></a>

#### max\_height

```python
@property
def max_height() -> int
```

(int32):  [Read-Write]

<a id="unreal.glTFRuntimeImagesConfig.max_height"></a>

#### max\_height

```python
@max_height.setter
def max_height(value: int) -> None
```

<a id="unreal.glTFRuntimeImagesConfig.vertical_flip"></a>

#### vertical\_flip

```python
@property
def vertical_flip() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeImagesConfig.vertical_flip"></a>

#### vertical\_flip

```python
@vertical_flip.setter
def vertical_flip(value: bool) -> None
```

<a id="unreal.glTFRuntimeImagesConfig.force_hdr"></a>

#### force\_hdr

```python
@property
def force_hdr() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeImagesConfig.force_hdr"></a>

#### force\_hdr

```python
@force_hdr.setter
def force_hdr(value: bool) -> None
```

<a id="unreal.glTFRuntimeImagesConfig.compress_mips"></a>

#### compress\_mips

```python
@property
def compress_mips() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeImagesConfig.compress_mips"></a>

#### compress\_mips

```python
@compress_mips.setter
def compress_mips(value: bool) -> None
```

<a id="unreal.glTFRuntimeImagesConfig.streaming"></a>

#### streaming

```python
@property
def streaming() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeImagesConfig.streaming"></a>

#### streaming

```python
@streaming.setter
def streaming(value: bool) -> None
```

<a id="unreal.glTFRuntimeImagesConfig.lod_bias"></a>

#### lod\_bias

```python
@property
def lod_bias() -> int
```

(int32):  [Read-Write]

<a id="unreal.glTFRuntimeImagesConfig.lod_bias"></a>

#### lod\_bias

```python
@lod_bias.setter
def lod_bias(value: int) -> None
```

<a id="unreal.glTFRuntimeTextureSampler"></a>