## SkyCreatorSkyAtmosphereSettings\_51 Objects

```python
class SkyCreatorSkyAtmosphereSettings_51(StructBase)
```

大气设置

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings_51.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absorption`` (LinearColor):  [Read-Write] 另一大气图层的吸收系数。
  密度将在10到25公里之间，以0到1范围增加；在25公里到40公里之间，以1到0范围降低。
  默认值代表地球大气中的臭氧分子吸收
- ``absorption_curve`` (CurveLinearColor):  [Read-Write] 另一大气图层的吸收系数。
  密度将在10到25公里之间，以0到1范围增加；在25公里到40公里之间，以1到0范围降低。
  默认值代表地球大气中的臭氧分子吸收
- ``absorption_scale`` (float):  [Read-Write] 另一大气图层的吸收系数。
  密度将在10到25公里之间，以0到1范围增加；在25公里到40公里之间，以1到0范围降低。
  此值类似于地球大气中的臭氧分子吸收
- ``absorption_scale_curve`` (CurveFloat):  [Read-Write] 另一大气图层的吸收系数。
  密度将在10到25公里之间，以0到1范围增加；在25公里到40公里之间，以1到0范围降低。
  此值类似于地球大气中的臭氧分子吸收
- ``ground_albedo`` (LinearColor):  [Read-Write] The ground albedo that will tint the astmophere when the sun light will bounce on it.
  Only taken into account when MultiScattering > 0.0.
- ``ground_albedo_curve`` (CurveLinearColor):  [Read-Write]
- ``height_fog_contribution`` (float):  [Read-Write] SupportSkyAtmosphereAffectsHeightFog 项目设置为true时，将天空和大气贡献缩放到高度雾
- ``height_fog_contribution_curve`` (CurveFloat):  [Read-Write] SupportSkyAtmosphereAffectsHeightFog 项目设置为true时，将天空和大气贡献缩放到高度雾
- ``mie_absorption`` (LinearColor):  [Read-Write] 高度为0公里处，由空气粒子产生的米氏吸收系数
  该系数越高，光源吸收越多
- ``mie_absorption_curve`` (CurveLinearColor):  [Read-Write] 高度为0公里处，由空气粒子产生的米氏吸收系数
  该系数越高，光源吸收越多
- ``mie_absorption_scale`` (float):  [Read-Write] 米氏吸收系数范围
- ``mie_absorption_scale_curve`` (CurveFloat):  [Read-Write] 米氏吸收系数范围
- ``mie_anisotropy`` (float):  [Read-Write] 值为0时意味统一散射光源
  接近1的值为光源将向前散射，导致围绕光源的光晕
- ``mie_anisotropy_curve`` (CurveFloat):  [Read-Write] 值为0时意味统一散射光源
  接近1的值为光源将向前散射，导致围绕光源的光晕
- ``mie_exponential_distribution`` (float):  [Read-Write] 米氏效应降低到40%处的高度（以公里计）
- ``mie_exponential_distribution_curve`` (CurveFloat):  [Read-Write] 米氏效应降低到40%处的高度（以公里计）
- ``mie_scattering`` (LinearColor):  [Read-Write] 高度为0公里处，由空气粒子产生的米氏散射系数
  该系数越高，光源散射越多
- ``mie_scattering_curve`` (CurveLinearColor):  [Read-Write] 高度为0公里处，由空气粒子产生的米氏散射系数
  该系数越高，光源散射越多
