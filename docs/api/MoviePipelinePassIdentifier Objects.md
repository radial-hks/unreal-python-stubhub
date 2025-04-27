## MoviePipelinePassIdentifier Objects

```python
class MoviePipelinePassIdentifier(StructBase)
```

Movie Pipeline Pass Identifier

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieRenderPipelineDataTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_name`` (str):  [Read-Write] The name of the camera that this pass is for. Stored here so we can differentiate between
  multiple cameras within a single pass.
- ``name`` (str):  [Read-Write] The name of the pass such as "FinalImage" or "ObjectId", etc.

<a id="unreal.MoviePipelinePassIdentifier.__init__"></a>

#### __init__

```python
def __init__(name: str = "", camera_name: str = "") -> None
```

<a id="unreal.MoviePipelinePassIdentifier.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write] The name of the pass such as "FinalImage" or "ObjectId", etc.

<a id="unreal.MoviePipelinePassIdentifier.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.MoviePipelinePassIdentifier.camera_name"></a>

#### camera_name

```python
@property
def camera_name() -> str
```

(str):  [Read-Write] The name of the camera that this pass is for. Stored here so we can differentiate between
multiple cameras within a single pass.

<a id="unreal.MoviePipelinePassIdentifier.camera_name"></a>

#### camera_name

```python
@camera_name.setter
def camera_name(value: str) -> None
```

<a id="unreal.MoviePipelineRenderPassOutputData"></a>