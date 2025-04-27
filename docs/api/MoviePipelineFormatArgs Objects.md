## MoviePipelineFormatArgs Objects

```python
class MoviePipelineFormatArgs(StructBase)
```

Movie Pipeline Format Args

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieRenderPipelineDataTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``file_metadata`` (Map[str, str]):  [Read-Write] A set of Key/Value pairs for file metadata for file formats that support metadata.
- ``filename_arguments`` (Map[str, str]):  [Read-Write] A set of Key/Value pairs for output filename format strings (without {}) and their values.
- ``job`` (MoviePipelineExecutorJob):  [Read-Write] Which job is this for? Some settings are specific to the level sequence being rendered.

<a id="unreal.MoviePipelineFormatArgs.__init__"></a>

#### __init__

```python
def __init__(filename_arguments: Map[str, str] = {},
             file_metadata: Map[str, str] = {},
             job: MoviePipelineExecutorJob = None) -> None
```

<a id="unreal.MoviePipelineFormatArgs.filename_arguments"></a>

#### filename_arguments

```python
@property
def filename_arguments() -> Map[str, str]
```

(Map[str, str]):  [Read-Write] A set of Key/Value pairs for output filename format strings (without {}) and their values.

<a id="unreal.MoviePipelineFormatArgs.filename_arguments"></a>

#### filename_arguments

```python
@filename_arguments.setter
def filename_arguments(value: Map[str, str]) -> None
```

<a id="unreal.MoviePipelineFormatArgs.file_metadata"></a>

#### file_metadata

```python
@property
def file_metadata() -> Map[str, str]
```

(Map[str, str]):  [Read-Write] A set of Key/Value pairs for file metadata for file formats that support metadata.

<a id="unreal.MoviePipelineFormatArgs.file_metadata"></a>

#### file_metadata

```python
@file_metadata.setter
def file_metadata(value: Map[str, str]) -> None
```

<a id="unreal.MoviePipelineFormatArgs.job"></a>

#### job

```python
@property
def job() -> MoviePipelineExecutorJob
```

(MoviePipelineExecutorJob):  [Read-Write] Which job is this for? Some settings are specific to the level sequence being rendered.

<a id="unreal.MoviePipelineFormatArgs.job"></a>

#### job

```python
@job.setter
def job(value: MoviePipelineExecutorJob) -> None
```

<a id="unreal.MoviePipelineFilenameResolveParams"></a>