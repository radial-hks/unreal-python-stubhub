## DecalBlendMode Objects

```python
class DecalBlendMode(EnumBase)
```

Defines how the GBuffer channels are getting manipulated by a decal material pass. Actual index is used to control shader parameters so don't change order.

**C++ Source:**

- **Module**: Engine
- **File**: Material.h

<a id="unreal.DecalBlendMode.DBM_TRANSLUCENT"></a>

#### DBM_TRANSLUCENT

0: Blend full material, updating the GBuffer, does not work for baked lighting.

<a id="unreal.DecalBlendMode.DBM_STAIN"></a>

#### DBM_STAIN

1: Modulate BaseColor, blend rest, updating the GBuffer, does not work for baked lighting. Does not work in DBuffer mode (approximated as Translucent).

<a id="unreal.DecalBlendMode.DBM_NORMAL"></a>

#### DBM_NORMAL

2: Only blend normal, updating the GBuffer, does not work for baked lighting.

<a id="unreal.DecalBlendMode.DBM_EMISSIVE"></a>

#### DBM_EMISSIVE

3: Additive emissive only.

<a id="unreal.DecalBlendMode.DBM_D_BUFFER_COLOR_NORMAL_ROUGHNESS"></a>

#### DBM_D_BUFFER_COLOR_NORMAL_ROUGHNESS

4: Put into DBuffer to work for baked lighting as well (becomes DBM_TranslucentNormal if normal is not hooked up).

<a id="unreal.DecalBlendMode.DBM_D_BUFFER_COLOR"></a>

#### DBM_D_BUFFER_COLOR

5: Put into DBuffer to work for baked lighting as well.

<a id="unreal.DecalBlendMode.DBM_D_BUFFER_COLOR_NORMAL"></a>

#### DBM_D_BUFFER_COLOR_NORMAL

6: Put into DBuffer to work for baked lighting as well (becomes DBM_DBuffer_Color if normal is not hooked up).

<a id="unreal.DecalBlendMode.DBM_D_BUFFER_COLOR_ROUGHNESS"></a>

#### DBM_D_BUFFER_COLOR_ROUGHNESS

7: Put into DBuffer to work for baked lighting as well.

<a id="unreal.DecalBlendMode.DBM_D_BUFFER_NORMAL"></a>

#### DBM_D_BUFFER_NORMAL

8: Put into DBuffer to work for baked lighting as well.

<a id="unreal.DecalBlendMode.DBM_D_BUFFER_NORMAL_ROUGHNESS"></a>

#### DBM_D_BUFFER_NORMAL_ROUGHNESS

9: Put into DBuffer to work for baked lighting as well (becomes DBM_DBuffer_Roughness if normal is not hooked up).

<a id="unreal.DecalBlendMode.DBM_D_BUFFER_ROUGHNESS"></a>

#### DBM_D_BUFFER_ROUGHNESS

10: Put into DBuffer to work for baked lighting as well.

<a id="unreal.DecalBlendMode.DBM_VOLUMETRIC_DISTANCE_FUNCTION"></a>

#### DBM_VOLUMETRIC_DISTANCE_FUNCTION

14: Output signed distance in Opacity depending on LightVector. Note: Can be costly, no shadow casting but receiving, no per pixel normal yet, no quality settings yet

<a id="unreal.DecalBlendMode.DBM_ALPHA_COMPOSITE"></a>

#### DBM_ALPHA_COMPOSITE

15: Blend with existing scene color. Decal color is already pre-multiplied by alpha.

<a id="unreal.DecalBlendMode.DBM_AMBIENT_OCCLUSION"></a>

#### DBM_AMBIENT_OCCLUSION

16: Ambient occlusion.

<a id="unreal.MaterialDecalResponse"></a>