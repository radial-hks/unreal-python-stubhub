## EarthModuleAsset Objects

```python
class EarthModuleAsset(DataAsset)
```

Earth Module Asset

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthPrefabAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``module_definition`` (EarthSubAssetInfo):  [Read-Write] 键为模块的唯一名称，值为模块信息
- ``thumbnail`` (Texture2D):  [Read-Write] 预制体资产缩略图，推荐像素为256x256

<a id="unreal.EarthModuleAsset.module_definition"></a>

#### module\_definition

```python
@property
def module_definition() -> EarthSubAssetInfo
```

(EarthSubAssetInfo):  [Read-Write] 键为模块的唯一名称，值为模块信息

<a id="unreal.EarthModuleAsset.module_definition"></a>

#### module\_definition

```python
@module_definition.setter
def module_definition(value: EarthSubAssetInfo) -> None
```

<a id="unreal.EarthModuleAsset.thumbnail"></a>

#### thumbnail

```python
@property
def thumbnail() -> Texture2D
```

(Texture2D):  [Read-Write] 预制体资产缩略图，推荐像素为256x256

<a id="unreal.EarthModuleAsset.thumbnail"></a>

#### thumbnail

```python
@thumbnail.setter
def thumbnail(value: Texture2D) -> None
```

<a id="unreal.EarthModuleAsset.set_thumbnail"></a>

#### set\_thumbnail

```python
def set_thumbnail(thumbnail: Texture2D) -> None
```

x.set_thumbnail(thumbnail) -> None
设置预制体资产缩略图

Args:
    thumbnail (Texture2D):

<a id="unreal.EarthModuleAsset.load_thumbnail"></a>

#### load\_thumbnail

```python
def load_thumbnail() -> None
```

x.load_thumbnail() -> None
从缩略图资产加载缩略图

<a id="unreal.EarthModuleAsset.get_thumbnail"></a>

#### get\_thumbnail

```python
def get_thumbnail() -> Texture2D
```

x.get_thumbnail() -> Texture2D
获取预制体资产缩略图

Returns:
    Texture2D:

<a id="unreal.EarthPrefabAssetLibrary"></a>