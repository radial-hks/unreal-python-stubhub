## EarthPrefabAssetLibrary Objects

```python
class EarthPrefabAssetLibrary(DataAsset)
```

预制体资产库

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthPrefabAssetLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``class_paths`` (Array[SoftClassPath]):  [Read-Write] ActorComponent列表，用于确保资产库所用ActorComponent能正确预加载
- ``debug_prefab_asset_path`` (SoftObjectPath):  [Read-Write] 调试用的预制体资产，必须与预制体资产列表有相同的预制体类型
- ``prefab_assets_paths`` (Array[SoftObjectPath]):  [Read-Write] 预制体资产列表，所有资产必须拥有相同的预制体类型，否则将无法加入列表，预制体类型以预制体资产列表的第一个有效资产为准
- ``random_prefab_assets_paths`` (Array[SoftObjectPath]):  [Read-Write] 随机预制体资产路径列表，所有资产必须拥有相同的预制体类型，否则将无法加入列表
  如果预制体资产列表不为空，预制体类型以预制体资产列表的第一个有效资产为准
  如果预制体资产列表为空，预制体类型以随机预制体资产路径列表的第一个有效资产为准
- ``type`` (ScriptStruct):  [Read-Only] 预制体类型，读取自预制体资产列表的第一个有效资产

<a id="unreal.EarthPrefabAssetLibrary.type"></a>

#### type

```python
@property
def type() -> ScriptStruct
```

(ScriptStruct):  [Read-Only] 预制体类型，读取自预制体资产列表的第一个有效资产

<a id="unreal.EarthPrefabAssetLibrary.prefab_assets_paths"></a>

#### prefab\_assets\_paths

```python
@property
def prefab_assets_paths() -> Array[SoftObjectPath]
```

(Array[SoftObjectPath]):  [Read-Write] 预制体资产列表，所有资产必须拥有相同的预制体类型，否则将无法加入列表，预制体类型以预制体资产列表的第一个有效资产为准

<a id="unreal.EarthPrefabAssetLibrary.prefab_assets_paths"></a>

#### prefab\_assets\_paths

```python
@prefab_assets_paths.setter
def prefab_assets_paths(value: Array[SoftObjectPath]) -> None
```

<a id="unreal.EarthPrefabAssetLibrary.random_prefab_assets_paths"></a>

#### random\_prefab\_assets\_paths

```python
@property
def random_prefab_assets_paths() -> Array[SoftObjectPath]
```

(Array[SoftObjectPath]):  [Read-Write] 随机预制体资产路径列表，所有资产必须拥有相同的预制体类型，否则将无法加入列表
如果预制体资产列表不为空，预制体类型以预制体资产列表的第一个有效资产为准
如果预制体资产列表为空，预制体类型以随机预制体资产路径列表的第一个有效资产为准

<a id="unreal.EarthPrefabAssetLibrary.random_prefab_assets_paths"></a>

#### random\_prefab\_assets\_paths

```python
@random_prefab_assets_paths.setter
def random_prefab_assets_paths(value: Array[SoftObjectPath]) -> None
```

<a id="unreal.EarthPrefabAssetLibrary.debug_prefab_asset_path"></a>

#### debug\_prefab\_asset\_path

```python
@property
def debug_prefab_asset_path() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] 调试用的预制体资产，必须与预制体资产列表有相同的预制体类型

<a id="unreal.EarthPrefabAssetLibrary.debug_prefab_asset_path"></a>

#### debug\_prefab\_asset\_path

```python
@debug_prefab_asset_path.setter
def debug_prefab_asset_path(value: SoftObjectPath) -> None
```

<a id="unreal.EarthPrefabAssetLibrary.class_paths"></a>

#### class\_paths

```python
@property
def class_paths() -> Array[SoftClassPath]
```

(Array[SoftClassPath]):  [Read-Write] ActorComponent列表，用于确保资产库所用ActorComponent能正确预加载

<a id="unreal.EarthPrefabAssetLibrary.class_paths"></a>

#### class\_paths

```python
@class_paths.setter
def class_paths(value: Array[SoftClassPath]) -> None
```

<a id="unreal.EarthPrefabAssetLibrary.validate_library"></a>

#### validate\_library

```python
def validate_library() -> None
```

x.validate_library() -> None
执行预制体资产库的有效性验证

<a id="unreal.EarthPrefabAssetLibrary.add_selected_random_assets"></a>

#### add\_selected\_random\_assets

```python
def add_selected_random_assets() -> None
```

x.add_selected_random_assets() -> None
添加选中的随机预制体资产到表中

<a id="unreal.EarthPrefabAssetLibrary.add_selected_assets"></a>

#### add\_selected\_assets

```python
def add_selected_assets() -> None
```

x.add_selected_assets() -> None
添加选中的预制体资产到表中

<a id="unreal.EarthRegionalPrefabAssetLibrary"></a>