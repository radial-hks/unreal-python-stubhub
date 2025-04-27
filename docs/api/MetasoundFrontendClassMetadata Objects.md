## MetasoundFrontendClassMetadata Objects

```python
class MetasoundFrontendClassMetadata(StructBase)
```

Metasound Frontend Class Metadata

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundFrontend
- **File**: MetasoundFrontendDocument.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``author`` (str):  [Read-Write]
- ``category_hierarchy`` (Array[Text]):  [Read-Write]
- ``class_name`` (MetasoundFrontendClassName):  [Read-Only]
- ``description`` (Text):  [Read-Write]
- ``display_name`` (Text):  [Read-Write]
- ``is_deprecated`` (bool):  [Read-Write] If true, this node is deprecated and should not be used in new MetaSounds.
- ``keywords`` (Array[Text]):  [Read-Write]
- ``type`` (MetasoundFrontendClassType):  [Read-Only]
- ``version`` (MetasoundFrontendVersionNumber):  [Read-Only]

<a id="unreal.MetasoundFrontendClassMetadata.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MetasoundFrontendClassInterface"></a>