## MovieGraphTimeStepBase Objects

```python
class MovieGraphTimeStepBase(Object)
```

Movie Graph Time Step Base

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphDataTypes.h

<a id="unreal.MovieGraphTimeStepBase.get_calculated_time_data"></a>

#### get_calculated_time_data

```python
def get_calculated_time_data() -> MovieGraphTimeStepData
```

x.get_calculated_time_data() -> MovieGraphTimeStepData
TickProducingFrames will be called for a frame (before the frame starts) and then this will be
called at the end of the frame when we kick off the renders for the frame. Should return data
needed to calculate the correct rendering timestep.

Returns:
    MovieGraphTimeStepData:

<a id="unreal.MovieGraphCoreTimeStep"></a>