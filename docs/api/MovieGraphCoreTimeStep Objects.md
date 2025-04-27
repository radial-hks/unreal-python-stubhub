## MovieGraphCoreTimeStep Objects

```python
class MovieGraphCoreTimeStep(MovieGraphTimeStepBase)
```

Provides common logic for typical time-step functionality.

The number of temporal sub-samples is read from the graph for each output frame, and we then take the time the
shutter is open and break it into that many sub-samples. Subclasses must implement GetNextTemporalRangeIndex() to
indicate the index of the next temporal sub-sample.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphCoreTimeStep.h

<a id="unreal.MovieGraphRendererBase"></a>