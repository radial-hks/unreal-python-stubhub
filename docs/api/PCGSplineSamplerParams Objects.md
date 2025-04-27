## PCGSplineSamplerParams Objects

```python
class PCGSplineSamplerParams(StructBase)
```

PCGSpline Sampler Params

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSplineSampler.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha_attribute`` (Name):  [Read-Write] Attribute that will contain a value in [0,1] representing how far along the point is to the end of the line. Each segment on the line represents a same-size interval.
  For example, if there are three segments, each segment will take up 0.333... of the interval.
- ``arrive_tangent_attribute`` (Name):  [Read-Write] Attribute that will contain the arrive tangent vector. For control points, this will be the actual arrive tangent. For non-control points, this will only be the normalized tangent at this point.
- ``compute_alpha`` (bool):  [Read-Write] Compute an alpha value along the spline and write it to an attribute.
- ``compute_curvature`` (bool):  [Read-Write] Compute curvature along the spline and write it to an attribute.
- ``compute_direction_delta`` (bool):  [Read-Write] Compute the delta angle to the next point on the spline and write it to an attribute.
- ``compute_distance`` (bool):  [Read-Write] Compute distance along the spline and write it to an attribute.
- ``compute_input_key`` (bool):  [Read-Write] Compute an input key for each point along the spline and write the key to an attribute.
- ``compute_segment_index`` (bool):  [Read-Write] Compute the spline segment index and write it to an attribute.
- ``compute_subsegment_index`` (bool):  [Read-Write] Compute the sub-segment index of a point on the spline and write it to an attribute.
- ``compute_tangents`` (bool):  [Read-Write] Compute arrive and leave tangents along the spline and write them to attributes.
- ``curvature_attribute`` (Name):  [Read-Write] Attribute that will contain the curvature. Note that the radius of curvature is defined as 1/Curvature, and might need you to scale to world units.
- ``dimension`` (PCGSplineSamplingDimension):  [Read-Write]
- ``distance_attribute`` (Name):  [Read-Write] Attribute that will contain the distance along the spline at the sample point.
- ``distance_increment`` (float):  [Read-Write]
- ``end_offset`` (float):  [Read-Write] Distance (in cm) from the end of the spline at which sampling will end.
- ``fill`` (PCGSplineSamplingFill):  [Read-Write]
- ``fit_to_curve`` (bool):  [Read-Write] If the length of the spline does not divide evenly into the DistanceIncrement, the final sample point will not land on the end of the spline. Enable this to force
  the DistanceIncrement to be rounded up to the nearest value which would yield evenly spaced samples across the entire length of the spline.
- ``input_key_attribute`` (Name):  [Read-Write] Attribute that will contain the spline input key, a float value between [0, N], where N is the number of control points. Each range [i, i+1] represents an interpolation from 0 to 1 across spline segment i.
- ``interior_border_sample_spacing`` (float):  [Read-Write] The space between each sample point on the spline boundary. Used for computation; lower spacing is more expensive but more accurate.
- ``interior_density_falloff_curve`` (RuntimeFloatCurve):  [Read-Write] Defines the density for each sample based on its distance from the spline. X axis is normalized distance to boundary (0-1), Y axis is density value.
- ``interior_orientation`` (PCGSplineSamplingInteriorOrientation):  [Read-Write] Determines the orientation of interior points.
- ``interior_sample_spacing`` (float):  [Read-Write] The space between each sample point
- ``leave_tangent_attribute`` (Name):  [Read-Write] Attribute that will contain the leave tangent vector. For control points, this will be the actual leave tangent. For non-control points, this will only be the normalized tangent at this point.
- ``max_random_offset_normalized`` (float):  [Read-Write] Normalized value for the maximum possible offset for each sample point. 0.0 means no offset, and 1.0 means DistanceIncrement / 2.0.
- ``mode`` (PCGSplineSamplingMode):  [Read-Write]
- ``next_direction_delta_attribute`` (Name):  [Read-Write] Attribute that will contain the delta angle to the next point on the spline w.r.t to the current's point Up vector.
- ``num_height_subdivisions`` (int32):  [Read-Write]
- ``num_planar_subdivisions`` (int32):  [Read-Write]
- ``num_samples`` (int32):  [Read-Write]
- ``point_steepness`` (float):  [Read-Write] Each PCG point represents a discretized, volumetric region of world space. The points' Steepness value [0.0 to
  1.0] establishes how "hard" or "soft" that volume will be represented. From 0, it will ramp up linearly
  increasing its influence over the density from the point's center to up to two times the bounds. At 1, it will
  represent a binary box function with the size of the point's bounds.
