## SkyCreatorExposureSettings\_51 Objects

```python
class SkyCreatorExposureSettings_51(StructBase)
```

后期设置

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings_51.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_exposure_bias`` (float):  [Read-Write] 曝光的对数调整。只在色调映射器指定时使用。
         0：无调整、-1:2x偏暗、1:2x偏亮、2:4x偏亮、以此类推······
- ``auto_exposure_bias_curve`` (CurveFloat):  [Read-Write] 曝光的对数调整。只在色调映射器指定时使用。
         0：无调整、-1:2x偏暗、1:2x偏亮、2:4x偏亮、以此类推······
- ``bloom_intensity`` (float):  [Read-Write]
- ``bloom_intensity_curve`` (CurveFloat):  [Read-Write]
- ``bloom_threshold`` (float):  [Read-Write]
- ``bloom_threshold_curve`` (CurveFloat):  [Read-Write]
- ``detail_strength`` (float):  [Read-Write]
- ``detail_strength_curve`` (CurveFloat):  [Read-Write]
- ``exposure_priority`` (float):  [Read-Write] 此后期体积的优先级，如果出现重叠，最高优先级的后台体积将重载低优先级的体积
         如果有两个或多个后期体积拥有相同的优先级，则无法定义排序
- ``exposure_priority_curve`` (CurveFloat):  [Read-Write] 此后期体积的优先级，如果出现重叠，最高优先级的后台体积将重载低优先级的体积
         如果有两个或多个后期体积拥有相同的优先级，则无法定义排序
- ``highlight_contrast_scale`` (float):  [Read-Write]
- ``highlight_contrast_scale_curve`` (CurveFloat):  [Read-Write]
- ``max_ev100`` (float):  [Read-Write] 自动曝光最大适应。如最小等于最小，眼部适应将被禁用
         自动曝光的实现方式是选择一个曝光值，平均亮度将根据此值生成与衡量标定值相等的像素明亮度。
         最大/最小以像素亮度（cd/m²）表示，使用ExtendDefaultLuminanceRange时（参见项目设置）则以EV100表示。
- ``max_ev100_curve`` (CurveFloat):  [Read-Write] 自动曝光最大适应。如最小等于最小，眼部适应将被禁用
         自动曝光的实现方式是选择一个曝光值，平均亮度将根据此值生成与衡量标定值相等的像素明亮度。
         最大/最小以像素亮度（cd/m²）表示，使用ExtendDefaultLuminanceRange时（参见项目设置）则以EV100表示。
- ``min_ev100`` (float):  [Read-Write] 自动曝光最小适应。如最小等于最大，眼部适应将被禁用
         自动曝光的实现方式是选择一个曝光值，平均亮度将根据此值生成与衡量标定值相等的像素明亮度。
         最大/最小以像素亮度（cd/m²）表示，使用ExtendDefaultLuminanceRange时（参见项目设置）则以EV100表示。
- ``min_ev100_curve`` (CurveFloat):  [Read-Write] 自动曝光最小适应。如最小等于最大，眼部适应将被禁用
         自动曝光的实现方式是选择一个曝光值，平均亮度将根据此值生成与衡量标定值相等的像素明亮度。
         最大/最小以像素亮度（cd/m²）表示，使用ExtendDefaultLuminanceRange时（参见项目设置）则以EV100表示。
