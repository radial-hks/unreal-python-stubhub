## RefractionMode Objects

```python
class RefractionMode(EnumBase)
```

Determines how the refraction offset should be computed for the material.

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.RefractionMode.RM_INDEX_OF_REFRACTION"></a>

#### RM_INDEX_OF_REFRACTION

0: By default, when the root node refraction pin is unplugged, relies on the material IOR evaluated from F0.
Refraction is computed based on the camera vector entering a medium whose index of refraction is defined by the Refraction material input.
The new medium's surface is defined by the material's normal.  With this mode, a flat plane seen from the side will have a constant refraction offset.
This is a physical model of refraction but causes reading outside the scene color texture so is a poor fit for large refractive surfaces like water.

<a id="unreal.RefractionMode.RM_PIXEL_NORMAL_OFFSET"></a>

#### RM_PIXEL_NORMAL_OFFSET

1: By default, when the root node refraction pin is unplugged, no refraction will appear.
The refraction offset into Scene Color is computed based on the difference between the per-pixel normal and the per-vertex normal.
With this mode, a material whose normal is the default (0, 0, 1) will never cause any refraction.  This mode is only valid with tangent space normals.
The refraction material input scales the offset, although a value of 1.0 maps to no refraction, and a value of 2 maps to a scale of 1.0 on the offset.
This is a non-physical model of refraction but is useful on large refractive surfaces like water, since offsets have to stay small to avoid reading outside scene color.

<a id="unreal.RefractionMode.RM_2D_OFFSET"></a>

#### RM_2D_OFFSET

2: By default, when the root node refraction pin is unplugged, no refraction will appear.
Explicit 2D screen offset. This offset is independent of screen resolution and aspect ratio. The user is in charge of any strength and fading.

<a id="unreal.RefractionMode.RM_NONE"></a>

#### RM_NONE

3: Refraction is disabled.

<a id="unreal.RefractionCoverageMode"></a>