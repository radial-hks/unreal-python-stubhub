## MovieGraphSequenceDataSource Objects

```python
class MovieGraphSequenceDataSource(MovieGraphDataSourceBase)
```

The UMovieGraphSequenceDataSource allows using a ULevelSequence as the external datasource for the Movie Graph.
It will build the range of shots based on the contents of the level sequence (one shot per camera cut found inside
the sequence hierarchy, not allowing overlapping Camera Cut sections), and then it will evaluate the level sequence
for the given time when rendering.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphSequenceDataSource.h

<a id="unreal.MovieGraphSetCVarValueNode"></a>