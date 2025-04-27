## MoviePipelineTextureStreamingMethod Objects

```python
class MoviePipelineTextureStreamingMethod(EnumBase)
```

EMovie Pipeline Texture Streaming Method

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineGameOverrideSetting.h

<a id="unreal.MoviePipelineTextureStreamingMethod.NONE"></a>

#### NONE

0: This will not change the texture streaming method / cvars the users has set.

<a id="unreal.MoviePipelineTextureStreamingMethod.DISABLED"></a>

#### DISABLED

1: Disable the Texture Streaming system. Requires the highest amount of VRAM, but helps if Fully Load Used Textures still has blurry textures.

<a id="unreal.MoviePipelineTextureStreamingMethod.FULLY_LOAD"></a>

#### FULLY_LOAD

2: Fully load used textures instead of progressively streaming them in over multiple frames. Requires less VRAM but can occasionally still results in blurry textures.

<a id="unreal.MovieRenderPipelineState"></a>