## LidarToolActionsNormals Objects

```python
class LidarToolActionsNormals(InteractiveToolPropertySet)
```

Lidar Tool Actions Normals

**C++ Source:**

- **Plugin**: LidarPointCloud
- **Module**: LidarPointCloudEditor
- **File**: LidarPointCloudEditorTools.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``noise_tolerance`` (float):  [Read-Write] Higher values are less susceptible to noise, but will most likely lose finer details, especially around hard edges.
  Lower values retain more detail, at the expense of time.
  NOTE: setting this too low will cause visual artifacts and geometry holes in noisier datasets.
- ``quality`` (int32):  [Read-Write] Higher values will generally result in more accurate calculations, at the expense of time

<a id="unreal.LidarToolActionsNormals.noise_tolerance"></a>

#### noise_tolerance

```python
@property
def noise_tolerance() -> float
```

(float):  [Read-Write] Higher values are less susceptible to noise, but will most likely lose finer details, especially around hard edges.
Lower values retain more detail, at the expense of time.
NOTE: setting this too low will cause visual artifacts and geometry holes in noisier datasets.

<a id="unreal.LidarToolActionsNormals.noise_tolerance"></a>

#### noise_tolerance

```python
@noise_tolerance.setter
def noise_tolerance(value: float) -> None
```

<a id="unreal.LidarToolActionsSelection"></a>