- ``project_onto_surface`` (bool):  [Read-Write] Project sample points onto one possible surface given by the spline boundary.
- ``seed_from2d_position`` (bool):  [Read-Write] Controls whether we will seed the sampled points using the 3D position or the 2D (XY) position.
- ``seed_from_local_position`` (bool):  [Read-Write] Controls whether we will seed the sampled points using the final world position or the local position.
- ``seeding_mode`` (PCGSplineSamplingSeedingMode):  [Read-Write] Controls the mode for computing a sample point's seed.
- ``segment_index_attribute`` (Name):  [Read-Write] Attribute that will contain the spline segment index.
- ``start_offset`` (float):  [Read-Write] Distance (in cm) along the spline at which sampling will begin.
- ``subdivisions_per_segment`` (int32):  [Read-Write]
- ``subsegment_index_attribute`` (Name):  [Read-Write] Attribute that will contain the sub-segment index of a point on the spline. When the sub-segment index is 0, the point is a control point on the actual spline. Only applies to Subdivision mode.
- ``treat_spline_as_polyline`` (bool):  [Read-Write] Use the spline points to form a polyline, instead of computing many sample points along the spline. This is more accurate if your spline is linear.
- ``unbounded`` (bool):  [Read-Write] If no Bounding Shape input is provided, the actor bounds are used to limit the sample generation domain.
  This option allows ignoring the actor bounds and generating over the entire spline. Use with caution as this
  may generate a lot of points.

<a id="unreal.PCGSplineSamplerParams.__init__"></a>

#### __init__

```python
def __init__(
        dimension: PCGSplineSamplingDimension = PCGSplineSamplingDimension.
    ON_SPLINE,
        mode: PCGSplineSamplingMode = PCGSplineSamplingMode.SUBDIVISION,
        fill: PCGSplineSamplingFill = PCGSplineSamplingFill.FILL,
        subdivisions_per_segment: int = 0,
        distance_increment: float = 0.000000,
        num_samples: int = 0,
        num_planar_subdivisions: int = 0,
        num_height_subdivisions: int = 0,
        start_offset: float = 0.000000,
        end_offset: float = 0.000000,
        max_random_offset_normalized: float = 0.000000,
        fit_to_curve: bool = False,
        interior_sample_spacing: float = 0.000000,
        interior_border_sample_spacing: float = 0.000000,
        treat_spline_as_polyline: bool = False,
        interior_orientation:
    PCGSplineSamplingInteriorOrientation = PCGSplineSamplingInteriorOrientation
    .UNIFORM,
        project_onto_surface: bool = False,
        interior_density_falloff_curve: RuntimeFloatCurve = [],
        compute_direction_delta: bool = False,
        next_direction_delta_attribute: Name = "None",
        compute_curvature: bool = False,
        curvature_attribute: Name = "None",
        compute_segment_index: bool = False,
        segment_index_attribute: Name = "None",
        compute_subsegment_index: bool = False,
        subsegment_index_attribute: Name = "None",
        compute_tangents: bool = False,
        arrive_tangent_attribute: Name = "None",
        leave_tangent_attribute: Name = "None",
        compute_alpha: bool = False,
        alpha_attribute: Name = "None",
        compute_distance: bool = False,
        distance_attribute: Name = "None",
        compute_input_key: bool = False,
        input_key_attribute: Name = "None",
        unbounded: bool = False,
        point_steepness: float = 0.000000,
        seeding_mode: PCGSplineSamplingSeedingMode = PCGSplineSamplingSeedingMode
    .SEED_FROM_POSITION,
        seed_from_local_position: bool = False,
        seed_from2d_position: bool = False) -> None
```

