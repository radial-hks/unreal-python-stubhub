## ComposurePostProcessPassPolicy Objects

```python
class ComposurePostProcessPassPolicy(Object)
```

Abstract base class for setting up post passes. Used in conjuntion with UComposurePostProcessingPassProxy.

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: ComposurePostProcessingPassProxy.h

<a id="unreal.ComposurePostProcessPassPolicy.setup_post_process"></a>

#### setup_post_process

```python
def setup_post_process(
        scene_capture: SceneCaptureComponent2D) -> MaterialInterface
```

x.setup_post_process(scene_capture) -> MaterialInterface
Setup Post Process

Args:
    scene_capture (SceneCaptureComponent2D): 

Returns:
    MaterialInterface: 

    tonemapper_override (MaterialInterface):

<a id="unreal.ComposureLensBloomPassPolicy"></a>