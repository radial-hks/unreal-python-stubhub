## RuntimeVirtualTextureMainPassType Objects

```python
class RuntimeVirtualTextureMainPassType(EnumBase)
```

Enumeration of main pass behaviors when rendering to a runtime virtual texture.

**C++ Source:**

- **Module**: Engine
- **File**: RuntimeVirtualTextureEnum.h

<a id="unreal.RuntimeVirtualTextureMainPassType.NEVER"></a>

#### NEVER

0: Never render to the main pass.
Use this for primitives that only render to Runtime Virtual Texture and can be missing if there is no virtual texture support.

<a id="unreal.RuntimeVirtualTextureMainPassType.EXCLUSIVE"></a>

#### EXCLUSIVE

1: Render to the main pass if no associated Runtime Virtual Texture Volumes are set to 'Hide Primitives'.
This will render to the main pass if there is no matching Runtime Virtual Texture Volume placed in the scene.

<a id="unreal.RuntimeVirtualTextureMainPassType.ALWAYS"></a>

#### ALWAYS

2: Always render to the main pass.
Use this for items that both read from and write to a Runtime Virtual Texture.

<a id="unreal.HLODLevelExclusion"></a>