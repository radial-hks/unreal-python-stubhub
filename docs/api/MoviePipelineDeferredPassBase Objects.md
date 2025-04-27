## MoviePipelineDeferredPassBase Objects

```python
class MoviePipelineDeferredPassBase(MoviePipelineImagePassBase)
```

Movie Pipeline Deferred Pass Base

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
- ``render_main_pass`` (bool):  [Read-Write] This can be turned off if you're only doing a stencil-layer based render and don't need the main non-stencil approach.

<a id="unreal.MoviePipelineDeferredPassBase.accumulator_includes_alpha"></a>

#### accumulator_includes_alpha

```python
@property
def accumulator_includes_alpha() -> bool
```

(bool):  [Read-Write] Should multiple temporal/spatial samples accumulate the alpha channel? This requires r.PostProcessing.PropagateAlpha
to be enabled (see "Alpha Output" under Project Settings > Rendering). This adds
~30% cost to the accumulation so you should not enable it unless necessary. You must delete both the sky and fog to ensure
that they do not make all pixels opaque.

<a id="unreal.MoviePipelineDeferredPassBase.accumulator_includes_alpha"></a>

#### accumulator_includes_alpha

```python
@accumulator_includes_alpha.setter
def accumulator_includes_alpha(value: bool) -> None
```

<a id="unreal.MoviePipelineDeferredPassBase.disable_multisample_effects"></a>

#### disable_multisample_effects

```python
@property
def disable_multisample_effects() -> bool
```

(bool):  [Read-Write] Certain passes don't support post-processing effects that blend pixels together. These include effects like
Depth of Field, Temporal Anti-Aliasing, Motion Blur and chromattic abberation. When these post processing
effects are used then each final output pixel is composed of the influence of many other pixels which is
undesirable when rendering out an object id pass (which does not support post processing). This checkbox lets
you disable them on a per-render basis instead of having to disable them in the editor as well.

<a id="unreal.MoviePipelineDeferredPassBase.disable_multisample_effects"></a>

#### disable_multisample_effects

```python
@disable_multisample_effects.setter
def disable_multisample_effects(value: bool) -> None
```

<a id="unreal.MoviePipelineDeferredPassBase.additional_post_process_materials"></a>

#### additional_post_process_materials

```python
@property
def additional_post_process_materials() -> Array[MoviePipelinePostProcessPass]
```

(Array[MoviePipelinePostProcessPass]):  [Read-Write] An array of additional post-processing materials to run after the frame is rendered. Using this feature may add a notable amount of render time.

<a id="unreal.MoviePipelineDeferredPassBase.additional_post_process_materials"></a>

#### additional_post_process_materials

```python
@additional_post_process_materials.setter
def additional_post_process_materials(
        value: Array[MoviePipelinePostProcessPass]) -> None
```

<a id="unreal.MoviePipelineDeferredPassBase.render_main_pass"></a>

#### render_main_pass

```python
@property
def render_main_pass() -> bool
```

(bool):  [Read-Write] This can be turned off if you're only doing a stencil-layer based render and don't need the main non-stencil approach.

<a id="unreal.MoviePipelineDeferredPassBase.render_main_pass"></a>

#### render_main_pass

```python
@render_main_pass.setter
def render_main_pass(value: bool) -> None
```

<a id="unreal.MoviePipelineDeferredPassBase.add_default_layer"></a>

#### add_default_layer

```python
@property
def add_default_layer() -> bool
```

(bool):  [Read-Write] If true, an additional stencil layer will be rendered which contains all objects which do not belong to layers
specified in the Stencil Layers. This is useful for wanting to isolate one or two layers but still have everything
else to composite them over without having to remember to add all objects to a default layer.

<a id="unreal.MoviePipelineDeferredPassBase.add_default_layer"></a>

#### add_default_layer

```python
@add_default_layer.setter
def add_default_layer(value: bool) -> None
```

<a id="unreal.MoviePipelineDeferredPassBase.actor_layers"></a>

#### actor_layers

```python
@property
def actor_layers() -> Array[ActorLayer]
```

(Array[ActorLayer]):  [Read-Write] For each layer in the array, the world will be rendered and then a stencil mask will clip all pixels not affected
by the objects on that layer. This is NOT a true layer system, as translucent objects will show opaque objects from
another layer behind them. Does not write out additional post-process materials per-layer as they will match the
base layer. Only works with materials that can write to custom depth.

<a id="unreal.MoviePipelineDeferredPassBase.actor_layers"></a>

#### actor_layers

```python
@actor_layers.setter
def actor_layers(value: Array[ActorLayer]) -> None
```

<a id="unreal.MoviePipelineDeferredPassBase.stencil_layers"></a>

#### stencil_layers

```python
@property
def stencil_layers() -> Array[ActorLayer]
```

deprecated: 'stencil_layers' was renamed to 'actor_layers'.

<a id="unreal.MoviePipelineDeferredPassBase.stencil_layers"></a>

#### stencil_layers

```python
@stencil_layers.setter
def stencil_layers(value: Array[ActorLayer]) -> None
```

<a id="unreal.MoviePipelineDeferredPassBase.data_layers"></a>

#### data_layers

```python
@property
def data_layers() -> Array[SoftObjectPath]
```

(Array[SoftObjectPath]):  [Read-Write] If the map you are working with is a World Partition map, you can specify Data layers instead of Actor Layers. If any
Data Layers are specified, this will take precedence over any ActorLayers in this config. Does not affect whether or
not the Data Layers are actually loaded, you must ensure layers are loaded for rendering.

<a id="unreal.MoviePipelineDeferredPassBase.data_layers"></a>

#### data_layers

```python
@data_layers.setter
def data_layers(value: Array[SoftObjectPath]) -> None
```

<a id="unreal.MoviePipelineDeferredPass_Unlit"></a>