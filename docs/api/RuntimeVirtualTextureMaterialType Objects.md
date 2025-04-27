## RuntimeVirtualTextureMaterialType Objects

```python
class RuntimeVirtualTextureMaterialType(EnumBase)
```

Enumeration of virtual texture stack layouts to support.
Extend this enumeration with other layouts as required. For example we will probably want to add a displacement texture option.
This "fixed function" approach will probably break down if we end up needing to support some complex set of attribute combinations but it is OK to begin with.

**C++ Source:**

- **Module**: Engine
- **File**: RuntimeVirtualTextureEnum.h

<a id="unreal.RuntimeVirtualTextureMaterialType.BASE_COLOR"></a>

#### BASE_COLOR

0

<a id="unreal.RuntimeVirtualTextureMaterialType.MASK4"></a>

#### MASK4

1: 4 channel mask texture.

<a id="unreal.RuntimeVirtualTextureMaterialType.BASE_COLOR_NORMAL_ROUGHNESS"></a>

#### BASE_COLOR_NORMAL_ROUGHNESS

2: Local space Normal. Requires less memory than 'Base Color, Normal, Roughness, Specular'. Supports LQ compression.

<a id="unreal.RuntimeVirtualTextureMaterialType.BASE_COLOR_NORMAL_SPECULAR"></a>

#### BASE_COLOR_NORMAL_SPECULAR

3

<a id="unreal.RuntimeVirtualTextureMaterialType.BASE_COLOR_NORMAL_SPECULAR_Y_CO_CG"></a>

#### BASE_COLOR_NORMAL_SPECULAR_Y_CO_CG

4: Base Color is stored in YCoCg space. This requires more memory but may provide better quality.

<a id="unreal.RuntimeVirtualTextureMaterialType.BASE_COLOR_NORMAL_SPECULAR_MASK_Y_CO_CG"></a>

#### BASE_COLOR_NORMAL_SPECULAR_MASK_Y_CO_CG

5: Base Color is stored in YCoCg space. This requires more memory but may provide better quality.

<a id="unreal.RuntimeVirtualTextureMaterialType.WORLD_HEIGHT"></a>

#### WORLD_HEIGHT

6

<a id="unreal.RuntimeVirtualTextureMaterialType.DISPLACEMENT"></a>

#### DISPLACEMENT

7

<a id="unreal.RuntimeVirtualTextureTextureAddressMode"></a>