## InterchangeShaderGraphNode Objects

```python
class InterchangeShaderGraphNode(InterchangeShaderNode)
```

A shader graph has its own set of inputs on which shader nodes can be connected to.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeShaderGraphNode.h

<a id="unreal.InterchangeShaderGraphNode.set_custom_two_sided_transmission"></a>

#### set_custom_two_sided_transmission

```python
def set_custom_two_sided_transmission(attribute_value: bool) -> bool
```

x.set_custom_two_sided_transmission(attribute_value) -> bool
Set Custom Two Sided Transmission

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeShaderGraphNode.set_custom_two_sided"></a>

#### set_custom_two_sided

```python
def set_custom_two_sided(attribute_value: bool) -> bool
```

x.set_custom_two_sided(attribute_value) -> bool
Set if this shader graph should be rendered two-sided or not. Defaults to off.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeShaderGraphNode.set_custom_screen_space_reflections"></a>

#### set_custom_screen_space_reflections

```python
def set_custom_screen_space_reflections(attribute_value: bool) -> bool
```

x.set_custom_screen_space_reflections(attribute_value) -> bool
Set Custom Screen Space Reflections

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeShaderGraphNode.set_custom_opacity_mask_clip_value"></a>

#### set_custom_opacity_mask_clip_value

```python
def set_custom_opacity_mask_clip_value(attribute_value: float,
                                       add_apply_delegate: bool = True
                                       ) -> bool
```

x.set_custom_opacity_mask_clip_value(attribute_value, add_apply_delegate=True) -> bool
The shader is transparent if its alpha value is lower than the clip value, or opaque if it is higher.

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeShaderGraphNode.set_custom_is_a_shader_function"></a>

#### set_custom_is_a_shader_function

```python
def set_custom_is_a_shader_function(attribute_value: bool) -> bool
```

x.set_custom_is_a_shader_function(attribute_value) -> bool
Set whether this shader graph should be considered as a material (false), or a material function (true).

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeShaderGraphNode.set_custom_blend_mode"></a>

#### set_custom_blend_mode

```python
def set_custom_blend_mode(attribute_value: int) -> bool
```

x.set_custom_blend_mode(attribute_value) -> bool
Set Custom Blend Mode

Args:
    attribute_value (int32): 

Returns:
    bool:

<a id="unreal.InterchangeShaderGraphNode.get_custom_two_sided_transmission"></a>

#### get_custom_two_sided_transmission

```python
def get_custom_two_sided_transmission() -> Optional[bool]
```

x.get_custom_two_sided_transmission() -> bool or None
Forces two-sided even for Transmission materials.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeShaderGraphNode.get_custom_two_sided"></a>

#### get_custom_two_sided

```python
def get_custom_two_sided() -> Optional[bool]
```

x.get_custom_two_sided() -> bool or None
Get Custom Two Sided

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeShaderGraphNode.get_custom_screen_space_reflections"></a>

#### get_custom_screen_space_reflections

```python
def get_custom_screen_space_reflections() -> Optional[bool]
```

x.get_custom_screen_space_reflections() -> bool or None
Get Custom Screen Space Reflections

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeShaderGraphNode.get_custom_opacity_mask_clip_value"></a>

#### get_custom_opacity_mask_clip_value

```python
def get_custom_opacity_mask_clip_value() -> Optional[float]
```

x.get_custom_opacity_mask_clip_value() -> float or None
Get Custom Opacity Mask Clip Value

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeShaderGraphNode.get_custom_is_a_shader_function"></a>

#### get_custom_is_a_shader_function

```python
def get_custom_is_a_shader_function() -> Optional[bool]
```

x.get_custom_is_a_shader_function() -> bool or None
Get Custom Is AShader Function

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeShaderGraphNode.get_custom_blend_mode"></a>

#### get_custom_blend_mode

```python
def get_custom_blend_mode() -> Optional[int]
```

x.get_custom_blend_mode() -> int32 or None
Set the Blend Mode using EBlendMode to avoid a dependency on the Engine.

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeTexture2DNode"></a>