<a id="unreal.PCGSplineSamplerParams.dimension"></a>

#### dimension

```python
@property
def dimension() -> PCGSplineSamplingDimension
```

(PCGSplineSamplingDimension):  [Read-Write]

<a id="unreal.PCGSplineSamplerParams.dimension"></a>

#### dimension

```python
@dimension.setter
def dimension(value: PCGSplineSamplingDimension) -> None
```

<a id="unreal.PCGSplineSamplerParams.mode"></a>

#### mode

```python
@property
def mode() -> PCGSplineSamplingMode
```

(PCGSplineSamplingMode):  [Read-Write]

<a id="unreal.PCGSplineSamplerParams.mode"></a>

#### mode

```python
@mode.setter
def mode(value: PCGSplineSamplingMode) -> None
```

<a id="unreal.PCGSplineSamplerParams.fill"></a>

#### fill

```python
@property
def fill() -> PCGSplineSamplingFill
```

(PCGSplineSamplingFill):  [Read-Write]

<a id="unreal.PCGSplineSamplerParams.fill"></a>

#### fill

```python
@fill.setter
def fill(value: PCGSplineSamplingFill) -> None
```

<a id="unreal.PCGSplineSamplerParams.subdivisions_per_segment"></a>

#### subdivisions_per_segment

```python
@property
def subdivisions_per_segment() -> int
```

(int32):  [Read-Write]

<a id="unreal.PCGSplineSamplerParams.subdivisions_per_segment"></a>

#### subdivisions_per_segment

```python
@subdivisions_per_segment.setter
def subdivisions_per_segment(value: int) -> None
```

<a id="unreal.PCGSplineSamplerParams.distance_increment"></a>

#### distance_increment

```python
@property
def distance_increment() -> float
```

(float):  [Read-Write]

<a id="unreal.PCGSplineSamplerParams.distance_increment"></a>

#### distance_increment

```python
@distance_increment.setter
def distance_increment(value: float) -> None
```

<a id="unreal.PCGSplineSamplerParams.num_samples"></a>

#### num_samples

```python
@property
def num_samples() -> int
```

(int32):  [Read-Write]

<a id="unreal.PCGSplineSamplerParams.num_samples"></a>

#### num_samples

```python
@num_samples.setter
def num_samples(value: int) -> None
```

<a id="unreal.PCGSplineSamplerParams.num_planar_subdivisions"></a>

#### num_planar_subdivisions

```python
@property
def num_planar_subdivisions() -> int
```

(int32):  [Read-Write]

<a id="unreal.PCGSplineSamplerParams.num_planar_subdivisions"></a>

#### num_planar_subdivisions

```python
@num_planar_subdivisions.setter
def num_planar_subdivisions(value: int) -> None
```

<a id="unreal.PCGSplineSamplerParams.num_height_subdivisions"></a>

#### num_height_subdivisions

```python
@property
def num_height_subdivisions() -> int
```

(int32):  [Read-Write]

<a id="unreal.PCGSplineSamplerParams.num_height_subdivisions"></a>

#### num_height_subdivisions

```python
@num_height_subdivisions.setter
def num_height_subdivisions(value: int) -> None
```

<a id="unreal.PCGSplineSamplerParams.start_offset"></a>

#### start_offset

```python
@property
def start_offset() -> float
```

(float):  [Read-Write] Distance (in cm) along the spline at which sampling will begin.

<a id="unreal.PCGSplineSamplerParams.start_offset"></a>

#### start_offset

```python
@start_offset.setter
def start_offset(value: float) -> None
```

<a id="unreal.PCGSplineSamplerParams.end_offset"></a>

