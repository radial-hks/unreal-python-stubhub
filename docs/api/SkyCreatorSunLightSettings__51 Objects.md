## SkyCreatorSunLightSettings\_51 Objects

```python
class SkyCreatorSunLightSettings_51(StructBase)
```

阳光设置

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings_51.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``atmosphere_disk_color_scale`` (LinearColor):  [Read-Write] 乘以日轮亮度的一个颜色
- ``atmosphere_disk_color_scale_curve`` (CurveLinearColor):  [Read-Write] 乘以日轮亮度的一个颜色
- ``cloud_scattered_luminance_scale`` (LinearColor):  [Read-Write] 缩放在云参与媒介中散射时光的贡献度
  这有助于平衡这样一个事实，即我们的多重散射解决方案只能提供一个模拟效果
- ``cloud_scattered_luminance_scale_curve`` (CurveLinearColor):  [Read-Write] 缩放在云参与媒介中散射时光的贡献度
  这有助于平衡这样一个事实，即我们的多重散射解决方案只能提供一个模拟效果
- ``cloud_shadow_on_atmosphere_strength`` (float):  [Read-Write] 大气上的阴影强度。设为0时禁用
- ``cloud_shadow_on_atmosphere_strength_curve`` (CurveFloat):  [Read-Write] 大气上的阴影强度。设为0时禁用
- ``cloud_shadow_on_surface_strength`` (float):  [Read-Write] 不透明和透明网格体上的阴影强度。设为0时禁用
- ``cloud_shadow_on_surface_strength_curve`` (CurveFloat):  [Read-Write] 不透明和透明网格体上的阴影强度。设为0时禁用
- ``cloud_shadow_strength`` (float):  [Read-Write] 云阴影的整体强度。值越高，阻挡的光线越多
- ``cloud_shadow_strength_curve`` (CurveFloat):  [Read-Write] 云阴影的整体强度。值越高，阻挡的光线越多
- ``intensity`` (float):  [Read-Write] 来自光源的最大照度（按勒克斯计）
- ``intensity_curve`` (CurveFloat):  [Read-Write] 来自光源的最大照度（按勒克斯计）
- ``light_color`` (LinearColor):  [Read-Write] 过滤光照颜色
  注意：这会修改光照的效果强度
- ``light_color_curve`` (CurveLinearColor):  [Read-Write] 过滤光照颜色
  注意：这会修改光照的效果强度
- ``temperature`` (float):  [Read-Write] 黑体发光源的色温（以开尔文为单位）
  白色(D65)为6500K.
- ``temperature_curve`` (CurveFloat):  [Read-Write] 黑体发光源的色温（以开尔文为单位）
  白色(D65)为6500K.
- ``use_atmosphere_disk_color_scale`` (bool):  [Read-Write]
- ``use_cloud_scattered_luminance_scale`` (bool):  [Read-Write]
- ``use_cloud_shadow_on_atmosphere_strength`` (bool):  [Read-Write]
- ``use_cloud_shadow_on_surface_strength`` (bool):  [Read-Write]
- ``use_cloud_shadow_strength`` (bool):  [Read-Write]
- ``use_intensity`` (bool):  [Read-Write]
- ``use_light_color`` (bool):  [Read-Write]
- ``use_temperature`` (bool):  [Read-Write]
- ``use_volumetric_scattering_intensity`` (bool):  [Read-Write]
- ``volumetric_scattering_intensity`` (float):  [Read-Write] 此光照体积散射的强度
  此项将缩放 强度 和 光源颜色
- ``volumetric_scattering_intensity_curve`` (CurveFloat):  [Read-Write] 此光照体积散射的强度
  此项将缩放 强度 和 光源颜色

