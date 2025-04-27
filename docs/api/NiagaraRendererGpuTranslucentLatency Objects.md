## NiagaraRendererGpuTranslucentLatency Objects

```python
class NiagaraRendererGpuTranslucentLatency(EnumBase)
```

ENiagara Renderer Gpu Translucent Latency

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraRendererProperties.h

<a id="unreal.NiagaraRendererGpuTranslucentLatency.PROJECT_DEFAULT"></a>

#### PROJECT_DEFAULT

0: Uses the project default value.

<a id="unreal.NiagaraRendererGpuTranslucentLatency.IMMEDIATE"></a>

#### IMMEDIATE

1: Gpu simulations will always read this frames data for translucent materials.

<a id="unreal.NiagaraRendererGpuTranslucentLatency.LATENT"></a>

#### LATENT

2: Gpu simulations will read the previous frames data if the simulation has to run in PostRenderOpaque.

<a id="unreal.NiagaraRendererPixelCoverageMode"></a>