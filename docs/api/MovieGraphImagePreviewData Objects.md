## MovieGraphImagePreviewData Objects

```python
class MovieGraphImagePreviewData(StructBase)
```

Movie Graph Image Preview Data

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphDataTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``identifier`` (MovieGraphRenderDataIdentifier):  [Read-Write] The identifier for the image, containing the branch name, renderer, etc.
- ``multiple_camera_names`` (bool):  [Read-Write] If true, then there is more than one camera name being used (ie: multi-camera rendering)
- ``texture`` (Texture):  [Read-Write] The texture this preview image was rendered to.

<a id="unreal.MovieGraphImagePreviewData.__init__"></a>

#### __init__

```python
def __init__(texture: Texture = None,
             identifier: MovieGraphRenderDataIdentifier = [
                 "None", "", "", "", ""
             ],
             multiple_camera_names: bool = False) -> None
```

<a id="unreal.MovieGraphImagePreviewData.texture"></a>

#### texture

```python
@property
def texture() -> Texture
```

(Texture):  [Read-Only] The texture this preview image was rendered to.

<a id="unreal.MovieGraphImagePreviewData.identifier"></a>

#### identifier

```python
@property
def identifier() -> MovieGraphRenderDataIdentifier
```

(MovieGraphRenderDataIdentifier):  [Read-Only] The identifier for the image, containing the branch name, renderer, etc.

<a id="unreal.MovieGraphImagePreviewData.multiple_camera_names"></a>

#### multiple_camera_names

```python
@property
def multiple_camera_names() -> bool
```

(bool):  [Read-Only] If true, then there is more than one camera name being used (ie: multi-camera rendering)

<a id="unreal.MovieGraphInitConfig"></a>