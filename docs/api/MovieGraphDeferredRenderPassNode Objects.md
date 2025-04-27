## MovieGraphDeferredRenderPassNode Objects

```python
class MovieGraphDeferredRenderPassNode(MovieGraphImagePassBaseNode)
```

A render node which uses the Deferred Renderer.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineRenderPasses
- **File**: MovieGraphDeferredPassNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_post_process_materials`` (Array[MoviePipelinePostProcessPass]):  [Read-Write] An array of additional post-processing materials to run after the frame is rendered. Using this feature may add a notable amount of render time.
- ``allow_ocio`` (bool):  [Read-Write] Allow the output file OpenColorIO transform to be used on this render.
- ``anti_aliasing_method`` (AntiAliasingMethod):  [Read-Write] Which anti-aliasing method should this render use. If this is set to None, then Movie Render Graph
  will handle anti-aliasing by doing a sub-pixel jitter (one for each temporal/spatial sample). Some
  rendering effects rely on TSR or TAA to reduce noise so we recommend leaving them enabled
  where possible. All options work with Spatial and Temporal samples, but TSR/TAA may introduce minor
  visual artifacts (such as ghosting). MSAA is not supported in the deferred renderer.
- ``disable_tone_curve`` (bool):  [Read-Write] If true, the tone curve will be disabled for this render pass. This will result in values greater than 1.0 in final renders
  and can optionally be combined with OCIO profiles on the file output nodes to convert from Linear Values in Working Color Space
  (which is sRGB  (Rec. 709) by default, unless changed in the project settings).
- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``override_additional_post_process_materials`` (bool):  [Read-Write]
- ``override_anti_aliasing_method`` (bool):  [Read-Write]
- ``override_b_allow_ocio`` (bool):  [Read-Write]
- ``override_b_disable_tone_curve`` (bool):  [Read-Write]
- ``override_b_write_all_samples`` (bool):  [Read-Write]
- ``override_show_flags`` (bool):  [Read-Write] Note: Since *individual* show flags are overridden instead of the entire ShowFlags property, manually set to
  overridden so the traversal picks the changes up (otherwise they will be ignored).
- ``override_spatial_sample_count`` (bool):  [Read-Write]
- ``override_view_mode_index`` (bool):  [Read-Write]
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.
- ``show_flags`` (MovieGraphShowFlags):  [Read-Only] The show flags that should be active during a render for this node.
- ``spatial_sample_count`` (int32):  [Read-Write] How many sub-pixel jitter renders should we do per temporal sample? This can be used to achieve high
  sample counts without Temporal Sub-Sampling (allowing high sample counts without motion blur being enabled),
  but we generally recommend using Temporal Sub-Samples when possible. It can also be combined with
  temporal samples and you will get SpatialSampleCount many renders per temporal sample.
- ``view_mode_index`` (ViewModeIndex):  [Read-Write] The view mode index that will be applied to renders. These mirror the View Modes you find in the Viewport,
  but most view modes other than Lit are used for debugging so they may not do what you expect, or may
  have to be used in combination with certain Show Flags to produce a result similar to what you see in
  the viewport.
- ``write_all_samples`` (bool):  [Read-Write] Debug Feature. Can use this to write out each individual Temporal and Spatial sample rendered by this render pass,
  which allows you to see which images are being accumulated together. Can be useful for debugging incorrect looking
  frames to see which sub-frame evaluations were incorrect.

<a id="unreal.MovieGraphDeferredRenderPassNode.override_spatial_sample_count"></a>

#### override_spatial_sample_count

```python
@property
def override_spatial_sample_count() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphDeferredRenderPassNode.override_spatial_sample_count"></a>

#### override_spatial_sample_count

```python
@override_spatial_sample_count.setter
def override_spatial_sample_count(value: bool) -> None
```

<a id="unreal.MovieGraphDeferredRenderPassNode.override_anti_aliasing_method"></a>

#### override_anti_aliasing_method

```python
@property
def override_anti_aliasing_method() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphDeferredRenderPassNode.override_anti_aliasing_method"></a>

#### override_anti_aliasing_method

```python
@override_anti_aliasing_method.setter
def override_anti_aliasing_method(value: bool) -> None
```

<a id="unreal.MovieGraphDeferredRenderPassNode.override_b_disable_tone_curve"></a>

#### override_b_disable_tone_curve

```python
@property
def override_b_disable_tone_curve() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphDeferredRenderPassNode.override_b_disable_tone_curve"></a>

#### override_b_disable_tone_curve

```python
@override_b_disable_tone_curve.setter
def override_b_disable_tone_curve(value: bool) -> None
```

<a id="unreal.MovieGraphDeferredRenderPassNode.override_b_allow_ocio"></a>

#### override_b_allow_ocio

```python
@property
def override_b_allow_ocio() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphDeferredRenderPassNode.override_b_allow_ocio"></a>

#### override_b_allow_ocio

```python
@override_b_allow_ocio.setter
def override_b_allow_ocio(value: bool) -> None
```

<a id="unreal.MovieGraphDeferredRenderPassNode.override_view_mode_index"></a>

#### override_view_mode_index

```python
@property
def override_view_mode_index() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphDeferredRenderPassNode.override_view_mode_index"></a>

#### override_view_mode_index

```python
@override_view_mode_index.setter
def override_view_mode_index(value: bool) -> None
```

<a id="unreal.MovieGraphDeferredRenderPassNode.override_b_write_all_samples"></a>

#### override_b_write_all_samples

```python
@property
def override_b_write_all_samples() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphDeferredRenderPassNode.override_b_write_all_samples"></a>

