## InterchangeMaterialFactoryNode Objects

```python
class InterchangeMaterialFactoryNode(InterchangeBaseMaterialFactoryNode)
```

Interchange Material Factory Node

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeMaterialFactoryNode.h

<a id="unreal.InterchangeMaterialFactoryNode.set_custom_two_sided"></a>

#### set\_custom\_two\_sided

```python
def set_custom_two_sided(attribute_value: bool,
                         add_apply_delegate: bool = True) -> bool
```

x.set_custom_two_sided(attribute_value, add_apply_delegate=True) -> bool
Sets if this shader graph should be rendered two sided or not. Defaults to off.

Args:
    attribute_value (bool): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.set_custom_translucency_lighting_mode"></a>

#### set\_custom\_translucency\_lighting\_mode

```python
def set_custom_translucency_lighting_mode(
        attribute_value: TranslucencyLightingMode,
        add_apply_delegate: bool = True) -> bool
```

x.set_custom_translucency_lighting_mode(attribute_value, add_apply_delegate=True) -> bool
Set Custom Translucency Lighting Mode

Args:
    attribute_value (TranslucencyLightingMode): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.set_custom_shading_model"></a>

#### set\_custom\_shading\_model

```python
def set_custom_shading_model(attribute_value: MaterialShadingModel,
                             add_apply_delegate: bool = True) -> bool
```

x.set_custom_shading_model(attribute_value, add_apply_delegate=True) -> bool
Set Custom Shading Model

Args:
    attribute_value (MaterialShadingModel): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.set_custom_screen_space_reflections"></a>

#### set\_custom\_screen\_space\_reflections

```python
def set_custom_screen_space_reflections(attribute_value: bool) -> bool
```

x.set_custom_screen_space_reflections(attribute_value) -> bool
Set Custom Screen Space Reflections

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.set_custom_refraction_method"></a>

#### set\_custom\_refraction\_method

```python
def set_custom_refraction_method(attribute_value: RefractionMode,
                                 add_apply_delegate: bool = True) -> bool
```

x.set_custom_refraction_method(attribute_value, add_apply_delegate=True) -> bool
Set Custom Refraction Method

Args:
    attribute_value (RefractionMode): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.set_custom_opacity_mask_clip_value"></a>

#### set\_custom\_opacity\_mask\_clip\_value

```python
def set_custom_opacity_mask_clip_value(attribute_value: float,
                                       add_apply_delegate: bool = True
                                       ) -> bool
```

x.set_custom_opacity_mask_clip_value(attribute_value, add_apply_delegate=True) -> bool
Set Custom Opacity Mask Clip Value

Args:
    attribute_value (float): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.set_custom_blend_mode"></a>

#### set\_custom\_blend\_mode

```python
def set_custom_blend_mode(attribute_value: BlendMode,
                          add_apply_delegate: bool = True) -> bool
```

x.set_custom_blend_mode(attribute_value, add_apply_delegate=True) -> bool
Set Custom Blend Mode

Args:
    attribute_value (BlendMode): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.get_transmission_color_connection"></a>

#### get\_transmission\_color\_connection

```python
def get_transmission_color_connection() -> Optional[Tuple[str, str]]
```

x.get_transmission_color_connection() -> (expression_node_uid=str, output_name=str) or None
Get Transmission Color Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_tangent_connection"></a>

#### get\_tangent\_connection

```python
def get_tangent_connection() -> Optional[Tuple[str, str]]
```

x.get_tangent_connection() -> (expression_node_uid=str, output_name=str) or None
Get Tangent Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_surface_coverage_connection"></a>

#### get\_surface\_coverage\_connection

```python
def get_surface_coverage_connection() -> Optional[Tuple[str, str]]
```

x.get_surface_coverage_connection() -> (expression_node_uid=str, output_name=str) or None
Get Surface Coverage Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_subsurface_connection"></a>

#### get\_subsurface\_connection

```python
def get_subsurface_connection() -> Optional[Tuple[str, str]]
```

x.get_subsurface_connection() -> (expression_node_uid=str, output_name=str) or None
Get Subsurface Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_specular_connection"></a>

#### get\_specular\_connection

```python
def get_specular_connection() -> Optional[Tuple[str, str]]
```

x.get_specular_connection() -> (expression_node_uid=str, output_name=str) or None
Get Specular Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_roughness_connection"></a>

#### get\_roughness\_connection

