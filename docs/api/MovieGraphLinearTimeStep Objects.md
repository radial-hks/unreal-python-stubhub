## MovieGraphLinearTimeStep Objects

```python
class MovieGraphLinearTimeStep(MovieGraphCoreTimeStep)
```

Advances time forward linearly until the end of the range of time that is being rendered is reached. This is useful
for deferred rendering (where there's a small number of temporal sub-samples and no feedback mechanism for measuring
noise in the final image).

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphLinearTimeStep.h

<a id="unreal.MovieGraphModifierNode"></a>