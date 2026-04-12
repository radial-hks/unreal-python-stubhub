## EarthTextureOverlayerFragment Objects

```python
class EarthTextureOverlayerFragment(EarthOutputFragment)
```

定义贴图叠加器数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesMarkerSystem
- **File**: EarthTextureOverlayerFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha_strength`` (float):  [Read-Write] 影响透明贴图或透明通道的透明度应用效果
- ``alpha_texture`` (Texture):  [Read-Write] 透明度控制贴图资产引用，当不使用Alpha通道时，该贴图将作为透明度控制，需确保该贴图资产的MipGenSettings设置为NoMipmaps
- ``blend_type`` (EarthOverlayerBlendType):  [Read-Write] 叠加贴图的混合类型
- ``bottom_left`` (Vector2D):  [Read-Write] 贴图包围盒的左下角经纬度
- ``earth_actor`` (Actor):  [Read-Write] 对应的地球对象
- ``feature_id`` (EarthFeatureIDFragment):  [Read-Write] 要素识别码
- ``invalidate_producer_names`` (Array[Name]):  [Read-Only] 叠加器执行时需要更新的生产者
- ``owned_object`` (Object):  [Read-Write] 输出片段所拥有的组件
- ``producer_name`` (Name):  [Read-Only] 叠加贴图作用的生产者
- ``rotation`` (float):  [Read-Write] 贴图的平面旋转角度
- ``sampler_type`` (EarthOverlayerSamplerType):  [Read-Write] 叠加贴图的采样器类型
- ``sort_order`` (int32):  [Read-Write] 叠加贴图的渲染顺序。数值越高，越叠加在上层。多张叠加贴图的叠加顺序相同时，FeatureID越大，则越叠加在上层
- ``texture`` (Texture):  [Read-Write] 叠加贴图资产引用，需确保该贴图资产的MipGenSettings设置为NoMipmaps
- ``tiles`` (Set[str]):  [Read-Write] 贴图所在的最高级别地块ID
- ``top_level`` (int32):  [Read-Write] 叠加贴图应用的最上层地块级别，如：该值为10时，叠加贴图不会在0-9级地块中执行叠加，仅会在10-20级执行叠加
- ``top_right`` (Vector2D):  [Read-Write] 贴图包围盒的右上角经纬度
- ``use_alpha_channel`` (bool):  [Read-Write] 是否使用叠加贴图的Alpha通道作为叠加的透明度控制
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthTextureOverlayerFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        validated: bool = False,
        valid: bool = False,
        owned_object: Object = None,
        top_level: int = 0,
        texture: Texture = None,
        sampler_type: EarthOverlayerSamplerType = EarthOverlayerSamplerType.
    BILINEAR,
        blend_type: EarthOverlayerBlendType = EarthOverlayerBlendType.REPLACE,
        alpha_strength: float = 0.000000,
        use_alpha_channel: bool = False,
        alpha_texture: Texture = None,
        sort_order: int = 0,
        producer_name: Name = "None",
        invalidate_producer_names: Array[Name] = [],
        feature_id: EarthFeatureIDFragment = [0, 0, False, False],
        earth_actor: Actor = None,
        bottom_left: Vector2D = [0.000000, 0.000000],
        top_right: Vector2D = [0.000000, 0.000000],
        rotation: float = 0.000000,
        tiles: Set[str] = []) -> None