```python
def get_roughness_connection() -> Optional[Tuple[str, str]]
```

x.get_roughness_connection() -> (expression_node_uid=str, output_name=str) or None
Get Roughness Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_refraction_connection"></a>

#### get\_refraction\_connection

```python
def get_refraction_connection() -> Optional[Tuple[str, str]]
```

x.get_refraction_connection() -> (expression_node_uid=str, output_name=str) or None
Get Refraction Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_opacity_connection"></a>

#### get\_opacity\_connection

```python
def get_opacity_connection() -> Optional[Tuple[str, str]]
```

x.get_opacity_connection() -> (expression_node_uid=str, output_name=str) or None
Get Opacity Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_occlusion_connection"></a>

#### get\_occlusion\_connection

```python
def get_occlusion_connection() -> Optional[Tuple[str, str]]
```

x.get_occlusion_connection() -> (expression_node_uid=str, output_name=str) or None
Get Occlusion Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_object_class"></a>

#### get\_object\_class

```python
def get_object_class() -> Class
```

x.get_object_class() -> type(Class)
Get Object Class

Returns:
    type(Class):

<a id="unreal.InterchangeMaterialFactoryNode.get_normal_connection"></a>

#### get\_normal\_connection

```python
def get_normal_connection() -> Optional[Tuple[str, str]]
```

x.get_normal_connection() -> (expression_node_uid=str, output_name=str) or None
Get Normal Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_metallic_connection"></a>

#### get\_metallic\_connection

```python
def get_metallic_connection() -> Optional[Tuple[str, str]]
```

x.get_metallic_connection() -> (expression_node_uid=str, output_name=str) or None
Get Metallic Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_fuzz_color_connection"></a>

#### get\_fuzz\_color\_connection

```python
def get_fuzz_color_connection() -> Optional[Tuple[str, str]]
```

x.get_fuzz_color_connection() -> (expression_node_uid=str, output_name=str) or None
Get Fuzz Color Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_emissive_color_connection"></a>

#### get\_emissive\_color\_connection

```python
def get_emissive_color_connection() -> Optional[Tuple[str, str]]
```

x.get_emissive_color_connection() -> (expression_node_uid=str, output_name=str) or None
Get Emissive Color Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_displacement_connection"></a>

#### get\_displacement\_connection

```python
def get_displacement_connection() -> Optional[Tuple[str, str]]
```

x.get_displacement_connection() -> (expression_node_uid=str, output_name=str) or None
Get Displacement Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_custom_two_sided"></a>

#### get\_custom\_two\_sided

```python
def get_custom_two_sided() -> Optional[bool]
```

x.get_custom_two_sided() -> bool or None
Get Custom Two Sided

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMaterialFactoryNode.get_custom_translucency_lighting_mode"></a>

#### get\_custom\_translucency\_lighting\_mode

```python
def get_custom_translucency_lighting_mode(
) -> Optional[TranslucencyLightingMode]
```

x.get_custom_translucency_lighting_mode() -> TranslucencyLightingMode or None
Get Custom Translucency Lighting Mode

Returns:
    TranslucencyLightingMode or None: 

    attribute_value (TranslucencyLightingMode):

<a id="unreal.InterchangeMaterialFactoryNode.get_custom_shading_model"></a>

#### get\_custom\_shading\_model

```python
def get_custom_shading_model() -> Optional[MaterialShadingModel]
```

x.get_custom_shading_model() -> MaterialShadingModel or None
Get Custom Shading Model

Returns:
    MaterialShadingModel or None: 

    attribute_value (MaterialShadingModel):

<a id="unreal.InterchangeMaterialFactoryNode.get_custom_screen_space_reflections"></a>

#### get\_custom\_screen\_space\_reflections

```python
def get_custom_screen_space_reflections() -> Optional[bool]
```

x.get_custom_screen_space_reflections() -> bool or None
Get Custom Screen Space Reflections

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeMaterialFactoryNode.get_custom_refraction_method"></a>

#### get\_custom\_refraction\_method

```python
def get_custom_refraction_method() -> Optional[RefractionMode]
```

x.get_custom_refraction_method() -> RefractionMode or None
Get Custom Refraction Method

Returns:
    RefractionMode or None: 

    attribute_value (RefractionMode):

<a id="unreal.InterchangeMaterialFactoryNode.get_custom_opacity_mask_clip_value"></a>

