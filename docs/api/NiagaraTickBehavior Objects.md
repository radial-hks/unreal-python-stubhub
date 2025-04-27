## NiagaraTickBehavior Objects

```python
class NiagaraTickBehavior(EnumBase)
```

Niagara ticking behaviour

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraTickBehaviorEnum.h

<a id="unreal.NiagaraTickBehavior.USE_PREREQS"></a>

#### USE_PREREQS

0: Niagara will tick after all prereqs have ticked for attachements / data interfaces, this is the safest option.

<a id="unreal.NiagaraTickBehavior.USE_COMPONENT_TICK_GROUP"></a>

#### USE_COMPONENT_TICK_GROUP

1: Niagara will ignore prereqs (attachments / data interface dependencies) and use the tick group set on the component.

<a id="unreal.NiagaraTickBehavior.FORCE_TICK_FIRST"></a>

#### FORCE_TICK_FIRST

2: Niagara will tick in the first tick group (default is TG_PrePhysics).

<a id="unreal.NiagaraTickBehavior.FORCE_TICK_LAST"></a>

#### FORCE_TICK_LAST

3: Niagara will tick in the last tick group (default is TG_LastDemotable).

<a id="unreal.NiagaraOcclusionQueryMode"></a>