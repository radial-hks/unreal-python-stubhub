## MovieGraphResolveArgs Objects

```python
class MovieGraphResolveArgs(StructBase)
```

This data structure contains a list of key-value pairs (as strings) for both filename resolving, and file metadata.
They are stored as two separate arrays (as metadata is often a bit more verbose/human friendly) and it is not required
that the two arrays be in sync. When resolving final filenames, any {tokens} will be replaced with a matching key-value
if found in the FilenameArguments variable. Because of this, FilenameArguments should be short and avoid illegal filename chars.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphFilenameResolveParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``file_metadata`` (Map[str, str]):  [Read-Write] A set of Key/Value pairs for file metadata for file formats that support metadata.
- ``filename_arguments`` (Map[str, str]):  [Read-Write] A set of Key/Value pairs for output filename format strings (without {}) and their values.

<a id="unreal.MovieGraphResolveArgs.__init__"></a>

#### __init__

```python
def __init__(filename_arguments: Map[str, str] = {},
             file_metadata: Map[str, str] = {}) -> None
```

<a id="unreal.MovieGraphResolveArgs.filename_arguments"></a>

#### filename_arguments

```python
@property
def filename_arguments() -> Map[str, str]
```

(Map[str, str]):  [Read-Write] A set of Key/Value pairs for output filename format strings (without {}) and their values.

<a id="unreal.MovieGraphResolveArgs.filename_arguments"></a>

#### filename_arguments

```python
@filename_arguments.setter
def filename_arguments(value: Map[str, str]) -> None
```

<a id="unreal.MovieGraphResolveArgs.file_metadata"></a>

#### file_metadata

```python
@property
def file_metadata() -> Map[str, str]
```

(Map[str, str]):  [Read-Write] A set of Key/Value pairs for file metadata for file formats that support metadata.

<a id="unreal.MovieGraphResolveArgs.file_metadata"></a>

#### file_metadata

```python
@file_metadata.setter
def file_metadata(value: Map[str, str]) -> None
```

<a id="unreal.MovieGraphFilenameResolveParams"></a>