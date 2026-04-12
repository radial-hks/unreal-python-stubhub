## EarthRegionalPrefabAssetLibrary Objects

```python
class EarthRegionalPrefabAssetLibrary(DataAsset)
```

区域预制体资产库

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthPrefabAssetLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``all_deep_assets_loaded`` (bool):  [Read-Write] 检查是否所有深度资源已加载完毕
- ``class_paths`` (Array[SoftClassPath]):  [Read-Write] 区域ActorComponent列表，用于确保区域资产库所用ActorComponent能正确预加载
- ``outlines`` (Array[EarthRegionOutline]):  [Read-Write] 区域轮廓线列表
- ``prefab_asset_library_paths`` (Array[SoftObjectPath]):  [Read-Write] 区域资产库列表
- ``quad_keys`` (Array[Name]):  [Read-Write] 区域所在地块编号列表
- ``region_name`` (Name):  [Read-Write] 区域名称

<a id="unreal.EarthRegionalPrefabAssetLibrary.all_deep_assets_loaded"></a>

#### all\_deep\_assets\_loaded

```python
@property
def all_deep_assets_loaded() -> bool
```

(bool):  [Read-Only] 检查是否所有深度资源已加载完毕

<a id="unreal.EarthRegionalPrefabAssetLibrary.region_name"></a>

#### region\_name

```python
@property
def region_name() -> Name
```

(Name):  [Read-Write] 区域名称

<a id="unreal.EarthRegionalPrefabAssetLibrary.region_name"></a>

#### region\_name

```python
@region_name.setter
def region_name(value: Name) -> None
```

<a id="unreal.EarthRegionalPrefabAssetLibrary.quad_keys"></a>

#### quad\_keys

```python
@property
def quad_keys() -> Array[Name]
```

(Array[Name]):  [Read-Write] 区域所在地块编号列表

<a id="unreal.EarthRegionalPrefabAssetLibrary.quad_keys"></a>

#### quad\_keys

```python
@quad_keys.setter
def quad_keys(value: Array[Name]) -> None
```

<a id="unreal.EarthRegionalPrefabAssetLibrary.outlines"></a>

#### outlines

```python
@property
def outlines() -> Array[EarthRegionOutline]
```

(Array[EarthRegionOutline]):  [Read-Write] 区域轮廓线列表

<a id="unreal.EarthRegionalPrefabAssetLibrary.outlines"></a>

#### outlines

```python
@outlines.setter
def outlines(value: Array[EarthRegionOutline]) -> None
```

<a id="unreal.EarthRegionalPrefabAssetLibrary.prefab_asset_library_paths"></a>

#### prefab\_asset\_library\_paths

```python
@property
def prefab_asset_library_paths() -> Array[SoftObjectPath]
```

(Array[SoftObjectPath]):  [Read-Write] 区域资产库列表

<a id="unreal.EarthRegionalPrefabAssetLibrary.prefab_asset_library_paths"></a>

#### prefab\_asset\_library\_paths

```python
@prefab_asset_library_paths.setter
def prefab_asset_library_paths(value: Array[SoftObjectPath]) -> None
```

<a id="unreal.EarthRegionalPrefabAssetLibrary.class_paths"></a>

#### class\_paths

```python
@property
def class_paths() -> Array[SoftClassPath]
```

(Array[SoftClassPath]):  [Read-Write] 区域ActorComponent列表，用于确保区域资产库所用ActorComponent能正确预加载

<a id="unreal.EarthRegionalPrefabAssetLibrary.class_paths"></a>

#### class\_paths

```python
@class_paths.setter
def class_paths(value: Array[SoftClassPath]) -> None
```

<a id="unreal.EarthRegionalPrefabAssetLibrary.get_matched_regional_library"></a>

#### get\_matched\_regional\_library

```python
@classmethod
def get_matched_regional_library(
    cls,
    libraries: Array[EarthRegionalPrefabAssetLibrary],
    default_library: EarthRegionalPrefabAssetLibrary,
    quad_key: str,
    lon_lat: Vector2D = [0.000000,
                         0.000000]) -> EarthRegionalPrefabAssetLibrary
```

X.get_matched_regional_library(libraries, default_library, quad_key, lon_lat=[0.000000, 0.000000]) -> EarthRegionalPrefabAssetLibrary
获取匹配的区域资产库

Args:
    libraries (Array[EarthRegionalPrefabAssetLibrary]): 区域资产库列表
    default_library (EarthRegionalPrefabAssetLibrary): 当无法从区域资产库列表中匹配到合适的区域资产库时，使用该默认的区域资产库
    quad_key (str): 当前区域的QuadKey
    lon_lat (Vector2D): 当前区域的经纬度

Returns:
    EarthRegionalPrefabAssetLibrary:

<a id="unreal.EarthRoadJunctionPrefabAlgorithm"></a>