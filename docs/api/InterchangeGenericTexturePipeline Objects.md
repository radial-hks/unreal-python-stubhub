## InterchangeGenericTexturePipeline Objects

```python
class InterchangeGenericTexturePipeline(InterchangePipelineBase)
```

Interchange Generic Texture Pipeline

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangePipelines
- **File**: InterchangeGenericTexturePipeline.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_non_power_of_two`` (bool):  [Read-Write] If enabled, textures that have a non-power-of-two resolution are imported.
- ``asset_name`` (str):  [Read-Write] If set, and there is only one asset and one source, the imported asset will be given this name.
- ``detect_normal_map_texture`` (bool):  [Read-Write] If enabled, tests each newly imported texture to see if it is a normal map.
  If it is, the SRGB, Compression Settings, and LOD Group properties of that texture will be adjusted.
- ``file_extensions_to_import_as_long_lat_cubemap`` (Set[str]):  [Read-Write] Specify the file types that should be imported as long/lat cubemaps.
- ``flip_normal_map_green_channel`` (bool):  [Read-Write] If enabled, the texture's green channel will be inverted for normal maps. This setting is only used if the Detect Normal Map Texture setting is also enabled or if the texture has been imported as a Normal map.
- ``import_textures`` (bool):  [Read-Write] If enabled, imports all texture assets found in the source.
- ``import_udi_ms`` (bool):  [Read-Write] If enabled, imports textures as UDIMs if they are named using a UDIM naming pattern.
- ``pipeline_display_name`` (str):  [Read-Write] The name of the pipeline that will be display in the import dialog.
- ``prefer_compressed_source_data`` (bool):  [Read-Write] If enabled, the translator compresses the source data payload whenever possible. This generally results in smaller assets.
  However, some operations like the texture build might be slower, because the source data first needs to be decompressed.
  If disabled, the translator leaves the decision to the factory or the pipelines.

<a id="unreal.InterchangeGenericTexturePipeline.pipeline_display_name"></a>

#### pipeline_display_name

```python
@property
def pipeline_display_name() -> str
```

(str):  [Read-Write] The name of the pipeline that will be display in the import dialog.

<a id="unreal.InterchangeGenericTexturePipeline.pipeline_display_name"></a>

#### pipeline_display_name

```python
@pipeline_display_name.setter
def pipeline_display_name(value: str) -> None
```

<a id="unreal.InterchangeGenericTexturePipeline.import_textures"></a>

#### import_textures

```python
@property
def import_textures() -> bool
```

(bool):  [Read-Write] If enabled, imports all texture assets found in the source.

<a id="unreal.InterchangeGenericTexturePipeline.import_textures"></a>

#### import_textures

```python
@import_textures.setter
def import_textures(value: bool) -> None
```

<a id="unreal.InterchangeGenericTexturePipeline.asset_name"></a>

#### asset_name

```python
@property
def asset_name() -> str
```

(str):  [Read-Write] If set, and there is only one asset and one source, the imported asset will be given this name.

<a id="unreal.InterchangeGenericTexturePipeline.asset_name"></a>

#### asset_name

```python
@asset_name.setter
def asset_name(value: str) -> None
```

<a id="unreal.InterchangeGenericTexturePipeline.detect_normal_map_texture"></a>

#### detect_normal_map_texture

```python
@property
def detect_normal_map_texture() -> bool
```

(bool):  [Read-Write] If enabled, tests each newly imported texture to see if it is a normal map.
If it is, the SRGB, Compression Settings, and LOD Group properties of that texture will be adjusted.

<a id="unreal.InterchangeGenericTexturePipeline.detect_normal_map_texture"></a>

#### detect_normal_map_texture

```python
@detect_normal_map_texture.setter
def detect_normal_map_texture(value: bool) -> None
```

<a id="unreal.InterchangeGenericTexturePipeline.flip_normal_map_green_channel"></a>

#### flip_normal_map_green_channel

```python
@property
def flip_normal_map_green_channel() -> bool
```

(bool):  [Read-Write] If enabled, the texture's green channel will be inverted for normal maps. This setting is only used if the Detect Normal Map Texture setting is also enabled or if the texture has been imported as a Normal map.

<a id="unreal.InterchangeGenericTexturePipeline.flip_normal_map_green_channel"></a>

#### flip_normal_map_green_channel

```python
@flip_normal_map_green_channel.setter
def flip_normal_map_green_channel(value: bool) -> None
```

<a id="unreal.InterchangeGenericTexturePipeline.import_udi_ms"></a>

#### import_udi_ms

```python
@property
def import_udi_ms() -> bool
```

(bool):  [Read-Write] If enabled, imports textures as UDIMs if they are named using a UDIM naming pattern.

<a id="unreal.InterchangeGenericTexturePipeline.import_udi_ms"></a>

#### import_udi_ms

```python
@import_udi_ms.setter
def import_udi_ms(value: bool) -> None
```

<a id="unreal.InterchangeGenericTexturePipeline.file_extensions_to_import_as_long_lat_cubemap"></a>

#### file_extensions_to_import_as_long_lat_cubemap

```python
@property
def file_extensions_to_import_as_long_lat_cubemap() -> Set[str]
```

(Set[str]):  [Read-Write] Specify the file types that should be imported as long/lat cubemaps.

<a id="unreal.InterchangeGenericTexturePipeline.file_extensions_to_import_as_long_lat_cubemap"></a>

#### file_extensions_to_import_as_long_lat_cubemap

```python
@file_extensions_to_import_as_long_lat_cubemap.setter
def file_extensions_to_import_as_long_lat_cubemap(value: Set[str]) -> None
```

<a id="unreal.InterchangeGenericTexturePipeline.prefer_compressed_source_data"></a>

#### prefer_compressed_source_data

```python
@property
def prefer_compressed_source_data() -> bool
```

(bool):  [Read-Write] If enabled, the translator compresses the source data payload whenever possible. This generally results in smaller assets.
However, some operations like the texture build might be slower, because the source data first needs to be decompressed.
If disabled, the translator leaves the decision to the factory or the pipelines.

<a id="unreal.InterchangeGenericTexturePipeline.prefer_compressed_source_data"></a>

#### prefer_compressed_source_data

```python
@prefer_compressed_source_data.setter
def prefer_compressed_source_data(value: bool) -> None
```

<a id="unreal.InterchangeGenericTexturePipeline.allow_non_power_of_two"></a>

#### allow_non_power_of_two

```python
@property
def allow_non_power_of_two() -> bool
```

(bool):  [Read-Write] If enabled, textures that have a non-power-of-two resolution are imported.

<a id="unreal.InterchangeGenericTexturePipeline.allow_non_power_of_two"></a>

#### allow_non_power_of_two

```python
@allow_non_power_of_two.setter
def allow_non_power_of_two(value: bool) -> None
```

<a id="unreal.InterchangePipelineMeshesUtilities"></a>