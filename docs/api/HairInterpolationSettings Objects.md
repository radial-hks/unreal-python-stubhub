## HairInterpolationSettings Objects

```python
class HairInterpolationSettings(StructBase)
```

Hair Interpolation Settings

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomAssetInterpolation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guide_type`` (GroomGuideType):  [Read-Write] Type of guides:
   - Imported: use imported guides
   - Generated: generate guides from strands
   - Rigged: generated rigged guides from strands.
- ``hair_to_guide_density`` (float):  [Read-Write] Density factor for converting hair into guide curve if no guides are provided. The value should be between 0 and 1, and can be thought as a ratio/percentage of strands used as guides.
- ``interpolation_distance`` (HairInterpolationWeight):  [Read-Write] Interpolation distance metric.
- ``interpolation_quality`` (HairInterpolationQuality):  [Read-Write] Interpolation data quality.
- ``randomize_guide`` (bool):  [Read-Write] Randomize which guides affect a given hair strand.
- ``rigged_guide_num_curves`` (int32):  [Read-Write] Number of guides that will be generated on the groom and the skeletal mesh
- ``rigged_guide_num_points`` (int32):  [Read-Write] Number of points/bones per generated guide
- ``use_unique_guide`` (bool):  [Read-Write] Force a hair strand to be affected by a unique guide.

<a id="unreal.HairInterpolationSettings.__init__"></a>

#### __init__

```python
def __init__(guide_type: GroomGuideType = GroomGuideType.IMPORTED,
             hair_to_guide_density: float = 0.000000,
             rigged_guide_num_curves: int = 0,
             rigged_guide_num_points: int = 0,
             interpolation_quality:
             HairInterpolationQuality = HairInterpolationQuality.LOW,
             interpolation_distance:
             HairInterpolationWeight = HairInterpolationWeight.PARAMETRIC,
             randomize_guide: bool = False,
             use_unique_guide: bool = False) -> None
```

<a id="unreal.HairInterpolationSettings.guide_type"></a>

#### guide_type

```python
@property
def guide_type() -> GroomGuideType
```

(GroomGuideType):  [Read-Write] Type of guides:
 - Imported: use imported guides
 - Generated: generate guides from strands
 - Rigged: generated rigged guides from strands.

<a id="unreal.HairInterpolationSettings.guide_type"></a>

#### guide_type

```python
@guide_type.setter
def guide_type(value: GroomGuideType) -> None
```

<a id="unreal.HairInterpolationSettings.hair_to_guide_density"></a>

#### hair_to_guide_density

```python
@property
def hair_to_guide_density() -> float
```

(float):  [Read-Write] Density factor for converting hair into guide curve if no guides are provided. The value should be between 0 and 1, and can be thought as a ratio/percentage of strands used as guides.

<a id="unreal.HairInterpolationSettings.hair_to_guide_density"></a>

#### hair_to_guide_density

```python
@hair_to_guide_density.setter
def hair_to_guide_density(value: float) -> None
```

<a id="unreal.HairInterpolationSettings.rigged_guide_num_curves"></a>

#### rigged_guide_num_curves

```python
@property
def rigged_guide_num_curves() -> int
```

(int32):  [Read-Only] Number of guides that will be generated on the groom and the skeletal mesh

<a id="unreal.HairInterpolationSettings.rigged_guide_num_points"></a>

#### rigged_guide_num_points

```python
@property
def rigged_guide_num_points() -> int
```

(int32):  [Read-Only] Number of points/bones per generated guide

<a id="unreal.HairInterpolationSettings.interpolation_quality"></a>

#### interpolation_quality

```python
@property
def interpolation_quality() -> HairInterpolationQuality
```

(HairInterpolationQuality):  [Read-Write] Interpolation data quality.

<a id="unreal.HairInterpolationSettings.interpolation_quality"></a>

#### interpolation_quality

```python
@interpolation_quality.setter
def interpolation_quality(value: HairInterpolationQuality) -> None
```

<a id="unreal.HairInterpolationSettings.interpolation_distance"></a>

#### interpolation_distance

```python
@property
def interpolation_distance() -> HairInterpolationWeight
```

(HairInterpolationWeight):  [Read-Write] Interpolation distance metric.

<a id="unreal.HairInterpolationSettings.interpolation_distance"></a>

#### interpolation_distance

```python
@interpolation_distance.setter
def interpolation_distance(value: HairInterpolationWeight) -> None
```

<a id="unreal.HairInterpolationSettings.randomize_guide"></a>

#### randomize_guide

```python
@property
def randomize_guide() -> bool
```

(bool):  [Read-Write] Randomize which guides affect a given hair strand.

<a id="unreal.HairInterpolationSettings.randomize_guide"></a>

#### randomize_guide

```python
@randomize_guide.setter
def randomize_guide(value: bool) -> None
```

<a id="unreal.HairInterpolationSettings.use_unique_guide"></a>

#### use_unique_guide

```python
@property
def use_unique_guide() -> bool
```

(bool):  [Read-Write] Force a hair strand to be affected by a unique guide.

<a id="unreal.HairInterpolationSettings.use_unique_guide"></a>

#### use_unique_guide

```python
@use_unique_guide.setter
def use_unique_guide(value: bool) -> None
```

<a id="unreal.HairDeformationSettings"></a>