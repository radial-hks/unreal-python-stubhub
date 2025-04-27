## MovieGraphPathTracerRenderPassNode Objects

```python
class MovieGraphPathTracerRenderPassNode(MovieGraphImagePassBaseNode)
```

A render node which uses the path tracer.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineRenderPasses
- **File**: MovieGraphPathTracerPassNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_post_process_materials`` (Array[MoviePipelinePostProcessPass]):  [Read-Write] An array of additional post-processing materials to run after the frame is rendered. Using this feature may add a notable amount of render time.
- ``allow_ocio`` (bool):  [Read-Write] Allow the output file OpenColorIO transform to be used on this render.
- ``denoiser_type`` (MovieGraphPathTracerDenoiserType):  [Read-Write] Select which type of denoiser to use when the denoiser is enabled. Temporal denoisers will provide better results when
  denoising animated sequences (the denoising results will look more stable), especially when combined with an appropriate
  Frame Count (non-zero). Denoisers are implemented as plugins so you may need to enable a plugin as well for this to work.
- ``disable_tone_curve`` (bool):  [Read-Write] If true, the tone curve will be disabled for this render pass. This will result in values greater than 1.0 in final renders
  and can optionally be combined with OCIO profiles on the file output nodes to convert from Linear Values in Working Color Space
  (which is sRGB  (Rec. 709) by default, unless changed in the project settings).
- ``dynamic_properties`` (InstancedPropertyBag):  [Read-Write] Properties which can be dynamically declared on the node (vs. native properties which are always present).
- ``enable_denoiser`` (bool):  [Read-Write] If true the resulting image will be denoised at the end of each set of Spatial Samples.
- ``enable_reference_motion_blur`` (bool):  [Read-Write] When enabled, the path tracer will blend all spatial and temporal samples prior to the denoising and will disable post-processed motion blur.
  In this mode it is possible to use higher temporal sample counts to improve the motion blur quality. This mode also automatically enabled reference DOF.
  When this option is disabled, the path tracer will accumulate spatial samples, but denoise them prior to accumulation of temporal samples.
- ``frame_count`` (int32):  [Read-Write] The number of frames to consider when using temporal-based denoisers. Generally higher numbers will result in longer
  denoising times and higher memory requirements. For NFOR this number refers to how many frames to consider on both sides
  of the current frame (ie: 2 means consider 2 before, and 2 after the currently denoised frame), but other denoiser
  implementations may interpret this value differently.
- ``lighting_components_include_diffuse`` (bool):  [Read-Write] Whether the render should include diffuse lighting contributions.
- ``lighting_components_include_emissive`` (bool):  [Read-Write] Whether the render should include directly visible emissive components.
- ``lighting_components_include_indirect_diffuse`` (bool):  [Read-Write] Whether the render should include indirect diffuse lighting contributions.
- ``lighting_components_include_indirect_specular`` (bool):  [Read-Write] Whether the render should include indirect specular lighting contributions.
- ``lighting_components_include_indirect_volume`` (bool):  [Read-Write] Whether the render should include indirect volume lighting contributions.
- ``lighting_components_include_specular`` (bool):  [Read-Write] Whether the render should include specular lighting contributions.
- ``lighting_components_include_volume`` (bool):  [Read-Write] Whether the render should include volume lighting contributions.
- ``override_additional_post_process_materials`` (bool):  [Read-Write]
- ``override_b_allow_ocio`` (bool):  [Read-Write]
- ``override_b_disable_tone_curve`` (bool):  [Read-Write]
- ``override_b_enable_denoiser`` (bool):  [Read-Write]
- ``override_b_enable_reference_motion_blur`` (bool):  [Read-Write]
- ``override_b_lighting_components_include_diffuse`` (bool):  [Read-Write]
- ``override_b_lighting_components_include_emissive`` (bool):  [Read-Write]
- ``override_b_lighting_components_include_indirect_diffuse`` (bool):  [Read-Write]
- ``override_b_lighting_components_include_indirect_specular`` (bool):  [Read-Write]
- ``override_b_lighting_components_include_indirect_volume`` (bool):  [Read-Write]
- ``override_b_lighting_components_include_specular`` (bool):  [Read-Write]
- ``override_b_lighting_components_include_volume`` (bool):  [Read-Write]
- ``override_b_write_all_samples`` (bool):  [Read-Write]
- ``override_denoiser_type`` (bool):  [Read-Write]
- ``override_frame_count`` (bool):  [Read-Write]
- ``override_show_flags`` (bool):  [Read-Write] Note: Since *individual* show flags are overridden instead of the entire ShowFlags property, manually set to
  overridden so the traversal picks the changes up (otherwise they will be ignored).
