## SkyCreatorVolumetricCloudSettings Objects

```python
class SkyCreatorVolumetricCloudSettings(StructBase)
```

Sky Creator Volumetric Cloud Settings

**C++ Source:**

- **Plugin**: SkyCreatorPlugin
- **Module**: SkyCreatorPlugin
- **File**: SkyCreatorWeatherSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``albedo`` (LinearColor):  [Read-Write] Albedo color of Volumetric Cloudss.
- ``beers_powder_depth`` (float):  [Read-Write] Beer's Powder Depth.
- ``beers_powder_intensity`` (float):  [Read-Write] Beer's Powder Intensity.
- ``bottom_occlusion`` (float):  [Read-Write] Bottom Occlusion amount of the volumetric clouds. Affects only Cumulus and Cumulonimbus layers.
- ``bottom_occlusion_height`` (float):  [Read-Write] Normalized height of the Bottom Occlusion.
- ``cumulonimbus_anvil`` (float):  [Read-Write] Anvil factor of the Cumulonimbus cloud layer.
- ``cumulonimbus_coverage`` (float):  [Read-Write] Coverage of the Cumulonimbus cloud layer.
- ``cumulonimbus_height_variation`` (float):  [Read-Write] Height variation of the Cumulonimbus cloud layer.
- ``cumulus_coverage`` (float):  [Read-Write] Coverage of the Cumulus cloud layer.
- ``cumulus_coverage_variation`` (float):  [Read-Write] Coverage variation of the Cumulus cloud layer.
- ``cumulus_height_variation`` (float):  [Read-Write] Height variation of the Cumulus cloud layer.
- ``density_bottom`` (float):  [Read-Write] Density value of the bottom level of the Volumetric Clouds.
- ``density_middle`` (float):  [Read-Write] Density value of the middle level of the Volumetric Clouds.
- ``density_top`` (float):  [Read-Write] Density value of the top level of the Volumetric Clouds.
- ``ground_albedo`` (LinearColor):  [Read-Write] The ground albedo used to light the cloud from below with respect to the sun light and sky atmosphere.
  This is only used by the cloud material when the Ground Contribution is enabled from the Quality settings of Volumetric Clouds.
- ``multi_scattering_contribution`` (float):  [Read-Write] Multi-scattering approximation: represents how much contribution
  each successive octave will add. Evaluatead per pixel.
- ``multi_scattering_eccentricity`` (float):  [Read-Write] Multi-scattering approximation: represents how much the phase
  will become isotropic for each successive octave. Evaluatead per pixel.
- ``multi_scattering_occlusion`` (float):  [Read-Write] Multi-scattering approximation: represents how much occlussion
  will be reduced for each successive octave. Evaluatead per pixel.
- ``night_emissive`` (LinearColor):  [Read-Write] Emissive color of Volumetric Cloudss. Better to keep this value low.
- ``noise_shape_intensity_a`` (float):  [Read-Write] Desc.
- ``noise_shape_intensity_b`` (float):  [Read-Write] Desc.
- ``noise_shape_intensity_c`` (float):  [Read-Write] Desc.
- ``noise_shape_intensity_d`` (float):  [Read-Write] Desc.
- ``phase_blend`` (float):  [Read-Write] Lerp factor when blending the two phase functions.
- ``phase_g`` (float):  [Read-Write] Phase function describing how much forward (G < 0) of backward (G > 0) light scatter around.
- ``phase_g2`` (float):  [Read-Write] Second phase function describing how much forward (G < 0) of backward (G > 0) light scatter around.
- ``stratocumulus_coverage`` (float):  [Read-Write] Coverage of the Stratocumulus cloud layer.
- ``stratocumulus_coverage_variation`` (float):  [Read-Write] Coverage variation of the Stratocumulus cloud layer.
- ``stratocumulus_height_variation`` (float):  [Read-Write] Height variation of the Stratocumulus cloud layer.
- ``stratus_coverage`` (float):  [Read-Write] Coverage of the Stratus cloud layer.
- ``stratus_coverage_variation`` (float):  [Read-Write] Coverage variation of the Stratus cloud layer.
- ``stratus_height_variation`` (float):  [Read-Write] Height variation of the Stratus cloud layer.
- ``turbulence_intensity`` (float):  [Read-Write] Desc.

