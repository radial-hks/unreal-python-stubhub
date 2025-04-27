## NiagaraGpuSyncMode Objects

```python
class NiagaraGpuSyncMode(EnumBase)
```

ENiagara Gpu Sync Mode

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraCommon.h

<a id="unreal.NiagaraGpuSyncMode.NONE"></a>

#### NONE

0: Data will not be automatically pushed and could diverge between Cpu & Gpu.

<a id="unreal.NiagaraGpuSyncMode.SYNC_CPU_TO_GPU"></a>

#### SYNC_CPU_TO_GPU

1: Cpu modifications will be pushed to the Gpu.

<a id="unreal.NiagaraGpuSyncMode.SYNC_GPU_TO_CPU"></a>

#### SYNC_GPU_TO_CPU

2: Gpu will continuously push back to the Cpu, this will incur a performance penalty.

<a id="unreal.NiagaraGpuSyncMode.SYNC_BOTH"></a>

#### SYNC_BOTH

3: Gpu will continuously push back to the Cpu and Cpu modifications will be pushed to the Gpu.

<a id="unreal.SetResolutionMethod"></a>