#### end_offset

```python
@property
def end_offset() -> float
```

(float):  [Read-Write] Distance (in cm) from the end of the spline at which sampling will end.

<a id="unreal.PCGSplineSamplerParams.end_offset"></a>

#### end_offset

```python
@end_offset.setter
def end_offset(value: float) -> None
```

<a id="unreal.PCGSplineSamplerParams.max_random_offset_normalized"></a>

#### max_random_offset_normalized

```python
@property
def max_random_offset_normalized() -> float
```

(float):  [Read-Write] Normalized value for the maximum possible offset for each sample point. 0.0 means no offset, and 1.0 means DistanceIncrement / 2.0.

<a id="unreal.PCGSplineSamplerParams.max_random_offset_normalized"></a>

#### max_random_offset_normalized

```python
@max_random_offset_normalized.setter
def max_random_offset_normalized(value: float) -> None
```

<a id="unreal.PCGSplineSamplerParams.fit_to_curve"></a>

#### fit_to_curve

```python
@property
def fit_to_curve() -> bool
```

(bool):  [Read-Write] If the length of the spline does not divide evenly into the DistanceIncrement, the final sample point will not land on the end of the spline. Enable this to force
the DistanceIncrement to be rounded up to the nearest value which would yield evenly spaced samples across the entire length of the spline.

<a id="unreal.PCGSplineSamplerParams.fit_to_curve"></a>

#### fit_to_curve

```python
@fit_to_curve.setter
def fit_to_curve(value: bool) -> None
```

<a id="unreal.PCGSplineSamplerParams.interior_sample_spacing"></a>

#### interior_sample_spacing

```python
@property
def interior_sample_spacing() -> float
```

(float):  [Read-Write] The space between each sample point

<a id="unreal.PCGSplineSamplerParams.interior_sample_spacing"></a>

#### interior_sample_spacing

```python
@interior_sample_spacing.setter
def interior_sample_spacing(value: float) -> None
```

<a id="unreal.PCGSplineSamplerParams.interior_border_sample_spacing"></a>

#### interior_border_sample_spacing

```python
@property
def interior_border_sample_spacing() -> float
```

(float):  [Read-Write] The space between each sample point on the spline boundary. Used for computation; lower spacing is more expensive but more accurate.

<a id="unreal.PCGSplineSamplerParams.interior_border_sample_spacing"></a>

#### interior_border_sample_spacing

```python
@interior_border_sample_spacing.setter
def interior_border_sample_spacing(value: float) -> None
```

<a id="unreal.PCGSplineSamplerParams.treat_spline_as_polyline"></a>

#### treat_spline_as_polyline

```python
@property
def treat_spline_as_polyline() -> bool
```

(bool):  [Read-Write] Use the spline points to form a polyline, instead of computing many sample points along the spline. This is more accurate if your spline is linear.

<a id="unreal.PCGSplineSamplerParams.treat_spline_as_polyline"></a>

#### treat_spline_as_polyline

```python
@treat_spline_as_polyline.setter
def treat_spline_as_polyline(value: bool) -> None
```

<a id="unreal.PCGSplineSamplerParams.interior_orientation"></a>

#### interior_orientation

```python
@property
def interior_orientation() -> PCGSplineSamplingInteriorOrientation
```

(PCGSplineSamplingInteriorOrientation):  [Read-Write] Determines the orientation of interior points.

<a id="unreal.PCGSplineSamplerParams.interior_orientation"></a>

#### interior_orientation

```python
@interior_orientation.setter
def interior_orientation(value: PCGSplineSamplingInteriorOrientation) -> None
```

<a id="unreal.PCGSplineSamplerParams.project_onto_surface"></a>

#### project_onto_surface

```python
@property
def project_onto_surface() -> bool
```

(bool):  [Read-Write] Project sample points onto one possible surface given by the spline boundary.

<a id="unreal.PCGSplineSamplerParams.project_onto_surface"></a>

#### project_onto_surface

