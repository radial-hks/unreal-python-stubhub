## MetaSoundPatchBuilder Objects

```python
class MetaSoundPatchBuilder(MetaSoundBuilderBase)
```

Builder in charge of building a MetaSound Patch

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundEngine
- **File**: MetasoundBuilderSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``class_name`` (MetasoundFrontendClassName):  [Read-Write]
  deprecated: 5.5 - No longer used. ClassName should be queried from associated FrontendBuilder's MetaSound
- ``is_attached`` (bool):  [Read-Write]
  deprecated: 5.4 - All source builders now operate on an underlying document source document that is also used to audition.

<a id="unreal.MetaSoundSourceBuilder"></a>