<a id="unreal.SkyCreatorVolumetricCloudSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(stratus_coverage: float = 0.000000,
             stratus_coverage_variation: float = 0.000000,
             stratus_height_variation: float = 0.000000,
             stratocumulus_coverage: float = 0.000000,
             stratocumulus_coverage_variation: float = 0.000000,
             stratocumulus_height_variation: float = 0.000000,
             cumulus_coverage: float = 0.000000,
             cumulus_coverage_variation: float = 0.000000,
             cumulus_height_variation: float = 0.000000,
             cumulonimbus_coverage: float = 0.000000,
             cumulonimbus_anvil: float = 0.000000,
             cumulonimbus_height_variation: float = 0.000000,
             density_bottom: float = 0.000000,
             density_middle: float = 0.000000,
             density_top: float = 0.000000,
             albedo: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             ground_albedo: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             beers_powder_intensity: float = 0.000000,
             beers_powder_depth: float = 0.000000,
             bottom_occlusion: float = 0.000000,
             bottom_occlusion_height: float = 0.000000,
             night_emissive: LinearColor = [
                 0.000000, 0.000000, 0.000000, 0.000000
             ],
             phase_g: float = 0.000000,
             phase_g2: float = 0.000000,
             phase_blend: float = 0.000000,
             multi_scattering_contribution: float = 0.000000,
             multi_scattering_occlusion: float = 0.000000,
             multi_scattering_eccentricity: float = 0.000000,
             noise_shape_intensity_a: float = 0.000000,
             noise_shape_intensity_b: float = 0.000000,
             noise_shape_intensity_c: float = 0.000000,
             noise_shape_intensity_d: float = 0.000000,
             turbulence_intensity: float = 0.000000) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.stratus_coverage"></a>

#### stratus\_coverage

```python
@property
def stratus_coverage() -> float
```

(float):  [Read-Write] Coverage of the Stratus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings.stratus_coverage"></a>

#### stratus\_coverage

