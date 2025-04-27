## SamplerSourceMode Objects

```python
class SamplerSourceMode(EnumBase)
```

Controls where the sampler for different texture lookups comes from

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

<a id="unreal.SamplerSourceMode.SSM_FROM_TEXTURE_ASSET"></a>

#### SSM_FROM_TEXTURE_ASSET

0: Get the sampler from the texture.  Every unique texture will consume a sampler slot, which are limited in number.

<a id="unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS"></a>

#### SSM_WRAP_WORLD_GROUP_SETTINGS

1: Shared sampler source that does not consume a sampler slot.  Uses wrap addressing and gets filter mode from the world texture group.

<a id="unreal.SamplerSourceMode.SSM_CLAMP_WORLD_GROUP_SETTINGS"></a>

#### SSM_CLAMP_WORLD_GROUP_SETTINGS

2: Shared sampler source that does not consume a sampler slot.  Uses clamp addressing and gets filter mode from the world texture group.

<a id="unreal.TextureColorChannel"></a>