- ``shadow_contrast_scale`` (float):  [Read-Write]
- ``shadow_contrast_scale_blend_curve`` (CurveFloat):  [Read-Write]
- ``shadow_contrast_scale_curve`` (CurveFloat):  [Read-Write]
- ``use_auto_exposure_bias`` (bool):  [Read-Write]
- ``use_auto_exposure_bias_override`` (bool):  [Read-Write]
- ``use_bloom_intensity`` (bool):  [Read-Write]
- ``use_bloom_intensity_override`` (bool):  [Read-Write]
- ``use_bloom_threshold`` (bool):  [Read-Write]
- ``use_bloom_threshold_override`` (bool):  [Read-Write]
- ``use_detail_strength`` (bool):  [Read-Write]
- ``use_detail_strength_override`` (bool):  [Read-Write]
- ``use_exposure_priority`` (bool):  [Read-Write]
- ``use_highlight_contrast_scale`` (bool):  [Read-Write]
- ``use_highlight_contrast_scale_override`` (bool):  [Read-Write]
- ``use_max_ev100`` (bool):  [Read-Write]
- ``use_max_ev100_override`` (bool):  [Read-Write]
- ``use_min_ev100`` (bool):  [Read-Write]
- ``use_min_ev100_override`` (bool):  [Read-Write]
- ``use_shadow_contrast_scale`` (bool):  [Read-Write]
- ``use_shadow_contrast_scale_override`` (bool):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.__init__"></a>

#### \_\_init\_\_

```python
def __init__(use_exposure_priority: bool = False,
             exposure_priority: float = 0.000000,
             exposure_priority_curve: CurveFloat = None,
             use_auto_exposure_bias_override: bool = False,
             use_auto_exposure_bias: bool = False,
             auto_exposure_bias: float = 0.000000,
             auto_exposure_bias_curve: CurveFloat = None,
             use_min_ev100_override: bool = False,
             use_min_ev100: bool = False,
             min_ev100: float = 0.000000,
             min_ev100_curve: CurveFloat = None,
             use_max_ev100_override: bool = False,
             use_max_ev100: bool = False,
             max_ev100: float = 0.000000,
             max_ev100_curve: CurveFloat = None,
             use_highlight_contrast_scale_override: bool = False,
             use_highlight_contrast_scale: bool = False,
             highlight_contrast_scale: float = 0.000000,
             highlight_contrast_scale_curve: CurveFloat = None,
             use_shadow_contrast_scale_override: bool = False,
             use_shadow_contrast_scale: bool = False,
             shadow_contrast_scale: float = 0.000000,
             shadow_contrast_scale_curve: CurveFloat = None,
             use_detail_strength_override: bool = False,
             use_detail_strength: bool = False,
             detail_strength: float = 0.000000,
             detail_strength_curve: CurveFloat = None,
             shadow_contrast_scale_blend_curve: CurveFloat = None,
             use_bloom_intensity_override: bool = False,
             use_bloom_intensity: bool = False,
             bloom_intensity: float = 0.000000,
             bloom_intensity_curve: CurveFloat = None,
             use_bloom_threshold_override: bool = False,
             use_bloom_threshold: bool = False,
             bloom_threshold: float = 0.000000,
             bloom_threshold_curve: CurveFloat = None) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.use_exposure_priority"></a>

#### use\_exposure\_priority

```python
@property
def use_exposure_priority() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.use_exposure_priority"></a>

#### use\_exposure\_priority

```python
@use_exposure_priority.setter
def use_exposure_priority(value: bool) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.exposure_priority"></a>

#### exposure\_priority

```python
@property
def exposure_priority() -> float
```

(float):  [Read-Write] 此后期体积的优先级，如果出现重叠，最高优先级的后台体积将重载低优先级的体积
       如果有两个或多个后期体积拥有相同的优先级，则无法定义排序

<a id="unreal.SkyCreatorExposureSettings_51.exposure_priority"></a>

#### exposure\_priority

```python
@exposure_priority.setter
def exposure_priority(value: float) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.exposure_priority_curve"></a>

#### exposure\_priority\_curve

```python
@property
def exposure_priority_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 此后期体积的优先级，如果出现重叠，最高优先级的后台体积将重载低优先级的体积
       如果有两个或多个后期体积拥有相同的优先级，则无法定义排序

<a id="unreal.SkyCreatorExposureSettings_51.exposure_priority_curve"></a>

#### exposure\_priority\_curve

```python
@exposure_priority_curve.setter
def exposure_priority_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.use_auto_exposure_bias_override"></a>

