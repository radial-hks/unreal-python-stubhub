## SkyCreatorVolumetricCloudSettings\_51 Objects

```python
class SkyCreatorVolumetricCloudSettings_51(StructBase)
```

体积云设置

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings_51.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``albedo`` (LinearColor):  [Read-Write] Albedo color of VolumetricClouds.
- ``albedo_curve`` (CurveLinearColor):  [Read-Write]
- ``beers_powder_depth`` (float):  [Read-Write] Beer's Powder Depth.
- ``beers_powder_depth_curve`` (CurveFloat):  [Read-Write]
- ``beers_powder_intensity`` (float):  [Read-Write] Beer's Powder Intensity.
- ``beers_powder_intensity_curve`` (CurveFloat):  [Read-Write]
- ``bottom_occlusion`` (float):  [Read-Write] Bottom Occlusion amount of the VolumetricCloud. Affects only Cumulus and Cumulonimbus layers.
- ``bottom_occlusion_curve`` (CurveFloat):  [Read-Write]
- ``bottom_occlusion_height`` (float):  [Read-Write] Normalized height of the Bottom Occlusion.
- ``bottom_occlusion_height_curve`` (CurveFloat):  [Read-Write]
- ``cumulonimbus_anvil`` (float):  [Read-Write] Anvil factor of the Cumulonimbus cloud layer.
- ``cumulonimbus_anvil_curve`` (CurveFloat):  [Read-Write]
- ``cumulonimbus_coverage`` (float):  [Read-Write] Coverage of the Cumulonimbus cloud layer.
- ``cumulonimbus_coverage_curve`` (CurveFloat):  [Read-Write]
- ``cumulonimbus_height_variation`` (float):  [Read-Write] Height variation of the Cumulonimbus cloud layer.
- ``cumulonimbus_height_variation_curve`` (CurveFloat):  [Read-Write]
- ``cumulus_coverage`` (float):  [Read-Write] Coverage of the Cumulus cloud layer.
- ``cumulus_coverage_curve`` (CurveFloat):  [Read-Write]
- ``cumulus_coverage_variation`` (float):  [Read-Write] Coverage variation of the Cumulus cloud layer.
- ``cumulus_coverage_variation_curve`` (CurveFloat):  [Read-Write]
- ``cumulus_height_variation`` (float):  [Read-Write] Height variation of the Cumulus cloud layer.
- ``cumulus_height_variation_curve`` (CurveFloat):  [Read-Write]
- ``density_bottom`` (float):  [Read-Write] Density value of the bottom level of the VolumetricCloud.
- ``density_bottom_curve`` (CurveFloat):  [Read-Write]
- ``density_middle`` (float):  [Read-Write] Density value of the middle level of the VolumetricCloud.
- ``density_middle_curve`` (CurveFloat):  [Read-Write]
- ``density_top`` (float):  [Read-Write] Density value of the top level of the VolumetricCloud.
- ``density_top_curve`` (CurveFloat):  [Read-Write]
- ``ground_albedo`` (LinearColor):  [Read-Write] The ground albedo used to light the cloud from below with respect to the sun light and sky atmosphere.
  This is only used by the cloud material when the Ground Contribution is enabled from the Quality settings of 体积云.
- ``ground_albedo_curve`` (CurveLinearColor):  [Read-Write]
- ``multi_scattering_contribution`` (float):  [Read-Write] Multi-scattering approximation: represents how much contribution
  each successive octave will add. Evaluatead per pixel.
- ``multi_scattering_contribution_curve`` (CurveFloat):  [Read-Write]
- ``multi_scattering_eccentricity`` (float):  [Read-Write] Multi-scattering approximation: represents how much the phase
  will become isotropic for each successive octave. Evaluatead per pixel.
- ``multi_scattering_eccentricity_curve`` (CurveFloat):  [Read-Write]
- ``multi_scattering_occlusion`` (float):  [Read-Write] Multi-scattering approximation: represents how much occlussion
  will be reduced for each successive octave. Evaluatead per pixel.
