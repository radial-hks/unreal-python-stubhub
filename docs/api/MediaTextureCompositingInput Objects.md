## MediaTextureCompositingInput Objects

```python
class MediaTextureCompositingInput(CompositingMediaInput)
```

Media Texture Compositing Input

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: CompositingElementInputs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``intermediate`` (bool):  [Read-Write] Marks this pass for 'internal use only' - prevents it from being exposed to parent elements.
  When set, render target resources used by this element will be reused. For inputs, all 'Intermediate'
  passes are available to the first transform pass, and released after that.
- ``media_source`` (MediaTexture):  [Read-Write]
- ``media_transform_material`` (CompositingMaterial):  [Read-Write]
- ``pass_name`` (Name):  [Read-Write]

<a id="unreal.MediaTextureCompositingInput.media_source"></a>

#### media_source

```python
@property
def media_source() -> MediaTexture
```

(MediaTexture):  [Read-Only]

<a id="unreal.CompositingInputInterface"></a>