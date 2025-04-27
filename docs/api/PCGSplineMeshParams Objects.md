## PCGSplineMeshParams Objects

```python
class PCGSplineMeshParams(StructBase)
```

PCGSpline Mesh Params

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSplineMeshParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``forward_axis`` (PCGSplineMeshForwardAxis):  [Read-Write] Chooses the forward axis for the spline mesh orientation.
- ``nanite_cluster_bounds_scale`` (float):  [Read-Write] How much to scale the calculated culling bounds of Nanite clusters after deformation.
  NOTE: This should only be set greater than 1.0 if it fixes visible issues with clusters being
  incorrectly culled.
- ``scale_mesh_to_bounds`` (bool):  [Read-Write] Scale mesh to the spline control point bounds. Especially useful on Landscape Splines, where the bounds come from the width.
- ``scale_mesh_to_landscape_spline_full_width`` (bool):  [Read-Write] Scale the mesh to the full width of the Landscape Spline (including Falloff). Only applies to Landscape Splines.
- ``smooth_interp_roll_scale`` (bool):  [Read-Write] If true, will use smooth interpolation (ease in/out) for Scale, Roll, and Offset along this section of spline. If false, uses linear.
- ``spline_boundary_max`` (float):  [Read-Write] Maximum coordinate along the spline forward axis which corresponds to end of spline. If set to 0.0, will use bounding box to determine bounds.
- ``spline_boundary_min`` (float):  [Read-Write] Minimum coordinate along the spline forward axis which corresponds to start of spline. If set to 0.0, will use bounding box to determine bounds.
- ``spline_up_dir`` (Vector):  [Read-Write] Axis (in component space) that is used to determine X axis for coordinates along spline.

<a id="unreal.PCGSplineMeshParams.__init__"></a>

#### __init__

```python
def __init__(
        forward_axis: PCGSplineMeshForwardAxis = PCGSplineMeshForwardAxis.X,
        scale_mesh_to_bounds: bool = False,
        scale_mesh_to_landscape_spline_full_width: bool = False,
        spline_up_dir: Vector = [0.000000, 0.000000, 0.000000],
        nanite_cluster_bounds_scale: float = 0.000000,
        spline_boundary_min: float = 0.000000,
        spline_boundary_max: float = 0.000000,
        smooth_interp_roll_scale: bool = False) -> None
```

<a id="unreal.PCGSplineMeshParams.forward_axis"></a>

#### forward_axis

```python
@property
def forward_axis() -> PCGSplineMeshForwardAxis
```

(PCGSplineMeshForwardAxis):  [Read-Write] Chooses the forward axis for the spline mesh orientation.

<a id="unreal.PCGSplineMeshParams.forward_axis"></a>

#### forward_axis

```python
@forward_axis.setter
def forward_axis(value: PCGSplineMeshForwardAxis) -> None
```

<a id="unreal.PCGSplineMeshParams.scale_mesh_to_bounds"></a>

#### scale_mesh_to_bounds

```python
@property
def scale_mesh_to_bounds() -> bool
```

(bool):  [Read-Write] Scale mesh to the spline control point bounds. Especially useful on Landscape Splines, where the bounds come from the width.

<a id="unreal.PCGSplineMeshParams.scale_mesh_to_bounds"></a>

#### scale_mesh_to_bounds

```python
@scale_mesh_to_bounds.setter
def scale_mesh_to_bounds(value: bool) -> None
```

<a id="unreal.PCGSplineMeshParams.scale_mesh_to_landscape_spline_full_width"></a>

#### scale_mesh_to_landscape_spline_full_width

```python
@property
def scale_mesh_to_landscape_spline_full_width() -> bool
```

(bool):  [Read-Write] Scale the mesh to the full width of the Landscape Spline (including Falloff). Only applies to Landscape Splines.

<a id="unreal.PCGSplineMeshParams.scale_mesh_to_landscape_spline_full_width"></a>

#### scale_mesh_to_landscape_spline_full_width

```python
@scale_mesh_to_landscape_spline_full_width.setter
def scale_mesh_to_landscape_spline_full_width(value: bool) -> None
```

<a id="unreal.PCGSplineMeshParams.spline_up_dir"></a>

#### spline_up_dir

```python
@property
def spline_up_dir() -> Vector
```

(Vector):  [Read-Write] Axis (in component space) that is used to determine X axis for coordinates along spline.

<a id="unreal.PCGSplineMeshParams.spline_up_dir"></a>

#### spline_up_dir

```python
@spline_up_dir.setter
def spline_up_dir(value: Vector) -> None
```

<a id="unreal.PCGSplineMeshParams.nanite_cluster_bounds_scale"></a>

#### nanite_cluster_bounds_scale

```python
@property
def nanite_cluster_bounds_scale() -> float
```

(float):  [Read-Write] How much to scale the calculated culling bounds of Nanite clusters after deformation.
NOTE: This should only be set greater than 1.0 if it fixes visible issues with clusters being
incorrectly culled.

<a id="unreal.PCGSplineMeshParams.nanite_cluster_bounds_scale"></a>

#### nanite_cluster_bounds_scale

```python
@nanite_cluster_bounds_scale.setter
def nanite_cluster_bounds_scale(value: float) -> None
```

<a id="unreal.PCGSplineMeshParams.spline_boundary_min"></a>

#### spline_boundary_min

```python
@property
def spline_boundary_min() -> float
```

(float):  [Read-Write] Minimum coordinate along the spline forward axis which corresponds to start of spline. If set to 0.0, will use bounding box to determine bounds.

<a id="unreal.PCGSplineMeshParams.spline_boundary_min"></a>

#### spline_boundary_min

```python
@spline_boundary_min.setter
def spline_boundary_min(value: float) -> None
```

<a id="unreal.PCGSplineMeshParams.spline_boundary_max"></a>

#### spline_boundary_max

```python
@property
def spline_boundary_max() -> float
```

(float):  [Read-Write] Maximum coordinate along the spline forward axis which corresponds to end of spline. If set to 0.0, will use bounding box to determine bounds.

<a id="unreal.PCGSplineMeshParams.spline_boundary_max"></a>

#### spline_boundary_max

```python
@spline_boundary_max.setter
def spline_boundary_max(value: float) -> None
```

<a id="unreal.PCGSplineMeshParams.smooth_interp_roll_scale"></a>

#### smooth_interp_roll_scale

```python
@property
def smooth_interp_roll_scale() -> bool
```

(bool):  [Read-Write] If true, will use smooth interpolation (ease in/out) for Scale, Roll, and Offset along this section of spline. If false, uses linear.

<a id="unreal.PCGSplineMeshParams.smooth_interp_roll_scale"></a>

#### smooth_interp_roll_scale

```python
@smooth_interp_roll_scale.setter
def smooth_interp_roll_scale(value: bool) -> None
```

<a id="unreal.PCGSplineSamplerParams"></a>