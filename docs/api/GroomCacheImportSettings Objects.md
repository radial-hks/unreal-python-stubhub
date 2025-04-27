## GroomCacheImportSettings Objects

```python
class GroomCacheImportSettings(StructBase)
```

Groom Cache Import Settings

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomCacheImportOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``conversion_settings`` (GroomConversionSettings):  [Read-Write] Conversion settings to apply to the groom cache import when override is enabled
- ``frame_end`` (int32):  [Read-Write] Ending index to stop sampling the animation at
- ``frame_start`` (int32):  [Read-Write] Starting index to start sampling the animation from
- ``groom_asset`` (SoftObjectPath):  [Read-Write] The groom asset the groom cache will be built from (must be compatible)
- ``import_groom_asset`` (bool):  [Read-Write] Import or re-import the groom asset from this file
- ``import_groom_cache`` (bool):  [Read-Write] Import the animated groom that was detected in this file
- ``import_type`` (GroomCacheImportType):  [Read-Write] Groom Cache types to import
- ``override_conversion_settings`` (bool):  [Read-Write] Set to true to override the groom conversion settings. Otherwise, use the settings from the groom import options
- ``skip_empty_frames`` (bool):  [Read-Write] Skip empty (pre-roll) frames and start importing at the frame which actually contains data

<a id="unreal.GroomCacheImportSettings.__init__"></a>

#### __init__

```python
def __init__(
    import_groom_cache: bool = False,
    import_type: GroomCacheImportType = 0,
    frame_start: int = 0,
    frame_end: int = 0,
    skip_empty_frames: bool = False,
    import_groom_asset: bool = False,
    groom_asset: SoftObjectPath = [""],
    override_conversion_settings: bool = False,
    conversion_settings: GroomConversionSettings = [[
        0.000000, 0.000000, 0.000000
    ], [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.GroomCacheImportSettings.import_groom_cache"></a>

#### import_groom_cache

```python
@property
def import_groom_cache() -> bool
```

(bool):  [Read-Write] Import the animated groom that was detected in this file

<a id="unreal.GroomCacheImportSettings.import_groom_cache"></a>

#### import_groom_cache

```python
@import_groom_cache.setter
def import_groom_cache(value: bool) -> None
```

<a id="unreal.GroomCacheImportSettings.import_type"></a>

#### import_type

```python
@property
def import_type() -> GroomCacheImportType
```

(GroomCacheImportType):  [Read-Write] Groom Cache types to import

<a id="unreal.GroomCacheImportSettings.import_type"></a>

#### import_type

```python
@import_type.setter
def import_type(value: GroomCacheImportType) -> None
```

<a id="unreal.GroomCacheImportSettings.frame_start"></a>

#### frame_start

```python
@property
def frame_start() -> int
```

(int32):  [Read-Write] Starting index to start sampling the animation from

<a id="unreal.GroomCacheImportSettings.frame_start"></a>

#### frame_start

```python
@frame_start.setter
def frame_start(value: int) -> None
```

<a id="unreal.GroomCacheImportSettings.frame_end"></a>

#### frame_end

```python
@property
def frame_end() -> int
```

(int32):  [Read-Write] Ending index to stop sampling the animation at

<a id="unreal.GroomCacheImportSettings.frame_end"></a>

#### frame_end

```python
@frame_end.setter
def frame_end(value: int) -> None
```

<a id="unreal.GroomCacheImportSettings.skip_empty_frames"></a>

#### skip_empty_frames

```python
@property
def skip_empty_frames() -> bool
```

(bool):  [Read-Write] Skip empty (pre-roll) frames and start importing at the frame which actually contains data

<a id="unreal.GroomCacheImportSettings.skip_empty_frames"></a>

#### skip_empty_frames

```python
@skip_empty_frames.setter
def skip_empty_frames(value: bool) -> None
```

<a id="unreal.GroomCacheImportSettings.import_groom_asset"></a>

#### import_groom_asset

```python
@property
def import_groom_asset() -> bool
```

(bool):  [Read-Write] Import or re-import the groom asset from this file

<a id="unreal.GroomCacheImportSettings.import_groom_asset"></a>

#### import_groom_asset

```python
@import_groom_asset.setter
def import_groom_asset(value: bool) -> None
```

<a id="unreal.GroomCacheImportSettings.groom_asset"></a>

#### groom_asset

```python
@property
def groom_asset() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] The groom asset the groom cache will be built from (must be compatible)

<a id="unreal.GroomCacheImportSettings.groom_asset"></a>

#### groom_asset

```python
@groom_asset.setter
def groom_asset(value: SoftObjectPath) -> None
```

<a id="unreal.GroomCacheImportSettings.hair_strands_asset"></a>

#### hair_strands_asset

```python
@property
def hair_strands_asset() -> SoftObjectPath
```

deprecated: 'hair_strands_asset' was renamed to 'groom_asset'.

<a id="unreal.GroomCacheImportSettings.hair_strands_asset"></a>

#### hair_strands_asset

```python
@hair_strands_asset.setter
def hair_strands_asset(value: SoftObjectPath) -> None
```

<a id="unreal.GroomCacheImportSettings.override_conversion_settings"></a>

#### override_conversion_settings

```python
@property
def override_conversion_settings() -> bool
```

(bool):  [Read-Write] Set to true to override the groom conversion settings. Otherwise, use the settings from the groom import options

<a id="unreal.GroomCacheImportSettings.override_conversion_settings"></a>

#### override_conversion_settings

```python
@override_conversion_settings.setter
def override_conversion_settings(value: bool) -> None
```

<a id="unreal.GroomCacheImportSettings.conversion_settings"></a>

#### conversion_settings

```python
@property
def conversion_settings() -> GroomConversionSettings
```

(GroomConversionSettings):  [Read-Write] Conversion settings to apply to the groom cache import when override is enabled

<a id="unreal.GroomCacheImportSettings.conversion_settings"></a>

#### conversion_settings

```python
@conversion_settings.setter
def conversion_settings(value: GroomConversionSettings) -> None
```

<a id="unreal.GroomConversionSettings"></a>