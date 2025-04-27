## BlendableLocation Objects

```python
class BlendableLocation(EnumBase)
```

Where to place a post process material in the post processing chain.

**C++ Source:**

- **Module**: Engine
- **File**: BlendableInterface.h

<a id="unreal.BlendableLocation.BL_SCENE_COLOR_BEFORE_DOF"></a>

#### BL_SCENE_COLOR_BEFORE_DOF

2: Post process material location to modify the scene color, between translucency distortion and DOF.
Always run at rendering resolution.
Inputs and output always in linear color space.

Input0:former pass scene color, excluding AfterDOF translucency
Input1:AfterDOF translucency.

<a id="unreal.BlendableLocation.BL_SCENE_COLOR_AFTER_DOF"></a>

#### BL_SCENE_COLOR_AFTER_DOF

1: Post process material location to modify the scene color, between DOF and AfterDOF translucency.
Always run at rendering resolution.
Inputs and output always in linear color space.

Input0:former pass scene color, excluding AfterDOF translucency
Input1:AfterDOF translucency.

<a id="unreal.BlendableLocation.BL_TRANSLUCENCY_AFTER_DOF"></a>

#### BL_TRANSLUCENCY_AFTER_DOF

5: Post process material location to modify the AfterDOF translucency, before composition into the scene color.
Always run at rendering resolution.
Inputs and output always in linear color space.

Input0:scene color without translucency, after DOF,
Input1:AfterDOF translucency.

<a id="unreal.BlendableLocation.BL_SSR_INPUT"></a>

#### BL_SSR_INPUT

4: Post process material location to compose a backplate into SSR, between TSR/TAA and next frame's SSR.
Runs at display resolution with TSR or TAAU, rendering resolution otherwise.
Inputs and output always in linear color space.

Input0:TAA/TSR output,

<a id="unreal.BlendableLocation.BL_SCENE_COLOR_BEFORE_BLOOM"></a>

#### BL_SCENE_COLOR_BEFORE_BLOOM

6: Post process material location to modify the scene color, before bloom.
Runs at display resolution with TSR or TAAU, rendering resolution otherwise.
Inputs and output always in linear color space.

Input0:former pass scene color,

<a id="unreal.BlendableLocation.BL_REPLACING_TONEMAPPER"></a>

#### BL_REPLACING_TONEMAPPER

3: Post process material replacing the tone mapper, to modify the scene color.
Runs at display resolution with TSR or TAAU, rendering resolution otherwise.
Inputs are always linear color space.

Input0:former pass scene color,
Input1:AfterDOF translucency.

<a id="unreal.BlendableLocation.BL_SCENE_COLOR_AFTER_TONEMAPPING"></a>

#### BL_SCENE_COLOR_AFTER_TONEMAPPING

0: Post process material location to modify the scene color, after tone mapper.
Runs at display resolution with TSR or TAAU, rendering resolution otherwise.
Inputs and output in different color spaces, based rendering settings for instance (sRGB/Rec709, HDR or even Linear Color).

Input0:former pass scene color,
Input1:AfterDOF translucency.

<a id="unreal.MaterialStencilCompare"></a>