<a id="unreal.SkyCreatorSunLightSettings_51.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        use_intensity: bool = False,
        intensity: float = 0.000000,
        intensity_curve: CurveFloat = None,
        use_light_color: bool = False,
        light_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
        light_color_curve: CurveLinearColor = None,
        use_temperature: bool = False,
        temperature: float = 0.000000,
        temperature_curve: CurveFloat = None,
        use_volumetric_scattering_intensity: bool = False,
        volumetric_scattering_intensity: float = 0.000000,
        volumetric_scattering_intensity_curve: CurveFloat = None,
        use_atmosphere_disk_color_scale: bool = False,
        atmosphere_disk_color_scale: LinearColor = [
            0.000000, 0.000000, 0.000000, 0.000000
        ],
        atmosphere_disk_color_scale_curve: CurveLinearColor = None,
        use_cloud_scattered_luminance_scale: bool = False,
        cloud_scattered_luminance_scale: LinearColor = [
            0.000000, 0.000000, 0.000000, 0.000000
        ],
        cloud_scattered_luminance_scale_curve: CurveLinearColor = None,
        use_cloud_shadow_strength: bool = False,
        cloud_shadow_strength: float = 0.000000,
        cloud_shadow_strength_curve: CurveFloat = None,
        use_cloud_shadow_on_atmosphere_strength: bool = False,
        cloud_shadow_on_atmosphere_strength: float = 0.000000,
        cloud_shadow_on_atmosphere_strength_curve: CurveFloat = None,
        use_cloud_shadow_on_surface_strength: bool = False,
        cloud_shadow_on_surface_strength: float = 0.000000,
        cloud_shadow_on_surface_strength_curve: CurveFloat = None) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.use_intensity"></a>

#### use\_intensity

```python
@property
def use_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSunLightSettings_51.use_intensity"></a>

#### use\_intensity

```python
@use_intensity.setter
def use_intensity(value: bool) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.intensity"></a>

#### intensity

```python
@property
def intensity() -> float
```

(float):  [Read-Write] 来自光源的最大照度（按勒克斯计）

<a id="unreal.SkyCreatorSunLightSettings_51.intensity"></a>

#### intensity

```python
@intensity.setter
def intensity(value: float) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.intensity_curve"></a>

#### intensity\_curve

```python
@property
def intensity_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 来自光源的最大照度（按勒克斯计）

<a id="unreal.SkyCreatorSunLightSettings_51.intensity_curve"></a>

#### intensity\_curve

```python
@intensity_curve.setter
def intensity_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.use_light_color"></a>

#### use\_light\_color

```python
@property
def use_light_color() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSunLightSettings_51.use_light_color"></a>

#### use\_light\_color

```python
@use_light_color.setter
def use_light_color(value: bool) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.light_color"></a>

#### light\_color

```python
@property
def light_color() -> LinearColor
```

(LinearColor):  [Read-Write] 过滤光照颜色
注意：这会修改光照的效果强度

<a id="unreal.SkyCreatorSunLightSettings_51.light_color"></a>

#### light\_color

```python
@light_color.setter
def light_color(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.light_color_curve"></a>

#### light\_color\_curve

```python
@property
def light_color_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write] 过滤光照颜色
注意：这会修改光照的效果强度

<a id="unreal.SkyCreatorSunLightSettings_51.light_color_curve"></a>

#### light\_color\_curve

```python
@light_color_curve.setter
def light_color_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.use_temperature"></a>

#### use\_temperature

```python
@property
def use_temperature() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSunLightSettings_51.use_temperature"></a>

#### use\_temperature

```python
@use_temperature.setter
def use_temperature(value: bool) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.temperature"></a>

#### temperature

```python
@property
def temperature() -> float
```

(float):  [Read-Write] 黑体发光源的色温（以开尔文为单位）
白色(D65)为6500K.

<a id="unreal.SkyCreatorSunLightSettings_51.temperature"></a>

#### temperature

```python
@temperature.setter
def temperature(value: float) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.temperature_curve"></a>

#### temperature\_curve

```python
@property
def temperature_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 黑体发光源的色温（以开尔文为单位）
白色(D65)为6500K.

<a id="unreal.SkyCreatorSunLightSettings_51.temperature_curve"></a>

#### temperature\_curve

```python
@temperature_curve.setter
def temperature_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.use_volumetric_scattering_intensity"></a>

#### use\_volumetric\_scattering\_intensity

```python
@property
def use_volumetric_scattering_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSunLightSettings_51.use_volumetric_scattering_intensity"></a>

#### use\_volumetric\_scattering\_intensity

```python
@use_volumetric_scattering_intensity.setter
def use_volumetric_scattering_intensity(value: bool) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.volumetric_scattering_intensity"></a>

#### volumetric\_scattering\_intensity

```python
@property
def volumetric_scattering_intensity() -> float
```

(float):  [Read-Write] 此光照体积散射的强度
此项将缩放 强度 和 光源颜色

<a id="unreal.SkyCreatorSunLightSettings_51.volumetric_scattering_intensity"></a>

#### volumetric\_scattering\_intensity

```python
@volumetric_scattering_intensity.setter
def volumetric_scattering_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.volumetric_scattering_intensity_curve"></a>

#### volumetric\_scattering\_intensity\_curve

```python
@property
def volumetric_scattering_intensity_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 此光照体积散射的强度
此项将缩放 强度 和 光源颜色

<a id="unreal.SkyCreatorSunLightSettings_51.volumetric_scattering_intensity_curve"></a>

#### volumetric\_scattering\_intensity\_curve

```python
@volumetric_scattering_intensity_curve.setter
def volumetric_scattering_intensity_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.use_atmosphere_disk_color_scale"></a>

#### use\_atmosphere\_disk\_color\_scale

```python
@property
def use_atmosphere_disk_color_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSunLightSettings_51.use_atmosphere_disk_color_scale"></a>

#### use\_atmosphere\_disk\_color\_scale

```python
@use_atmosphere_disk_color_scale.setter
def use_atmosphere_disk_color_scale(value: bool) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.atmosphere_disk_color_scale"></a>

#### atmosphere\_disk\_color\_scale

```python
@property
def atmosphere_disk_color_scale() -> LinearColor
```

(LinearColor):  [Read-Write] 乘以日轮亮度的一个颜色

<a id="unreal.SkyCreatorSunLightSettings_51.atmosphere_disk_color_scale"></a>

#### atmosphere\_disk\_color\_scale

```python
@atmosphere_disk_color_scale.setter
def atmosphere_disk_color_scale(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.atmosphere_disk_color_scale_curve"></a>

#### atmosphere\_disk\_color\_scale\_curve

```python
@property
def atmosphere_disk_color_scale_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write] 乘以日轮亮度的一个颜色

