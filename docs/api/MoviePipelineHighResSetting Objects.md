## MoviePipelineHighResSetting Objects

```python
class MoviePipelineHighResSetting(MoviePipelineSetting)
```

Movie Pipeline High Res Setting

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineHighResSetting.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allocate_history_per_tile`` (bool):  [Read-Write] * If true, allocate a unique history for each tile. This is needed to make some render features work, but should be disabled
  * when dealing with extremely large resolutions as you will spend all of your GPU memory on history buffers.
- ``burley_sample_count`` (int32):  [Read-Write] * How many samples should the Burley Sub Surface Scattering use?
- ``overlap_ratio`` (float):  [Read-Write] How much should each tile overlap each other (0-0.5). Decreasing the overlap will result in smaller individual
  tiles (which means faster renders) but increases the likelyhood of edge-of-screen artifacts showing up which
  will become visible in the final image as a "grid" of repeated problem areas.
- ``override_sub_surface_scattering`` (bool):  [Read-Write] Sub Surface Scattering relies on history which is not available when using tiling. This can be overriden to use more samples
  to improve the quality.
- ``texture_sharpness_bias`` (float):  [Read-Write] This bias encourages the engine to use a higher detail texture when it would normally use a lower detail
  texture due to the size of the texture on screen. A more negative number means overall sharper images
  (up to the detail resolution of your texture). Too much sharpness will cause visual grain/noise in the
  resulting image, but this can be mitigated with more spatial samples.
- ``tile_count`` (int32):  [Read-Write] How many tiles should the resulting movie render be broken into? A tile should be no larger than
  the maximum texture resolution supported by your graphics card (likely 16k), so NumTiles should be
  ceil(Width/MaxTextureSize). More tiles mean more individual passes over the whole scene at a smaller
  resolution which may help with gpu timeouts. Requires at least 1 tile. Tiling is applied evenly to
  both X and Y.

<a id="unreal.MoviePipelineHighResSetting.tile_count"></a>

#### tile_count

```python
@property
def tile_count() -> int
```

(int32):  [Read-Write] How many tiles should the resulting movie render be broken into? A tile should be no larger than
the maximum texture resolution supported by your graphics card (likely 16k), so NumTiles should be
ceil(Width/MaxTextureSize). More tiles mean more individual passes over the whole scene at a smaller
resolution which may help with gpu timeouts. Requires at least 1 tile. Tiling is applied evenly to
both X and Y.

<a id="unreal.MoviePipelineHighResSetting.tile_count"></a>

#### tile_count

```python
@tile_count.setter
def tile_count(value: int) -> None
```

<a id="unreal.MoviePipelineHighResSetting.texture_sharpness_bias"></a>

#### texture_sharpness_bias

```python
@property
def texture_sharpness_bias() -> float
```

(float):  [Read-Write] This bias encourages the engine to use a higher detail texture when it would normally use a lower detail
texture due to the size of the texture on screen. A more negative number means overall sharper images
(up to the detail resolution of your texture). Too much sharpness will cause visual grain/noise in the
resulting image, but this can be mitigated with more spatial samples.

<a id="unreal.MoviePipelineHighResSetting.texture_sharpness_bias"></a>

#### texture_sharpness_bias

```python
@texture_sharpness_bias.setter
def texture_sharpness_bias(value: float) -> None
```

<a id="unreal.MoviePipelineHighResSetting.overlap_ratio"></a>

#### overlap_ratio

```python
@property
def overlap_ratio() -> float
```

(float):  [Read-Write] How much should each tile overlap each other (0-0.5). Decreasing the overlap will result in smaller individual
tiles (which means faster renders) but increases the likelyhood of edge-of-screen artifacts showing up which
will become visible in the final image as a "grid" of repeated problem areas.

<a id="unreal.MoviePipelineHighResSetting.overlap_ratio"></a>

#### overlap_ratio

```python
@overlap_ratio.setter
def overlap_ratio(value: float) -> None
```

<a id="unreal.MoviePipelineHighResSetting.override_sub_surface_scattering"></a>

#### override_sub_surface_scattering

```python
@property
def override_sub_surface_scattering() -> bool
```

(bool):  [Read-Write] Sub Surface Scattering relies on history which is not available when using tiling. This can be overriden to use more samples
to improve the quality.

<a id="unreal.MoviePipelineHighResSetting.override_sub_surface_scattering"></a>

#### override_sub_surface_scattering

```python
@override_sub_surface_scattering.setter
def override_sub_surface_scattering(value: bool) -> None
```

<a id="unreal.MoviePipelineHighResSetting.burley_sample_count"></a>

#### burley_sample_count

```python
@property
def burley_sample_count() -> int
```

(int32):  [Read-Write] * How many samples should the Burley Sub Surface Scattering use?

<a id="unreal.MoviePipelineHighResSetting.burley_sample_count"></a>

#### burley_sample_count

```python
@burley_sample_count.setter
def burley_sample_count(value: int) -> None
```

<a id="unreal.MoviePipelineHighResSetting.allocate_history_per_tile"></a>

#### allocate_history_per_tile

```python
@property
def allocate_history_per_tile() -> bool
```

(bool):  [Read-Write] * If true, allocate a unique history for each tile. This is needed to make some render features work, but should be disabled
* when dealing with extremely large resolutions as you will spend all of your GPU memory on history buffers.

<a id="unreal.MoviePipelineHighResSetting.allocate_history_per_tile"></a>

#### allocate_history_per_tile

```python
@allocate_history_per_tile.setter
def allocate_history_per_tile(value: bool) -> None
```

<a id="unreal.MoviePipelineInProcessExecutorSettings"></a>