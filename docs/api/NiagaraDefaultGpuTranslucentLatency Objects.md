## NiagaraDefaultGpuTranslucentLatency Objects

```python
class NiagaraDefaultGpuTranslucentLatency(EnumBase)
```

ENiagara Default Gpu Translucent Latency

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraSettings.h

<a id="unreal.NiagaraDefaultGpuTranslucentLatency.IMMEDIATE"></a>

#### IMMEDIATE

0: Gpu simulations will always read this frames data for translucent materials.

<a id="unreal.NiagaraDefaultGpuTranslucentLatency.LATENT"></a>

#### LATENT

1: Gpu simulations will read the previous frames data if the simulation has to run in PostRenderOpaque.

<a id="unreal.NDISkelMesh_GpuMaxInfluences"></a>