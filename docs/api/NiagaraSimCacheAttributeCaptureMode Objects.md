## NiagaraSimCacheAttributeCaptureMode Objects

```python
class NiagaraSimCacheAttributeCaptureMode(EnumBase)
```

ENiagara Sim Cache Attribute Capture Mode

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraSimCache.h

<a id="unreal.NiagaraSimCacheAttributeCaptureMode.ALL"></a>

#### ALL

0: Captures all attributes available.
This kind of cache will be useful for restarting a simulation from or debugging.

<a id="unreal.NiagaraSimCacheAttributeCaptureMode.RENDERING_ONLY"></a>

#### RENDERING_ONLY

1: Captures attributes that are required to render the system only.
This kind of cache is useful for rendering only and should have a much smaller
size than capturing all attributes.

<a id="unreal.NiagaraSimCacheAttributeCaptureMode.EXPLICIT_ATTRIBUTES"></a>

#### EXPLICIT_ATTRIBUTES

2: Captures only attributes that match the 'ExplicitCaptureAttributes' list provided by the user.
This kind of cache is useful to keep the size down if you need to debug a very
specific attribute, or you want to do some additional process on the attributes
i.e. capture MyEmitter.Particles.Position and place static meshes in those locations.

<a id="unreal.NiagartaDataChannelReadResult"></a>