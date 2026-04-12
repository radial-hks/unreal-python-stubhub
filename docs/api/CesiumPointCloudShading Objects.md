## CesiumPointCloudShading Objects

```python
class CesiumPointCloudShading(StructBase)
```

Options for adjusting how point clouds are rendered using 3D Tiles.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumPointCloudShading.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attenuation`` (bool):  [Read-Write] Whether or not to perform point attenuation. Attenuation controls the size
  of the points rendered based on the geometric error of their tile.
- ``base_resolution`` (float):  [Read-Write] The average base resolution for the dataset in meters. For example,
  a base resolution of 0.05 assumes an original capture resolution of
  5 centimeters between neighboring points.

  This is used in place of geometric error when the tile's geometric error is
  0. If this value is zero, each tile with a geometric error of 0 will have
  its geometric error approximated instead.
- ``geometric_error_scale`` (float):  [Read-Write] The scale to be applied to the tile's geometric error before it is used
  to compute attenuation. Larger values will result in larger points.
- ``maximum_attenuation`` (float):  [Read-Write] The maximum point attenuation in pixels. If this is zero, the
  Cesium3DTileset's maximumScreenSpaceError will be used as the maximum point
  attenuation.

<a id="unreal.CesiumPointCloudShading.__init__"></a>

#### \_\_init\_\_

```python
def __init__(attenuation: bool = False,
             geometric_error_scale: float = 0.000000,
             maximum_attenuation: float = 0.000000,
             base_resolution: float = 0.000000) -> None
```

<a id="unreal.CesiumPointCloudShading.attenuation"></a>

#### attenuation

```python
@property
def attenuation() -> bool
```

(bool):  [Read-Write] Whether or not to perform point attenuation. Attenuation controls the size
of the points rendered based on the geometric error of their tile.

<a id="unreal.CesiumPointCloudShading.attenuation"></a>

#### attenuation

```python
@attenuation.setter
def attenuation(value: bool) -> None
```

<a id="unreal.CesiumPointCloudShading.geometric_error_scale"></a>

#### geometric\_error\_scale

```python
@property
def geometric_error_scale() -> float
```

(float):  [Read-Write] The scale to be applied to the tile's geometric error before it is used
to compute attenuation. Larger values will result in larger points.

<a id="unreal.CesiumPointCloudShading.geometric_error_scale"></a>

#### geometric\_error\_scale

```python
@geometric_error_scale.setter
def geometric_error_scale(value: float) -> None
```

<a id="unreal.CesiumPointCloudShading.maximum_attenuation"></a>

#### maximum\_attenuation

```python
@property
def maximum_attenuation() -> float
```

(float):  [Read-Write] The maximum point attenuation in pixels. If this is zero, the
Cesium3DTileset's maximumScreenSpaceError will be used as the maximum point
attenuation.

<a id="unreal.CesiumPointCloudShading.maximum_attenuation"></a>

#### maximum\_attenuation

```python
@maximum_attenuation.setter
def maximum_attenuation(value: float) -> None
```

<a id="unreal.CesiumPointCloudShading.base_resolution"></a>

#### base\_resolution

```python
@property
def base_resolution() -> float
```

(float):  [Read-Write] The average base resolution for the dataset in meters. For example,
a base resolution of 0.05 assumes an original capture resolution of
5 centimeters between neighboring points.

This is used in place of geometric error when the tile's geometric error is
0. If this value is zero, each tile with a geometric error of 0 will have
its geometric error approximated instead.

<a id="unreal.CesiumPointCloudShading.base_resolution"></a>

#### base\_resolution

```python
@base_resolution.setter
def base_resolution(value: float) -> None
```

<a id="unreal.CesiumPrimitiveFeatures"></a>