## GLTFOverrideMaterialBakeSettings Objects

```python
class GLTFOverrideMaterialBakeSettings(StructBase)
```

GLTFOverride Material Bake Settings

**C++ Source:**

- **Plugin**: GLTFExporter
- **Module**: GLTFExporter
- **File**: GLTFMaterialUserData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``filter`` (TextureFilter):  [Read-Write] Overrides the default filtering mode used when sampling the baked out texture.
- ``override_filter`` (bool):  [Read-Write] If enabled, default filtering mode will be overridden by the corresponding property.
- ``override_size`` (bool):  [Read-Write] If enabled, default size will be overridden by the corresponding property.
- ``override_tiling`` (bool):  [Read-Write] If enabled, default addressing mode will be overridden by the corresponding property.
- ``size`` (GLTFMaterialBakeSize):  [Read-Write] Overrides default size of the baked out texture.
- ``tiling`` (TextureAddress):  [Read-Write] Overrides the default addressing mode used when sampling the baked out texture.

<a id="unreal.GLTFOverrideMaterialBakeSettings.__init__"></a>

#### __init__

```python
def __init__(override_size: bool = False,
             size: GLTFMaterialBakeSize = [1, 1, False],
             override_filter: bool = False,
             filter: TextureFilter = TextureFilter.TF_NEAREST,
             override_tiling: bool = False,
             tiling: TextureAddress = TextureAddress.TA_WRAP) -> None
```

<a id="unreal.GLTFOverrideMaterialBakeSettings.override_size"></a>

#### override_size

```python
@property
def override_size() -> bool
```

(bool):  [Read-Write] If enabled, default size will be overridden by the corresponding property.

<a id="unreal.GLTFOverrideMaterialBakeSettings.override_size"></a>

#### override_size

```python
@override_size.setter
def override_size(value: bool) -> None
```

<a id="unreal.GLTFOverrideMaterialBakeSettings.size"></a>

#### size

```python
@property
def size() -> GLTFMaterialBakeSize
```

(GLTFMaterialBakeSize):  [Read-Write] Overrides default size of the baked out texture.

<a id="unreal.GLTFOverrideMaterialBakeSettings.size"></a>

#### size

```python
@size.setter
def size(value: GLTFMaterialBakeSize) -> None
```

<a id="unreal.GLTFOverrideMaterialBakeSettings.override_filter"></a>

#### override_filter

```python
@property
def override_filter() -> bool
```

(bool):  [Read-Write] If enabled, default filtering mode will be overridden by the corresponding property.

<a id="unreal.GLTFOverrideMaterialBakeSettings.override_filter"></a>

#### override_filter

```python
@override_filter.setter
def override_filter(value: bool) -> None
```

<a id="unreal.GLTFOverrideMaterialBakeSettings.filter"></a>

#### filter

```python
@property
def filter() -> TextureFilter
```

(TextureFilter):  [Read-Write] Overrides the default filtering mode used when sampling the baked out texture.

<a id="unreal.GLTFOverrideMaterialBakeSettings.filter"></a>

#### filter

```python
@filter.setter
def filter(value: TextureFilter) -> None
```

<a id="unreal.GLTFOverrideMaterialBakeSettings.override_tiling"></a>

#### override_tiling

```python
@property
def override_tiling() -> bool
```

(bool):  [Read-Write] If enabled, default addressing mode will be overridden by the corresponding property.

<a id="unreal.GLTFOverrideMaterialBakeSettings.override_tiling"></a>

#### override_tiling

```python
@override_tiling.setter
def override_tiling(value: bool) -> None
```

<a id="unreal.GLTFOverrideMaterialBakeSettings.tiling"></a>

#### tiling

```python
@property
def tiling() -> TextureAddress
```

(TextureAddress):  [Read-Write] Overrides the default addressing mode used when sampling the baked out texture.

<a id="unreal.GLTFOverrideMaterialBakeSettings.tiling"></a>

#### tiling

```python
@tiling.setter
def tiling(value: TextureAddress) -> None
```

<a id="unreal.LidarPointCloudTraceHit"></a>