## LiveLinkVirtualSubject Objects

```python
class LiveLinkVirtualSubject(Object)
```

A Virtual subject is made up of one or more real subjects from a source

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkVirtualSubject.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_translators`` (Array[LiveLinkFrameTranslator]):  [Read-Write] List of available translator the subject can use.
- ``rebroadcast_subject`` (bool):  [Read-Write] If enabled, rebroadcast this subject
- ``subjects`` (Array[LiveLinkSubjectName]):  [Read-Write] Names of the real subjects to combine into a virtual subject

<a id="unreal.LiveLinkBlueprintVirtualSubject"></a>