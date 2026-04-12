## EarthDomOverlayerSettings Objects

```python
class EarthDomOverlayerSettings(EarthTextureOverlayerSettings)
```

Earth Dom Overlayer Settings

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthMisc
- **File**: EarthTerrainSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha_strength`` (float):  [Read-Write] 透明度控制强度
- ``alpha_texture`` (Texture):  [Read-Write] 透明度控制贴图资产引用，当不使用Alpha通道时，该贴图将作为透明度控制
- ``bottom_left`` (Vector2D):  [Read-Write] 贴图包围盒的左下角经纬度
- ``feature_id`` (int64):  [Read-Write] 要素识别码
- ``rotation`` (float):  [Read-Write] 贴图的平面旋转角度
- ``sort_order`` (int32):  [Read-Write] 叠加贴图的渲染顺序。数值越高，越显示在上层。多张贴图渲染顺序相同时，FeatureID越大，则越显示在上层
- ``texture`` (Texture):  [Read-Write] 叠加贴图资产引用
- ``tiles`` (Array[str]):  [Read-Write] 贴图所在的最高级别地块ID
- ``top_level`` (int32):  [Read-Write] 叠加贴图应用的最上层地块级别
- ``top_right`` (Vector2D):  [Read-Write] 贴图包围盒的右上角经纬度
- ``use_alpha_channel`` (bool):  [Read-Write] 是否使用叠加贴图的Alpha通道作为叠加的透明度控制

<a id="unreal.EarthDomOverlayerSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.EarthDemOverlayerSettings"></a>