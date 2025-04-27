## MoviePipelinePostProcessPass Objects

```python
class MoviePipelinePostProcessPass(StructBase)
```

Movie Pipeline Post Process Pass

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineRenderPasses
- **File**: MoviePipelineDeferredPasses.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write] Additional passes add a significant amount of render time. May produce multiple output files if using Screen Percentage.
- ``high_precision_output`` (bool):  [Read-Write] Request output to be 32-bit, usually for data exports. Note that scene color precision is still defined by r.SceneColorFormat.
- ``material`` (MaterialInterface):  [Read-Write] Material should be set to Post Process domain, and Blendable Location = After Tonemapping.
  This will need bDisableMultisampleEffects enabled for pixels to line up(ie : no DoF, MotionBlur, TAA)
- ``name`` (str):  [Read-Write] An optional name which which will identify this material in the file name. For MRQ, the material name will be included in the {render_pass}
  token. For Movie Render Graph, the material name will be used in {renderer_sub_name}. If a name is not specified here, the full name of the material
  will be used in these tokens instead.

<a id="unreal.MoviePipelinePostProcessPass.__init__"></a>

#### __init__

```python
def __init__(enabled: bool = False,
             name: str = "",
             material: MaterialInterface = None,
             high_precision_output: bool = False) -> None
```

<a id="unreal.MoviePipelinePostProcessPass.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] Additional passes add a significant amount of render time. May produce multiple output files if using Screen Percentage.

<a id="unreal.MoviePipelinePostProcessPass.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.MoviePipelinePostProcessPass.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write] An optional name which which will identify this material in the file name. For MRQ, the material name will be included in the {render_pass}
token. For Movie Render Graph, the material name will be used in {renderer_sub_name}. If a name is not specified here, the full name of the material
will be used in these tokens instead.

<a id="unreal.MoviePipelinePostProcessPass.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.MoviePipelinePostProcessPass.material"></a>

#### material

```python
@property
def material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write] Material should be set to Post Process domain, and Blendable Location = After Tonemapping.
This will need bDisableMultisampleEffects enabled for pixels to line up(ie : no DoF, MotionBlur, TAA)

<a id="unreal.MoviePipelinePostProcessPass.material"></a>

#### material

```python
@material.setter
def material(value: MaterialInterface) -> None
```

<a id="unreal.MoviePipelinePostProcessPass.high_precision_output"></a>

#### high_precision_output

```python
@property
def high_precision_output() -> bool
```

(bool):  [Read-Write] Request output to be 32-bit, usually for data exports. Note that scene color precision is still defined by r.SceneColorFormat.

<a id="unreal.MoviePipelinePostProcessPass.high_precision_output"></a>

#### high_precision_output

```python
@high_precision_output.setter
def high_precision_output(value: bool) -> None
```

<a id="unreal.DynamicMeshChangeContainer"></a>