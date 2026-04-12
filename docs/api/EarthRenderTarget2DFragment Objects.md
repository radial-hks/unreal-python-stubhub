## EarthRenderTarget2DFragment Objects

```python
class EarthRenderTarget2DFragment(EarthOutputFragment)
```

定义动态网格体数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRenderTarget2DFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``owned_object`` (Object):  [Read-Write] 输出片段所拥有的组件
- ``render_target2d`` (TextureRenderTarget2D):  [Read-Write]
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证
- ``water_color_presets`` (Array[EarthWaterColorPreset]):  [Read-Write]

<a id="unreal.EarthRenderTarget2DFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             owned_object: Object = None,
             render_target2d: TextureRenderTarget2D = None,
             water_color_presets: Array[EarthWaterColorPreset] = []) -> None
```

<a id="unreal.EarthRenderTarget2DFragment.render_target2d"></a>

#### render\_target2d

```python
@property
def render_target2d() -> TextureRenderTarget2D
```

(TextureRenderTarget2D):  [Read-Write]

<a id="unreal.EarthRenderTarget2DFragment.render_target2d"></a>

#### render\_target2d

```python
@render_target2d.setter
def render_target2d(value: TextureRenderTarget2D) -> None
```

<a id="unreal.EarthRenderTarget2DFragment.water_color_presets"></a>

#### water\_color\_presets

```python
@property
def water_color_presets() -> Array[EarthWaterColorPreset]
```

(Array[EarthWaterColorPreset]):  [Read-Write]

<a id="unreal.EarthRenderTarget2DFragment.water_color_presets"></a>

#### water\_color\_presets

```python
@water_color_presets.setter
def water_color_presets(value: Array[EarthWaterColorPreset]) -> None
```

<a id="unreal.EarthModuleFragment"></a>