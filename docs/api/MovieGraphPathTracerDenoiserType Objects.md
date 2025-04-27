## MovieGraphPathTracerDenoiserType Objects

```python
class MovieGraphPathTracerDenoiserType(EnumBase)
```

EMovie Graph Path Tracer Denoiser Type

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineRenderPasses
- **File**: MovieGraphPathTracerPassNode.h

<a id="unreal.MovieGraphPathTracerDenoiserType.SPATIAL"></a>

#### SPATIAL

0: The active spatial denoiser plugin will be used for denoising. If the denoiser is not loaded, a warning will show in the log.
If multiple spatial denoiser plugins are enabled, the last one to get loaded will be the one used.

<a id="unreal.MovieGraphPathTracerDenoiserType.TEMPORAL"></a>

#### TEMPORAL

1: The active spatial-temporal denoiser plugin will be used for denoising. It provides more temporal stability than spatial denoiser
if the Frame Count of past/future frames are used (Frame Count > 0) in the plugin. The user needs to config `Frame Count` to
match the requirements of the chosen denoiser plugin. If the denoiser is not loaded, a warning will show in the log. If multiple
spatial-temporal denoiser plugins are enabled, the last one to get loaded will be the one used.

<a id="unreal.EXRCompressionFormat"></a>