#### use\_auto\_exposure\_bias\_override

```python
@property
def use_auto_exposure_bias_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.use_auto_exposure_bias_override"></a>

#### use\_auto\_exposure\_bias\_override

```python
@use_auto_exposure_bias_override.setter
def use_auto_exposure_bias_override(value: bool) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.use_auto_exposure_bias"></a>

#### use\_auto\_exposure\_bias

```python
@property
def use_auto_exposure_bias() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.use_auto_exposure_bias"></a>

#### use\_auto\_exposure\_bias

```python
@use_auto_exposure_bias.setter
def use_auto_exposure_bias(value: bool) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.auto_exposure_bias"></a>

#### auto\_exposure\_bias

```python
@property
def auto_exposure_bias() -> float
```

(float):  [Read-Write] 曝光的对数调整。只在色调映射器指定时使用。
       0：无调整、-1:2x偏暗、1:2x偏亮、2:4x偏亮、以此类推······

<a id="unreal.SkyCreatorExposureSettings_51.auto_exposure_bias"></a>

#### auto\_exposure\_bias

```python
@auto_exposure_bias.setter
def auto_exposure_bias(value: float) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.auto_exposure_bias_curve"></a>

#### auto\_exposure\_bias\_curve

```python
@property
def auto_exposure_bias_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 曝光的对数调整。只在色调映射器指定时使用。
       0：无调整、-1:2x偏暗、1:2x偏亮、2:4x偏亮、以此类推······

<a id="unreal.SkyCreatorExposureSettings_51.auto_exposure_bias_curve"></a>

#### auto\_exposure\_bias\_curve

```python
@auto_exposure_bias_curve.setter
def auto_exposure_bias_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.use_min_ev100_override"></a>

#### use\_min\_ev100\_override

```python
@property
def use_min_ev100_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.use_min_ev100_override"></a>

#### use\_min\_ev100\_override

```python
@use_min_ev100_override.setter
def use_min_ev100_override(value: bool) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.use_min_ev100"></a>

#### use\_min\_ev100

```python
@property
def use_min_ev100() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.use_min_ev100"></a>

#### use\_min\_ev100

```python
@use_min_ev100.setter
def use_min_ev100(value: bool) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.min_ev100"></a>

#### min\_ev100

```python
@property
def min_ev100() -> float
```

(float):  [Read-Write] 自动曝光最小适应。如最小等于最大，眼部适应将被禁用
       自动曝光的实现方式是选择一个曝光值，平均亮度将根据此值生成与衡量标定值相等的像素明亮度。
       最大/最小以像素亮度（cd/m²）表示，使用ExtendDefaultLuminanceRange时（参见项目设置）则以EV100表示。

<a id="unreal.SkyCreatorExposureSettings_51.min_ev100"></a>

#### min\_ev100

```python
@min_ev100.setter
def min_ev100(value: float) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.min_ev100_curve"></a>

#### min\_ev100\_curve

```python
@property
def min_ev100_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 自动曝光最小适应。如最小等于最大，眼部适应将被禁用
       自动曝光的实现方式是选择一个曝光值，平均亮度将根据此值生成与衡量标定值相等的像素明亮度。
       最大/最小以像素亮度（cd/m²）表示，使用ExtendDefaultLuminanceRange时（参见项目设置）则以EV100表示。

<a id="unreal.SkyCreatorExposureSettings_51.min_ev100_curve"></a>

#### min\_ev100\_curve

```python
@min_ev100_curve.setter
def min_ev100_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.use_max_ev100_override"></a>

#### use\_max\_ev100\_override

```python
@property
def use_max_ev100_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.use_max_ev100_override"></a>

#### use\_max\_ev100\_override

```python
@use_max_ev100_override.setter
def use_max_ev100_override(value: bool) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.use_max_ev100"></a>

#### use\_max\_ev100

