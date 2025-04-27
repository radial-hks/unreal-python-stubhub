## MediaCaptureCroppingType Objects

```python
class MediaCaptureCroppingType(EnumBase)
```

Type of cropping

**C++ Source:**

- **Plugin**: MediaIOFramework
- **Module**: MediaIOCore
- **File**: MediaCapture.h

<a id="unreal.MediaCaptureCroppingType.NONE"></a>

#### NONE

0: Do not crop the captured image.

<a id="unreal.MediaCaptureCroppingType.CENTER"></a>

#### CENTER

1: Keep the center of the captured image.

<a id="unreal.MediaCaptureCroppingType.TOP_LEFT"></a>

#### TOP_LEFT

2: Keep the top left corner of the captured image.

<a id="unreal.MediaCaptureCroppingType.CUSTOM"></a>

#### CUSTOM

3: Use the StartCapturePoint and the size of the MediaOutput to keep of the captured image.

<a id="unreal.MediaCaptureOverrunAction"></a>