## EarthTextureExtractorFragment Objects

```python
class EarthTextureExtractorFragment(EarthOutputFragment)
```

定义贴图提取器数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesMarkerSystem
- **File**: EarthTextureExtractorFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

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

<a id="unreal.EarthTextureExtractorFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             owned_object: Object = None,
             extract_level: int = 0,
             texture: TextureRenderTarget2D = None,
             producer_name: Name = "None",
             render_target_format:
             TextureRenderTargetFormat = TextureRenderTargetFormat.RTF_R8,
             srgb: bool = False,
             need_swizzle_channel: bool = False,
             earth_actor: Actor = None,
             source_bounds: Box2D = [[0.000000, 0.000000],
                                     [0.000000, 0.000000], False],
             target_bounds: Box2D = [[0.000000, 0.000000],
                                     [0.000000, 0.000000], False],
             tiles: Array[str] = [],
             tile_size: IntPoint = [0, 0]) -> None
```

<a id="unreal.EarthTextureExtractorFragment.extract_level"></a>

#### extract\_level

```python
@property
def extract_level() -> int
```

(int32):  [Read-Write] 想提取卫星图的级别，该级别必须从Levels参数中选择

<a id="unreal.EarthTextureExtractorFragment.extract_level"></a>

#### extract\_level

```python
@extract_level.setter
def extract_level(value: int) -> None
```

<a id="unreal.EarthTextureExtractorFragment.texture"></a>

#### texture

```python
@property
def texture() -> TextureRenderTarget2D
```

(TextureRenderTarget2D):  [Read-Write] 可以预览要提取的贴图，可以手动指定一个RenderTarget2D资产，如果不指定，则会自动创建一个临时的

<a id="unreal.EarthTextureExtractorFragment.texture"></a>

#### texture

```python
@texture.setter
def texture(value: TextureRenderTarget2D) -> None
```

<a id="unreal.EarthTextureExtractorFragment.producer_name"></a>

#### producer\_name

```python
@property
def producer_name() -> Name
```

(Name):  [Read-Only] 提取数据的生产者名称

<a id="unreal.EarthTextureExtractorFragment.render_target_format"></a>

#### render\_target\_format

```python
@property
def render_target_format() -> TextureRenderTargetFormat
```

(TextureRenderTargetFormat):  [Read-Only] 渲染对象的贴图格式

<a id="unreal.EarthTextureExtractorFragment.srgb"></a>

#### srgb

```python
@property
def srgb() -> bool
```

(bool):  [Read-Only] 是否在SRGB伽玛颜色空间中

<a id="unreal.EarthTextureExtractorFragment.need_swizzle_channel"></a>

#### need\_swizzle\_channel

```python
@property
def need_swizzle_channel() -> bool
```

(bool):  [Read-Only] 是否需要交换通道

<a id="unreal.EarthTextureExtractorFragment.earth_actor"></a>

#### earth\_actor

```python
@property
def earth_actor() -> Actor
```

(Actor):  [Read-Write] 对应的地球对象

<a id="unreal.EarthTextureExtractorFragment.earth_actor"></a>

#### earth\_actor

```python
@earth_actor.setter
def earth_actor(value: Actor) -> None
```

<a id="unreal.EarthTextureExtractorFragment.source_bounds"></a>

#### source\_bounds

```python
@property
def source_bounds() -> Box2D
```

(Box2D):  [Read-Write] 要提取的数据源的包围盒

<a id="unreal.EarthTextureExtractorFragment.source_bounds"></a>

#### source\_bounds

```python
@source_bounds.setter
def source_bounds(value: Box2D) -> None
```

<a id="unreal.EarthTextureExtractorFragment.target_bounds"></a>

#### target\_bounds

```python
@property
def target_bounds() -> Box2D
```

(Box2D):  [Read-Write] 贴图包围盒

<a id="unreal.EarthTextureExtractorFragment.target_bounds"></a>

#### target\_bounds

```python
@target_bounds.setter
def target_bounds(value: Box2D) -> None
```

<a id="unreal.EarthTextureExtractorFragment.tiles"></a>

#### tiles

```python
@property
def tiles() -> Array[str]
```

(Array[str]):  [Read-Write] 提取贴图所在的地块ID，数组排序按地块从左到右从上到下

<a id="unreal.EarthTextureExtractorFragment.tiles"></a>

#### tiles

```python
@tiles.setter
def tiles(value: Array[str]) -> None
```

<a id="unreal.EarthTextureExtractorFragment.tile_size"></a>

#### tile\_size

```python
@property
def tile_size() -> IntPoint
```

(IntPoint):  [Read-Write] 提取贴图所在的地块的XY数量

<a id="unreal.EarthTextureExtractorFragment.tile_size"></a>

#### tile\_size

```python
@tile_size.setter
def tile_size(value: IntPoint) -> None
```

<a id="unreal.EarthDemExtractorFragment"></a>