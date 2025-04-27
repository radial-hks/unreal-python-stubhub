## AbcImportSettings Objects

```python
class AbcImportSettings(Object)
```

Class that contains all options for importing an alembic file

**C++ Source:**

- **Plugin**: AlembicImporter
- **Module**: AlembicLibrary
- **File**: AbcImportSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``compression_settings`` (AbcCompressionSettings):  [Read-Write]
- ``conversion_settings`` (AbcConversionSettings):  [Read-Write]
- ``geometry_cache_settings`` (AbcGeometryCacheSettings):  [Read-Write]
- ``import_type`` (AlembicImportType):  [Read-Write] Type of asset to import from Alembic file
- ``material_settings`` (AbcMaterialSettings):  [Read-Write]
- ``normal_generation_settings`` (AbcNormalGenerationSettings):  [Read-Write]
- ``sampling_settings`` (AbcSamplingSettings):  [Read-Write]
- ``static_mesh_settings`` (AbcStaticMeshSettings):  [Read-Write]

<a id="unreal.AbcImportSettings.import_type"></a>

#### import_type

```python
@property
def import_type() -> AlembicImportType
```

(AlembicImportType):  [Read-Write] Type of asset to import from Alembic file

<a id="unreal.AbcImportSettings.import_type"></a>

#### import_type

```python
@import_type.setter
def import_type(value: AlembicImportType) -> None
```

<a id="unreal.AbcImportSettings.sampling_settings"></a>

#### sampling_settings

```python
@property
def sampling_settings() -> AbcSamplingSettings
```

(AbcSamplingSettings):  [Read-Write]

<a id="unreal.AbcImportSettings.sampling_settings"></a>

#### sampling_settings

```python
@sampling_settings.setter
def sampling_settings(value: AbcSamplingSettings) -> None
```

<a id="unreal.AbcImportSettings.normal_generation_settings"></a>

#### normal_generation_settings

```python
@property
def normal_generation_settings() -> AbcNormalGenerationSettings
```

(AbcNormalGenerationSettings):  [Read-Write]

<a id="unreal.AbcImportSettings.normal_generation_settings"></a>

#### normal_generation_settings

```python
@normal_generation_settings.setter
def normal_generation_settings(value: AbcNormalGenerationSettings) -> None
```

<a id="unreal.AbcImportSettings.material_settings"></a>

#### material_settings

```python
@property
def material_settings() -> AbcMaterialSettings
```

(AbcMaterialSettings):  [Read-Write]

<a id="unreal.AbcImportSettings.material_settings"></a>

#### material_settings

```python
@material_settings.setter
def material_settings(value: AbcMaterialSettings) -> None
```

<a id="unreal.AbcImportSettings.compression_settings"></a>

#### compression_settings

```python
@property
def compression_settings() -> AbcCompressionSettings
```

(AbcCompressionSettings):  [Read-Write]

<a id="unreal.AbcImportSettings.compression_settings"></a>

#### compression_settings

```python
@compression_settings.setter
def compression_settings(value: AbcCompressionSettings) -> None
```

<a id="unreal.AbcImportSettings.static_mesh_settings"></a>

#### static_mesh_settings

```python
@property
def static_mesh_settings() -> AbcStaticMeshSettings
```

(AbcStaticMeshSettings):  [Read-Write]

<a id="unreal.AbcImportSettings.static_mesh_settings"></a>

#### static_mesh_settings

```python
@static_mesh_settings.setter
def static_mesh_settings(value: AbcStaticMeshSettings) -> None
```

<a id="unreal.AbcImportSettings.geometry_cache_settings"></a>

#### geometry_cache_settings

```python
@property
def geometry_cache_settings() -> AbcGeometryCacheSettings
```

(AbcGeometryCacheSettings):  [Read-Write]

<a id="unreal.AbcImportSettings.geometry_cache_settings"></a>

#### geometry_cache_settings

```python
@geometry_cache_settings.setter
def geometry_cache_settings(value: AbcGeometryCacheSettings) -> None
```

<a id="unreal.AbcImportSettings.conversion_settings"></a>

#### conversion_settings

```python
@property
def conversion_settings() -> AbcConversionSettings
```

(AbcConversionSettings):  [Read-Write]

<a id="unreal.AbcImportSettings.conversion_settings"></a>

#### conversion_settings

```python
@conversion_settings.setter
def conversion_settings(value: AbcConversionSettings) -> None
```

<a id="unreal.AlembicImportFactory"></a>