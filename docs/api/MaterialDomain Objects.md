## MaterialDomain Objects

```python
class MaterialDomain(EnumBase)
```

Defines the domain of a material.

**C++ Source:**

- **Module**: Engine
- **File**: MaterialDomain.h

<a id="unreal.MaterialDomain.MD_SURFACE"></a>

#### MD\_SURFACE

0: The material's attributes describe a 3d surface.

<a id="unreal.MaterialDomain.MD_DEFERRED_DECAL"></a>

#### MD\_DEFERRED\_DECAL

1: The material's attributes describe a deferred decal, and will be mapped onto the decal's frustum.

<a id="unreal.MaterialDomain.MD_LIGHT_FUNCTION"></a>

#### MD\_LIGHT\_FUNCTION

2: The material's attributes describe a light's distribution.

<a id="unreal.MaterialDomain.MD_VOLUME"></a>

#### MD\_VOLUME

3: The material's attributes describe a 3d volume.

<a id="unreal.MaterialDomain.MD_POST_PROCESS"></a>

#### MD\_POST\_PROCESS

4: The material will be used in a custom post process pass.

<a id="unreal.MaterialDomain.MD_UI"></a>

#### MD\_UI

5: The material will be used for UMG or Slate UI

<a id="unreal.DecalBlendMode"></a>