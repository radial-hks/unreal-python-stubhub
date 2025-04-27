## MetasoundFrontendVersionNumber Objects

```python
class MetasoundFrontendVersionNumber(StructBase)
```

General purpose version number for Metasound Frontend objects.

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundFrontend
- **File**: MetasoundFrontendDocument.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``major`` (int32):  [Read-Only] Major version number.
- ``minor`` (int32):  [Read-Only] Minor version number.

<a id="unreal.MetasoundFrontendVersionNumber.__init__"></a>

#### __init__

```python
def __init__(major: int = 0, minor: int = 0) -> None
```

<a id="unreal.MetasoundFrontendVersionNumber.major"></a>

#### major

```python
@property
def major() -> int
```

(int32):  [Read-Only] Major version number.

<a id="unreal.MetasoundFrontendVersionNumber.minor"></a>

#### minor

```python
@property
def minor() -> int
```

(int32):  [Read-Only] Minor version number.

<a id="unreal.MetasoundFrontendVersion"></a>