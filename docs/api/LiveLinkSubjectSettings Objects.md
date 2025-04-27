## LiveLinkSubjectSettings Objects

```python
class LiveLinkSubjectSettings(Object)
```

Base class for live link subject settings

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkSubjectSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_rate`` (FrameRate):  [Read-Only] Last FrameRate estimated by the subject. If in Timecode mode, this will come directly from the QualifiedFrameTime.
- ``interpolation_processor`` (LiveLinkFrameInterpolationProcessor):  [Read-Write] The interpolation processor the subject will use.
- ``pre_processors`` (Array[LiveLinkFramePreProcessor]):  [Read-Write] List of available preprocessor the subject will use.
- ``rebroadcast_subject`` (bool):  [Read-Write] If enabled, rebroadcast this subject
- ``remapper`` (LiveLinkSubjectRemapper):  [Read-Write] Remapper used to modify incoming static and frame data for a subject.
- ``translators`` (Array[LiveLinkFrameTranslator]):  [Read-Write] List of available translator the subject can use.

<a id="unreal.LiveLinkFrameInterpolationProcessor"></a>