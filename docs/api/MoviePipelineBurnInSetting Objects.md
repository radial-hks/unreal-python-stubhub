## MoviePipelineBurnInSetting Objects

```python
class MoviePipelineBurnInSetting(MoviePipelineRenderPass)
```

Movie Pipeline Burn in Setting

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineSettings
- **File**: MoviePipelineBurnInSetting.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``burn_in_class`` (SoftClassPath):  [Read-Write]
- ``composite_onto_final_image`` (bool):  [Read-Write] If true, the Burn In image will be composited into the Final Image pass. Doesn't apply to multi-layer EXR files.

<a id="unreal.MoviePipelineBurnInSetting.burn_in_class"></a>

#### burn_in_class

```python
@property
def burn_in_class() -> SoftClassPath
```

(SoftClassPath):  [Read-Write]

<a id="unreal.MoviePipelineBurnInSetting.burn_in_class"></a>

#### burn_in_class

```python
@burn_in_class.setter
def burn_in_class(value: SoftClassPath) -> None
```

<a id="unreal.MoviePipelineBurnInSetting.composite_onto_final_image"></a>

#### composite_onto_final_image

```python
@property
def composite_onto_final_image() -> bool
```

(bool):  [Read-Write] If true, the Burn In image will be composited into the Final Image pass. Doesn't apply to multi-layer EXR files.

<a id="unreal.MoviePipelineBurnInSetting.composite_onto_final_image"></a>

#### composite_onto_final_image

```python
@composite_onto_final_image.setter
def composite_onto_final_image(value: bool) -> None
```

<a id="unreal.MoviePipelineConsoleVariableSetting"></a>