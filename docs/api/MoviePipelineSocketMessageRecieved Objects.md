## MoviePipelineSocketMessageRecieved Objects

```python
class MoviePipelineSocketMessageRecieved(MulticastDelegateBase)
```

Called when a socket message is recieved. String is UTF8 encoded and has had the length byte stripped from it.

Args:
    message (str):

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MoviePipelineExecutor.h

<a id="unreal.MoviePipelineSocketMessageRecieved.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.MoviePipelineWorkFinished"></a>