```python
@stratus_coverage.setter
def stratus_coverage(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.stratus_coverage_variation"></a>

#### stratus\_coverage\_variation

```python
@property
def stratus_coverage_variation() -> float
```

(float):  [Read-Write] Coverage variation of the Stratus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings.stratus_coverage_variation"></a>

#### stratus\_coverage\_variation

```python
@stratus_coverage_variation.setter
def stratus_coverage_variation(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.stratus_height_variation"></a>

#### stratus\_height\_variation

```python
@property
def stratus_height_variation() -> float
```

(float):  [Read-Write] Height variation of the Stratus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings.stratus_height_variation"></a>

#### stratus\_height\_variation

```python
@stratus_height_variation.setter
def stratus_height_variation(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.stratocumulus_coverage"></a>

#### stratocumulus\_coverage

```python
@property
def stratocumulus_coverage() -> float
```

(float):  [Read-Write] Coverage of the Stratocumulus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings.stratocumulus_coverage"></a>

#### stratocumulus\_coverage

```python
@stratocumulus_coverage.setter
def stratocumulus_coverage(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.stratocumulus_coverage_variation"></a>

#### stratocumulus\_coverage\_variation

```python
@property
def stratocumulus_coverage_variation() -> float
```

(float):  [Read-Write] Coverage variation of the Stratocumulus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings.stratocumulus_coverage_variation"></a>

#### stratocumulus\_coverage\_variation

```python
@stratocumulus_coverage_variation.setter
def stratocumulus_coverage_variation(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.stratocumulus_height_variation"></a>

#### stratocumulus\_height\_variation

```python
@property
def stratocumulus_height_variation() -> float
```

(float):  [Read-Write] Height variation of the Stratocumulus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings.stratocumulus_height_variation"></a>

#### stratocumulus\_height\_variation

```python
@stratocumulus_height_variation.setter
def stratocumulus_height_variation(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.cumulus_coverage"></a>

#### cumulus\_coverage

```python
@property
def cumulus_coverage() -> float
```

(float):  [Read-Write] Coverage of the Cumulus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings.cumulus_coverage"></a>

#### cumulus\_coverage

```python
@cumulus_coverage.setter
def cumulus_coverage(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.cumulus_coverage_variation"></a>

#### cumulus\_coverage\_variation

```python
@property
def cumulus_coverage_variation() -> float
```

(float):  [Read-Write] Coverage variation of the Cumulus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings.cumulus_coverage_variation"></a>

#### cumulus\_coverage\_variation

```python
@cumulus_coverage_variation.setter
def cumulus_coverage_variation(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.cumulus_height_variation"></a>

#### cumulus\_height\_variation

```python
@property
def cumulus_height_variation() -> float
```

(float):  [Read-Write] Height variation of the Cumulus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings.cumulus_height_variation"></a>

#### cumulus\_height\_variation

```python
@cumulus_height_variation.setter
def cumulus_height_variation(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.cumulonimbus_coverage"></a>

#### cumulonimbus\_coverage

```python
@property
def cumulonimbus_coverage() -> float
```

(float):  [Read-Write] Coverage of the Cumulonimbus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings.cumulonimbus_coverage"></a>

#### cumulonimbus\_coverage

```python
@cumulonimbus_coverage.setter
def cumulonimbus_coverage(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.cumulonimbus_anvil"></a>

#### cumulonimbus\_anvil

```python
@property
def cumulonimbus_anvil() -> float
```

(float):  [Read-Write] Anvil factor of the Cumulonimbus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings.cumulonimbus_anvil"></a>

#### cumulonimbus\_anvil

```python
@cumulonimbus_anvil.setter
def cumulonimbus_anvil(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.cumulonimbus_height_variation"></a>

#### cumulonimbus\_height\_variation

```python
@property
def cumulonimbus_height_variation() -> float
```

(float):  [Read-Write] Height variation of the Cumulonimbus cloud layer.

<a id="unreal.SkyCreatorVolumetricCloudSettings.cumulonimbus_height_variation"></a>

#### cumulonimbus\_height\_variation

```python
@cumulonimbus_height_variation.setter
def cumulonimbus_height_variation(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.density_bottom"></a>

#### density\_bottom

```python
@property
def density_bottom() -> float
```

(float):  [Read-Write] Density value of the bottom level of the Volumetric Clouds.

<a id="unreal.SkyCreatorVolumetricCloudSettings.density_bottom"></a>

#### density\_bottom

```python
@density_bottom.setter
def density_bottom(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.density_middle"></a>

#### density\_middle

```python
@property
def density_middle() -> float
```

(float):  [Read-Write] Density value of the middle level of the Volumetric Clouds.

<a id="unreal.SkyCreatorVolumetricCloudSettings.density_middle"></a>

#### density\_middle

```python
@density_middle.setter
def density_middle(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.density_top"></a>

#### density\_top

```python
@property
def density_top() -> float
```

(float):  [Read-Write] Density value of the top level of the Volumetric Clouds.

<a id="unreal.SkyCreatorVolumetricCloudSettings.density_top"></a>

#### density\_top

```python
@density_top.setter
def density_top(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.albedo"></a>

#### albedo

```python
@property
def albedo() -> LinearColor
```

(LinearColor):  [Read-Write] Albedo color of Volumetric Cloudss.

<a id="unreal.SkyCreatorVolumetricCloudSettings.albedo"></a>

#### albedo

```python
@albedo.setter
def albedo(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.ground_albedo"></a>

#### ground\_albedo

```python
@property
def ground_albedo() -> LinearColor
```

(LinearColor):  [Read-Write] The ground albedo used to light the cloud from below with respect to the sun light and sky atmosphere.
This is only used by the cloud material when the Ground Contribution is enabled from the Quality settings of Volumetric Clouds.

<a id="unreal.SkyCreatorVolumetricCloudSettings.ground_albedo"></a>

#### ground\_albedo

```python
@ground_albedo.setter
def ground_albedo(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.beers_powder_intensity"></a>

#### beers\_powder\_intensity

```python
@property
def beers_powder_intensity() -> float
```

(float):  [Read-Write] Beer's Powder Intensity.

<a id="unreal.SkyCreatorVolumetricCloudSettings.beers_powder_intensity"></a>

#### beers\_powder\_intensity

```python
@beers_powder_intensity.setter
def beers_powder_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.beers_powder_depth"></a>

#### beers\_powder\_depth

```python
@property
def beers_powder_depth() -> float
```

(float):  [Read-Write] Beer's Powder Depth.

<a id="unreal.SkyCreatorVolumetricCloudSettings.beers_powder_depth"></a>

#### beers\_powder\_depth

```python
@beers_powder_depth.setter
def beers_powder_depth(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.bottom_occlusion"></a>

#### bottom\_occlusion

```python
@property
def bottom_occlusion() -> float
```

(float):  [Read-Write] Bottom Occlusion amount of the volumetric clouds. Affects only Cumulus and Cumulonimbus layers.

<a id="unreal.SkyCreatorVolumetricCloudSettings.bottom_occlusion"></a>

#### bottom\_occlusion

```python
@bottom_occlusion.setter
def bottom_occlusion(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.bottom_occlusion_height"></a>

#### bottom\_occlusion\_height

```python
@property
def bottom_occlusion_height() -> float
```

(float):  [Read-Write] Normalized height of the Bottom Occlusion.

<a id="unreal.SkyCreatorVolumetricCloudSettings.bottom_occlusion_height"></a>

#### bottom\_occlusion\_height

```python
@bottom_occlusion_height.setter
def bottom_occlusion_height(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.night_emissive"></a>

#### night\_emissive

```python
@property
def night_emissive() -> LinearColor
```

(LinearColor):  [Read-Write] Emissive color of Volumetric Cloudss. Better to keep this value low.

<a id="unreal.SkyCreatorVolumetricCloudSettings.night_emissive"></a>

#### night\_emissive

```python
@night_emissive.setter
def night_emissive(value: LinearColor) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.phase_g"></a>

#### phase\_g

```python
@property
def phase_g() -> float
```

(float):  [Read-Write] Phase function describing how much forward (G < 0) of backward (G > 0) light scatter around.

<a id="unreal.SkyCreatorVolumetricCloudSettings.phase_g"></a>

#### phase\_g

```python
@phase_g.setter
def phase_g(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.phase_g2"></a>

#### phase\_g2

```python
@property
def phase_g2() -> float
```

(float):  [Read-Write] Second phase function describing how much forward (G < 0) of backward (G > 0) light scatter around.

<a id="unreal.SkyCreatorVolumetricCloudSettings.phase_g2"></a>

#### phase\_g2

```python
@phase_g2.setter
def phase_g2(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.phase_blend"></a>

#### phase\_blend

```python
@property
def phase_blend() -> float
```

(float):  [Read-Write] Lerp factor when blending the two phase functions.

<a id="unreal.SkyCreatorVolumetricCloudSettings.phase_blend"></a>

#### phase\_blend

```python
@phase_blend.setter
def phase_blend(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.multi_scattering_contribution"></a>

#### multi\_scattering\_contribution

```python
@property
def multi_scattering_contribution() -> float
```

(float):  [Read-Write] Multi-scattering approximation: represents how much contribution
each successive octave will add. Evaluatead per pixel.

<a id="unreal.SkyCreatorVolumetricCloudSettings.multi_scattering_contribution"></a>

#### multi\_scattering\_contribution

```python
@multi_scattering_contribution.setter
def multi_scattering_contribution(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.multi_scattering_occlusion"></a>

#### multi\_scattering\_occlusion

```python
@property
def multi_scattering_occlusion() -> float
```

(float):  [Read-Write] Multi-scattering approximation: represents how much occlussion
will be reduced for each successive octave. Evaluatead per pixel.

<a id="unreal.SkyCreatorVolumetricCloudSettings.multi_scattering_occlusion"></a>

#### multi\_scattering\_occlusion

```python
@multi_scattering_occlusion.setter
def multi_scattering_occlusion(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.multi_scattering_eccentricity"></a>

#### multi\_scattering\_eccentricity

```python
@property
def multi_scattering_eccentricity() -> float
```

(float):  [Read-Write] Multi-scattering approximation: represents how much the phase
will become isotropic for each successive octave. Evaluatead per pixel.

<a id="unreal.SkyCreatorVolumetricCloudSettings.multi_scattering_eccentricity"></a>

#### multi\_scattering\_eccentricity

```python
@multi_scattering_eccentricity.setter
def multi_scattering_eccentricity(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.noise_shape_intensity_a"></a>

#### noise\_shape\_intensity\_a

```python
@property
def noise_shape_intensity_a() -> float
```

(float):  [Read-Write] Desc.

<a id="unreal.SkyCreatorVolumetricCloudSettings.noise_shape_intensity_a"></a>

#### noise\_shape\_intensity\_a

```python
@noise_shape_intensity_a.setter
def noise_shape_intensity_a(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.noise_shape_intensity_b"></a>

#### noise\_shape\_intensity\_b

```python
@property
def noise_shape_intensity_b() -> float
```

(float):  [Read-Write] Desc.

<a id="unreal.SkyCreatorVolumetricCloudSettings.noise_shape_intensity_b"></a>

#### noise\_shape\_intensity\_b

```python
@noise_shape_intensity_b.setter
def noise_shape_intensity_b(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.noise_shape_intensity_c"></a>

#### noise\_shape\_intensity\_c

```python
@property
def noise_shape_intensity_c() -> float
```

(float):  [Read-Write] Desc.

<a id="unreal.SkyCreatorVolumetricCloudSettings.noise_shape_intensity_c"></a>

#### noise\_shape\_intensity\_c

```python
@noise_shape_intensity_c.setter
def noise_shape_intensity_c(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.noise_shape_intensity_d"></a>

#### noise\_shape\_intensity\_d

```python
@property
def noise_shape_intensity_d() -> float
```

(float):  [Read-Write] Desc.

<a id="unreal.SkyCreatorVolumetricCloudSettings.noise_shape_intensity_d"></a>

#### noise\_shape\_intensity\_d

```python
@noise_shape_intensity_d.setter
def noise_shape_intensity_d(value: float) -> None
```

<a id="unreal.SkyCreatorVolumetricCloudSettings.turbulence_intensity"></a>

#### turbulence\_intensity

```python
@property
def turbulence_intensity() -> float
```

(float):  [Read-Write] Desc.

<a id="unreal.SkyCreatorVolumetricCloudSettings.turbulence_intensity"></a>

#### turbulence\_intensity

```python
@turbulence_intensity.setter
def turbulence_intensity(value: float) -> None
```

<a id="unreal.SkyCreatorBackgroundCloudSettings"></a>