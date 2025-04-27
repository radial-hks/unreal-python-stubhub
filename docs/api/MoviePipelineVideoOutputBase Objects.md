## MoviePipelineVideoOutputBase Objects

```python
class MoviePipelineVideoOutputBase(MoviePipelineOutputBase)
```

A base class for video codec outputs for the Movie Pipeline system. To simplify encoder implementations
this handles multi-threading for you and will call all of the encoding functions on a dedicated thread.
This allows an encoder to do more expensive operations (such as image quantization) without implementing
threading yourself, nor having to worry about blocking the game thread.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineVideoOutputBase.h

<a id="unreal.AvaMRQRundownPageSetting"></a>