## DistortionRenderingMode Objects

```python
class DistortionRenderingMode(EnumBase)
```

Specifies how the distortion should be rendered in the post-processing pipeline

**C++ Source:**

- **Plugin**: LensComponent
- **Module**: LensComponent
- **File**: LensComponent.h

<a id="unreal.DistortionRenderingMode.POST_PROCESS_MATERIAL"></a>

#### POST_PROCESS_MATERIAL

0: Use the plugin post process material

<a id="unreal.DistortionRenderingMode.SCENE_VIEW_EXTENSION"></a>

#### SCENE_VIEW_EXTENSION

1: Use the experimental lens distortion scene view extension. Further control of where distortion is rendered can be set via the console command r.TSR.LensDistortion

<a id="unreal.TargetUsageFlags"></a>