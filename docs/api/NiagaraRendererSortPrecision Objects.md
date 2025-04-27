## NiagaraRendererSortPrecision Objects

```python
class NiagaraRendererSortPrecision(EnumBase)
```

ENiagara Renderer Sort Precision

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraRendererProperties.h

<a id="unreal.NiagaraRendererSortPrecision.DEFAULT"></a>

#### DEFAULT

0: Uses the project settings value.

<a id="unreal.NiagaraRendererSortPrecision.LOW"></a>

#### LOW

1: Low precision sorting, half float (fp16) precision, faster and adequate for most cases.

<a id="unreal.NiagaraRendererSortPrecision.HIGH"></a>

#### HIGH

2: High precision sorting, float (fp32) precision, slower but may fix sorting artifacts.

<a id="unreal.NiagaraRendererGpuTranslucentLatency"></a>