```python
@project_onto_surface.setter
def project_onto_surface(value: bool) -> None
```

<a id="unreal.PCGSplineSamplerParams.interior_density_falloff_curve"></a>

#### interior_density_falloff_curve

```python
@property
def interior_density_falloff_curve() -> RuntimeFloatCurve
```

(RuntimeFloatCurve):  [Read-Write] Defines the density for each sample based on its distance from the spline. X axis is normalized distance to boundary (0-1), Y axis is density value.

<a id="unreal.PCGSplineSamplerParams.interior_density_falloff_curve"></a>

#### interior_density_falloff_curve

```python
@interior_density_falloff_curve.setter
def interior_density_falloff_curve(value: RuntimeFloatCurve) -> None
```

<a id="unreal.PCGSplineSamplerParams.compute_direction_delta"></a>

#### compute_direction_delta

```python
@property
def compute_direction_delta() -> bool
```

(bool):  [Read-Write] Compute the delta angle to the next point on the spline and write it to an attribute.

<a id="unreal.PCGSplineSamplerParams.compute_direction_delta"></a>

#### compute_direction_delta

```python
@compute_direction_delta.setter
def compute_direction_delta(value: bool) -> None
```

<a id="unreal.PCGSplineSamplerParams.next_direction_delta_attribute"></a>

#### next_direction_delta_attribute

```python
@property
def next_direction_delta_attribute() -> Name
```

(Name):  [Read-Write] Attribute that will contain the delta angle to the next point on the spline w.r.t to the current's point Up vector.

<a id="unreal.PCGSplineSamplerParams.next_direction_delta_attribute"></a>

#### next_direction_delta_attribute

```python
@next_direction_delta_attribute.setter
def next_direction_delta_attribute(value: Name) -> None
```

<a id="unreal.PCGSplineSamplerParams.compute_curvature"></a>

#### compute_curvature

```python
@property
def compute_curvature() -> bool
```

(bool):  [Read-Write] Compute curvature along the spline and write it to an attribute.

<a id="unreal.PCGSplineSamplerParams.compute_curvature"></a>

#### compute_curvature

```python
@compute_curvature.setter
def compute_curvature(value: bool) -> None
```

<a id="unreal.PCGSplineSamplerParams.curvature_attribute"></a>

#### curvature_attribute

```python
@property
def curvature_attribute() -> Name
```

(Name):  [Read-Write] Attribute that will contain the curvature. Note that the radius of curvature is defined as 1/Curvature, and might need you to scale to world units.

<a id="unreal.PCGSplineSamplerParams.curvature_attribute"></a>

#### curvature_attribute

```python
@curvature_attribute.setter
def curvature_attribute(value: Name) -> None
```

<a id="unreal.PCGSplineSamplerParams.compute_segment_index"></a>

#### compute_segment_index

```python
@property
def compute_segment_index() -> bool
```

(bool):  [Read-Write] Compute the spline segment index and write it to an attribute.

<a id="unreal.PCGSplineSamplerParams.compute_segment_index"></a>

#### compute_segment_index

```python
@compute_segment_index.setter
def compute_segment_index(value: bool) -> None
```

<a id="unreal.PCGSplineSamplerParams.segment_index_attribute"></a>

#### segment_index_attribute

```python
@property
def segment_index_attribute() -> Name
```

(Name):  [Read-Write] Attribute that will contain the spline segment index.

<a id="unreal.PCGSplineSamplerParams.segment_index_attribute"></a>

#### segment_index_attribute

```python
@segment_index_attribute.setter
def segment_index_attribute(value: Name) -> None
```

<a id="unreal.PCGSplineSamplerParams.compute_subsegment_index"></a>

#### compute_subsegment_index

```python
@property
def compute_subsegment_index() -> bool
```

(bool):  [Read-Write] Compute the sub-segment index of a point on the spline and write it to an attribute.

<a id="unreal.PCGSplineSamplerParams.compute_subsegment_index"></a>

