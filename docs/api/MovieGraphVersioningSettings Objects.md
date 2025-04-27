## MovieGraphVersioningSettings Objects

```python
class MovieGraphVersioningSettings(StructBase)
```

Movie Graph Versioning Settings

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphGlobalOutputSettingNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_versioning`` (bool):  [Read-Write] If true, {version} tokens specified in the Output Directory and File Name Format properties will automatically
  be incremented with each local render. If false, the version specified in Version Number will be used instead.

  Auto-versioning will search across all render branches and use the highest version found as the basis for the
  next version used.
- ``version_number`` (int32):  [Read-Write] The value to use for the version token if versions are not automatically incremented (Auto Version is off).

<a id="unreal.MovieGraphVersioningSettings.__init__"></a>

#### __init__

```python
def __init__(auto_versioning: bool = False, version_number: int = 0) -> None
```

<a id="unreal.MovieGraphVersioningSettings.auto_versioning"></a>

#### auto_versioning

```python
@property
def auto_versioning() -> bool
```

(bool):  [Read-Write] If true, {version} tokens specified in the Output Directory and File Name Format properties will automatically
be incremented with each local render. If false, the version specified in Version Number will be used instead.

Auto-versioning will search across all render branches and use the highest version found as the basis for the
next version used.

<a id="unreal.MovieGraphVersioningSettings.auto_versioning"></a>

#### auto_versioning

```python
@auto_versioning.setter
def auto_versioning(value: bool) -> None
```

<a id="unreal.MovieGraphVersioningSettings.version_number"></a>

#### version_number

```python
@property
def version_number() -> int
```

(int32):  [Read-Write] The value to use for the version token if versions are not automatically incremented (Auto Version is off).

<a id="unreal.MovieGraphVersioningSettings.version_number"></a>

#### version_number

```python
@version_number.setter
def version_number(value: int) -> None
```

<a id="unreal.MovieGraphNamedResolution"></a>