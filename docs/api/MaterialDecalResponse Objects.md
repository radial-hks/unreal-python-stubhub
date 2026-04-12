## MaterialDecalResponse Objects

```python
class MaterialDecalResponse(EnumBase)
```

Defines how the material reacts on DBuffer decals, later we can expose more variants between None and Default.

**C++ Source:**

- **Module**: Engine
- **File**: Material.h

<a id="unreal.MaterialDecalResponse.MDR_NONE"></a>

#### MDR\_NONE

0: Do not receive decals (Later we still can read the DBuffer channels to customize the effect, this frees up some interpolators).

<a id="unreal.MaterialDecalResponse.MDR_COLOR_NORMAL_ROUGHNESS"></a>

#### MDR\_COLOR\_NORMAL\_ROUGHNESS

1: Receive Decals, applies all DBuffer channels.

<a id="unreal.MaterialDecalResponse.MDR_COLOR"></a>

#### MDR\_COLOR

2: Receive Decals, applies color DBuffer channels.

<a id="unreal.MaterialDecalResponse.MDR_COLOR_NORMAL"></a>

#### MDR\_COLOR\_NORMAL

3: Receive Decals, applies color and normal DBuffer channels.

<a id="unreal.MaterialDecalResponse.MDR_COLOR_ROUGHNESS"></a>

#### MDR\_COLOR\_ROUGHNESS

4: Receive Decals, applies color, roughness, specular and metallic DBuffer channels.

<a id="unreal.MaterialDecalResponse.MDR_NORMAL"></a>

#### MDR\_NORMAL

5: Receive Decals, applies normal DBuffer channels.

<a id="unreal.MaterialDecalResponse.MDR_NORMAL_ROUGHNESS"></a>

#### MDR\_NORMAL\_ROUGHNESS

6: Receive Decals, applies normal, roughness, specular and metallic DBuffer channels.

<a id="unreal.MaterialDecalResponse.MDR_ROUGHNESS"></a>

#### MDR\_ROUGHNESS

7: Receive Decals, applies roughness, specular and metallic DBuffer channels.

<a id="unreal.MaterialShadingModel"></a>