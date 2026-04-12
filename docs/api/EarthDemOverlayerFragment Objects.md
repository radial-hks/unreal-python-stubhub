## EarthDemOverlayerFragment Objects

```python
class EarthDemOverlayerFragment(EarthTextureOverlayerFragment)
```

定义数字高程图叠加器数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesMarkerSystem
- **File**: EarthDemOverlayerFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha_strength`` (float):  [Read-Write] 影响透明贴图或透明通道的透明度应用效果
- ``alpha_texture`` (Texture):  [Read-Write] 透明度控制贴图资产引用，当不使用Alpha通道时，该贴图将作为透明度控制，需确保该贴图资产的MipGenSettings设置为NoMipmaps
- ``blend_type`` (EarthOverlayerBlendType):  [Read-Write] 叠加贴图的混合类型
- ``bottom_left`` (Vector2D):  [Read-Write] 贴图包围盒的左下角经纬度
- ``earth_actor`` (Actor):  [Read-Write] 对应的地球对象
- ``feature_id`` (EarthFeatureIDFragment):  [Read-Write] 要素识别码
- ``input_height_range`` (Vector2f):  [Read-Write] 输入高度范围（原始数据的高度范围）
  X = 最小高度值，Y = 最大高度值（单位：米）
  仅在启用高度重映射功能时生效
- ``invalidate_producer_names`` (Array[Name]):  [Read-Only] 叠加器执行时需要更新的生产者
- ``output_height_range`` (Vector2f):  [Read-Write] 输出高度范围（目标高度范围）
  X = 最小高度值，Y = 最大高度值（单位：米）
  仅在启用高度重映射功能时生效
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
- ``use_height_remap`` (bool):  [Read-Write] 是否启用高度重映射功能
  开启时：将纹理中的像素值从"输入高度范围"重新映射到"输出高度范围"
  关闭时：直接使用纹理中的像素值作为实际的海拔高度（单位：米）
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthDemOverlayerFragment.__init__"></a>

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
        tiles: Set[str] = [],
        use_height_remap: bool = False,
        input_height_range: Vector2f = [0.000000, 0.000000],
        output_height_range: Vector2f = [0.000000, 0.000000]) -> None
```

<a id="unreal.EarthDemOverlayerFragment.use_height_remap"></a>

#### use\_height\_remap

```python
@property
def use_height_remap() -> bool
```

(bool):  [Read-Write] 是否启用高度重映射功能
开启时：将纹理中的像素值从"输入高度范围"重新映射到"输出高度范围"
关闭时：直接使用纹理中的像素值作为实际的海拔高度（单位：米）

<a id="unreal.EarthDemOverlayerFragment.use_height_remap"></a>

#### use\_height\_remap

```python
@use_height_remap.setter
def use_height_remap(value: bool) -> None
```

<a id="unreal.EarthDemOverlayerFragment.input_height_range"></a>

#### input\_height\_range

```python
@property
def input_height_range() -> Vector2f
```

(Vector2f):  [Read-Write] 输入高度范围（原始数据的高度范围）
X = 最小高度值，Y = 最大高度值（单位：米）
仅在启用高度重映射功能时生效

<a id="unreal.EarthDemOverlayerFragment.input_height_range"></a>

#### input\_height\_range

```python
@input_height_range.setter
def input_height_range(value: Vector2f) -> None
```

<a id="unreal.EarthDemOverlayerFragment.output_height_range"></a>

#### output\_height\_range

```python
@property
def output_height_range() -> Vector2f
```

(Vector2f):  [Read-Write] 输出高度范围（目标高度范围）
X = 最小高度值，Y = 最大高度值（单位：米）
仅在启用高度重映射功能时生效

<a id="unreal.EarthDemOverlayerFragment.output_height_range"></a>

#### output\_height\_range

```python
@output_height_range.setter
def output_height_range(value: Vector2f) -> None
```

<a id="unreal.EarthDomExtractorFragment"></a>