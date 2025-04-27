## CompositingElementTransform Objects

```python
class CompositingElementTransform(CompositingElementPass)
```

Compositing Element Transform

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: CompositingElementPasses.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``intermediate`` (bool):  [Read-Write] Marks this pass for 'internal use only' - prevents it from being exposed to parent elements.
  When set, render target resources used by this element will be reused. For transforms, all 'Intermediate'
  passes are available to the next transform pass, and released after that.
- ``pass_name`` (Name):  [Read-Write]

<a id="unreal.CompositingElementTransform.intermediate"></a>

#### intermediate

```python
@property
def intermediate() -> bool
```

(bool):  [Read-Only] Marks this pass for 'internal use only' - prevents it from being exposed to parent elements.
When set, render target resources used by this element will be reused. For transforms, all 'Intermediate'
passes are available to the next transform pass, and released after that.

<a id="unreal.CompositingElementTransform.find_named_pre_pass_result"></a>

#### find_named_pre_pass_result

```python
def find_named_pre_pass_result(pass_lookup_name: Name) -> Texture
```

x.find_named_pre_pass_result(pass_lookup_name) -> Texture
Find Named Pre Pass Result

Args:
    pass_lookup_name (Name): 

Returns:
    Texture:

<a id="unreal.CompositingElementTransform.apply_transform"></a>

#### apply_transform

```python
def apply_transform(input: Texture,
                    post_process_proxy: ComposurePostProcessingPassProxy,
                    target_camera: CameraActor) -> Texture
```

x.apply_transform(input, post_process_proxy, target_camera) -> Texture
Apply Transform

Args:
    input (Texture): 
    post_process_proxy (ComposurePostProcessingPassProxy): 
    target_camera (CameraActor): 

Returns:
    Texture:

<a id="unreal.CompositingPostProcessPass"></a>