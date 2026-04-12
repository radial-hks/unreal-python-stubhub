## EarthDomExtractorFragment Objects

```python
class EarthDomExtractorFragment(EarthTextureExtractorFragment)
```

定义正射影像图提取器数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesMarkerSystem
- **File**: EarthDomExtractorFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dom_extractor_type`` (EarthDomExtractorType):  [Read-Write] 正射影像图叠加器类型，改变叠加器类型会自动修改相关参数的默认值
- ``earth_actor`` (Actor):  [Read-Write] 对应的地球对象
- ``extract_level`` (int32):  [Read-Write] 想提取卫星图的级别，该级别必须从Levels参数中选择
- ``need_swizzle_channel`` (bool):  [Read-Only] 是否需要交换通道
- ``owned_object`` (Object):  [Read-Write] 输出片段所拥有的组件
- ``producer_name`` (Name):  [Read-Only] 提取数据的生产者名称
- ``render_target_format`` (TextureRenderTargetFormat):  [Read-Only] 渲染对象的贴图格式
- ``source_bounds`` (Box2D):  [Read-Write] 要提取的数据源的包围盒
- ``srgb`` (bool):  [Read-Only] 是否在SRGB伽玛颜色空间中
- ``target_bounds`` (Box2D):  [Read-Write] 贴图包围盒
- ``texture`` (TextureRenderTarget2D):  [Read-Write] 可以预览要提取的贴图，可以手动指定一个RenderTarget2D资产，如果不指定，则会自动创建一个临时的
- ``tile_size`` (IntPoint):  [Read-Write] 提取贴图所在的地块的XY数量
- ``tiles`` (Array[str]):  [Read-Write] 提取贴图所在的地块ID，数组排序按地块从左到右从上到下
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthDomExtractorFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    validated: bool = False,
    valid: bool = False,
    owned_object: Object = None,
    extract_level: int = 0,
    texture: TextureRenderTarget2D = None,
    producer_name: Name = "None",
    render_target_format: TextureRenderTargetFormat = TextureRenderTargetFormat
    .RTF_R8,
    srgb: bool = False,
    need_swizzle_channel: bool = False,
    earth_actor: Actor = None,
    source_bounds: Box2D = [[0.000000, 0.000000], [0.000000, 0.000000], False],
    target_bounds: Box2D = [[0.000000, 0.000000], [0.000000, 0.000000], False],
    tiles: Array[str] = [],
    tile_size: IntPoint = [0, 0],
    dom_extractor_type: EarthDomExtractorType = EarthDomExtractorType.DOM
) -> None
```

<a id="unreal.EarthDomExtractorFragment.dom_extractor_type"></a>

#### dom\_extractor\_type

```python
@property
def dom_extractor_type() -> EarthDomExtractorType
```

(EarthDomExtractorType):  [Read-Write] 正射影像图叠加器类型，改变叠加器类型会自动修改相关参数的默认值

<a id="unreal.EarthDomExtractorFragment.dom_extractor_type"></a>

#### dom\_extractor\_type

```python
@dom_extractor_type.setter
def dom_extractor_type(value: EarthDomExtractorType) -> None
```

<a id="unreal.EarthDomOverlayerFragment"></a>