## NiagaraRendererSourceDataMode Objects

```python
class NiagaraRendererSourceDataMode(EnumBase)
```

This enum decides how a renderer will attempt to process the incoming data from the stack.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraCommon.h

<a id="unreal.NiagaraRendererSourceDataMode.PARTICLES"></a>

#### PARTICLES

0: The renderer will draw particle data, but can potentially pull in data from the Emitter/User/or System namespaces when drawing each Particle.

<a id="unreal.NiagaraRendererSourceDataMode.EMITTER"></a>

#### EMITTER

1: The renderer will draw only one element per Emitter. It can only pull in data from Emitter/User/or System namespaces when drawing the single element.

<a id="unreal.NiagaraPreviewGridResetMode"></a>