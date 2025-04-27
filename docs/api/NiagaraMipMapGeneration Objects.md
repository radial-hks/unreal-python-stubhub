## NiagaraMipMapGeneration Objects

```python
class NiagaraMipMapGeneration(EnumBase)
```

ENiagara Mip Map Generation

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraCommon.h

<a id="unreal.NiagaraMipMapGeneration.DISABLED"></a>

#### DISABLED

0: Mips will not be created or automatically generated.

<a id="unreal.NiagaraMipMapGeneration.POST_STAGE"></a>

#### POST_STAGE

1: Mips will be generated after each stage where the interfaces is written to.

<a id="unreal.NiagaraMipMapGeneration.POST_SIMULATE"></a>

#### POST_SIMULATE

2: Mips will be generated after all stages have been run if the interface was written to.

<a id="unreal.NiagaraMipMapGenerationType"></a>