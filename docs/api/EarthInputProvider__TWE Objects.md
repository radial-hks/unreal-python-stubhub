## EarthInputProvider\_TWE Objects

```python
class EarthInputProvider_TWE(EarthInputProviderBase)
```

基于TWE数据格式的输入数据提供者

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesMarkerSystem
- **File**: CGLFileReader.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_level`` (int32):  [Read-Write] TWE数据源的基础级别,默认为6级
- ``data_quad_keys`` (Array[str]):  [Read-Only] 预览数据源所包含的所有QuadKey
- ``data_source_path`` (FilePath):  [Read-Write] TWE数据源路径
- ``geo_referencing_system`` (EarthGeoReferencingSystem):  [Read-Write]
- ``global_prefab`` (EarthPrefabBase):  [Read-Write] 由输入数据提供者提供的全局预制体数据
- ``layer_type`` (LayerType):  [Read-Write] 使用何种数据源
- ``quad_key`` (str):  [Read-Write] 地图瓦片的QuadKey
- ``quad_key_level`` (int32):  [Read-Only] 预览QuadKey所代表的级别，矢量数据默认为14级
- ``road_water_merge`` (bool):  [Read-Only]

<a id="unreal.EarthInputProvider_TWE.geo_referencing_system"></a>

#### geo\_referencing\_system

```python
@property
def geo_referencing_system() -> EarthGeoReferencingSystem
```

(EarthGeoReferencingSystem):  [Read-Write]

<a id="unreal.EarthInputProvider_TWE.geo_referencing_system"></a>

#### geo\_referencing\_system

```python
@geo_referencing_system.setter
def geo_referencing_system(value: EarthGeoReferencingSystem) -> None
```

<a id="unreal.EarthInputProvider_TWE.data_source_path"></a>

#### data\_source\_path

```python
@property
def data_source_path() -> FilePath
```

(FilePath):  [Read-Write] TWE数据源路径

<a id="unreal.EarthInputProvider_TWE.data_source_path"></a>

#### data\_source\_path

```python
@data_source_path.setter
def data_source_path(value: FilePath) -> None
```

<a id="unreal.EarthInputProvider_TWE.layer_type"></a>

#### layer\_type

```python
@property
def layer_type() -> LayerType
```

(LayerType):  [Read-Write] 使用何种数据源

<a id="unreal.EarthInputProvider_TWE.layer_type"></a>

#### layer\_type

```python
@layer_type.setter
def layer_type(value: LayerType) -> None
```

<a id="unreal.EarthInputProvider_TWE.base_level"></a>

#### base\_level

```python
@property
def base_level() -> int
```

(int32):  [Read-Write] TWE数据源的基础级别,默认为6级

<a id="unreal.EarthInputProvider_TWE.base_level"></a>

#### base\_level

```python
@base_level.setter
def base_level(value: int) -> None
```

<a id="unreal.EarthInputProvider_TWE.quad_key"></a>

#### quad\_key

```python
@property
def quad_key() -> str
```

(str):  [Read-Write] 地图瓦片的QuadKey

<a id="unreal.EarthInputProvider_TWE.quad_key"></a>

#### quad\_key

```python
@quad_key.setter
def quad_key(value: str) -> None
```

<a id="unreal.EarthActorEntity"></a>