#### compute_subsegment_index

```python
@compute_subsegment_index.setter
def compute_subsegment_index(value: bool) -> None
```

<a id="unreal.PCGSplineSamplerParams.subsegment_index_attribute"></a>

#### subsegment_index_attribute

```python
@property
def subsegment_index_attribute() -> Name
```

(Name):  [Read-Write] Attribute that will contain the sub-segment index of a point on the spline. When the sub-segment index is 0, the point is a control point on the actual spline. Only applies to Subdivision mode.

<a id="unreal.PCGSplineSamplerParams.subsegment_index_attribute"></a>

#### subsegment_index_attribute

```python
@subsegment_index_attribute.setter
def subsegment_index_attribute(value: Name) -> None
```

<a id="unreal.PCGSplineSamplerParams.compute_tangents"></a>

#### compute_tangents

```python
@property
def compute_tangents() -> bool
```

(bool):  [Read-Write] Compute arrive and leave tangents along the spline and write them to attributes.

<a id="unreal.PCGSplineSamplerParams.compute_tangents"></a>

#### compute_tangents

```python
@compute_tangents.setter
def compute_tangents(value: bool) -> None
```

<a id="unreal.PCGSplineSamplerParams.arrive_tangent_attribute"></a>

#### arrive_tangent_attribute

```python
@property
def arrive_tangent_attribute() -> Name
```

(Name):  [Read-Write] Attribute that will contain the arrive tangent vector. For control points, this will be the actual arrive tangent. For non-control points, this will only be the normalized tangent at this point.

<a id="unreal.PCGSplineSamplerParams.arrive_tangent_attribute"></a>

#### arrive_tangent_attribute

```python
@arrive_tangent_attribute.setter
def arrive_tangent_attribute(value: Name) -> None
```

<a id="unreal.PCGSplineSamplerParams.leave_tangent_attribute"></a>

#### leave_tangent_attribute

```python
@property
def leave_tangent_attribute() -> Name
```

(Name):  [Read-Write] Attribute that will contain the leave tangent vector. For control points, this will be the actual leave tangent. For non-control points, this will only be the normalized tangent at this point.

<a id="unreal.PCGSplineSamplerParams.leave_tangent_attribute"></a>

#### leave_tangent_attribute

```python
@leave_tangent_attribute.setter
def leave_tangent_attribute(value: Name) -> None
```

<a id="unreal.PCGSplineSamplerParams.compute_alpha"></a>

#### compute_alpha

```python
@property
def compute_alpha() -> bool
```

(bool):  [Read-Write] Compute an alpha value along the spline and write it to an attribute.

<a id="unreal.PCGSplineSamplerParams.compute_alpha"></a>

#### compute_alpha

```python
@compute_alpha.setter
def compute_alpha(value: bool) -> None
```

<a id="unreal.PCGSplineSamplerParams.alpha_attribute"></a>

#### alpha_attribute

```python
@property
def alpha_attribute() -> Name
```

(Name):  [Read-Write] Attribute that will contain a value in [0,1] representing how far along the point is to the end of the line. Each segment on the line represents a same-size interval.
For example, if there are three segments, each segment will take up 0.333... of the interval.

<a id="unreal.PCGSplineSamplerParams.alpha_attribute"></a>

#### alpha_attribute

```python
@alpha_attribute.setter
def alpha_attribute(value: Name) -> None
```

<a id="unreal.PCGSplineSamplerParams.compute_distance"></a>

#### compute_distance

```python
@property
def compute_distance() -> bool
```

(bool):  [Read-Write] Compute distance along the spline and write it to an attribute.

<a id="unreal.PCGSplineSamplerParams.compute_distance"></a>

#### compute_distance

```python
@compute_distance.setter
def compute_distance(value: bool) -> None
```

<a id="unreal.PCGSplineSamplerParams.distance_attribute"></a>

#### distance_attribute

```python
@property
def distance_attribute() -> Name
```

(Name):  [Read-Write] Attribute that will contain the distance along the spline at the sample point.