#### get\_custom\_opacity\_mask\_clip\_value

```python
def get_custom_opacity_mask_clip_value() -> Optional[float]
```

x.get_custom_opacity_mask_clip_value() -> float or None
Get Custom Opacity Mask Clip Value

Returns:
    float or None: 

    attribute_value (float):

<a id="unreal.InterchangeMaterialFactoryNode.get_custom_blend_mode"></a>

#### get\_custom\_blend\_mode

```python
def get_custom_blend_mode() -> Optional[BlendMode]
```

x.get_custom_blend_mode() -> BlendMode or None
Get Custom Blend Mode

Returns:
    BlendMode or None: 

    attribute_value (BlendMode):

<a id="unreal.InterchangeMaterialFactoryNode.get_cloth_connection"></a>

#### get\_cloth\_connection

```python
def get_cloth_connection() -> Optional[Tuple[str, str]]
```

x.get_cloth_connection() -> (expression_node_uid=str, output_name=str) or None
Get Cloth Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_clear_coat_roughness_connection"></a>

#### get\_clear\_coat\_roughness\_connection

```python
def get_clear_coat_roughness_connection() -> Optional[Tuple[str, str]]
```

x.get_clear_coat_roughness_connection() -> (expression_node_uid=str, output_name=str) or None
Get Clear Coat Roughness Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_clear_coat_normal_connection"></a>

#### get\_clear\_coat\_normal\_connection

```python
def get_clear_coat_normal_connection() -> Optional[Tuple[str, str]]
```

x.get_clear_coat_normal_connection() -> (expression_node_uid=str, output_name=str) or None
Get Clear Coat Normal Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_clear_coat_connection"></a>

#### get\_clear\_coat\_connection

```python
def get_clear_coat_connection() -> Optional[Tuple[str, str]]
```

x.get_clear_coat_connection() -> (expression_node_uid=str, output_name=str) or None
Get Clear Coat Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_base_color_connection"></a>

#### get\_base\_color\_connection

```python
def get_base_color_connection() -> Optional[Tuple[str, str]]
```

x.get_base_color_connection() -> (expression_node_uid=str, output_name=str) or None
Get Base Color Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.get_anisotropy_connection"></a>

#### get\_anisotropy\_connection

```python
def get_anisotropy_connection() -> Optional[Tuple[str, str]]
```

x.get_anisotropy_connection() -> (expression_node_uid=str, output_name=str) or None
Get Anisotropy Connection

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_transmission_color"></a>

#### connect\_to\_transmission\_color

```python
def connect_to_transmission_color(attribute_value: str) -> bool
```

x.connect_to_transmission_color(attribute_value) -> bool
Connect to Transmission Color

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_tangent"></a>

#### connect\_to\_tangent

```python
def connect_to_tangent(expression_node_uid: str) -> bool
```

x.connect_to_tangent(expression_node_uid) -> bool
Connect to Tangent

Args:
    expression_node_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_surface_coverage"></a>

#### connect\_to\_surface\_coverage

```python
def connect_to_surface_coverage(expression_uid: str) -> bool
```

x.connect_to_surface_coverage(expression_uid) -> bool
Connect to Surface Coverage

Args:
    expression_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_subsurface"></a>

#### connect\_to\_subsurface

```python
def connect_to_subsurface(expression_node_uid: str) -> bool
```

x.connect_to_subsurface(expression_node_uid) -> bool
Connect to Subsurface

Args:
    expression_node_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_specular"></a>

#### connect\_to\_specular

```python
def connect_to_specular(expression_node_uid: str) -> bool
```

x.connect_to_specular(expression_node_uid) -> bool
Connect to Specular

Args:
    expression_node_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_roughness"></a>

#### connect\_to\_roughness

```python
def connect_to_roughness(expression_node_uid: str) -> bool
```

x.connect_to_roughness(expression_node_uid) -> bool
Connect to Roughness

Args:
    expression_node_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_refraction"></a>

#### connect\_to\_refraction

```python
def connect_to_refraction(attribute_value: str) -> bool
```

x.connect_to_refraction(attribute_value) -> bool
Connect to Refraction

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_opacity"></a>

#### connect\_to\_opacity

```python
def connect_to_opacity(attribute_value: str) -> bool
```

x.connect_to_opacity(attribute_value) -> bool
Connect to Opacity

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_occlusion"></a>

#### connect\_to\_occlusion

