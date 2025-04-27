## MovieGraphShowFlags Objects

```python
class MovieGraphShowFlags(Object)
```

Stores show flag enable/disable state, as well as per-flag override state.

Here, enable/disable state refers to the actual state of the show flag itself (ie, whether it is turned on or off).
This is the value that will be applied to renders. "Override" state is whether the flag has been marked as overridden
in the UI (ie, whether it is a value that graph traversal should respect). Flags must be marked as overridden in order
for their values to deviate from the default.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphShowFlags.h

<a id="unreal.MovieGraphSubgraphNode"></a>