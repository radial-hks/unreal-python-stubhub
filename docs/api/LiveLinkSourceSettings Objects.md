## LiveLinkSourceSettings Objects

```python
class LiveLinkSourceSettings(Object)
```

Base class for live link source settings (can be replaced by sources themselves)

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkSourceSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``buffer_settings`` (LiveLinkSourceBufferManagementSettings):  [Read-Write] How the frame buffers are managed.
- ``connection_string`` (str):  [Read-Write] Connection information that is needed by the factory to recreate the source from a preset.
- ``mode`` (LiveLinkSourceMode):  [Read-Write] The the subject how to create the frame snapshot.
  note: A client may evaluate manually the subject in a different mode by using EvaluateFrameAtWorldTime or EvaluateFrameAtSceneTime.
- ``parent_subject`` (LiveLinkSubjectName):  [Read-Write] Which subject should be used as a synchronization source for this source.
  If this is set, this source's subjects will only be rebroadcast when the parent subject receives data.
  Additionally this source's subjects' timecode will match the parent's subject received timecode.
  This can be useful for synchronizing a higher frequency source to a lower frequency one.

<a id="unreal.LiveLinkSubjectSettings"></a>