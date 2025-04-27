## BlueprintMaterialTextureNodesBPLibrary Objects

```python
class BlueprintMaterialTextureNodesBPLibrary(BlueprintFunctionLibrary)
```

*      Function library class.
*      Each function in it is expected to be static and represents blueprint node that can be called in any blueprint.
*
*      When declaring function you can define metadata for the node. Key function specifiers will be BlueprintPure and BlueprintCallable.
*      BlueprintPure - means the function does not affect the owning object in any way and thus creates a node without Exec pins.
*      BlueprintCallable - makes a function which can be executed in Blueprints - Thus it has Exec pins.
*      DisplayName - full name of the node, shown when you mouse over the node and in the blueprint drop down menu.
*                              Its lets you name the node using characters not allowed in C++ function names.
*      CompactNodeTitle - the word(s) that appear on the node.
*      Keywords -      the list of keywords that helps you to find node when you search for it using Blueprint drop-down menu.
*                              Good example is "Print String" node which you can find also by using keyword "log".
*      Category -      the category your node will be under in the Blueprint drop-down menu.
*
*      For more info on custom blueprint nodes visit documentation:
*      https://docs.unrealengine.com/ProgrammingAndScripting/Blueprints/TechnicalGuide/ExtendingBlueprints

**C++ Source:**

- **Plugin**: BlueprintMaterialTextureNodes
- **Module**: BlueprintMaterialTextureNodes
- **File**: BlueprintMaterialTextureNodesBPLibrary.h

<a id="unreal.BlueprintMaterialTextureNodesBPLibrary.texture2d_sample_uv_editor_only"></a>

#### texture2d_sample_uv_editor_only

```python
@classmethod
def texture2d_sample_uv_editor_only(cls, texture: Texture2D,
                                    uv: Vector2D) -> LinearColor
```

X.texture2d_sample_uv_editor_only(texture, uv) -> LinearColor
Samples a texel from a Texture 2D with VectorDisplacement Compression

Args:
    texture (Texture2D): 
    uv (Vector2D): 

Returns:
    LinearColor:

<a id="unreal.BlueprintMaterialTextureNodesBPLibrary.set_mic_vector_param_editor_only"></a>

#### set_mic_vector_param_editor_only

```python
@classmethod
def set_mic_vector_param_editor_only(
        cls,
        material: MaterialInstanceConstant,
        param_name: str,
        value: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> bool
```

X.set_mic_vector_param_editor_only(material, param_name, value=[0.000000, 0.000000, 0.000000, 0.000000]) -> bool
Sets a Vector Parameter value in a Material Instance Constant
Only works in the editor

Args:
    material (MaterialInstanceConstant): 
    param_name (str): 
    value (LinearColor): 

Returns:
    bool:

<a id="unreal.BlueprintMaterialTextureNodesBPLibrary.set_mic_two_sided_editor_only"></a>

#### set_mic_two_sided_editor_only

```python
@classmethod
def set_mic_two_sided_editor_only(cls,
                                  material: MaterialInstanceConstant,
                                  two_sided: bool = False) -> bool
```

X.set_mic_two_sided_editor_only(material, two_sided=False) -> bool
Overrides the Two Sided setting of a Material Instance Constant
Only works in the editor

Args:
    material (MaterialInstanceConstant): 
    two_sided (bool): 

Returns:
    bool:

<a id="unreal.BlueprintMaterialTextureNodesBPLibrary.set_mic_texture_param_editor_only"></a>

#### set_mic_texture_param_editor_only

```python
@classmethod
def set_mic_texture_param_editor_only(cls,
                                      material: MaterialInstanceConstant,
                                      param_name: str,
                                      texture: Texture2D = None) -> bool
```

X.set_mic_texture_param_editor_only(material, param_name, texture=None) -> bool
Sets a Texture Parameter value in a Material Instance Constant
Only works in the editor

Args:
    material (MaterialInstanceConstant): 
    param_name (str): 
    texture (Texture2D): 

Returns:
    bool:

<a id="unreal.BlueprintMaterialTextureNodesBPLibrary.set_mic_shading_model_editor_only"></a>

#### set_mic_shading_model_editor_only

```python
@classmethod
def set_mic_shading_model_editor_only(
    cls,
    material: MaterialInstanceConstant,
    shading_model: MaterialShadingModel = MaterialShadingModel.MSM_DEFAULT_LIT
) -> bool
```

X.set_mic_shading_model_editor_only(material, shading_model=MaterialShadingModel.MSM_DEFAULT_LIT) -> bool
Overrides the Shading Model of a Material Instance Constant
Only works in the editor

Args:
    material (MaterialInstanceConstant): 
    shading_model (MaterialShadingModel): 

