## MoviePipelineDeferredPass_PathTracer Objects

```python
class MoviePipelineDeferredPass_PathTracer(MoviePipelineDeferredPassBase)
```

Movie Pipeline Deferred Pass Path Tracer

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineRenderPasses
- **File**: MoviePipelineDeferredPasses.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accumulator_includes_alpha`` (bool):  [Read-Write] Should multiple temporal/spatial samples accumulate the alpha channel? This requires r.PostProcessing.PropagateAlpha
  to be enabled (see "Alpha Output" under Project Settings > Rendering). This adds
  ~30% cost to the accumulation so you should not enable it unless necessary. You must delete both the sky and fog to ensure
  that they do not make all pixels opaque.
- ``actor_layers`` (Array[ActorLayer]):  [Read-Write] For each layer in the array, the world will be rendered and then a stencil mask will clip all pixels not affected
  by the objects on that layer. This is NOT a true layer system, as translucent objects will show opaque objects from
  another layer behind them. Does not write out additional post-process materials per-layer as they will match the
  base layer. Only works with materials that can write to custom depth.
- ``add_default_layer`` (bool):  [Read-Write] If true, an additional stencil layer will be rendered which contains all objects which do not belong to layers
  specified in the Stencil Layers. This is useful for wanting to isolate one or two layers but still have everything
  else to composite them over without having to remember to add all objects to a default layer.
- ``additional_post_process_materials`` (Array[MoviePipelinePostProcessPass]):  [Read-Write] An array of additional post-processing materials to run after the frame is rendered. Using this feature may add a notable amount of render time.
- ``data_layers`` (Array[SoftObjectPath]):  [Read-Write] If the map you are working with is a World Partition map, you can specify Data layers instead of Actor Layers. If any
  Data Layers are specified, this will take precedence over any ActorLayers in this config. Does not affect whether or
  not the Data Layers are actually loaded, you must ensure layers are loaded for rendering.
- ``disable_multisample_effects`` (bool):  [Read-Write] Certain passes don't support post-processing effects that blend pixels together. These include effects like
  Depth of Field, Temporal Anti-Aliasing, Motion Blur and chromattic abberation. When these post processing
  effects are used then each final output pixel is composed of the influence of many other pixels which is
  undesirable when rendering out an object id pass (which does not support post processing). This checkbox lets
  you disable them on a per-render basis instead of having to disable them in the editor as well.
- ``reference_motion_blur`` (bool):  [Read-Write] When enabled, the path tracer will blend all spatial and temporal samples prior to the denoising and will disable post-processed motion blur.
  In this mode it is possible to use higher temporal sample counts to improve the motion blur quality.
  When this option is disabled, the path tracer will accumulate spatial samples, but denoise them prior to accumulation of temporal samples.
- ``render_main_pass`` (bool):  [Read-Write] This can be turned off if you're only doing a stencil-layer based render and don't need the main non-stencil approach.

<a id="unreal.MoviePipelineDeferredPass_PathTracer.reference_motion_blur"></a>

#### reference_motion_blur

```python
@property
def reference_motion_blur() -> bool
```

(bool):  [Read-Write] When enabled, the path tracer will blend all spatial and temporal samples prior to the denoising and will disable post-processed motion blur.
In this mode it is possible to use higher temporal sample counts to improve the motion blur quality.
When this option is disabled, the path tracer will accumulate spatial samples, but denoise them prior to accumulation of temporal samples.

<a id="unreal.MoviePipelineDeferredPass_PathTracer.reference_motion_blur"></a>

#### reference_motion_blur

```python
@reference_motion_blur.setter
def reference_motion_blur(value: bool) -> None
```

<a id="unreal.MoviePipelineImageSequenceOutputBase"></a>