- ``mie_scattering_scale`` (float):  [Read-Write] 米氏散射系数范围
- ``mie_scattering_scale_curve`` (CurveFloat):  [Read-Write] 米氏散射系数范围
- ``rayleigh_exponential_distribution`` (float):  [Read-Write] 瑞利散射效应降低到40%处的高度（以公里计）
- ``rayleigh_exponential_distribution_curve`` (CurveFloat):  [Read-Write] 瑞利散射效应降低到40%处的高度（以公里计）
- ``rayleigh_scattering`` (LinearColor):  [Read-Write] 高度0公里处的空气分子产生的瑞利散射系数
- ``rayleigh_scattering_curve`` (CurveLinearColor):  [Read-Write] 高度0公里处的空气分子产生的瑞利散射系数
- ``rayleigh_scattering_scale`` (float):  [Read-Write] 瑞利散射系数范围
- ``rayleigh_scattering_scale_curve`` (CurveFloat):  [Read-Write] 瑞利散射系数范围
- ``sky_luminance_factor`` (LinearColor):  [Read-Write] 代表天空的像素亮度范围，即不属于任何表面
- ``sky_luminance_factor_curve`` (CurveLinearColor):  [Read-Write] 代表天空的像素亮度范围，即不属于任何表面
- ``use_absorption`` (bool):  [Read-Write]
- ``use_absorption_scale`` (bool):  [Read-Write]
- ``use_ground_albedo`` (bool):  [Read-Write]
- ``use_height_fog_contribution`` (bool):  [Read-Write]
- ``use_mie_absorption`` (bool):  [Read-Write]
- ``use_mie_absorption_scale`` (bool):  [Read-Write]
- ``use_mie_anisotropy`` (bool):  [Read-Write]
- ``use_mie_exponential_distribution`` (bool):  [Read-Write]
- ``use_mie_scattering`` (bool):  [Read-Write]
- ``use_mie_scattering_scale`` (bool):  [Read-Write]
- ``use_rayleigh_exponential_distribution`` (bool):  [Read-Write]
- ``use_rayleigh_scattering`` (bool):  [Read-Write]
- ``use_rayleigh_scattering_scale`` (bool):  [Read-Write]
- ``use_sky_luminance_factor`` (bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.__init__"></a>

#### \_\_init\_\_

```python
def __init__(use_rayleigh_scattering_scale: bool = False,
             rayleigh_scattering_scale: float = 0.000000,
             rayleigh_scattering_scale_curve: CurveFloat = None,
             use_rayleigh_scattering: bool = False,
             rayleigh_scattering: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             rayleigh_scattering_curve: CurveLinearColor = None,
             use_rayleigh_exponential_distribution: bool = False,
             rayleigh_exponential_distribution: float = 0.000000,
             rayleigh_exponential_distribution_curve: CurveFloat = None,
             use_mie_scattering_scale: bool = False,
             mie_scattering_scale: float = 0.000000,
             mie_scattering_scale_curve: CurveFloat = None,
             use_mie_scattering: bool = False,
             mie_scattering: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             mie_scattering_curve: CurveLinearColor = None,
             use_mie_absorption_scale: bool = False,
             mie_absorption_scale: float = 0.000000,
             mie_absorption_scale_curve: CurveFloat = None,
             use_mie_absorption: bool = False,
             mie_absorption: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             mie_absorption_curve: CurveLinearColor = None,
             use_mie_anisotropy: bool = False,
             mie_anisotropy: float = 0.000000,
             mie_anisotropy_curve: CurveFloat = None,
             use_mie_exponential_distribution: bool = False,
             mie_exponential_distribution: float = 0.000000,
             mie_exponential_distribution_curve: CurveFloat = None,
             use_absorption_scale: bool = False,
             absorption_scale: float = 0.000000,
             absorption_scale_curve: CurveFloat = None,
             use_absorption: bool = False,
             absorption: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             absorption_curve: CurveLinearColor = None,
             use_sky_luminance_factor: bool = False,
             sky_luminance_factor: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             sky_luminance_factor_curve: CurveLinearColor = None,
             use_ground_albedo: bool = False,
             ground_albedo: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             ground_albedo_curve: CurveLinearColor = None,
             use_height_fog_contribution: bool = False,
             height_fog_contribution: float = 0.000000,
             height_fog_contribution_curve: CurveFloat = None) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_rayleigh_scattering_scale"></a>

#### use\_rayleigh\_scattering\_scale

```python
@property
def use_rayleigh_scattering_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_rayleigh_scattering_scale"></a>

#### use\_rayleigh\_scattering\_scale

```python
@use_rayleigh_scattering_scale.setter
def use_rayleigh_scattering_scale(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.rayleigh_scattering_scale"></a>

#### rayleigh\_scattering\_scale

```python
@property
def rayleigh_scattering_scale() -> float
```

(float):  [Read-Write] 瑞利散射系数范围

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.rayleigh_scattering_scale"></a>

#### rayleigh\_scattering\_scale

```python
@rayleigh_scattering_scale.setter
def rayleigh_scattering_scale(value: float) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.rayleigh_scattering_scale_curve"></a>

#### rayleigh\_scattering\_scale\_curve

```python
@property
def rayleigh_scattering_scale_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 瑞利散射系数范围

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.rayleigh_scattering_scale_curve"></a>

#### rayleigh\_scattering\_scale\_curve

```python
@rayleigh_scattering_scale_curve.setter
def rayleigh_scattering_scale_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_rayleigh_scattering"></a>

#### use\_rayleigh\_scattering

```python
@property
def use_rayleigh_scattering() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_rayleigh_scattering"></a>

#### use\_rayleigh\_scattering

```python
@use_rayleigh_scattering.setter
def use_rayleigh_scattering(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.rayleigh_scattering"></a>

#### rayleigh\_scattering

```python
@property
def rayleigh_scattering() -> LinearColor
```

(LinearColor):  [Read-Write] 高度0公里处的空气分子产生的瑞利散射系数

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.rayleigh_scattering"></a>

#### rayleigh\_scattering

```python
@rayleigh_scattering.setter
def rayleigh_scattering(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.rayleigh_scattering_curve"></a>

#### rayleigh\_scattering\_curve

```python
@property
def rayleigh_scattering_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write] 高度0公里处的空气分子产生的瑞利散射系数

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.rayleigh_scattering_curve"></a>

#### rayleigh\_scattering\_curve

```python
@rayleigh_scattering_curve.setter
def rayleigh_scattering_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_rayleigh_exponential_distribution"></a>

#### use\_rayleigh\_exponential\_distribution

```python
@property
def use_rayleigh_exponential_distribution() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_rayleigh_exponential_distribution"></a>

#### use\_rayleigh\_exponential\_distribution

```python
@use_rayleigh_exponential_distribution.setter
def use_rayleigh_exponential_distribution(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.rayleigh_exponential_distribution"></a>

#### rayleigh\_exponential\_distribution

```python
@property
def rayleigh_exponential_distribution() -> float
```

(float):  [Read-Write] 瑞利散射效应降低到40%处的高度（以公里计）

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.rayleigh_exponential_distribution"></a>

#### rayleigh\_exponential\_distribution

```python
@rayleigh_exponential_distribution.setter
def rayleigh_exponential_distribution(value: float) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.rayleigh_exponential_distribution_curve"></a>

#### rayleigh\_exponential\_distribution\_curve

```python
@property
def rayleigh_exponential_distribution_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 瑞利散射效应降低到40%处的高度（以公里计）

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.rayleigh_exponential_distribution_curve"></a>

#### rayleigh\_exponential\_distribution\_curve

```python
@rayleigh_exponential_distribution_curve.setter
def rayleigh_exponential_distribution_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_mie_scattering_scale"></a>

#### use\_mie\_scattering\_scale

```python
@property
def use_mie_scattering_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_mie_scattering_scale"></a>

#### use\_mie\_scattering\_scale

```python
@use_mie_scattering_scale.setter
def use_mie_scattering_scale(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_scattering_scale"></a>

#### mie\_scattering\_scale

```python
@property
def mie_scattering_scale() -> float
```

(float):  [Read-Write] 米氏散射系数范围

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_scattering_scale"></a>

#### mie\_scattering\_scale

```python
@mie_scattering_scale.setter
def mie_scattering_scale(value: float) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_scattering_scale_curve"></a>

#### mie\_scattering\_scale\_curve

```python
@property
def mie_scattering_scale_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 米氏散射系数范围

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_scattering_scale_curve"></a>

#### mie\_scattering\_scale\_curve

```python
@mie_scattering_scale_curve.setter
def mie_scattering_scale_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_mie_scattering"></a>

#### use\_mie\_scattering

```python
@property
def use_mie_scattering() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_mie_scattering"></a>

#### use\_mie\_scattering

```python
@use_mie_scattering.setter
def use_mie_scattering(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_scattering"></a>

#### mie\_scattering

```python
@property
def mie_scattering() -> LinearColor
```

(LinearColor):  [Read-Write] 高度为0公里处，由空气粒子产生的米氏散射系数
该系数越高，光源散射越多

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_scattering"></a>

#### mie\_scattering

```python
@mie_scattering.setter
def mie_scattering(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_scattering_curve"></a>

#### mie\_scattering\_curve

```python
@property
def mie_scattering_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write] 高度为0公里处，由空气粒子产生的米氏散射系数
该系数越高，光源散射越多

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_scattering_curve"></a>

#### mie\_scattering\_curve

```python
@mie_scattering_curve.setter
def mie_scattering_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_mie_absorption_scale"></a>

#### use\_mie\_absorption\_scale

```python
@property
def use_mie_absorption_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_mie_absorption_scale"></a>

#### use\_mie\_absorption\_scale

```python
@use_mie_absorption_scale.setter
def use_mie_absorption_scale(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_absorption_scale"></a>

#### mie\_absorption\_scale

```python
@property
def mie_absorption_scale() -> float
```

(float):  [Read-Write] 米氏吸收系数范围

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_absorption_scale"></a>

#### mie\_absorption\_scale

```python
@mie_absorption_scale.setter
def mie_absorption_scale(value: float) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_absorption_scale_curve"></a>

#### mie\_absorption\_scale\_curve

```python
@property
def mie_absorption_scale_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 米氏吸收系数范围

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_absorption_scale_curve"></a>

#### mie\_absorption\_scale\_curve

```python
@mie_absorption_scale_curve.setter
def mie_absorption_scale_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_mie_absorption"></a>

#### use\_mie\_absorption

```python
@property
def use_mie_absorption() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_mie_absorption"></a>

#### use\_mie\_absorption

```python
@use_mie_absorption.setter
def use_mie_absorption(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_absorption"></a>

#### mie\_absorption

```python
@property
def mie_absorption() -> LinearColor
```

(LinearColor):  [Read-Write] 高度为0公里处，由空气粒子产生的米氏吸收系数
该系数越高，光源吸收越多

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_absorption"></a>

#### mie\_absorption

```python
@mie_absorption.setter
def mie_absorption(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_absorption_curve"></a>

#### mie\_absorption\_curve

```python
@property
def mie_absorption_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write] 高度为0公里处，由空气粒子产生的米氏吸收系数
该系数越高，光源吸收越多

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_absorption_curve"></a>

#### mie\_absorption\_curve

```python
@mie_absorption_curve.setter
def mie_absorption_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_mie_anisotropy"></a>

#### use\_mie\_anisotropy

```python
@property
def use_mie_anisotropy() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_mie_anisotropy"></a>

#### use\_mie\_anisotropy

```python
@use_mie_anisotropy.setter
def use_mie_anisotropy(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_anisotropy"></a>

#### mie\_anisotropy

```python
@property
def mie_anisotropy() -> float
```

(float):  [Read-Write] 值为0时意味统一散射光源
接近1的值为光源将向前散射，导致围绕光源的光晕

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_anisotropy"></a>

#### mie\_anisotropy

```python
@mie_anisotropy.setter
def mie_anisotropy(value: float) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_anisotropy_curve"></a>

#### mie\_anisotropy\_curve

```python
@property
def mie_anisotropy_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 值为0时意味统一散射光源
接近1的值为光源将向前散射，导致围绕光源的光晕

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_anisotropy_curve"></a>

#### mie\_anisotropy\_curve

```python
@mie_anisotropy_curve.setter
def mie_anisotropy_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_mie_exponential_distribution"></a>

#### use\_mie\_exponential\_distribution

```python
@property
def use_mie_exponential_distribution() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_mie_exponential_distribution"></a>

#### use\_mie\_exponential\_distribution

```python
@use_mie_exponential_distribution.setter
def use_mie_exponential_distribution(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_exponential_distribution"></a>

#### mie\_exponential\_distribution

```python
@property
def mie_exponential_distribution() -> float
```

(float):  [Read-Write] 米氏效应降低到40%处的高度（以公里计）

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_exponential_distribution"></a>

#### mie\_exponential\_distribution

```python
@mie_exponential_distribution.setter
def mie_exponential_distribution(value: float) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_exponential_distribution_curve"></a>

#### mie\_exponential\_distribution\_curve

```python
@property
def mie_exponential_distribution_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 米氏效应降低到40%处的高度（以公里计）

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.mie_exponential_distribution_curve"></a>

#### mie\_exponential\_distribution\_curve

```python
@mie_exponential_distribution_curve.setter
def mie_exponential_distribution_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_absorption_scale"></a>

#### use\_absorption\_scale

```python
@property
def use_absorption_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_absorption_scale"></a>

#### use\_absorption\_scale

```python
@use_absorption_scale.setter
def use_absorption_scale(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.absorption_scale"></a>

#### absorption\_scale

```python
@property
def absorption_scale() -> float
```

(float):  [Read-Write] 另一大气图层的吸收系数。
密度将在10到25公里之间，以0到1范围增加；在25公里到40公里之间，以1到0范围降低。
此值类似于地球大气中的臭氧分子吸收

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.absorption_scale"></a>

#### absorption\_scale

```python
@absorption_scale.setter
def absorption_scale(value: float) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.absorption_scale_curve"></a>

#### absorption\_scale\_curve

```python
@property
def absorption_scale_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] 另一大气图层的吸收系数。
密度将在10到25公里之间，以0到1范围增加；在25公里到40公里之间，以1到0范围降低。
此值类似于地球大气中的臭氧分子吸收

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.absorption_scale_curve"></a>

#### absorption\_scale\_curve

```python
@absorption_scale_curve.setter
def absorption_scale_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_absorption"></a>

#### use\_absorption

```python
@property
def use_absorption() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_absorption"></a>

#### use\_absorption

```python
@use_absorption.setter
def use_absorption(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.absorption"></a>

#### absorption

```python
@property
def absorption() -> LinearColor
```

(LinearColor):  [Read-Write] 另一大气图层的吸收系数。
密度将在10到25公里之间，以0到1范围增加；在25公里到40公里之间，以1到0范围降低。
默认值代表地球大气中的臭氧分子吸收

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.absorption"></a>

#### absorption

```python
@absorption.setter
def absorption(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.absorption_curve"></a>

#### absorption\_curve

```python
@property
def absorption_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write] 另一大气图层的吸收系数。
密度将在10到25公里之间，以0到1范围增加；在25公里到40公里之间，以1到0范围降低。
默认值代表地球大气中的臭氧分子吸收

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.absorption_curve"></a>

#### absorption\_curve

```python
@absorption_curve.setter
def absorption_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_sky_luminance_factor"></a>

#### use\_sky\_luminance\_factor

```python
@property
def use_sky_luminance_factor() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_sky_luminance_factor"></a>

#### use\_sky\_luminance\_factor

```python
@use_sky_luminance_factor.setter
def use_sky_luminance_factor(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.sky_luminance_factor"></a>

#### sky\_luminance\_factor

```python
@property
def sky_luminance_factor() -> LinearColor
```

(LinearColor):  [Read-Write] 代表天空的像素亮度范围，即不属于任何表面

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.sky_luminance_factor"></a>

#### sky\_luminance\_factor

```python
@sky_luminance_factor.setter
def sky_luminance_factor(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.sky_luminance_factor_curve"></a>

#### sky\_luminance\_factor\_curve

```python
@property
def sky_luminance_factor_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write] 代表天空的像素亮度范围，即不属于任何表面

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.sky_luminance_factor_curve"></a>

#### sky\_luminance\_factor\_curve

```python
@sky_luminance_factor_curve.setter
def sky_luminance_factor_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_ground_albedo"></a>

#### use\_ground\_albedo

```python
@property
def use_ground_albedo() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_ground_albedo"></a>

#### use\_ground\_albedo

```python
@use_ground_albedo.setter
def use_ground_albedo(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.ground_albedo"></a>

#### ground\_albedo

```python
@property
def ground_albedo() -> LinearColor
```

(LinearColor):  [Read-Write] The ground albedo that will tint the astmophere when the sun light will bounce on it.
Only taken into account when MultiScattering > 0.0.

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.ground_albedo"></a>

#### ground\_albedo

```python
@ground_albedo.setter
def ground_albedo(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.ground_albedo_curve"></a>

#### ground\_albedo\_curve

```python
@property
def ground_albedo_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write]

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.ground_albedo_curve"></a>

#### ground\_albedo\_curve

```python
@ground_albedo_curve.setter
def ground_albedo_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_height_fog_contribution"></a>

#### use\_height\_fog\_contribution

```python
@property
def use_height_fog_contribution() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.use_height_fog_contribution"></a>

#### use\_height\_fog\_contribution

```python
@use_height_fog_contribution.setter
def use_height_fog_contribution(value: bool) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.height_fog_contribution"></a>

#### height\_fog\_contribution

```python
@property
def height_fog_contribution() -> float
```

(float):  [Read-Write] SupportSkyAtmosphereAffectsHeightFog 项目设置为true时，将天空和大气贡献缩放到高度雾

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.height_fog_contribution"></a>

#### height\_fog\_contribution

```python
@height_fog_contribution.setter
def height_fog_contribution(value: float) -> None
```

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.height_fog_contribution_curve"></a>

#### height\_fog\_contribution\_curve

```python
@property
def height_fog_contribution_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] SupportSkyAtmosphereAffectsHeightFog 项目设置为true时，将天空和大气贡献缩放到高度雾

<a id="unreal.SkyCreatorSkyAtmosphereSettings_51.height_fog_contribution_curve"></a>

#### height\_fog\_contribution\_curve

```python
@height_fog_contribution_curve.setter
def height_fog_contribution_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51"></a>