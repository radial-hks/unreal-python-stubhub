## MetasoundFrontendVersion Objects

```python
class MetasoundFrontendVersion(StructBase)
```

General purpose version info for Metasound Frontend objects.

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundFrontend
- **File**: MetasoundFrontendDocument.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (Name):  [Read-Only] Name of version.
- ``number`` (MetasoundFrontendVersionNumber):  [Read-Only] Version number.

<a id="unreal.MetasoundFrontendVersion.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             number: MetasoundFrontendVersionNumber = [1, 0]) -> None
```

<a id="unreal.MetasoundFrontendVersion.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Only] Name of version.

<a id="unreal.MetasoundFrontendVersion.number"></a>

#### number

```python
@property
def number() -> MetasoundFrontendVersionNumber
```

(MetasoundFrontendVersionNumber):  [Read-Only] Version number.

<a id="unreal.MetasoundFrontendLiteral"></a>