- ``multi_scattering_occlusion_curve`` (CurveFloat):  [Read-Write]
- ``night_emissive`` (LinearColor):  [Read-Write] Emissive color of VolumetricClouds. Better to keep this value low.
- ``night_emissive_curve`` (CurveLinearColor):  [Read-Write] FLinearColor(0.010725f, 0.015880f, 0.025000f);
- ``noise_shape_intensity_a`` (float):  [Read-Write] Desc.
- ``noise_shape_intensity_a_curve`` (CurveFloat):  [Read-Write]
- ``noise_shape_intensity_b`` (float):  [Read-Write] Desc.
- ``noise_shape_intensity_b_curve`` (CurveFloat):  [Read-Write]
- ``noise_shape_intensity_c`` (float):  [Read-Write] Desc.
- ``noise_shape_intensity_c_curve`` (CurveFloat):  [Read-Write]
- ``noise_shape_intensity_d`` (float):  [Read-Write] Desc.
- ``noise_shape_intensity_d_curve`` (CurveFloat):  [Read-Write]
- ``phase_blend`` (float):  [Read-Write] Lerp factor when blending the two phase functions.
- ``phase_blend_curve`` (CurveFloat):  [Read-Write]
- ``phase_g`` (float):  [Read-Write] Phase function describing how much forward (G < 0) of backward (G > 0) light scatter around.
- ``phase_g2`` (float):  [Read-Write] Second phase function describing how much forward (G < 0) of backward (G > 0) light scatter around.
- ``phase_g2_curve`` (CurveFloat):  [Read-Write]
- ``phase_g_curve`` (CurveFloat):  [Read-Write]
- ``stratocumulus_coverage`` (float):  [Read-Write] Coverage of the Stratocumulus cloud layer.
- ``stratocumulus_coverage_curve`` (CurveFloat):  [Read-Write]
- ``stratocumulus_coverage_variation`` (float):  [Read-Write] Coverage variation of the Stratocumulus cloud layer.
- ``stratocumulus_coverage_variation_curve`` (CurveFloat):  [Read-Write]
- ``stratocumulus_height_variation`` (float):  [Read-Write] Height variation of the Stratocumulus cloud layer.
- ``stratocumulus_height_variation_curve`` (CurveFloat):  [Read-Write]
- ``stratus_coverage`` (float):  [Read-Write] Coverage of the Stratus cloud layer.
- ``stratus_coverage_curve`` (CurveFloat):  [Read-Write]
- ``stratus_coverage_variation`` (float):  [Read-Write] Coverage variation of the Stratus cloud layer.
- ``stratus_coverage_variation_curve`` (CurveFloat):  [Read-Write]
- ``stratus_height_variation`` (float):  [Read-Write] Height variation of the Stratus cloud layer.
- ``stratus_height_variation_curve`` (CurveFloat):  [Read-Write]
- ``turbulence_intensity`` (float):  [Read-Write] Desc.
- ``turbulence_intensity_curve`` (CurveFloat):  [Read-Write]
- ``use_albedo`` (bool):  [Read-Write]
- ``use_beers_powder_depth`` (bool):  [Read-Write]
- ``use_beers_powder_intensity`` (bool):  [Read-Write]
- ``use_bottom_occlusion`` (bool):  [Read-Write]
- ``use_bottom_occlusion_height`` (bool):  [Read-Write]
- ``use_cumulonimbus_anvil`` (bool):  [Read-Write]
- ``use_cumulonimbus_coverage`` (bool):  [Read-Write]
- ``use_cumulonimbus_height_variation`` (bool):  [Read-Write]
- ``use_cumulus_coverage`` (bool):  [Read-Write]
- ``use_cumulus_coverage_variation`` (bool):  [Read-Write]
- ``use_cumulus_height_variation`` (bool):  [Read-Write]
- ``use_density_bottom`` (bool):  [Read-Write]
- ``use_density_middle`` (bool):  [Read-Write]
- ``use_density_top`` (bool):  [Read-Write]
- ``use_ground_albedo`` (bool):  [Read-Write]
- ``use_multi_scattering_contribution`` (bool):  [Read-Write]
- ``use_multi_scattering_eccentricity`` (bool):  [Read-Write]
- ``use_multi_scattering_occlusion`` (bool):  [Read-Write]
- ``use_night_emissive`` (bool):  [Read-Write]
- ``use_noise_shape_intensity_a`` (bool):  [Read-Write]
- ``use_noise_shape_intensity_b`` (bool):  [Read-Write]
- ``use_noise_shape_intensity_c`` (bool):  [Read-Write]
- ``use_noise_shape_intensity_d`` (bool):  [Read-Write]
- ``use_phase_blend`` (bool):  [Read-Write]
- ``use_phase_g`` (bool):  [Read-Write]
- ``use_phase_g2`` (bool):  [Read-Write]
- ``use_stratocumulus_coverage`` (bool):  [Read-Write]
- ``use_stratocumulus_coverage_variation`` (bool):  [Read-Write]
- ``use_stratocumulus_height_variation`` (bool):  [Read-Write]
- ``use_stratus_coverage`` (bool):  [Read-Write]
- ``use_stratus_coverage_variation`` (bool):  [Read-Write]
- ``use_stratus_height_variation`` (bool):  [Read-Write]
- ``use_turbulence_intensity`` (bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.__init__"></a>

#### \_\_init\_\_

```python
def __init__(use_stratus_coverage: bool = False,
             stratus_coverage: float = 0.000000,
             stratus_coverage_curve: CurveFloat = None,
             use_stratus_coverage_variation: bool = False,
             stratus_coverage_variation: float = 0.000000,
             stratus_coverage_variation_curve: CurveFloat = None,
             use_stratus_height_variation: bool = False,
             stratus_height_variation: float = 0.000000,
             stratus_height_variation_curve: CurveFloat = None,
             use_stratocumulus_coverage: bool = False,
             stratocumulus_coverage: float = 0.000000,
             stratocumulus_coverage_curve: CurveFloat = None,
             use_stratocumulus_coverage_variation: bool = False,
             stratocumulus_coverage_variation: float = 0.000000,
             stratocumulus_coverage_variation_curve: CurveFloat = None,
             use_stratocumulus_height_variation: bool = False,
             stratocumulus_height_variation: float = 0.000000,
             stratocumulus_height_variation_curve: CurveFloat = None,
             use_cumulus_coverage: bool = False,
             cumulus_coverage: float = 0.000000,
             cumulus_coverage_curve: CurveFloat = None,
             use_cumulus_coverage_variation: bool = False,
             cumulus_coverage_variation: float = 0.000000,
             cumulus_coverage_variation_curve: CurveFloat = None,
             use_cumulus_height_variation: bool = False,
             cumulus_height_variation: float = 0.000000,
             cumulus_height_variation_curve: CurveFloat = None,
             use_cumulonimbus_coverage: bool = False,
             cumulonimbus_coverage: float = 0.000000,
             cumulonimbus_coverage_curve: CurveFloat = None,
             use_cumulonimbus_anvil: bool = False,
             cumulonimbus_anvil: float = 0.000000,
             cumulonimbus_anvil_curve: CurveFloat = None,
             use_cumulonimbus_height_variation: bool = False,
             cumulonimbus_height_variation: float = 0.000000,
             cumulonimbus_height_variation_curve: CurveFloat = None,
             use_density_bottom: bool = False,
             density_bottom: float = 0.000000,
             density_bottom_curve: CurveFloat = None,
             use_density_middle: bool = False,
             density_middle: float = 0.000000,
             density_middle_curve: CurveFloat = None,
             use_density_top: bool = False,
             density_top: float = 0.000000,
             density_top_curve: CurveFloat = None,
             use_albedo: bool = False,
             albedo: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             albedo_curve: CurveLinearColor = None,
             use_ground_albedo: bool = False,
             ground_albedo: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             ground_albedo_curve: CurveLinearColor = None,
             use_beers_powder_intensity: bool = False,
             beers_powder_intensity: float = 0.000000,
             beers_powder_intensity_curve: CurveFloat = None,
             use_beers_powder_depth: bool = False,
             beers_powder_depth: float = 0.000000,
             beers_powder_depth_curve: CurveFloat = None,
             use_bottom_occlusion: bool = False,
             bottom_occlusion: float = 0.000000,
             bottom_occlusion_curve: CurveFloat = None,
             use_bottom_occlusion_height: bool = False,
             bottom_occlusion_height: float = 0.000000,
             bottom_occlusion_height_curve: CurveFloat = None,
             use_night_emissive: bool = False,
             night_emissive: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             night_emissive_curve: CurveLinearColor = None,
             use_phase_g: bool = False,
             phase_g: float = 0.000000,
             phase_g_curve: CurveFloat = None,
             use_phase_g2: bool = False,
             phase_g2: float = 0.000000,
             phase_g2_curve: CurveFloat = None,
             use_phase_blend: bool = False,
             phase_blend: float = 0.000000,
             phase_blend_curve: CurveFloat = None,
             use_multi_scattering_contribution: bool = False,
             multi_scattering_contribution: float = 0.000000,
             multi_scattering_contribution_curve: CurveFloat = None,
             use_multi_scattering_occlusion: bool = False,
             multi_scattering_occlusion: float = 0.000000,
             multi_scattering_occlusion_curve: CurveFloat = None,
             use_multi_scattering_eccentricity: bool = False,
             multi_scattering_eccentricity: float = 0.000000,
             multi_scattering_eccentricity_curve: CurveFloat = None,
             use_noise_shape_intensity_a: bool = False,
             noise_shape_intensity_a: float = 0.000000,
             noise_shape_intensity_a_curve: CurveFloat = None,
             use_noise_shape_intensity_b: bool = False,
             noise_shape_intensity_b: float = 0.000000,
             noise_shape_intensity_b_curve: CurveFloat = None,
             use_noise_shape_intensity_c: bool = False,
             noise_shape_intensity_c: float = 0.000000,
             noise_shape_intensity_c_curve: CurveFloat = None,
             use_noise_shape_intensity_d: bool = False,
             noise_shape_intensity_d: float = 0.000000,
             noise_shape_intensity_d_curve: CurveFloat = None,
             use_turbulence_intensity: bool = False,
             turbulence_intensity: float = 0.000000,
             turbulence_intensity_curve: CurveFloat = None) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_stratus_coverage"></a>

#### use\_stratus\_coverage

```python
@property
def use_stratus_coverage() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_stratus_coverage"></a>

#### use\_stratus\_coverage

```python
@use_stratus_coverage.setter
def use_stratus_coverage(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratus_coverage"></a>

#### stratus\_coverage

```python
@property
def stratus_coverage() -> float
```

(float):  [Read-Write] Coverage of the Stratus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratus_coverage"></a>

#### stratus\_coverage

```python
@stratus_coverage.setter
def stratus_coverage(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratus_coverage_curve"></a>

#### stratus\_coverage\_curve

```python
@property
def stratus_coverage_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratus_coverage_curve"></a>

#### stratus\_coverage\_curve

```python
@stratus_coverage_curve.setter
def stratus_coverage_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_stratus_coverage_variation"></a>

#### use\_stratus\_coverage\_variation

```python
@property
def use_stratus_coverage_variation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_stratus_coverage_variation"></a>

#### use\_stratus\_coverage\_variation

```python
@use_stratus_coverage_variation.setter
def use_stratus_coverage_variation(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratus_coverage_variation"></a>

#### stratus\_coverage\_variation

```python
@property
def stratus_coverage_variation() -> float
```

(float):  [Read-Write] Coverage variation of the Stratus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratus_coverage_variation"></a>

#### stratus\_coverage\_variation

```python
@stratus_coverage_variation.setter
def stratus_coverage_variation(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratus_coverage_variation_curve"></a>

#### stratus\_coverage\_variation\_curve

```python
@property
def stratus_coverage_variation_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratus_coverage_variation_curve"></a>

#### stratus\_coverage\_variation\_curve

```python
@stratus_coverage_variation_curve.setter
def stratus_coverage_variation_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_stratus_height_variation"></a>

#### use\_stratus\_height\_variation

```python
@property
def use_stratus_height_variation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_stratus_height_variation"></a>

#### use\_stratus\_height\_variation

```python
@use_stratus_height_variation.setter
def use_stratus_height_variation(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratus_height_variation"></a>

#### stratus\_height\_variation

```python
@property
def stratus_height_variation() -> float
```

(float):  [Read-Write] Height variation of the Stratus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratus_height_variation"></a>

#### stratus\_height\_variation

```python
@stratus_height_variation.setter
def stratus_height_variation(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratus_height_variation_curve"></a>

#### stratus\_height\_variation\_curve

```python
@property
def stratus_height_variation_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratus_height_variation_curve"></a>

#### stratus\_height\_variation\_curve

```python
@stratus_height_variation_curve.setter
def stratus_height_variation_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_stratocumulus_coverage"></a>

#### use\_stratocumulus\_coverage

```python
@property
def use_stratocumulus_coverage() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_stratocumulus_coverage"></a>

#### use\_stratocumulus\_coverage

```python
@use_stratocumulus_coverage.setter
def use_stratocumulus_coverage(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratocumulus_coverage"></a>

#### stratocumulus\_coverage

```python
@property
def stratocumulus_coverage() -> float
```

(float):  [Read-Write] Coverage of the Stratocumulus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratocumulus_coverage"></a>

#### stratocumulus\_coverage

```python
@stratocumulus_coverage.setter
def stratocumulus_coverage(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratocumulus_coverage_curve"></a>

#### stratocumulus\_coverage\_curve

```python
@property
def stratocumulus_coverage_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratocumulus_coverage_curve"></a>

#### stratocumulus\_coverage\_curve

```python
@stratocumulus_coverage_curve.setter
def stratocumulus_coverage_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_stratocumulus_coverage_variation"></a>

#### use\_stratocumulus\_coverage\_variation

```python
@property
def use_stratocumulus_coverage_variation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_stratocumulus_coverage_variation"></a>

#### use\_stratocumulus\_coverage\_variation

```python
@use_stratocumulus_coverage_variation.setter
def use_stratocumulus_coverage_variation(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratocumulus_coverage_variation"></a>

#### stratocumulus\_coverage\_variation

```python
@property
def stratocumulus_coverage_variation() -> float
```

(float):  [Read-Write] Coverage variation of the Stratocumulus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratocumulus_coverage_variation"></a>

#### stratocumulus\_coverage\_variation

```python
@stratocumulus_coverage_variation.setter
def stratocumulus_coverage_variation(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratocumulus_coverage_variation_curve"></a>

#### stratocumulus\_coverage\_variation\_curve

```python
@property
def stratocumulus_coverage_variation_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratocumulus_coverage_variation_curve"></a>

#### stratocumulus\_coverage\_variation\_curve

```python
@stratocumulus_coverage_variation_curve.setter
def stratocumulus_coverage_variation_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_stratocumulus_height_variation"></a>

#### use\_stratocumulus\_height\_variation

```python
@property
def use_stratocumulus_height_variation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_stratocumulus_height_variation"></a>

#### use\_stratocumulus\_height\_variation

```python
@use_stratocumulus_height_variation.setter
def use_stratocumulus_height_variation(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratocumulus_height_variation"></a>

#### stratocumulus\_height\_variation

```python
@property
def stratocumulus_height_variation() -> float
```

(float):  [Read-Write] Height variation of the Stratocumulus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratocumulus_height_variation"></a>

#### stratocumulus\_height\_variation

```python
@stratocumulus_height_variation.setter
def stratocumulus_height_variation(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratocumulus_height_variation_curve"></a>

#### stratocumulus\_height\_variation\_curve

```python
@property
def stratocumulus_height_variation_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.stratocumulus_height_variation_curve"></a>

#### stratocumulus\_height\_variation\_curve

```python
@stratocumulus_height_variation_curve.setter
def stratocumulus_height_variation_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_cumulus_coverage"></a>

#### use\_cumulus\_coverage

```python
@property
def use_cumulus_coverage() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_cumulus_coverage"></a>

#### use\_cumulus\_coverage

```python
@use_cumulus_coverage.setter
def use_cumulus_coverage(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulus_coverage"></a>

#### cumulus\_coverage

```python
@property
def cumulus_coverage() -> float
```

(float):  [Read-Write] Coverage of the Cumulus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulus_coverage"></a>

#### cumulus\_coverage

```python
@cumulus_coverage.setter
def cumulus_coverage(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulus_coverage_curve"></a>

#### cumulus\_coverage\_curve

```python
@property
def cumulus_coverage_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulus_coverage_curve"></a>

#### cumulus\_coverage\_curve

```python
@cumulus_coverage_curve.setter
def cumulus_coverage_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_cumulus_coverage_variation"></a>

#### use\_cumulus\_coverage\_variation

```python
@property
def use_cumulus_coverage_variation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_cumulus_coverage_variation"></a>

#### use\_cumulus\_coverage\_variation

```python
@use_cumulus_coverage_variation.setter
def use_cumulus_coverage_variation(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulus_coverage_variation"></a>

#### cumulus\_coverage\_variation

```python
@property
def cumulus_coverage_variation() -> float
```

(float):  [Read-Write] Coverage variation of the Cumulus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulus_coverage_variation"></a>

#### cumulus\_coverage\_variation

```python
@cumulus_coverage_variation.setter
def cumulus_coverage_variation(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulus_coverage_variation_curve"></a>

#### cumulus\_coverage\_variation\_curve

```python
@property
def cumulus_coverage_variation_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulus_coverage_variation_curve"></a>

#### cumulus\_coverage\_variation\_curve

```python
@cumulus_coverage_variation_curve.setter
def cumulus_coverage_variation_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_cumulus_height_variation"></a>

#### use\_cumulus\_height\_variation

```python
@property
def use_cumulus_height_variation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_cumulus_height_variation"></a>

#### use\_cumulus\_height\_variation

```python
@use_cumulus_height_variation.setter
def use_cumulus_height_variation(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulus_height_variation"></a>

#### cumulus\_height\_variation

```python
@property
def cumulus_height_variation() -> float
```

(float):  [Read-Write] Height variation of the Cumulus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulus_height_variation"></a>

#### cumulus\_height\_variation

```python
@cumulus_height_variation.setter
def cumulus_height_variation(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulus_height_variation_curve"></a>

#### cumulus\_height\_variation\_curve

```python
@property
def cumulus_height_variation_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulus_height_variation_curve"></a>

#### cumulus\_height\_variation\_curve

```python
@cumulus_height_variation_curve.setter
def cumulus_height_variation_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_cumulonimbus_coverage"></a>

#### use\_cumulonimbus\_coverage

```python
@property
def use_cumulonimbus_coverage() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_cumulonimbus_coverage"></a>

#### use\_cumulonimbus\_coverage

```python
@use_cumulonimbus_coverage.setter
def use_cumulonimbus_coverage(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulonimbus_coverage"></a>

#### cumulonimbus\_coverage

```python
@property
def cumulonimbus_coverage() -> float
```

(float):  [Read-Write] Coverage of the Cumulonimbus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulonimbus_coverage"></a>

#### cumulonimbus\_coverage

```python
@cumulonimbus_coverage.setter
def cumulonimbus_coverage(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulonimbus_coverage_curve"></a>

#### cumulonimbus\_coverage\_curve

```python
@property
def cumulonimbus_coverage_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulonimbus_coverage_curve"></a>

#### cumulonimbus\_coverage\_curve

```python
@cumulonimbus_coverage_curve.setter
def cumulonimbus_coverage_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_cumulonimbus_anvil"></a>

#### use\_cumulonimbus\_anvil

```python
@property
def use_cumulonimbus_anvil() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_cumulonimbus_anvil"></a>

#### use\_cumulonimbus\_anvil

```python
@use_cumulonimbus_anvil.setter
def use_cumulonimbus_anvil(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulonimbus_anvil"></a>

#### cumulonimbus\_anvil

```python
@property
def cumulonimbus_anvil() -> float
```

(float):  [Read-Write] Anvil factor of the Cumulonimbus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulonimbus_anvil"></a>

#### cumulonimbus\_anvil

```python
@cumulonimbus_anvil.setter
def cumulonimbus_anvil(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulonimbus_anvil_curve"></a>

#### cumulonimbus\_anvil\_curve

```python
@property
def cumulonimbus_anvil_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulonimbus_anvil_curve"></a>

#### cumulonimbus\_anvil\_curve

```python
@cumulonimbus_anvil_curve.setter
def cumulonimbus_anvil_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_cumulonimbus_height_variation"></a>

#### use\_cumulonimbus\_height\_variation

```python
@property
def use_cumulonimbus_height_variation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_cumulonimbus_height_variation"></a>

#### use\_cumulonimbus\_height\_variation

```python
@use_cumulonimbus_height_variation.setter
def use_cumulonimbus_height_variation(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulonimbus_height_variation"></a>

#### cumulonimbus\_height\_variation

```python
@property
def cumulonimbus_height_variation() -> float
```

(float):  [Read-Write] Height variation of the Cumulonimbus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulonimbus_height_variation"></a>

#### cumulonimbus\_height\_variation

```python
@cumulonimbus_height_variation.setter
def cumulonimbus_height_variation(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulonimbus_height_variation_curve"></a>

#### cumulonimbus\_height\_variation\_curve

```python
@property
def cumulonimbus_height_variation_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.cumulonimbus_height_variation_curve"></a>

#### cumulonimbus\_height\_variation\_curve

```python
@cumulonimbus_height_variation_curve.setter
def cumulonimbus_height_variation_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_density_bottom"></a>

#### use\_density\_bottom

```python
@property
def use_density_bottom() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_density_bottom"></a>

#### use\_density\_bottom

```python
@use_density_bottom.setter
def use_density_bottom(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.density_bottom"></a>

#### density\_bottom

```python
@property
def density_bottom() -> float
```

(float):  [Read-Write] Density value of the bottom level of the VolumetricCloud.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.density_bottom"></a>

#### density\_bottom

```python
@density_bottom.setter
def density_bottom(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.density_bottom_curve"></a>

#### density\_bottom\_curve

```python
@property
def density_bottom_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.density_bottom_curve"></a>

#### density\_bottom\_curve

```python
@density_bottom_curve.setter
def density_bottom_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_density_middle"></a>

#### use\_density\_middle

```python
@property
def use_density_middle() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_density_middle"></a>

#### use\_density\_middle

```python
@use_density_middle.setter
def use_density_middle(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.density_middle"></a>

#### density\_middle

```python
@property
def density_middle() -> float
```

(float):  [Read-Write] Density value of the middle level of the VolumetricCloud.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.density_middle"></a>

#### density\_middle

```python
@density_middle.setter
def density_middle(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.density_middle_curve"></a>

#### density\_middle\_curve

```python
@property
def density_middle_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.density_middle_curve"></a>

#### density\_middle\_curve

```python
@density_middle_curve.setter
def density_middle_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_density_top"></a>

#### use\_density\_top

```python
@property
def use_density_top() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_density_top"></a>

#### use\_density\_top

```python
@use_density_top.setter
def use_density_top(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.density_top"></a>

#### density\_top

```python
@property
def density_top() -> float
```

(float):  [Read-Write] Density value of the top level of the VolumetricCloud.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.density_top"></a>

#### density\_top

```python
@density_top.setter
def density_top(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.density_top_curve"></a>

#### density\_top\_curve

```python
@property
def density_top_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.density_top_curve"></a>

#### density\_top\_curve

```python
@density_top_curve.setter
def density_top_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_albedo"></a>

#### use\_albedo

```python
@property
def use_albedo() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_albedo"></a>

#### use\_albedo

```python
@use_albedo.setter
def use_albedo(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.albedo"></a>

#### albedo

```python
@property
def albedo() -> LinearColor
```

(LinearColor):  [Read-Write] Albedo color of VolumetricClouds.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.albedo"></a>

#### albedo

```python
@albedo.setter
def albedo(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.albedo_curve"></a>

#### albedo\_curve

```python
@property
def albedo_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.albedo_curve"></a>

#### albedo\_curve

```python
@albedo_curve.setter
def albedo_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_ground_albedo"></a>

#### use\_ground\_albedo

```python
@property
def use_ground_albedo() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_ground_albedo"></a>

#### use\_ground\_albedo

```python
@use_ground_albedo.setter
def use_ground_albedo(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.ground_albedo"></a>

#### ground\_albedo

```python
@property
def ground_albedo() -> LinearColor
```

(LinearColor):  [Read-Write] The ground albedo used to light the cloud from below with respect to the sun light and sky atmosphere.
This is only used by the cloud material when the Ground Contribution is enabled from the Quality settings of 体积云.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.ground_albedo"></a>

#### ground\_albedo

```python
@ground_albedo.setter
def ground_albedo(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.ground_albedo_curve"></a>

#### ground\_albedo\_curve

```python
@property
def ground_albedo_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.ground_albedo_curve"></a>

#### ground\_albedo\_curve

```python
@ground_albedo_curve.setter
def ground_albedo_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_beers_powder_intensity"></a>

#### use\_beers\_powder\_intensity

```python
@property
def use_beers_powder_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_beers_powder_intensity"></a>

#### use\_beers\_powder\_intensity

```python
@use_beers_powder_intensity.setter
def use_beers_powder_intensity(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.beers_powder_intensity"></a>

#### beers\_powder\_intensity

```python
@property
def beers_powder_intensity() -> float
```

(float):  [Read-Write] Beer's Powder Intensity.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.beers_powder_intensity"></a>

#### beers\_powder\_intensity

```python
@beers_powder_intensity.setter
def beers_powder_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.beers_powder_intensity_curve"></a>

#### beers\_powder\_intensity\_curve

```python
@property
def beers_powder_intensity_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.beers_powder_intensity_curve"></a>

#### beers\_powder\_intensity\_curve

```python
@beers_powder_intensity_curve.setter
def beers_powder_intensity_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_beers_powder_depth"></a>

#### use\_beers\_powder\_depth

```python
@property
def use_beers_powder_depth() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_beers_powder_depth"></a>

#### use\_beers\_powder\_depth

```python
@use_beers_powder_depth.setter
def use_beers_powder_depth(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.beers_powder_depth"></a>

#### beers\_powder\_depth

```python
@property
def beers_powder_depth() -> float
```

(float):  [Read-Write] Beer's Powder Depth.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.beers_powder_depth"></a>

#### beers\_powder\_depth

```python
@beers_powder_depth.setter
def beers_powder_depth(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.beers_powder_depth_curve"></a>

#### beers\_powder\_depth\_curve

```python
@property
def beers_powder_depth_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.beers_powder_depth_curve"></a>

#### beers\_powder\_depth\_curve

```python
@beers_powder_depth_curve.setter
def beers_powder_depth_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_bottom_occlusion"></a>

#### use\_bottom\_occlusion

```python
@property
def use_bottom_occlusion() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_bottom_occlusion"></a>

#### use\_bottom\_occlusion

```python
@use_bottom_occlusion.setter
def use_bottom_occlusion(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.bottom_occlusion"></a>

#### bottom\_occlusion

```python
@property
def bottom_occlusion() -> float
```

(float):  [Read-Write] Bottom Occlusion amount of the VolumetricCloud. Affects only Cumulus and Cumulonimbus layers.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.bottom_occlusion"></a>

#### bottom\_occlusion

```python
@bottom_occlusion.setter
def bottom_occlusion(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.bottom_occlusion_curve"></a>

#### bottom\_occlusion\_curve

```python
@property
def bottom_occlusion_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.bottom_occlusion_curve"></a>

#### bottom\_occlusion\_curve

```python
@bottom_occlusion_curve.setter
def bottom_occlusion_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_bottom_occlusion_height"></a>

#### use\_bottom\_occlusion\_height

```python
@property
def use_bottom_occlusion_height() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_bottom_occlusion_height"></a>

#### use\_bottom\_occlusion\_height

```python
@use_bottom_occlusion_height.setter
def use_bottom_occlusion_height(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.bottom_occlusion_height"></a>

#### bottom\_occlusion\_height

```python
@property
def bottom_occlusion_height() -> float
```

(float):  [Read-Write] Normalized height of the Bottom Occlusion.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.bottom_occlusion_height"></a>

#### bottom\_occlusion\_height

```python
@bottom_occlusion_height.setter
def bottom_occlusion_height(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.bottom_occlusion_height_curve"></a>

#### bottom\_occlusion\_height\_curve

```python
@property
def bottom_occlusion_height_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.bottom_occlusion_height_curve"></a>

#### bottom\_occlusion\_height\_curve

```python
@bottom_occlusion_height_curve.setter
def bottom_occlusion_height_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_night_emissive"></a>

#### use\_night\_emissive

```python
@property
def use_night_emissive() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_night_emissive"></a>

#### use\_night\_emissive

```python
@use_night_emissive.setter
def use_night_emissive(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.night_emissive"></a>

#### night\_emissive

```python
@property
def night_emissive() -> LinearColor
```

(LinearColor):  [Read-Write] Emissive color of VolumetricClouds. Better to keep this value low.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.night_emissive"></a>

#### night\_emissive

```python
@night_emissive.setter
def night_emissive(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.night_emissive_curve"></a>

#### night\_emissive\_curve

```python
@property
def night_emissive_curve() -> CurveLinearColor
```

(CurveLinearColor):  [Read-Write] FLinearColor(0.010725f, 0.015880f, 0.025000f);

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.night_emissive_curve"></a>

#### night\_emissive\_curve

```python
@night_emissive_curve.setter
def night_emissive_curve(value: CurveLinearColor) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_phase_g"></a>

#### use\_phase\_g

```python
@property
def use_phase_g() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_phase_g"></a>

#### use\_phase\_g

```python
@use_phase_g.setter
def use_phase_g(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.phase_g"></a>

#### phase\_g

```python
@property
def phase_g() -> float
```

(float):  [Read-Write] Phase function describing how much forward (G < 0) of backward (G > 0) light scatter around.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.phase_g"></a>

#### phase\_g

```python
@phase_g.setter
def phase_g(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.phase_g_curve"></a>

#### phase\_g\_curve

```python
@property
def phase_g_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.phase_g_curve"></a>

#### phase\_g\_curve

```python
@phase_g_curve.setter
def phase_g_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_phase_g2"></a>

#### use\_phase\_g2

```python
@property
def use_phase_g2() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_phase_g2"></a>

#### use\_phase\_g2

```python
@use_phase_g2.setter
def use_phase_g2(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.phase_g2"></a>

#### phase\_g2

```python
@property
def phase_g2() -> float
```

(float):  [Read-Write] Second phase function describing how much forward (G < 0) of backward (G > 0) light scatter around.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.phase_g2"></a>

#### phase\_g2

```python
@phase_g2.setter
def phase_g2(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.phase_g2_curve"></a>

#### phase\_g2\_curve

```python
@property
def phase_g2_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.phase_g2_curve"></a>

#### phase\_g2\_curve

```python
@phase_g2_curve.setter
def phase_g2_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_phase_blend"></a>

#### use\_phase\_blend

```python
@property
def use_phase_blend() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_phase_blend"></a>

#### use\_phase\_blend

```python
@use_phase_blend.setter
def use_phase_blend(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.phase_blend"></a>

#### phase\_blend

```python
@property
def phase_blend() -> float
```

(float):  [Read-Write] Lerp factor when blending the two phase functions.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.phase_blend"></a>

#### phase\_blend

```python
@phase_blend.setter
def phase_blend(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.phase_blend_curve"></a>

#### phase\_blend\_curve

```python
@property
def phase_blend_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.phase_blend_curve"></a>

#### phase\_blend\_curve

```python
@phase_blend_curve.setter
def phase_blend_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_multi_scattering_contribution"></a>

#### use\_multi\_scattering\_contribution

```python
@property
def use_multi_scattering_contribution() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_multi_scattering_contribution"></a>

#### use\_multi\_scattering\_contribution

```python
@use_multi_scattering_contribution.setter
def use_multi_scattering_contribution(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.multi_scattering_contribution"></a>

#### multi\_scattering\_contribution

```python
@property
def multi_scattering_contribution() -> float
```

(float):  [Read-Write] Multi-scattering approximation: represents how much contribution
each successive octave will add. Evaluatead per pixel.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.multi_scattering_contribution"></a>

#### multi\_scattering\_contribution

```python
@multi_scattering_contribution.setter
def multi_scattering_contribution(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.multi_scattering_contribution_curve"></a>

#### multi\_scattering\_contribution\_curve

```python
@property
def multi_scattering_contribution_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.multi_scattering_contribution_curve"></a>

#### multi\_scattering\_contribution\_curve

```python
@multi_scattering_contribution_curve.setter
def multi_scattering_contribution_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_multi_scattering_occlusion"></a>

#### use\_multi\_scattering\_occlusion

```python
@property
def use_multi_scattering_occlusion() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_multi_scattering_occlusion"></a>

#### use\_multi\_scattering\_occlusion

```python
@use_multi_scattering_occlusion.setter
def use_multi_scattering_occlusion(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.multi_scattering_occlusion"></a>

#### multi\_scattering\_occlusion

```python
@property
def multi_scattering_occlusion() -> float
```

(float):  [Read-Write] Multi-scattering approximation: represents how much occlussion
will be reduced for each successive octave. Evaluatead per pixel.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.multi_scattering_occlusion"></a>

#### multi\_scattering\_occlusion

```python
@multi_scattering_occlusion.setter
def multi_scattering_occlusion(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.multi_scattering_occlusion_curve"></a>

#### multi\_scattering\_occlusion\_curve

```python
@property
def multi_scattering_occlusion_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.multi_scattering_occlusion_curve"></a>

#### multi\_scattering\_occlusion\_curve

```python
@multi_scattering_occlusion_curve.setter
def multi_scattering_occlusion_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_multi_scattering_eccentricity"></a>

#### use\_multi\_scattering\_eccentricity

```python
@property
def use_multi_scattering_eccentricity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_multi_scattering_eccentricity"></a>

#### use\_multi\_scattering\_eccentricity

```python
@use_multi_scattering_eccentricity.setter
def use_multi_scattering_eccentricity(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.multi_scattering_eccentricity"></a>

#### multi\_scattering\_eccentricity

```python
@property
def multi_scattering_eccentricity() -> float
```

(float):  [Read-Write] Multi-scattering approximation: represents how much the phase
will become isotropic for each successive octave. Evaluatead per pixel.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.multi_scattering_eccentricity"></a>

#### multi\_scattering\_eccentricity

```python
@multi_scattering_eccentricity.setter
def multi_scattering_eccentricity(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.multi_scattering_eccentricity_curve"></a>

#### multi\_scattering\_eccentricity\_curve

```python
@property
def multi_scattering_eccentricity_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.multi_scattering_eccentricity_curve"></a>

#### multi\_scattering\_eccentricity\_curve

```python
@multi_scattering_eccentricity_curve.setter
def multi_scattering_eccentricity_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_noise_shape_intensity_a"></a>

#### use\_noise\_shape\_intensity\_a

```python
@property
def use_noise_shape_intensity_a() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_noise_shape_intensity_a"></a>

#### use\_noise\_shape\_intensity\_a

```python
@use_noise_shape_intensity_a.setter
def use_noise_shape_intensity_a(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_a"></a>

#### noise\_shape\_intensity\_a

```python
@property
def noise_shape_intensity_a() -> float
```

(float):  [Read-Write] Desc.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_a"></a>

#### noise\_shape\_intensity\_a

```python
@noise_shape_intensity_a.setter
def noise_shape_intensity_a(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_a_curve"></a>

#### noise\_shape\_intensity\_a\_curve

```python
@property
def noise_shape_intensity_a_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_a_curve"></a>

#### noise\_shape\_intensity\_a\_curve

```python
@noise_shape_intensity_a_curve.setter
def noise_shape_intensity_a_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_noise_shape_intensity_b"></a>

#### use\_noise\_shape\_intensity\_b

```python
@property
def use_noise_shape_intensity_b() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_noise_shape_intensity_b"></a>

#### use\_noise\_shape\_intensity\_b

```python
@use_noise_shape_intensity_b.setter
def use_noise_shape_intensity_b(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_b"></a>

#### noise\_shape\_intensity\_b

```python
@property
def noise_shape_intensity_b() -> float
```

(float):  [Read-Write] Desc.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_b"></a>

#### noise\_shape\_intensity\_b

```python
@noise_shape_intensity_b.setter
def noise_shape_intensity_b(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_b_curve"></a>

#### noise\_shape\_intensity\_b\_curve

```python
@property
def noise_shape_intensity_b_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_b_curve"></a>

#### noise\_shape\_intensity\_b\_curve

```python
@noise_shape_intensity_b_curve.setter
def noise_shape_intensity_b_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_noise_shape_intensity_c"></a>

#### use\_noise\_shape\_intensity\_c

```python
@property
def use_noise_shape_intensity_c() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_noise_shape_intensity_c"></a>

#### use\_noise\_shape\_intensity\_c

```python
@use_noise_shape_intensity_c.setter
def use_noise_shape_intensity_c(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_c"></a>

#### noise\_shape\_intensity\_c

```python
@property
def noise_shape_intensity_c() -> float
```

(float):  [Read-Write] Desc.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_c"></a>

#### noise\_shape\_intensity\_c

```python
@noise_shape_intensity_c.setter
def noise_shape_intensity_c(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_c_curve"></a>

#### noise\_shape\_intensity\_c\_curve

```python
@property
def noise_shape_intensity_c_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_c_curve"></a>

#### noise\_shape\_intensity\_c\_curve

```python
@noise_shape_intensity_c_curve.setter
def noise_shape_intensity_c_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_noise_shape_intensity_d"></a>

#### use\_noise\_shape\_intensity\_d

```python
@property
def use_noise_shape_intensity_d() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_noise_shape_intensity_d"></a>

#### use\_noise\_shape\_intensity\_d

```python
@use_noise_shape_intensity_d.setter
def use_noise_shape_intensity_d(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_d"></a>

#### noise\_shape\_intensity\_d

```python
@property
def noise_shape_intensity_d() -> float
```

(float):  [Read-Write] Desc.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_d"></a>

#### noise\_shape\_intensity\_d

```python
@noise_shape_intensity_d.setter
def noise_shape_intensity_d(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_d_curve"></a>

#### noise\_shape\_intensity\_d\_curve

```python
@property
def noise_shape_intensity_d_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.noise_shape_intensity_d_curve"></a>

#### noise\_shape\_intensity\_d\_curve

```python
@noise_shape_intensity_d_curve.setter
def noise_shape_intensity_d_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_turbulence_intensity"></a>

#### use\_turbulence\_intensity

```python
@property
def use_turbulence_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.use_turbulence_intensity"></a>

#### use\_turbulence\_intensity

```python
@use_turbulence_intensity.setter
def use_turbulence_intensity(value: bool) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.turbulence_intensity"></a>

#### turbulence\_intensity

```python
@property
def turbulence_intensity() -> float
```

(float):  [Read-Write] Desc.

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.turbulence_intensity"></a>

#### turbulence\_intensity

```python
@turbulence_intensity.setter
def turbulence_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.turbulence_intensity_curve"></a>

#### turbulence\_intensity\_curve

```python
@property
def turbulence_intensity_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write]

<a id="unreal.SkyCreatorVolumetricCloudSettings_51.turbulence_intensity_curve"></a>

#### turbulence\_intensity\_curve

```python
@turbulence_intensity_curve.setter
def turbulence_intensity_curve(value: CurveFloat) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings_51"></a>