<a id="unreal.PCGSplineSamplerParams.distance_attribute"></a>

#### distance_attribute

```python
@distance_attribute.setter
def distance_attribute(value: Name) -> None
```

<a id="unreal.PCGSplineSamplerParams.compute_input_key"></a>

#### compute_input_key

```python
@property
def compute_input_key() -> bool
```

(bool):  [Read-Write] Compute an input key for each point along the spline and write the key to an attribute.

<a id="unreal.PCGSplineSamplerParams.compute_input_key"></a>

#### compute_input_key

```python
@compute_input_key.setter
def compute_input_key(value: bool) -> None
```

<a id="unreal.PCGSplineSamplerParams.input_key_attribute"></a>

#### input_key_attribute

```python
@property
def input_key_attribute() -> Name
```

(Name):  [Read-Write] Attribute that will contain the spline input key, a float value between [0, N], where N is the number of control points. Each range [i, i+1] represents an interpolation from 0 to 1 across spline segment i.

<a id="unreal.PCGSplineSamplerParams.input_key_attribute"></a>

#### input_key_attribute

```python
@input_key_attribute.setter
def input_key_attribute(value: Name) -> None
```

<a id="unreal.PCGSplineSamplerParams.unbounded"></a>

#### unbounded

```python
@property
def unbounded() -> bool
```

(bool):  [Read-Write] If no Bounding Shape input is provided, the actor bounds are used to limit the sample generation domain.
This option allows ignoring the actor bounds and generating over the entire spline. Use with caution as this
may generate a lot of points.

<a id="unreal.PCGSplineSamplerParams.unbounded"></a>

#### unbounded

```python
@unbounded.setter
def unbounded(value: bool) -> None
```

<a id="unreal.PCGSplineSamplerParams.point_steepness"></a>

#### point_steepness

```python
@property
def point_steepness() -> float
```

(float):  [Read-Write] Each PCG point represents a discretized, volumetric region of world space. The points' Steepness value [0.0 to
1.0] establishes how "hard" or "soft" that volume will be represented. From 0, it will ramp up linearly
increasing its influence over the density from the point's center to up to two times the bounds. At 1, it will
represent a binary box function with the size of the point's bounds.

<a id="unreal.PCGSplineSamplerParams.point_steepness"></a>

#### point_steepness

```python
@point_steepness.setter
def point_steepness(value: float) -> None
```

<a id="unreal.PCGSplineSamplerParams.seeding_mode"></a>

#### seeding_mode

```python
@property
def seeding_mode() -> PCGSplineSamplingSeedingMode
```

(PCGSplineSamplingSeedingMode):  [Read-Write] Controls the mode for computing a sample point's seed.

<a id="unreal.PCGSplineSamplerParams.seeding_mode"></a>

#### seeding_mode

```python
@seeding_mode.setter
def seeding_mode(value: PCGSplineSamplingSeedingMode) -> None
```

<a id="unreal.PCGSplineSamplerParams.seed_from_local_position"></a>

#### seed_from_local_position

```python
@property
def seed_from_local_position() -> bool
```

(bool):  [Read-Write] Controls whether we will seed the sampled points using the final world position or the local position.

<a id="unreal.PCGSplineSamplerParams.seed_from_local_position"></a>

#### seed_from_local_position

```python
@seed_from_local_position.setter
def seed_from_local_position(value: bool) -> None
```

<a id="unreal.PCGSplineSamplerParams.seed_from2d_position"></a>

#### seed_from2d_position

```python
@property
def seed_from2d_position() -> bool
```

(bool):  [Read-Write] Controls whether we will seed the sampled points using the 3D position or the 2D (XY) position.

<a id="unreal.PCGSplineSamplerParams.seed_from2d_position"></a>

#### seed_from2d_position

```python
@seed_from2d_position.setter
def seed_from2d_position(value: bool) -> None
```

<a id="unreal.PCGLandscapeLayerWeight"></a>