#### override_b_write_all_samples

```python
@override_b_write_all_samples.setter
def override_b_write_all_samples(value: bool) -> None
```

<a id="unreal.MovieGraphDeferredRenderPassNode.override_additional_post_process_materials"></a>

#### override_additional_post_process_materials

```python
@property
def override_additional_post_process_materials() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphDeferredRenderPassNode.override_additional_post_process_materials"></a>

#### override_additional_post_process_materials

```python
@override_additional_post_process_materials.setter
def override_additional_post_process_materials(value: bool) -> None
```

<a id="unreal.MovieGraphDeferredRenderPassNode.spatial_sample_count"></a>

#### spatial_sample_count

```python
@property
def spatial_sample_count() -> int
```

(int32):  [Read-Write] How many sub-pixel jitter renders should we do per temporal sample? This can be used to achieve high
sample counts without Temporal Sub-Sampling (allowing high sample counts without motion blur being enabled),
but we generally recommend using Temporal Sub-Samples when possible. It can also be combined with
temporal samples and you will get SpatialSampleCount many renders per temporal sample.

<a id="unreal.MovieGraphDeferredRenderPassNode.spatial_sample_count"></a>

#### spatial_sample_count

```python
@spatial_sample_count.setter
def spatial_sample_count(value: int) -> None
```

<a id="unreal.MovieGraphDeferredRenderPassNode.anti_aliasing_method"></a>

#### anti_aliasing_method

```python
@property
def anti_aliasing_method() -> AntiAliasingMethod
```

(AntiAliasingMethod):  [Read-Write] Which anti-aliasing method should this render use. If this is set to None, then Movie Render Graph
will handle anti-aliasing by doing a sub-pixel jitter (one for each temporal/spatial sample). Some
rendering effects rely on TSR or TAA to reduce noise so we recommend leaving them enabled
where possible. All options work with Spatial and Temporal samples, but TSR/TAA may introduce minor
visual artifacts (such as ghosting). MSAA is not supported in the deferred renderer.

<a id="unreal.MovieGraphDeferredRenderPassNode.anti_aliasing_method"></a>

#### anti_aliasing_method

```python
@anti_aliasing_method.setter
def anti_aliasing_method(value: AntiAliasingMethod) -> None
```

<a id="unreal.MovieGraphDeferredRenderPassNode.write_all_samples"></a>

#### write_all_samples

```python
@property
def write_all_samples() -> bool
```

(bool):  [Read-Write] Debug Feature. Can use this to write out each individual Temporal and Spatial sample rendered by this render pass,
which allows you to see which images are being accumulated together. Can be useful for debugging incorrect looking
frames to see which sub-frame evaluations were incorrect.

<a id="unreal.MovieGraphDeferredRenderPassNode.write_all_samples"></a>

#### write_all_samples

```python
@write_all_samples.setter
def write_all_samples(value: bool) -> None
```

<a id="unreal.MovieGraphDeferredRenderPassNode.disable_tone_curve"></a>

#### disable_tone_curve

```python
@property
def disable_tone_curve() -> bool
```

(bool):  [Read-Write] If true, the tone curve will be disabled for this render pass. This will result in values greater than 1.0 in final renders
and can optionally be combined with OCIO profiles on the file output nodes to convert from Linear Values in Working Color Space
(which is sRGB  (Rec. 709) by default, unless changed in the project settings).

<a id="unreal.MovieGraphDeferredRenderPassNode.disable_tone_curve"></a>

#### disable_tone_curve

```python
@disable_tone_curve.setter
def disable_tone_curve(value: bool) -> None
```

<a id="unreal.MovieGraphDeferredRenderPassNode.allow_ocio"></a>

#### allow_ocio

```python
@property
def allow_ocio() -> bool
```

(bool):  [Read-Write] Allow the output file OpenColorIO transform to be used on this render.

<a id="unreal.MovieGraphDeferredRenderPassNode.allow_ocio"></a>

#### allow_ocio

```python
@allow_ocio.setter
def allow_ocio(value: bool) -> None
```

<a id="unreal.MovieGraphDeferredRenderPassNode.view_mode_index"></a>

#### view_mode_index

```python
@property
def view_mode_index() -> ViewModeIndex
```

(ViewModeIndex):  [Read-Write] The view mode index that will be applied to renders. These mirror the View Modes you find in the Viewport,
but most view modes other than Lit are used for debugging so they may not do what you expect, or may
have to be used in combination with certain Show Flags to produce a result similar to what you see in
the viewport.

<a id="unreal.MovieGraphDeferredRenderPassNode.view_mode_index"></a>

#### view_mode_index

```python
@view_mode_index.setter
def view_mode_index(value: ViewModeIndex) -> None
```

<a id="unreal.MovieGraphDeferredRenderPassNode.additional_post_process_materials"></a>

#### additional_post_process_materials

```python
@property
def additional_post_process_materials() -> Array[MoviePipelinePostProcessPass]
```

(Array[MoviePipelinePostProcessPass]):  [Read-Write] An array of additional post-processing materials to run after the frame is rendered. Using this feature may add a notable amount of render time.

<a id="unreal.MovieGraphDeferredRenderPassNode.additional_post_process_materials"></a>

#### additional_post_process_materials

```python
@additional_post_process_materials.setter
def additional_post_process_materials(
        value: Array[MoviePipelinePostProcessPass]) -> None
```

<a id="unreal.MovieGraphImageSequenceOutputNode"></a>