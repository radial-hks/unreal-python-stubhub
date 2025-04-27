## MetasoundFrontendDocument Objects

```python
class MetasoundFrontendDocument(StructBase)
```

Metasound Frontend Document

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundFrontend
- **File**: MetasoundFrontendDocument.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``archetype_version`` (MetasoundFrontendVersion):  [Read-Write]
  deprecated: 5.0 - ArchetypeVersion has been migrated to InterfaceVersions array.
- ``interface_versions`` (Array[MetasoundFrontendVersion]):  [Read-Write]
  deprecated: 5.0 - InterfaceVersions has been migrated to Interfaces set.
- ``interfaces`` (Set[MetasoundFrontendVersion]):  [Read-Only]
- ``metadata`` (MetasoundFrontendDocumentMetadata):  [Read-Write]
- ``root_graph`` (MetasoundFrontendGraphClass):  [Read-Write]

<a id="unreal.MetasoundFrontendDocument.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MetasoundFrontendDocument.archetype_version"></a>

#### archetype_version

```python
@property
def archetype_version() -> MetasoundFrontendVersion
```

(MetasoundFrontendVersion):  [Read-Write]
deprecated: 5.0 - ArchetypeVersion has been migrated to InterfaceVersions array.

<a id="unreal.MetasoundFrontendDocument.archetype_version"></a>

#### archetype_version

```python
@archetype_version.setter
def archetype_version(value: MetasoundFrontendVersion) -> None
```

<a id="unreal.MetasoundFrontendDocument.interface_versions"></a>

#### interface_versions

```python
@property
def interface_versions() -> Array[MetasoundFrontendVersion]
```

(Array[MetasoundFrontendVersion]):  [Read-Write]
deprecated: 5.0 - InterfaceVersions has been migrated to Interfaces set.

<a id="unreal.MetasoundFrontendDocument.interface_versions"></a>

#### interface_versions

```python
@interface_versions.setter
def interface_versions(value: Array[MetasoundFrontendVersion]) -> None
```

<a id="unreal.StateTreeStateParameters"></a>