## GroomBuildSettings Objects

```python
class GroomBuildSettings(StructBase)
```

Groom Build Settings

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``hair_to_guide_density`` (float):  [Read-Write] Density factor for converting hair into guide curve if no guides are provided.
- ``interpolation_distance`` (GroomInterpolationWeight):  [Read-Write] Interpolation distance metric.
- ``interpolation_quality`` (GroomInterpolationQuality):  [Read-Write] Interpolation data quality.
- ``override_guides`` (bool):  [Read-Write] If checked, override imported guides with generated ones.
- ``randomize_guide`` (bool):  [Read-Write] Randomize which guides affect a given hair strand.
- ``use_unique_guide`` (bool):  [Read-Write] Force a hair strand to be affected by a unique guide.

<a id="unreal.GroomBuildSettings.__init__"></a>

#### __init__

```python
def __init__(override_guides: bool = False,
             hair_to_guide_density: float = 0.000000,
             interpolation_quality:
             GroomInterpolationQuality = GroomInterpolationQuality.LOW,
             interpolation_distance:
             GroomInterpolationWeight = GroomInterpolationWeight.PARAMETRIC,
             randomize_guide: bool = False,
             use_unique_guide: bool = False) -> None
```

<a id="unreal.GroomBuildSettings.override_guides"></a>

#### override_guides

```python
@property
def override_guides() -> bool
```

(bool):  [Read-Write] If checked, override imported guides with generated ones.

<a id="unreal.GroomBuildSettings.override_guides"></a>

#### override_guides

```python
@override_guides.setter
def override_guides(value: bool) -> None
```

<a id="unreal.GroomBuildSettings.hair_to_guide_density"></a>

#### hair_to_guide_density

```python
@property
def hair_to_guide_density() -> float
```

(float):  [Read-Write] Density factor for converting hair into guide curve if no guides are provided.

<a id="unreal.GroomBuildSettings.hair_to_guide_density"></a>

#### hair_to_guide_density

```python
@hair_to_guide_density.setter
def hair_to_guide_density(value: float) -> None
```

<a id="unreal.GroomBuildSettings.interpolation_quality"></a>

#### interpolation_quality

```python
@property
def interpolation_quality() -> GroomInterpolationQuality
```

(GroomInterpolationQuality):  [Read-Write] Interpolation data quality.

<a id="unreal.GroomBuildSettings.interpolation_quality"></a>

#### interpolation_quality

```python
@interpolation_quality.setter
def interpolation_quality(value: GroomInterpolationQuality) -> None
```

<a id="unreal.GroomBuildSettings.interpolation_distance"></a>

#### interpolation_distance

```python
@property
def interpolation_distance() -> GroomInterpolationWeight
```

(GroomInterpolationWeight):  [Read-Write] Interpolation distance metric.

<a id="unreal.GroomBuildSettings.interpolation_distance"></a>

#### interpolation_distance

```python
@interpolation_distance.setter
def interpolation_distance(value: GroomInterpolationWeight) -> None
```

<a id="unreal.GroomBuildSettings.randomize_guide"></a>

#### randomize_guide

```python
@property
def randomize_guide() -> bool
```

(bool):  [Read-Write] Randomize which guides affect a given hair strand.

<a id="unreal.GroomBuildSettings.randomize_guide"></a>

#### randomize_guide

```python
@randomize_guide.setter
def randomize_guide(value: bool) -> None
```

<a id="unreal.GroomBuildSettings.use_unique_guide"></a>

#### use_unique_guide

```python
@property
def use_unique_guide() -> bool
```

(bool):  [Read-Write] Force a hair strand to be affected by a unique guide.

<a id="unreal.GroomBuildSettings.use_unique_guide"></a>

#### use_unique_guide

```python
@use_unique_guide.setter
def use_unique_guide(value: bool) -> None
```

<a id="unreal.OpenCVArucoDetectedMarker"></a>