<a id="unreal.SkyCreatorSunLightSettings_51.atmosphere_disk_color_scale_curve"></a>

#### atmosphere\_disk\_color\_scale\_curve

```python
@atmosphere_disk_color_scale_curve.setter
def atmosphere_disk_color_scale_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.use_cloud_scattered_luminance_scale"></a>

#### use\_cloud\_scattered\_luminance\_scale

```python
@property
def use_cloud_scattered_luminance_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSunLightSettings_51.use_cloud_scattered_luminance_scale"></a>

#### use\_cloud\_scattered\_luminance\_scale

```python
@use_cloud_scattered_luminance_scale.setter
def use_cloud_scattered_luminance_scale(value: bool) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.cloud_scattered_luminance_scale"></a>

#### cloud\_scattered\_luminance\_scale

```python
@property
def cloud_scattered_luminance_scale() -> LinearColor
```

(LinearColor):  [Read-Write] 缩放在云参与媒介中散射时光的贡献度
这有助于平衡这样一个事实，即我们的多重散射解决方案只能提供一个模拟效果

<a id="unreal.SkyCreatorSunLightSettings_51.cloud_scattered_luminance_scale"></a>

#### cloud\_scattered\_luminance\_scale

```python
@cloud_scattered_luminance_scale.setter
def cloud_scattered_luminance_scale(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.cloud_scattered_luminance_scale_curve"></a>

#### cloud\_scattered\_luminance\_scale\_curve

```python
@property
def cloud_scattered_luminance_scale_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write] 缩放在云参与媒介中散射时光的贡献度
这有助于平衡这样一个事实，即我们的多重散射解决方案只能提供一个模拟效果

<a id="unreal.SkyCreatorSunLightSettings_51.cloud_scattered_luminance_scale_curve"></a>

#### cloud\_scattered\_luminance\_scale\_curve

```python
@cloud_scattered_luminance_scale_curve.setter
def cloud_scattered_luminance_scale_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.use_cloud_shadow_strength"></a>

#### use\_cloud\_shadow\_strength

```python
@property
def use_cloud_shadow_strength() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSunLightSettings_51.use_cloud_shadow_strength"></a>

#### use\_cloud\_shadow\_strength

```python
@use_cloud_shadow_strength.setter
def use_cloud_shadow_strength(value: bool) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.cloud_shadow_strength"></a>

#### cloud\_shadow\_strength

```python
@property
def cloud_shadow_strength() -> float
```

(float):  [Read-Write] 云阴影的整体强度。值越高，阻挡的光线越多

<a id="unreal.SkyCreatorSunLightSettings_51.cloud_shadow_strength"></a>

#### cloud\_shadow\_strength

```python
@cloud_shadow_strength.setter
def cloud_shadow_strength(value: float) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.cloud_shadow_strength_curve"></a>

#### cloud\_shadow\_strength\_curve

```python
@property
def cloud_shadow_strength_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 云阴影的整体强度。值越高，阻挡的光线越多

<a id="unreal.SkyCreatorSunLightSettings_51.cloud_shadow_strength_curve"></a>

#### cloud\_shadow\_strength\_curve

```python
@cloud_shadow_strength_curve.setter
def cloud_shadow_strength_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.use_cloud_shadow_on_atmosphere_strength"></a>

#### use\_cloud\_shadow\_on\_atmosphere\_strength

```python
@property
def use_cloud_shadow_on_atmosphere_strength() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSunLightSettings_51.use_cloud_shadow_on_atmosphere_strength"></a>

#### use\_cloud\_shadow\_on\_atmosphere\_strength

```python
@use_cloud_shadow_on_atmosphere_strength.setter
def use_cloud_shadow_on_atmosphere_strength(value: bool) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.cloud_shadow_on_atmosphere_strength"></a>

#### cloud\_shadow\_on\_atmosphere\_strength

```python
@property
def cloud_shadow_on_atmosphere_strength() -> float
```

(float):  [Read-Write] 大气上的阴影强度。设为0时禁用

<a id="unreal.SkyCreatorSunLightSettings_51.cloud_shadow_on_atmosphere_strength"></a>

#### cloud\_shadow\_on\_atmosphere\_strength

```python
@cloud_shadow_on_atmosphere_strength.setter
def cloud_shadow_on_atmosphere_strength(value: float) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.cloud_shadow_on_atmosphere_strength_curve"></a>

#### cloud\_shadow\_on\_atmosphere\_strength\_curve

```python
@property
def cloud_shadow_on_atmosphere_strength_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 大气上的阴影强度。设为0时禁用

<a id="unreal.SkyCreatorSunLightSettings_51.cloud_shadow_on_atmosphere_strength_curve"></a>

#### cloud\_shadow\_on\_atmosphere\_strength\_curve

```python
@cloud_shadow_on_atmosphere_strength_curve.setter
def cloud_shadow_on_atmosphere_strength_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.use_cloud_shadow_on_surface_strength"></a>

#### use\_cloud\_shadow\_on\_surface\_strength

```python
@property
def use_cloud_shadow_on_surface_strength() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSunLightSettings_51.use_cloud_shadow_on_surface_strength"></a>

#### use\_cloud\_shadow\_on\_surface\_strength

```python
@use_cloud_shadow_on_surface_strength.setter
def use_cloud_shadow_on_surface_strength(value: bool) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.cloud_shadow_on_surface_strength"></a>

#### cloud\_shadow\_on\_surface\_strength

```python
@property
def cloud_shadow_on_surface_strength() -> float
```

(float):  [Read-Write] 不透明和透明网格体上的阴影强度。设为0时禁用

<a id="unreal.SkyCreatorSunLightSettings_51.cloud_shadow_on_surface_strength"></a>

#### cloud\_shadow\_on\_surface\_strength

```python
@cloud_shadow_on_surface_strength.setter
def cloud_shadow_on_surface_strength(value: float) -> None
```

<a id="unreal.SkyCreatorSunLightSettings_51.cloud_shadow_on_surface_strength_curve"></a>

#### cloud\_shadow\_on\_surface\_strength\_curve

```python
@property
def cloud_shadow_on_surface_strength_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 不透明和透明网格体上的阴影强度。设为0时禁用

<a id="unreal.SkyCreatorSunLightSettings_51.cloud_shadow_on_surface_strength_curve"></a>

#### cloud\_shadow\_on\_surface\_strength\_curve

```python
@cloud_shadow_on_surface_strength_curve.setter
def cloud_shadow_on_surface_strength_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorMoonLightSettings_51"></a>