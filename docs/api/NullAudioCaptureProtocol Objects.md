## NullAudioCaptureProtocol Objects

```python
class NullAudioCaptureProtocol(MovieSceneAudioCaptureProtocolBase)
```

This is a null audio capture implementation which skips capturing audio. The MovieSceneCapture is explicitly
aware of this type and will skip processing an audio pass if this is specified.

**C++ Source:**

- **Module**: MovieSceneCapture
- **File**: AudioCaptureProtocol.h

<a id="unreal.MasterAudioSubmixCaptureProtocol"></a>