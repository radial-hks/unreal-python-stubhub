## MovieGraphDataSourceBase Objects

```python
class MovieGraphDataSourceBase(Object)
```

Movie Graph Pipeline is mostly interested in knowing about ranges of time that
it should render, and less concerned with the specifics of where that data comes
from (ie: a Level Sequence). This lets you synchronize with a different data source
to provide the ranges of time to render, and then the UMovieGraphTimeStepBase class
figures out how to move around within that time step, before calling some functions
to synchronize your external data source to actually match the evaluated time.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphDataTypes.h

<a id="unreal.MovieGraphAudioRendererBase"></a>