```python
def connect_to_occlusion(attribute_value: str) -> bool
```

x.connect_to_occlusion(attribute_value) -> bool
Connect to Occlusion

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_normal"></a>

#### connect\_to\_normal

```python
def connect_to_normal(expression_node_uid: str) -> bool
```

x.connect_to_normal(expression_node_uid) -> bool
Connect to Normal

Args:
    expression_node_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_metallic"></a>

#### connect\_to\_metallic

```python
def connect_to_metallic(attribute_value: str) -> bool
```

x.connect_to_metallic(attribute_value) -> bool
Connect to Metallic

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_fuzz_color"></a>

#### connect\_to\_fuzz\_color

```python
def connect_to_fuzz_color(attribute_value: str) -> bool
```

x.connect_to_fuzz_color(attribute_value) -> bool
Connect to Fuzz Color

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_emissive_color"></a>

#### connect\_to\_emissive\_color

```python
def connect_to_emissive_color(expression_node_uid: str) -> bool
```

x.connect_to_emissive_color(expression_node_uid) -> bool
Connect to Emissive Color

Args:
    expression_node_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_displacement"></a>

#### connect\_to\_displacement

```python
def connect_to_displacement(attribute_value: str) -> bool
```

x.connect_to_displacement(attribute_value) -> bool
Connect to Displacement

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_cloth"></a>

#### connect\_to\_cloth

```python
def connect_to_cloth(attribute_value: str) -> bool
```

x.connect_to_cloth(attribute_value) -> bool
Connect to Cloth

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_clear_coat_roughness"></a>

#### connect\_to\_clear\_coat\_roughness

```python
def connect_to_clear_coat_roughness(attribute_value: str) -> bool
```

x.connect_to_clear_coat_roughness(attribute_value) -> bool
Connect to Clear Coat Roughness

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_clear_coat_normal"></a>

#### connect\_to\_clear\_coat\_normal

```python
def connect_to_clear_coat_normal(attribute_value: str) -> bool
```

x.connect_to_clear_coat_normal(attribute_value) -> bool
Connect to Clear Coat Normal

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_clear_coat"></a>

#### connect\_to\_clear\_coat

```python
def connect_to_clear_coat(attribute_value: str) -> bool
```

x.connect_to_clear_coat(attribute_value) -> bool
Connect to Clear Coat

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_base_color"></a>

#### connect\_to\_base\_color

```python
def connect_to_base_color(attribute_value: str) -> bool
```

x.connect_to_base_color(attribute_value) -> bool
Connect to Base Color

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_to_anisotropy"></a>

#### connect\_to\_anisotropy

```python
def connect_to_anisotropy(expression_node_uid: str) -> bool
```

x.connect_to_anisotropy(expression_node_uid) -> bool
Connect to Anisotropy

Args:
    expression_node_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_transmission_color"></a>

#### connect\_output\_to\_transmission\_color

```python
def connect_output_to_transmission_color(expression_node_uid: str,
                                         output_name: str) -> bool
```

x.connect_output_to_transmission_color(expression_node_uid, output_name) -> bool
Connect Output to Transmission Color

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_tangent"></a>

#### connect\_output\_to\_tangent

```python
def connect_output_to_tangent(expression_node_uid: str,
                              output_name: str) -> bool
```

x.connect_output_to_tangent(expression_node_uid, output_name) -> bool
Connect Output to Tangent

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_surface_coverage"></a>

#### connect\_output\_to\_surface\_coverage

```python
def connect_output_to_surface_coverage(expression_node_uid: str,
                                       output_name: str) -> bool
```

x.connect_output_to_surface_coverage(expression_node_uid, output_name) -> bool
Connect Output to Surface Coverage

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_subsurface"></a>

#### connect\_output\_to\_subsurface

```python
def connect_output_to_subsurface(expression_node_uid: str,
                                 output_name: str) -> bool
```

x.connect_output_to_subsurface(expression_node_uid, output_name) -> bool
Connect Output to Subsurface

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_specular"></a>

#### connect\_output\_to\_specular

```python
def connect_output_to_specular(expression_node_uid: str,
                               output_name: str) -> bool
```

x.connect_output_to_specular(expression_node_uid, output_name) -> bool
Connect Output to Specular

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_roughness"></a>

#### connect\_output\_to\_roughness

```python
def connect_output_to_roughness(expression_node_uid: str,
                                output_name: str) -> bool
```