Returns:
    bool:

<a id="unreal.BlueprintMaterialTextureNodesBPLibrary.set_mic_scalar_param_editor_only"></a>

#### set_mic_scalar_param_editor_only

```python
@classmethod
def set_mic_scalar_param_editor_only(cls,
                                     material: MaterialInstanceConstant,
                                     param_name: str = "test",
                                     value: float = 0.000000) -> bool
```

X.set_mic_scalar_param_editor_only(material, param_name="test", value=0.000000) -> bool
Sets a Scalar Parameter value in a Material Instance Constant
Only works in the editor

Args:
    material (MaterialInstanceConstant): 
    param_name (str): 
    value (float): 

Returns:
    bool:

<a id="unreal.BlueprintMaterialTextureNodesBPLibrary.set_mic_is_thin_surface_editor_only"></a>

#### set_mic_is_thin_surface_editor_only

```python
@classmethod
def set_mic_is_thin_surface_editor_only(cls,
                                        material: MaterialInstanceConstant,
                                        is_thin_surface: bool = False) -> bool
```

X.set_mic_is_thin_surface_editor_only(material, is_thin_surface=False) -> bool
Overrides the IsThinSurface setting of a Material Instance Constant
Only works in the editor

Args:
    material (MaterialInstanceConstant): 
    is_thin_surface (bool): 

Returns:
    bool:

<a id="unreal.BlueprintMaterialTextureNodesBPLibrary.set_mic_dithered_lod_transition_editor_only"></a>

#### set_mic_dithered_lod_transition_editor_only

```python
@classmethod
def set_mic_dithered_lod_transition_editor_only(
        cls,
        material: MaterialInstanceConstant,
        dithered_lod_transition: bool = False) -> bool
```

X.set_mic_dithered_lod_transition_editor_only(material, dithered_lod_transition=False) -> bool
Overrides the Blend Mode of a Material Instance Constant
Only works in the editor

Args:
    material (MaterialInstanceConstant): 
    dithered_lod_transition (bool): 

Returns:
    bool:

<a id="unreal.BlueprintMaterialTextureNodesBPLibrary.set_mic_blend_mode_editor_only"></a>

#### set_mic_blend_mode_editor_only

```python
@classmethod
def set_mic_blend_mode_editor_only(
        cls,
        material: MaterialInstanceConstant,
        blend_mode: BlendMode = BlendMode.BLEND_OPAQUE) -> bool
```

X.set_mic_blend_mode_editor_only(material, blend_mode=BlendMode.BLEND_OPAQUE) -> bool
Overrides the Blend Mode of a Material Instance Constant
Only works in the editor

Args:
    material (MaterialInstanceConstant): 
    blend_mode (BlendMode): 

Returns:
    bool:

<a id="unreal.BlueprintMaterialTextureNodesBPLibrary.render_target_sample_uv_editor_only"></a>

#### render_target_sample_uv_editor_only

```python
@classmethod
def render_target_sample_uv_editor_only(cls,
                                        render_target: TextureRenderTarget2D,
                                        uv: Vector2D) -> LinearColor
```

X.render_target_sample_uv_editor_only(render_target, uv) -> LinearColor
Samples a value from a Texture Render Target 2D. Currently only 4 channel formats are supported.
Only works in the editor

Args:
    render_target (TextureRenderTarget2D): 
    uv (Vector2D): 

Returns:
    LinearColor:

<a id="unreal.BlueprintMaterialTextureNodesBPLibrary.render_target_sample_rectangle_editor_only"></a>

#### render_target_sample_rectangle_editor_only

```python
@classmethod
def render_target_sample_rectangle_editor_only(
        cls, render_target: TextureRenderTarget2D,
        rect: LinearColor) -> Array[LinearColor]
```

X.render_target_sample_rectangle_editor_only(render_target, rect) -> Array[LinearColor]
Samples an array of values from a Texture Render Target 2D. Currently only 4 channel formats are supported.
Only works in the editor

Args:
    render_target (TextureRenderTarget2D): 
    rect (LinearColor): 

Returns:
    Array[LinearColor]:

<a id="unreal.BlueprintMaterialTextureNodesBPLibrary.create_mic_editor_only"></a>

#### create_mic_editor_only

```python
@classmethod
def create_mic_editor_only(cls,
                           material: MaterialInterface,
                           name: str = "MIC_") -> MaterialInstanceConstant
```

X.create_mic_editor_only(material, name="MIC_") -> MaterialInstanceConstant
Creates a new Material Instance Constant asset
Only works in the editor

Args:
    material (MaterialInterface): 
    name (str): 

Returns:
    MaterialInstanceConstant:

<a id="unreal.AndroidFileServerBPLibrary"></a>