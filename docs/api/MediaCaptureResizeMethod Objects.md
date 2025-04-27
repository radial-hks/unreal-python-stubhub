## MediaCaptureResizeMethod Objects

```python
class MediaCaptureResizeMethod(EnumBase)
```

EMedia Capture Resize Method

**C++ Source:**

- **Plugin**: MediaIOFramework
- **Module**: MediaIOCore
- **File**: MediaCapture.h

<a id="unreal.MediaCaptureResizeMethod.NONE"></a>

#### NONE

0: Leaves the source texture as is, which might be incompatible with the output size, causing an error.

<a id="unreal.MediaCaptureResizeMethod.RESIZE_SOURCE"></a>

#### RESIZE_SOURCE

1: Resize the source that is being captured. This will resize the viewport when doing a viewport capture and will resize the render target when capturing a render target. Not valid for immediate capture of RHI resource

<a id="unreal.MediaCaptureResizeMethod.RESIZE_IN_RENDER_PASS"></a>

#### RESIZE_IN_RENDER_PASS

2: Leaves the source as is, but will add a render pass where we resize the captured texture, leaving the source intact. This is useful when the output size is smaller than the captured source.

<a id="unreal.AvaRundownPageListType"></a>