x.connect_output_to_roughness(expression_node_uid, output_name) -> bool
Connect Output to Roughness

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_refraction"></a>

#### connect\_output\_to\_refraction

```python
def connect_output_to_refraction(expression_node_uid: str,
                                 output_name: str) -> bool
```

x.connect_output_to_refraction(expression_node_uid, output_name) -> bool
Connect Output to Refraction

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_opacity"></a>

#### connect\_output\_to\_opacity

```python
def connect_output_to_opacity(expression_node_uid: str,
                              output_name: str) -> bool
```

x.connect_output_to_opacity(expression_node_uid, output_name) -> bool
Connect Output to Opacity

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_occlusion"></a>

#### connect\_output\_to\_occlusion

```python
def connect_output_to_occlusion(expression_node_uid: str,
                                output_name: str) -> bool
```

x.connect_output_to_occlusion(expression_node_uid, output_name) -> bool
Connect Output to Occlusion

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_normal"></a>

#### connect\_output\_to\_normal

```python
def connect_output_to_normal(expression_node_uid: str,
                             output_name: str) -> bool
```

x.connect_output_to_normal(expression_node_uid, output_name) -> bool
Connect Output to Normal

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_metallic"></a>

#### connect\_output\_to\_metallic

```python
def connect_output_to_metallic(expression_node_uid: str,
                               output_name: str) -> bool
```

x.connect_output_to_metallic(expression_node_uid, output_name) -> bool
Connect Output to Metallic

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_fuzz_color"></a>

#### connect\_output\_to\_fuzz\_color

```python
def connect_output_to_fuzz_color(expression_node_uid: str,
                                 output_name: str) -> bool
```

x.connect_output_to_fuzz_color(expression_node_uid, output_name) -> bool
Connect Output to Fuzz Color

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_emissive_color"></a>

#### connect\_output\_to\_emissive\_color

```python
def connect_output_to_emissive_color(expression_node_uid: str,
                                     output_name: str) -> bool
```

x.connect_output_to_emissive_color(expression_node_uid, output_name) -> bool
Connect Output to Emissive Color

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_displacement"></a>

#### connect\_output\_to\_displacement

```python
def connect_output_to_displacement(expression_node_uid: str,
                                   output_name: str) -> bool
```

x.connect_output_to_displacement(expression_node_uid, output_name) -> bool
Connect Output to Displacement

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_cloth"></a>

#### connect\_output\_to\_cloth

```python
def connect_output_to_cloth(expression_node_uid: str,
                            output_name: str) -> bool
```

x.connect_output_to_cloth(expression_node_uid, output_name) -> bool
Connect Output to Cloth

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_clear_coat_roughness"></a>

#### connect\_output\_to\_clear\_coat\_roughness

```python
def connect_output_to_clear_coat_roughness(expression_node_uid: str,
                                           output_name: str) -> bool
```

x.connect_output_to_clear_coat_roughness(expression_node_uid, output_name) -> bool
Connect Output to Clear Coat Roughness

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_clear_coat_normal"></a>

#### connect\_output\_to\_clear\_coat\_normal

```python
def connect_output_to_clear_coat_normal(expression_node_uid: str,
                                        output_name: str) -> bool
```

x.connect_output_to_clear_coat_normal(expression_node_uid, output_name) -> bool
Connect Output to Clear Coat Normal

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_clear_coat"></a>

#### connect\_output\_to\_clear\_coat

```python
def connect_output_to_clear_coat(expression_node_uid: str,
                                 output_name: str) -> bool
```

x.connect_output_to_clear_coat(expression_node_uid, output_name) -> bool
Connect Output to Clear Coat

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_base_color"></a>

#### connect\_output\_to\_base\_color

```python
def connect_output_to_base_color(expression_node_uid: str,
                                 output_name: str) -> bool
```

x.connect_output_to_base_color(expression_node_uid, output_name) -> bool
Connect Output to Base Color

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFactoryNode.connect_output_to_anisotropy"></a>

#### connect\_output\_to\_anisotropy

```python
def connect_output_to_anisotropy(expression_node_uid: str,
                                 output_name: str) -> bool
```

x.connect_output_to_anisotropy(expression_node_uid, output_name) -> bool
Connect Output to Anisotropy

Args:
    expression_node_uid (str): 
    output_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialExpressionFactoryNode"></a>