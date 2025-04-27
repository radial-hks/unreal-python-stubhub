## MetasoundFrontendClassInput Objects

```python
class MetasoundFrontendClassInput(MetasoundFrontendClassVertex)
```

Contains info for input vertex of a Metasound class.

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundFrontend
- **File**: MetasoundFrontendDocument.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``defaults`` (Array[MetasoundFrontendClassInputDefault]):  [Read-Write]
- ``metadata`` (MetasoundFrontendVertexMetadata):  [Read-Write] Metadata associated with vertex.
- ``name`` (Name):  [Read-Only] Name of the vertex. Unique amongst other vertices on the same interface.
- ``type_name`` (Name):  [Read-Only] Data type name of the vertex.

<a id="unreal.MetasoundFrontendClassInput.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MetasoundFrontendClassOutput"></a>