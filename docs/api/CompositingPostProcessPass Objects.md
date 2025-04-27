## CompositingPostProcessPass Objects

```python
class CompositingPostProcessPass(CompositingElementTransform)
```

Compositing Post Process Pass

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: CompositingElementTransforms.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``intermediate`` (bool):  [Read-Write] Marks this pass for 'internal use only' - prevents it from being exposed to parent elements.
  When set, render target resources used by this element will be reused. For transforms, all 'Intermediate'
  passes are available to the next transform pass, and released after that.
- ``pass_name`` (Name):  [Read-Write]
- ``post_process_passes`` (Array[ComposurePostProcessPassPolicy]):  [Read-Write]
- ``render_scale`` (float):  [Read-Write]

<a id="unreal.CompositingPostProcessPass.render_scale"></a>

#### render_scale

```python
@property
def render_scale() -> float
```

(float):  [Read-Only]

<a id="unreal.CompositingPostProcessPass.post_process_passes"></a>

#### post_process_passes

```python
@property
def post_process_passes() -> Array[ComposurePostProcessPassPolicy]
```

(Array[ComposurePostProcessPassPolicy]):  [Read-Only]

<a id="unreal.CompositingElementMaterialPass"></a>