- ``override_spatial_sample_count`` (bool):  [Read-Write]
- ``script_tags`` (Array[str]):  [Read-Write] Tags that can be used to identify this node within a pre/post render script. Tags can be unique in order to identify this specific node,
  or the same tag can be applied to multiple nodes in order to identify a grouping of nodes.
- ``show_flags`` (MovieGraphShowFlags):  [Read-Only] The show flags that should be active during a render for this node.
- ``spatial_sample_count`` (int32):  [Read-Write] How many sub-pixel jitter renders should we do per temporal sample? This can be used to achieve high
  sample counts without Temporal Sub-Sampling (allowing high sample counts without motion blur being enabled),
  but we generally recommend using Temporal Sub-Samples when possible. It can also be combined with
  temporal samples and you will get SpatialSampleCount many renders per temporal sample.
- ``write_all_samples`` (bool):  [Read-Write] Debug Feature. This can be used to write out each individual spatial sample rendered by this render pass,
  which allows you to see which images are being accumulated together. Can be useful for debugging incorrect looking
  frames to see which sub-frame evaluations were incorrect.

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_spatial_sample_count"></a>

#### override_spatial_sample_count

```python
@property
def override_spatial_sample_count() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_spatial_sample_count"></a>

#### override_spatial_sample_count

```python
@override_spatial_sample_count.setter
def override_spatial_sample_count(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_enable_reference_motion_blur"></a>

#### override_b_enable_reference_motion_blur

```python
@property
def override_b_enable_reference_motion_blur() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_enable_reference_motion_blur"></a>

#### override_b_enable_reference_motion_blur

```python
@override_b_enable_reference_motion_blur.setter
def override_b_enable_reference_motion_blur(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_enable_denoiser"></a>

#### override_b_enable_denoiser

```python
@property
def override_b_enable_denoiser() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_enable_denoiser"></a>

#### override_b_enable_denoiser

```python
@override_b_enable_denoiser.setter
def override_b_enable_denoiser(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_denoiser_type"></a>

#### override_denoiser_type

```python
@property
def override_denoiser_type() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_denoiser_type"></a>

#### override_denoiser_type

```python
@override_denoiser_type.setter
def override_denoiser_type(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_frame_count"></a>

#### override_frame_count

```python
@property
def override_frame_count() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_frame_count"></a>

#### override_frame_count

```python
@override_frame_count.setter
def override_frame_count(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_disable_tone_curve"></a>

#### override_b_disable_tone_curve

```python
@property
def override_b_disable_tone_curve() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_disable_tone_curve"></a>

#### override_b_disable_tone_curve

```python
@override_b_disable_tone_curve.setter
def override_b_disable_tone_curve(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_allow_ocio"></a>

#### override_b_allow_ocio

```python
@property
def override_b_allow_ocio() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_allow_ocio"></a>

#### override_b_allow_ocio

```python
@override_b_allow_ocio.setter
def override_b_allow_ocio(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_lighting_components_include_emissive"></a>

#### override_b_lighting_components_include_emissive

```python
@property
def override_b_lighting_components_include_emissive() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_lighting_components_include_emissive"></a>

#### override_b_lighting_components_include_emissive

```python
@override_b_lighting_components_include_emissive.setter
def override_b_lighting_components_include_emissive(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_lighting_components_include_diffuse"></a>

#### override_b_lighting_components_include_diffuse

```python
@property
def override_b_lighting_components_include_diffuse() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_lighting_components_include_diffuse"></a>

#### override_b_lighting_components_include_diffuse

```python
@override_b_lighting_components_include_diffuse.setter
def override_b_lighting_components_include_diffuse(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_lighting_components_include_indirect_diffuse"></a>

#### override_b_lighting_components_include_indirect_diffuse

```python
@property
def override_b_lighting_components_include_indirect_diffuse() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_lighting_components_include_indirect_diffuse"></a>

#### override_b_lighting_components_include_indirect_diffuse

```python
@override_b_lighting_components_include_indirect_diffuse.setter
def override_b_lighting_components_include_indirect_diffuse(
        value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_lighting_components_include_specular"></a>

#### override_b_lighting_components_include_specular

```python
@property
def override_b_lighting_components_include_specular() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_lighting_components_include_specular"></a>

#### override_b_lighting_components_include_specular

```python
@override_b_lighting_components_include_specular.setter
def override_b_lighting_components_include_specular(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_lighting_components_include_indirect_specular"></a>

#### override_b_lighting_components_include_indirect_specular

```python
@property
def override_b_lighting_components_include_indirect_specular() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_lighting_components_include_indirect_specular"></a>

#### override_b_lighting_components_include_indirect_specular

```python
@override_b_lighting_components_include_indirect_specular.setter
def override_b_lighting_components_include_indirect_specular(
        value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_lighting_components_include_volume"></a>

#### override_b_lighting_components_include_volume

```python
@property
def override_b_lighting_components_include_volume() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_lighting_components_include_volume"></a>

#### override_b_lighting_components_include_volume

```python
@override_b_lighting_components_include_volume.setter
def override_b_lighting_components_include_volume(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_lighting_components_include_indirect_volume"></a>

#### override_b_lighting_components_include_indirect_volume

```python
@property
def override_b_lighting_components_include_indirect_volume() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_lighting_components_include_indirect_volume"></a>

#### override_b_lighting_components_include_indirect_volume

```python
@override_b_lighting_components_include_indirect_volume.setter
def override_b_lighting_components_include_indirect_volume(
        value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_write_all_samples"></a>

#### override_b_write_all_samples

```python
@property
def override_b_write_all_samples() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_b_write_all_samples"></a>

#### override_b_write_all_samples

```python
@override_b_write_all_samples.setter
def override_b_write_all_samples(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_additional_post_process_materials"></a>

#### override_additional_post_process_materials

```python
@property
def override_additional_post_process_materials() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieGraphPathTracerRenderPassNode.override_additional_post_process_materials"></a>

#### override_additional_post_process_materials

```python
@override_additional_post_process_materials.setter
def override_additional_post_process_materials(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.spatial_sample_count"></a>

#### spatial_sample_count

```python
@property
def spatial_sample_count() -> int
```

(int32):  [Read-Write] How many sub-pixel jitter renders should we do per temporal sample? This can be used to achieve high
sample counts without Temporal Sub-Sampling (allowing high sample counts without motion blur being enabled),
but we generally recommend using Temporal Sub-Samples when possible. It can also be combined with
temporal samples and you will get SpatialSampleCount many renders per temporal sample.

<a id="unreal.MovieGraphPathTracerRenderPassNode.spatial_sample_count"></a>

#### spatial_sample_count

```python
@spatial_sample_count.setter
def spatial_sample_count(value: int) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.enable_reference_motion_blur"></a>

#### enable_reference_motion_blur

```python
@property
def enable_reference_motion_blur() -> bool
```

(bool):  [Read-Write] When enabled, the path tracer will blend all spatial and temporal samples prior to the denoising and will disable post-processed motion blur.
In this mode it is possible to use higher temporal sample counts to improve the motion blur quality. This mode also automatically enabled reference DOF.
When this option is disabled, the path tracer will accumulate spatial samples, but denoise them prior to accumulation of temporal samples.

<a id="unreal.MovieGraphPathTracerRenderPassNode.enable_reference_motion_blur"></a>

#### enable_reference_motion_blur

```python
@enable_reference_motion_blur.setter
def enable_reference_motion_blur(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.enable_denoiser"></a>

#### enable_denoiser

```python
@property
def enable_denoiser() -> bool
```

(bool):  [Read-Write] If true the resulting image will be denoised at the end of each set of Spatial Samples.

<a id="unreal.MovieGraphPathTracerRenderPassNode.enable_denoiser"></a>

#### enable_denoiser

```python
@enable_denoiser.setter
def enable_denoiser(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.denoiser_type"></a>

#### denoiser_type

```python
@property
def denoiser_type() -> MovieGraphPathTracerDenoiserType
```

(MovieGraphPathTracerDenoiserType):  [Read-Write] Select which type of denoiser to use when the denoiser is enabled. Temporal denoisers will provide better results when
denoising animated sequences (the denoising results will look more stable), especially when combined with an appropriate
Frame Count (non-zero). Denoisers are implemented as plugins so you may need to enable a plugin as well for this to work.

<a id="unreal.MovieGraphPathTracerRenderPassNode.denoiser_type"></a>

#### denoiser_type

```python
@denoiser_type.setter
def denoiser_type(value: MovieGraphPathTracerDenoiserType) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.frame_count"></a>

#### frame_count

```python
@property
def frame_count() -> int
```

(int32):  [Read-Write] The number of frames to consider when using temporal-based denoisers. Generally higher numbers will result in longer
denoising times and higher memory requirements. For NFOR this number refers to how many frames to consider on both sides
of the current frame (ie: 2 means consider 2 before, and 2 after the currently denoised frame), but other denoiser
implementations may interpret this value differently.

<a id="unreal.MovieGraphPathTracerRenderPassNode.frame_count"></a>

#### frame_count

```python
@frame_count.setter
def frame_count(value: int) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.write_all_samples"></a>

#### write_all_samples

```python
@property
def write_all_samples() -> bool
```

(bool):  [Read-Write] Debug Feature. This can be used to write out each individual spatial sample rendered by this render pass,
which allows you to see which images are being accumulated together. Can be useful for debugging incorrect looking
frames to see which sub-frame evaluations were incorrect.

<a id="unreal.MovieGraphPathTracerRenderPassNode.write_all_samples"></a>

#### write_all_samples

```python
@write_all_samples.setter
def write_all_samples(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.disable_tone_curve"></a>

#### disable_tone_curve

```python
@property
def disable_tone_curve() -> bool
```

(bool):  [Read-Write] If true, the tone curve will be disabled for this render pass. This will result in values greater than 1.0 in final renders
and can optionally be combined with OCIO profiles on the file output nodes to convert from Linear Values in Working Color Space
(which is sRGB  (Rec. 709) by default, unless changed in the project settings).

<a id="unreal.MovieGraphPathTracerRenderPassNode.disable_tone_curve"></a>

#### disable_tone_curve

```python
@disable_tone_curve.setter
def disable_tone_curve(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.allow_ocio"></a>

#### allow_ocio

```python
@property
def allow_ocio() -> bool
```

(bool):  [Read-Write] Allow the output file OpenColorIO transform to be used on this render.

<a id="unreal.MovieGraphPathTracerRenderPassNode.allow_ocio"></a>

#### allow_ocio

```python
@allow_ocio.setter
def allow_ocio(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.lighting_components_include_emissive"></a>

#### lighting_components_include_emissive

```python
@property
def lighting_components_include_emissive() -> bool
```

(bool):  [Read-Write] Whether the render should include directly visible emissive components.

<a id="unreal.MovieGraphPathTracerRenderPassNode.lighting_components_include_emissive"></a>

#### lighting_components_include_emissive

```python
@lighting_components_include_emissive.setter
def lighting_components_include_emissive(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.lighting_components_include_diffuse"></a>

#### lighting_components_include_diffuse

```python
@property
def lighting_components_include_diffuse() -> bool
```

(bool):  [Read-Write] Whether the render should include diffuse lighting contributions.

<a id="unreal.MovieGraphPathTracerRenderPassNode.lighting_components_include_diffuse"></a>

#### lighting_components_include_diffuse

```python
@lighting_components_include_diffuse.setter
def lighting_components_include_diffuse(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.lighting_components_include_indirect_diffuse"></a>

#### lighting_components_include_indirect_diffuse

```python
@property
def lighting_components_include_indirect_diffuse() -> bool
```

(bool):  [Read-Write] Whether the render should include indirect diffuse lighting contributions.

<a id="unreal.MovieGraphPathTracerRenderPassNode.lighting_components_include_indirect_diffuse"></a>

#### lighting_components_include_indirect_diffuse

```python
@lighting_components_include_indirect_diffuse.setter
def lighting_components_include_indirect_diffuse(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.lighting_components_include_specular"></a>

#### lighting_components_include_specular

```python
@property
def lighting_components_include_specular() -> bool
```

(bool):  [Read-Write] Whether the render should include specular lighting contributions.

<a id="unreal.MovieGraphPathTracerRenderPassNode.lighting_components_include_specular"></a>

#### lighting_components_include_specular

```python
@lighting_components_include_specular.setter
def lighting_components_include_specular(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.lighting_components_include_indirect_specular"></a>

#### lighting_components_include_indirect_specular

```python
@property
def lighting_components_include_indirect_specular() -> bool
```

(bool):  [Read-Write] Whether the render should include indirect specular lighting contributions.

<a id="unreal.MovieGraphPathTracerRenderPassNode.lighting_components_include_indirect_specular"></a>

#### lighting_components_include_indirect_specular

```python
@lighting_components_include_indirect_specular.setter
def lighting_components_include_indirect_specular(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.lighting_components_include_volume"></a>

#### lighting_components_include_volume

```python
@property
def lighting_components_include_volume() -> bool
```

(bool):  [Read-Write] Whether the render should include volume lighting contributions.

<a id="unreal.MovieGraphPathTracerRenderPassNode.lighting_components_include_volume"></a>

#### lighting_components_include_volume

```python
@lighting_components_include_volume.setter
def lighting_components_include_volume(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.lighting_components_include_indirect_volume"></a>

#### lighting_components_include_indirect_volume

```python
@property
def lighting_components_include_indirect_volume() -> bool
```

(bool):  [Read-Write] Whether the render should include indirect volume lighting contributions.

<a id="unreal.MovieGraphPathTracerRenderPassNode.lighting_components_include_indirect_volume"></a>

#### lighting_components_include_indirect_volume

```python
@lighting_components_include_indirect_volume.setter
def lighting_components_include_indirect_volume(value: bool) -> None
```

<a id="unreal.MovieGraphPathTracerRenderPassNode.additional_post_process_materials"></a>

#### additional_post_process_materials

```python
@property
def additional_post_process_materials() -> Array[MoviePipelinePostProcessPass]
```

(Array[MoviePipelinePostProcessPass]):  [Read-Write] An array of additional post-processing materials to run after the frame is rendered. Using this feature may add a notable amount of render time.

<a id="unreal.MovieGraphPathTracerRenderPassNode.additional_post_process_materials"></a>

#### additional_post_process_materials

```python
@additional_post_process_materials.setter
def additional_post_process_materials(
        value: Array[MoviePipelinePostProcessPass]) -> None
```

<a id="unreal.MovieGraphPathTracedRenderPassNode"></a>