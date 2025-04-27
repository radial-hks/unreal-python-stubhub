## GeometryScript_MeshSampling Objects

```python
class GeometryScript_MeshSampling(BlueprintFunctionLibrary)
```

Geometry Script Library Mesh Sampling Functions

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshSamplingFunctions.h

<a id="unreal.GeometryScript_MeshSampling.compute_vertex_weighted_point_sampling"></a>

#### compute_vertex_weighted_point_sampling

```python
@classmethod
def compute_vertex_weighted_point_sampling(
    cls,
    target_mesh: DynamicMesh,
    options: GeometryScriptMeshPointSamplingOptions,
    non_uniform_options: GeometryScriptNonUniformPointSamplingOptions,
    vertex_weights: GeometryScriptScalarList,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[Transform], Array[float],
           GeometryScriptIndexList]
```

X.compute_vertex_weighted_point_sampling(target_mesh, options, non_uniform_options, vertex_weights, debug=None) -> (DynamicMesh, samples=Array[Transform], sample_radii=Array[double], triangle_i_ds=GeometryScriptIndexList)
Compute a set of sample points lying on the surface of TargetMesh based on the provided sampling Options and NonUniformOptions.
The sample points have radii in the range [Options.SamplingRadius, NonUniformOptions.MaxSamplingRadius], and
are non-overlapping, ie the distance between two points is always larger than the sum of their respective radii.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptMeshPointSamplingOptions): 
    non_uniform_options (GeometryScriptNonUniformPointSamplingOptions): 
    vertex_weights (GeometryScriptScalarList): defines a per-vertex weight in range [0,1], these are interpolated to create a scalar field over the mesh triangles which is used to weight the sampling radii
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    samples (Array[Transform]): 

    sample_radii (Array[double]): 

    triangle_i_ds (GeometryScriptIndexList):

<a id="unreal.GeometryScript_MeshSampling.compute_render_capture_point_sampling"></a>

#### compute_render_capture_point_sampling

```python
@classmethod
def compute_render_capture_point_sampling(
        cls,
        actors: Array[Actor],
        cameras: Array[GeometryScriptRenderCaptureCamera],
        debug: GeometryScriptDebug = None) -> Array[Transform]
```

X.compute_render_capture_point_sampling(actors, cameras, debug=None) -> Array[Transform]
Compute oriented sample points on the visible surfaces of the given Actors
The Samples are computed using Render Capture from the given virtual Cameras

Args:
    actors (Array[Actor]): 
    cameras (Array[GeometryScriptRenderCaptureCamera]): 
    debug (GeometryScriptDebug): 

Returns:
    Array[Transform]: 

    samples (Array[Transform]):

<a id="unreal.GeometryScript_MeshSampling.compute_render_capture_cameras_for_box"></a>

#### compute_render_capture_cameras_for_box

```python
@classmethod
def compute_render_capture_cameras_for_box(
    cls,
    box: Box,
    options: GeometryScriptRenderCaptureCamerasForBoxOptions,
    debug: GeometryScriptDebug = None
) -> Array[GeometryScriptRenderCaptureCamera]
```

X.compute_render_capture_cameras_for_box(box, options, debug=None) -> Array[GeometryScriptRenderCaptureCamera]
Compute a set of Render Capture Cameras to capture a scene within the given Box

Args:
    box (Box): Bounding Box containing the scene to be captured
    options (GeometryScriptRenderCaptureCamerasForBoxOptions): Defines the Camera viewing directions into the box and other Camera parameters
    debug (GeometryScriptDebug): 

Returns:
    Array[GeometryScriptRenderCaptureCamera]: 

    cameras (Array[GeometryScriptRenderCaptureCamera]): Output Cameras with view frustums that contain the Box while maintaining the desired FOV

<a id="unreal.GeometryScript_MeshSampling.compute_point_sampling"></a>

#### compute_point_sampling

```python
@classmethod
def compute_point_sampling(
    cls,
    target_mesh: DynamicMesh,
    options: GeometryScriptMeshPointSamplingOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[Transform], GeometryScriptIndexList]
```

X.compute_point_sampling(target_mesh, options, debug=None) -> (DynamicMesh, samples=Array[Transform], triangle_i_ds=GeometryScriptIndexList)
Compute a set of sample points lying on the surface of TargetMesh based on the provided sampling Options.
Samples are approximately uniformly distributed, and non-overlapping relative to the provided Options.SamplingRadius,
ie the distance between any pair of samples if >= 2*SamplingRadius.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptMeshPointSamplingOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    samples (Array[Transform]): output list of sample points. Transform Location is sample position, Rotation orients Z with the triangle normal

    triangle_i_ds (GeometryScriptIndexList): TriangleID that contains each sample point. Length is the same as Samples array.

<a id="unreal.GeometryScript_MeshSampling.compute_non_uniform_point_sampling"></a>

#### compute_non_uniform_point_sampling

```python
@classmethod
def compute_non_uniform_point_sampling(
    cls,
    target_mesh: DynamicMesh,
    options: GeometryScriptMeshPointSamplingOptions,
    non_uniform_options: GeometryScriptNonUniformPointSamplingOptions,
    debug: GeometryScriptDebug = None
) -> Tuple[DynamicMesh, Array[Transform], Array[float],
           GeometryScriptIndexList]
```

X.compute_non_uniform_point_sampling(target_mesh, options, non_uniform_options, debug=None) -> (DynamicMesh, samples=Array[Transform], sample_radii=Array[double], triangle_i_ds=GeometryScriptIndexList)
Compute a set of sample points lying on the surface of TargetMesh based on the provided sampling Options and NonUniformOptions.
The sample points have radii in the range [Options.SamplingRadius, NonUniformOptions.MaxSamplingRadius], and
are non-overlapping, ie the distance between two points is always larger than the sum of their respective radii.

Args:
    target_mesh (DynamicMesh): 
    options (GeometryScriptMeshPointSamplingOptions): 
    non_uniform_options (GeometryScriptNonUniformPointSamplingOptions): 
    debug (GeometryScriptDebug): 

Returns:
    tuple: 

    samples (Array[Transform]): 

    sample_radii (Array[double]): 

    triangle_i_ds (GeometryScriptIndexList):

<a id="unreal.GeometryScript_MeshSelection"></a>