```

<a id="unreal.EarthTextureOverlayerFragment.top_level"></a>

#### top\_level

```python
@property
def top_level() -> int
```

(int32):  [Read-Write] 叠加贴图应用的最上层地块级别，如：该值为10时，叠加贴图不会在0-9级地块中执行叠加，仅会在10-20级执行叠加

<a id="unreal.EarthTextureOverlayerFragment.top_level"></a>

#### top\_level

```python
@top_level.setter
def top_level(value: int) -> None
```

<a id="unreal.EarthTextureOverlayerFragment.texture"></a>

#### texture

```python
@property
def texture() -> Texture
```

(Texture):  [Read-Write] 叠加贴图资产引用，需确保该贴图资产的MipGenSettings设置为NoMipmaps

<a id="unreal.EarthTextureOverlayerFragment.texture"></a>

#### texture

```python
@texture.setter
def texture(value: Texture) -> None
```

<a id="unreal.EarthTextureOverlayerFragment.sampler_type"></a>

#### sampler\_type

```python
@property
def sampler_type() -> EarthOverlayerSamplerType
```

(EarthOverlayerSamplerType):  [Read-Write] 叠加贴图的采样器类型

<a id="unreal.EarthTextureOverlayerFragment.sampler_type"></a>

#### sampler\_type

```python
@sampler_type.setter
def sampler_type(value: EarthOverlayerSamplerType) -> None
```

<a id="unreal.EarthTextureOverlayerFragment.blend_type"></a>

#### blend\_type

```python
@property
def blend_type() -> EarthOverlayerBlendType
```

(EarthOverlayerBlendType):  [Read-Write] 叠加贴图的混合类型

<a id="unreal.EarthTextureOverlayerFragment.blend_type"></a>

#### blend\_type

```python
@blend_type.setter
def blend_type(value: EarthOverlayerBlendType) -> None
```

<a id="unreal.EarthTextureOverlayerFragment.alpha_strength"></a>

#### alpha\_strength

```python
@property
def alpha_strength() -> float
```

(float):  [Read-Write] 影响透明贴图或透明通道的透明度应用效果

<a id="unreal.EarthTextureOverlayerFragment.alpha_strength"></a>

#### alpha\_strength

```python
@alpha_strength.setter
def alpha_strength(value: float) -> None
```

<a id="unreal.EarthTextureOverlayerFragment.use_alpha_channel"></a>

#### use\_alpha\_channel

```python
@property
def use_alpha_channel() -> bool
```

(bool):  [Read-Write] 是否使用叠加贴图的Alpha通道作为叠加的透明度控制

<a id="unreal.EarthTextureOverlayerFragment.use_alpha_channel"></a>

#### use\_alpha\_channel

```python
@use_alpha_channel.setter
def use_alpha_channel(value: bool) -> None
```

<a id="unreal.EarthTextureOverlayerFragment.alpha_texture"></a>

#### alpha\_texture

```python
@property
def alpha_texture() -> Texture
```

(Texture):  [Read-Write] 透明度控制贴图资产引用，当不使用Alpha通道时，该贴图将作为透明度控制，需确保该贴图资产的MipGenSettings设置为NoMipmaps

<a id="unreal.EarthTextureOverlayerFragment.alpha_texture"></a>

#### alpha\_texture

```python
@alpha_texture.setter
def alpha_texture(value: Texture) -> None
```

<a id="unreal.EarthTextureOverlayerFragment.sort_order"></a>

#### sort\_order

```python
@property
def sort_order() -> int
```

(int32):  [Read-Write] 叠加贴图的渲染顺序。数值越高，越叠加在上层。多张叠加贴图的叠加顺序相同时，FeatureID越大，则越叠加在上层

<a id="unreal.EarthTextureOverlayerFragment.sort_order"></a>

#### sort\_order

```python
@sort_order.setter
def sort_order(value: int) -> None
```

<a id="unreal.EarthTextureOverlayerFragment.producer_name"></a>

#### producer\_name

```python
@property
def producer_name() -> Name
```

(Name):  [Read-Only] 叠加贴图作用的生产者

<a id="unreal.EarthTextureOverlayerFragment.invalidate_producer_names"></a>

#### invalidate\_producer\_names

```python
@property
def invalidate_producer_names() -> Array[Name]
```

(Array[Name]):  [Read-Only] 叠加器执行时需要更新的生产者

<a id="unreal.EarthTextureOverlayerFragment.feature_id"></a>

#### feature\_id

```python
@property
def feature_id() -> EarthFeatureIDFragment
```

(EarthFeatureIDFragment):  [Read-Write] 要素识别码

<a id="unreal.EarthTextureOverlayerFragment.feature_id"></a>

#### feature\_id

```python
@feature_id.setter
def feature_id(value: EarthFeatureIDFragment) -> None
```

<a id="unreal.EarthTextureOverlayerFragment.earth_actor"></a>

#### earth\_actor

```python
@property
def earth_actor() -> Actor
```

(Actor):  [Read-Write] 对应的地球对象

<a id="unreal.EarthTextureOverlayerFragment.earth_actor"></a>

#### earth\_actor

```python
@earth_actor.setter
def earth_actor(value: Actor) -> None
```

<a id="unreal.EarthTextureOverlayerFragment.bottom_left"></a>

#### bottom\_left

```python
@property
def bottom_left() -> Vector2D
```

(Vector2D):  [Read-Write] 贴图包围盒的左下角经纬度

<a id="unreal.EarthTextureOverlayerFragment.bottom_left"></a>

#### bottom\_left

```python
@bottom_left.setter
def bottom_left(value: Vector2D) -> None
```

<a id="unreal.EarthTextureOverlayerFragment.top_right"></a>

#### top\_right

```python
@property
def top_right() -> Vector2D
```

(Vector2D):  [Read-Write] 贴图包围盒的右上角经纬度

<a id="unreal.EarthTextureOverlayerFragment.top_right"></a>

#### top\_right

```python
@top_right.setter
def top_right(value: Vector2D) -> None
```

<a id="unreal.EarthTextureOverlayerFragment.rotation"></a>

#### rotation

```python
@property
def rotation() -> float
```

(float):  [Read-Write] 贴图的平面旋转角度

<a id="unreal.EarthTextureOverlayerFragment.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: float) -> None
```

<a id="unreal.EarthTextureOverlayerFragment.tiles"></a>

#### tiles

```python
@property
def tiles() -> Set[str]
```

(Set[str]):  [Read-Write] 贴图所在的最高级别地块ID

<a id="unreal.EarthTextureOverlayerFragment.tiles"></a>

#### tiles

```python
@tiles.setter
def tiles(value: Set[str]) -> None
```

<a id="unreal.EarthDemOverlayerFragment"></a>