```python
@property
def use_max_ev100() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.use_max_ev100"></a>

#### use\_max\_ev100

```python
@use_max_ev100.setter
def use_max_ev100(value: bool) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.max_ev100"></a>

#### max\_ev100

```python
@property
def max_ev100() -> float
```

(float):  [Read-Write] 自动曝光最大适应。如最小等于最小，眼部适应将被禁用
       自动曝光的实现方式是选择一个曝光值，平均亮度将根据此值生成与衡量标定值相等的像素明亮度。
       最大/最小以像素亮度（cd/m²）表示，使用ExtendDefaultLuminanceRange时（参见项目设置）则以EV100表示。

<a id="unreal.SkyCreatorExposureSettings_51.max_ev100"></a>

#### max\_ev100

```python
@max_ev100.setter
def max_ev100(value: float) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.max_ev100_curve"></a>

#### max\_ev100\_curve

```python
@property
def max_ev100_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 自动曝光最大适应。如最小等于最小，眼部适应将被禁用
       自动曝光的实现方式是选择一个曝光值，平均亮度将根据此值生成与衡量标定值相等的像素明亮度。
       最大/最小以像素亮度（cd/m²）表示，使用ExtendDefaultLuminanceRange时（参见项目设置）则以EV100表示。

<a id="unreal.SkyCreatorExposureSettings_51.max_ev100_curve"></a>

#### max\_ev100\_curve

```python
@max_ev100_curve.setter
def max_ev100_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.use_highlight_contrast_scale_override"></a>

#### use\_highlight\_contrast\_scale\_override

```python
@property
def use_highlight_contrast_scale_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.use_highlight_contrast_scale_override"></a>

#### use\_highlight\_contrast\_scale\_override

```python
@use_highlight_contrast_scale_override.setter
def use_highlight_contrast_scale_override(value: bool) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.use_highlight_contrast_scale"></a>

#### use\_highlight\_contrast\_scale

```python
@property
def use_highlight_contrast_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.use_highlight_contrast_scale"></a>

#### use\_highlight\_contrast\_scale

```python
@use_highlight_contrast_scale.setter
def use_highlight_contrast_scale(value: bool) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.highlight_contrast_scale"></a>

#### highlight\_contrast\_scale

```python
@property
def highlight_contrast_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.highlight_contrast_scale"></a>

#### highlight\_contrast\_scale

```python
@highlight_contrast_scale.setter
def highlight_contrast_scale(value: float) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.highlight_contrast_scale_curve"></a>

#### highlight\_contrast\_scale\_curve

```python
@property
def highlight_contrast_scale_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.highlight_contrast_scale_curve"></a>

#### highlight\_contrast\_scale\_curve

```python
@highlight_contrast_scale_curve.setter
def highlight_contrast_scale_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.use_shadow_contrast_scale_override"></a>

#### use\_shadow\_contrast\_scale\_override

```python
@property
def use_shadow_contrast_scale_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.use_shadow_contrast_scale_override"></a>

#### use\_shadow\_contrast\_scale\_override

```python
@use_shadow_contrast_scale_override.setter
def use_shadow_contrast_scale_override(value: bool) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.use_shadow_contrast_scale"></a>

#### use\_shadow\_contrast\_scale

```python
@property
def use_shadow_contrast_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.use_shadow_contrast_scale"></a>

#### use\_shadow\_contrast\_scale

```python
@use_shadow_contrast_scale.setter
def use_shadow_contrast_scale(value: bool) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.shadow_contrast_scale"></a>

#### shadow\_contrast\_scale

```python
@property
def shadow_contrast_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.shadow_contrast_scale"></a>

#### shadow\_contrast\_scale

```python
@shadow_contrast_scale.setter
def shadow_contrast_scale(value: float) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.shadow_contrast_scale_curve"></a>

#### shadow\_contrast\_scale\_curve

```python
@property
def shadow_contrast_scale_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.shadow_contrast_scale_curve"></a>

