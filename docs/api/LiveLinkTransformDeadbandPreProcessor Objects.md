## LiveLinkTransformDeadbandPreProcessor Objects

```python
class LiveLinkTransformDeadbandPreProcessor(LiveLinkFramePreProcessor)
```

Implements a deadband filter that gets applied to the transform, with independent thresholds
for rotation and translation.

**C++ Source:**

- **Plugin**: LiveLink
- **Module**: LiveLink
- **File**: LiveLinkDeadbandPreProcessor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_deadband`` (bool):  [Read-Write] If false, transform is left untouched
- ``rotation_deadband_in_degrees`` (float):  [Read-Write] Rotation is updated only if the change is larger than this threshold
- ``translation_deadband`` (float):  [Read-Write] Translation is updated only if the change is larger than this threshold

<a id="unreal.LiveLinkBlueprintLibrary"></a>