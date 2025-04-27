## MetaSoundPatch Objects

```python
class MetaSoundPatch(Object)
```

This asset type is used for Metasound assets that can only be used as nodes in other Metasound graphs.
Because of this, they contain no required inputs or outputs.

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundEngine
- **File**: Metasound.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``graph`` (MetasoundEditorGraphBase):  [Read-Write]
  deprecated: Use EditorGraph instead as it is now transient and generated via the FrontendDocument dynamically.
- ``root_meta_sound_document`` (MetasoundFrontendDocument):  [Read-Write]

<a id="unreal.MetaSoundPatch.graph"></a>

#### graph

```python
@property
def graph() -> MetasoundEditorGraphBase
```

(MetasoundEditorGraphBase):  [Read-Write]
deprecated: Use EditorGraph instead as it is now transient and generated via the FrontendDocument dynamically.

<a id="unreal.MetaSoundPatch.graph"></a>

#### graph

```python
@graph.setter
def graph(value: MetasoundEditorGraphBase) -> None
```

<a id="unreal.MetaSound"></a>