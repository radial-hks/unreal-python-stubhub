## NiagaraCullReaction Objects

```python
class NiagaraCullReaction(EnumBase)
```

Controls what action is taken by a Niagara system that fails it's cull checks.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraEffectType.h

<a id="unreal.NiagaraCullReaction.DEACTIVATE"></a>

#### DEACTIVATE

0: The system instance will be deactivated. Particles will be allowed to die naturally. It will not be reactivated automatically by the scalability system.

<a id="unreal.NiagaraCullReaction.DEACTIVATE_IMMEDIATE"></a>

#### DEACTIVATE\_IMMEDIATE

1: The system instance will be deactivated and particles killed immediately. It will not be reactivated automatically by the scalability system.

<a id="unreal.NiagaraCullReaction.DEACTIVATE_RESUME"></a>

#### DEACTIVATE\_RESUME

2: The system instance will be deactivated. Particles will be allowed to die naturally. Will reactivate when it passes cull tests again.

<a id="unreal.NiagaraCullReaction.DEACTIVATE_IMMEDIATE_RESUME"></a>

#### DEACTIVATE\_IMMEDIATE\_RESUME

3: The system instance will be deactivated and particles killed immediately. Will reactivate when it passes cull tests again.

<a id="unreal.NiagaraCullReaction.PAUSE_RESUME"></a>

#### PAUSE\_RESUME

4: The system instance will be paused, maintaining it's current state, but will resume ticking when it passes cull tests again.

<a id="unreal.NiagaraScriptLibraryVisibility"></a>