#### shadow\_contrast\_scale\_curve

```python
@shadow_contrast_scale_curve.setter
def shadow_contrast_scale_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.use_detail_strength_override"></a>

#### use\_detail\_strength\_override

```python
@property
def use_detail_strength_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.use_detail_strength_override"></a>

#### use\_detail\_strength\_override

```python
@use_detail_strength_override.setter
def use_detail_strength_override(value: bool) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.use_detail_strength"></a>

#### use\_detail\_strength

```python
@property
def use_detail_strength() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.use_detail_strength"></a>

#### use\_detail\_strength

```python
@use_detail_strength.setter
def use_detail_strength(value: bool) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.detail_strength"></a>

#### detail\_strength

```python
@property
def detail_strength() -> float
```

(float):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.detail_strength"></a>

#### detail\_strength

```python
@detail_strength.setter
def detail_strength(value: float) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.detail_strength_curve"></a>

#### detail\_strength\_curve

```python
@property
def detail_strength_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.detail_strength_curve"></a>

#### detail\_strength\_curve

```python
@detail_strength_curve.setter
def detail_strength_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.shadow_contrast_scale_blend_curve"></a>

#### shadow\_contrast\_scale\_blend\_curve

```python
@property
def shadow_contrast_scale_blend_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.shadow_contrast_scale_blend_curve"></a>

#### shadow\_contrast\_scale\_blend\_curve

```python
@shadow_contrast_scale_blend_curve.setter
def shadow_contrast_scale_blend_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.use_bloom_intensity_override"></a>

#### use\_bloom\_intensity\_override

```python
@property
def use_bloom_intensity_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.use_bloom_intensity_override"></a>

#### use\_bloom\_intensity\_override

```python
@use_bloom_intensity_override.setter
def use_bloom_intensity_override(value: bool) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.use_bloom_intensity"></a>

#### use\_bloom\_intensity

```python
@property
def use_bloom_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.use_bloom_intensity"></a>

#### use\_bloom\_intensity

```python
@use_bloom_intensity.setter
def use_bloom_intensity(value: bool) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.bloom_intensity"></a>

#### bloom\_intensity

```python
@property
def bloom_intensity() -> float
```

(float):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.bloom_intensity"></a>

#### bloom\_intensity

```python
@bloom_intensity.setter
def bloom_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.bloom_intensity_curve"></a>

#### bloom\_intensity\_curve

```python
@property
def bloom_intensity_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.bloom_intensity_curve"></a>

#### bloom\_intensity\_curve

```python
@bloom_intensity_curve.setter
def bloom_intensity_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.use_bloom_threshold_override"></a>

#### use\_bloom\_threshold\_override

```python
@property
def use_bloom_threshold_override() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.use_bloom_threshold_override"></a>

#### use\_bloom\_threshold\_override

```python
@use_bloom_threshold_override.setter
def use_bloom_threshold_override(value: bool) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.use_bloom_threshold"></a>

#### use\_bloom\_threshold

```python
@property
def use_bloom_threshold() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.use_bloom_threshold"></a>

#### use\_bloom\_threshold

```python
@use_bloom_threshold.setter
def use_bloom_threshold(value: bool) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.bloom_threshold"></a>

#### bloom\_threshold

```python
@property
def bloom_threshold() -> float
```

(float):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.bloom_threshold"></a>

#### bloom\_threshold

```python
@bloom_threshold.setter
def bloom_threshold(value: float) -> None
```

<a id="unreal.SkyCreatorExposureSettings_51.bloom_threshold_curve"></a>

#### bloom\_threshold\_curve

```python
@property
def bloom_threshold_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorExposureSettings_51.bloom_threshold_curve"></a>

#### bloom\_threshold\_curve

```python
@bloom_threshold_curve.setter
def bloom_threshold_curve(value: CurveFloat) -> None
```

<a id="unreal.ExtendMPCSettings_51"></a>