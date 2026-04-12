## EarthPrefabAssetFunctionLibrary Objects

```python
class EarthPrefabAssetFunctionLibrary(BlueprintFunctionLibrary)
```

预制体资产函数库

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthPrefabAssetFunctionLibrary.h

<a id="unreal.EarthPrefabAssetFunctionLibrary.generate_thumbnail_from_viewport"></a>

#### generate\_thumbnail\_from\_viewport

```python
@classmethod
def generate_thumbnail_from_viewport(cls, asset: Object) -> bool
```

X.generate_thumbnail_from_viewport(asset) -> bool
通过捕捉编辑器视口生成缩略图

Args:
    asset (Object): 需要生成缩略图的目标资产

Returns:
    bool: 是否成功捕获视口并生成缩略图

<a id="unreal.EarthPrefabAssetFunctionLibrary.generate_thumbnail_from_texture"></a>

#### generate\_thumbnail\_from\_texture

```python
@classmethod
def generate_thumbnail_from_texture(cls, asset: Object,
                                    thumbnail_texture: Texture2D) -> bool
```

X.generate_thumbnail_from_texture(asset, thumbnail_texture) -> bool
将现有纹理设置为资产的缩略图

Args:
    asset (Object): 目标资产对象
    thumbnail_texture (Texture2D): 用作缩略图的纹理资源

Returns:
    bool: 是否成功应用缩略图

<a id="unreal.EarthPrefabAssetFunctionLibrary.generate_thumbnail_from_bitmap"></a>

#### generate\_thumbnail\_from\_bitmap

```python
@classmethod
def generate_thumbnail_from_bitmap(cls, asset: Object, bitmap: Array[Color],
                                   src_width: int, src_height: int) -> bool
```

X.generate_thumbnail_from_bitmap(asset, bitmap, src_width, src_height) -> bool
从原始位图数据生成缩略图

Args:
    asset (Object): 目标资产对象
    bitmap (Array[Color]): 像素颜色数据数组（按行优先排列）
    src_width (int32): 原始位图宽度（像素数）
    src_height (int32): 原始位图高度（像素数）

Returns:
    bool: 是否成功转换位图数据并生成缩略图

<a id="unreal.EarthPrefabAssetFunctionLibrary.generate_thumbnail_from_actor"></a>

#### generate\_thumbnail\_from\_actor

```python
@classmethod
def generate_thumbnail_from_actor(cls, actor: Actor, asset: Object) -> bool
```

X.generate_thumbnail_from_actor(actor, asset) -> bool
Generate Thumbnail from Actor

Args:
    actor (Actor): 
    asset (Object): 

Returns:
    bool:

<a id="unreal.EarthPrefabAssetFunctionLibrary.generate_thumbnail_for_prefab_asset"></a>

#### generate\_thumbnail\_for\_prefab\_asset

```python
@classmethod
def generate_thumbnail_for_prefab_asset(cls,
                                        prefab_asset: EarthPrefabAsset,
                                        actor: Actor = None) -> bool
```

X.generate_thumbnail_for_prefab_asset(prefab_asset, actor=None) -> bool
为预制资产生成缩略图

Args:
    prefab_asset (EarthPrefabAsset): 需要生成缩略图的预制资产
    actor (Actor): 可选参数，用于生成缩略图的Actor对象（为空时使用当前视图捕捉缩略图）

Returns:
    bool: 是否成功生成缩略图

<a id="unreal.EarthPrefabAssetFunctionLibrary.generate_thumbnail_for_object"></a>

#### generate\_thumbnail\_for\_object

```python
@classmethod
def generate_thumbnail_for_object(cls,
                                  asset: Object,
                                  texture: Texture2D = None) -> Texture2D
```

X.generate_thumbnail_for_object(asset, texture=None) -> Texture2D
为指定资产生成或更新缩略图

Args:
    asset (Object): 需要生成缩略图的目标资产对象
    texture (Texture2D): 可选参数，用于更新的现有纹理对象（为空时创建新纹理）

Returns:
    Texture2D: 生成的纹理对象，失败返回nullptr

<a id="unreal.EarthPrefabAssetFunctionLibrary.generate_texture_from_thumbnail"></a>

#### generate\_texture\_from\_thumbnail

```python
@classmethod
def generate_texture_from_thumbnail(cls,
                                    asset: Object,
                                    texture: Texture2D = None,
                                    outer: Object = None) -> Texture2D
```

X.generate_texture_from_thumbnail(asset, texture=None, outer=None) -> Texture2D
从现有缩略图数据创建纹理对象

Args:
    asset (Object): 关联的资产对象（用于获取缩略图数据）
    texture (Texture2D): 可选参数，用于更新的现有纹理对象（为空时创建新纹理）
    outer (Object): 可选参数，用于创建新纹理对象时指定纹理的Outer对象（默认为InAsset）

Returns:
    Texture2D: 包含缩略图数据的纹理对象，失败返回nullptr

<a id="unreal.AesEntity"></a>