## LiveLinkBlueprintVirtualSubject Objects

```python
class LiveLinkBlueprintVirtualSubject(LiveLinkVirtualSubject)
```

Base class for creating virtual subjects in Blueprints

**C++ Source:**

- **Plugin**: LiveLink
- **Module**: LiveLink
- **File**: LiveLinkBlueprintVirtualSubject.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_translators`` (Array[LiveLinkFrameTranslator]):  [Read-Write] List of available translator the subject can use.
- ``rebroadcast_subject`` (bool):  [Read-Write] If enabled, rebroadcast this subject
- ``subjects`` (Array[LiveLinkSubjectName]):  [Read-Write] Names of the real subjects to combine into a virtual subject

<a id="unreal.LiveLinkBlueprintVirtualSubject.on_update"></a>

#### on_update

```python
def on_update() -> None
```

x.on_update() -> None
On Update

<a id="unreal.LiveLinkBlueprintVirtualSubject.on_initialize"></a>

#### on_initialize

```python
def on_initialize() -> None
```

x.on_initialize() -> None
On Initialize

<a id="unreal.LiveLinkInstance"></a>