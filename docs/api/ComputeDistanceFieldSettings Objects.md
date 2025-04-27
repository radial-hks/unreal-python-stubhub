## ComputeDistanceFieldSettings Objects

```python
class ComputeDistanceFieldSettings(StructBase)
```

Settings for computing distance fields

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: VolumeTextureBakeFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``compute_mode`` (DistanceFieldComputeMode):  [Read-Write] Whether to compute distances only in a band around the surface (faster) or compute the full grid
  Note: If full grid is computed, the distances will still be more accurately computed in the narrow band
  In narrow band mode, values outside the band will have a large magnitude with the correct sign
- ``narrow_band_units`` (DistanceFieldUnits):  [Read-Write] Whether Narrow Band Width is expressed as a number of voxels (rounded up to nearest int) or a distance
- ``narrow_band_width`` (float):  [Read-Write] Width of the narrow band where distances are computed accurately
- ``require_power2`` (bool):  [Read-Write] Whether to round voxel count on each dimension up to the nearest power of two
- ``voxels_per_dimensions`` (IntVector):  [Read-Write] Number of voxels to use along each axis

<a id="unreal.ComputeDistanceFieldSettings.__init__"></a>

#### __init__

```python
def __init__(compute_mode: DistanceFieldComputeMode = DistanceFieldComputeMode.
             NARROW_BAND,
             narrow_band_width: float = 0.000000,
             narrow_band_units: DistanceFieldUnits = DistanceFieldUnits.
             NUMBER_OF_VOXELS,
             voxels_per_dimensions: IntVector = [0, 0, 0],
             require_power2: bool = False) -> None
```

<a id="unreal.ComputeDistanceFieldSettings.compute_mode"></a>

#### compute_mode

```python
@property
def compute_mode() -> DistanceFieldComputeMode
```

(DistanceFieldComputeMode):  [Read-Write] Whether to compute distances only in a band around the surface (faster) or compute the full grid
Note: If full grid is computed, the distances will still be more accurately computed in the narrow band
In narrow band mode, values outside the band will have a large magnitude with the correct sign

<a id="unreal.ComputeDistanceFieldSettings.compute_mode"></a>

#### compute_mode

```python
@compute_mode.setter
def compute_mode(value: DistanceFieldComputeMode) -> None
```

<a id="unreal.ComputeDistanceFieldSettings.narrow_band_width"></a>

#### narrow_band_width

```python
@property
def narrow_band_width() -> float
```

(float):  [Read-Write] Width of the narrow band where distances are computed accurately

<a id="unreal.ComputeDistanceFieldSettings.narrow_band_width"></a>

#### narrow_band_width

```python
@narrow_band_width.setter
def narrow_band_width(value: float) -> None
```

<a id="unreal.ComputeDistanceFieldSettings.narrow_band_units"></a>

#### narrow_band_units

```python
@property
def narrow_band_units() -> DistanceFieldUnits
```

(DistanceFieldUnits):  [Read-Write] Whether Narrow Band Width is expressed as a number of voxels (rounded up to nearest int) or a distance

<a id="unreal.ComputeDistanceFieldSettings.narrow_band_units"></a>

#### narrow_band_units

```python
@narrow_band_units.setter
def narrow_band_units(value: DistanceFieldUnits) -> None
```

<a id="unreal.ComputeDistanceFieldSettings.voxels_per_dimensions"></a>

#### voxels_per_dimensions

```python
@property
def voxels_per_dimensions() -> IntVector
```

(IntVector):  [Read-Write] Number of voxels to use along each axis

<a id="unreal.ComputeDistanceFieldSettings.voxels_per_dimensions"></a>

#### voxels_per_dimensions

```python
@voxels_per_dimensions.setter
def voxels_per_dimensions(value: IntVector) -> None
```

<a id="unreal.ComputeDistanceFieldSettings.require_power2"></a>

#### require_power2

```python
@property
def require_power2() -> bool
```

(bool):  [Read-Write] Whether to round voxel count on each dimension up to the nearest power of two

<a id="unreal.ComputeDistanceFieldSettings.require_power2"></a>

#### require_power2

```python
@require_power2.setter
def require_power2(value: bool) -> None
```

<a id="unreal.DistanceFieldToTextureSettings"></a>