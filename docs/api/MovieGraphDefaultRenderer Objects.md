## MovieGraphDefaultRenderer Objects

```python
class MovieGraphDefaultRenderer(MovieGraphRendererBase)
```

This class is the default implementation for the Movie Graph Pipeline renderer. This
is split off into a separate class to minimize the complexity of the core UMovieGraphPipeline,
and to provide a better way to store render-specific data during runtime. It is responsible
for taking all of the render passes and rendering them, and then moving their rendered
data back to the main UMoviePipeline OutputMerger once finished.

It is unlikely you will want to implement your own renderer. If you need to create new render
passes, inherit from UMovieGraphRenderPassNode and add it to your configuration, at which point
MRQ will call function on the CDO of it that allow you to set up your own render data.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphDefaultRenderer.h

<a id="unreal.MovieGraphScriptBase"></a>