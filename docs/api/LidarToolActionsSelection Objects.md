## LidarToolActionsSelection Objects

```python
class LidarToolActionsSelection(InteractiveToolPropertySet)
```

Lidar Tool Actions Selection

**C++ Source:**

- **Plugin**: LidarPointCloud
- **Module**: LidarPointCloudEditor
- **File**: LidarPointCloudEditorTools.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max_meshing_error`` (float):  [Read-Write] Max error around the meshed areas. Leave at 0 for max quality
- ``merge_meshes`` (bool):  [Read-Write]
- ``noise_tolerance`` (float):  [Read-Write] Higher values are less susceptible to noise, but will most likely lose finer details, especially around hard edges.
  Lower values retain more detail, at the expense of time.
  NOTE: setting this too low will cause visual artifacts and geometry holes in noisier datasets.
- ``quality`` (int32):  [Read-Write] Higher values will generally result in more accurate calculations, at the expense of time
- ``retain_transform`` (bool):  [Read-Write] If not merging meshes, this will retain the transform of the original cloud

<a id="unreal.LidarToolActionsSelection.noise_tolerance"></a>

#### noise_tolerance

```python
@property
def noise_tolerance() -> float
```

(float):  [Read-Write] Higher values are less susceptible to noise, but will most likely lose finer details, especially around hard edges.
Lower values retain more detail, at the expense of time.
NOTE: setting this too low will cause visual artifacts and geometry holes in noisier datasets.

<a id="unreal.LidarToolActionsSelection.noise_tolerance"></a>

#### noise_tolerance

```python
@noise_tolerance.setter
def noise_tolerance(value: float) -> None
```

<a id="unreal.LidarToolActionsPaintSelection"></a>