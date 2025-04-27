## LiveLinkTimecodeProvider Objects

```python
class LiveLinkTimecodeProvider(TimecodeProvider)
```

Fetch the latest frames from the LiveLink subject and create a Timecode from it.

**C++ Source:**

- **Plugin**: LiveLink
- **Module**: LiveLink
- **File**: LiveLinkTimecodeProvider.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``buffer_size`` (int32):  [Read-Write] The number of frame to keep in memory. The provider will not be synchronized until the buffer is full at least once.
- ``evaluation`` (LiveLinkTimecodeProviderEvaluationType):  [Read-Write] How to evaluate the timecode.
- ``frame_delay`` (float):  [Read-Write] Number of frames to subtract from the qualified frame time when GetDelayedQualifiedFrameTime or GetDelayedTimecode is called.
  see: GetDelayedQualifiedFrameTime, GetDelayedTimecode
- ``override_frame_rate`` (FrameRate):  [Read-Write] Override the frame rate at which this timecode provider will create its timecode value.
  By default, we use the subject frame rate.
- ``override_frame_rate`` (bool):  [Read-Write]
- ``subject_key`` (LiveLinkSubjectKey):  [Read-Write] The specific subject that we listen to.

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor"></a>