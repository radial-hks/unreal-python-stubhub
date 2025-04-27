## NiagaraScalabilityUpdateFrequency Objects

```python
class NiagaraScalabilityUpdateFrequency(EnumBase)
```

Controls how often should we update scalability states for these effects.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraEffectType.h

<a id="unreal.NiagaraScalabilityUpdateFrequency.SPAWN_ONLY"></a>

#### SPAWN_ONLY

0: Scalability will be checked only on spawn.

<a id="unreal.NiagaraScalabilityUpdateFrequency.LOW"></a>

#### LOW

1: Scalability will be checked every 1.0s (default for fx.NiagaraScalabilityUpdateTime_Low).

<a id="unreal.NiagaraScalabilityUpdateFrequency.MEDIUM"></a>

#### MEDIUM

2: Scalability will be checked every 0.5s (default for fx.NiagaraScalabilityUpdateTime_Medium).

<a id="unreal.NiagaraScalabilityUpdateFrequency.HIGH"></a>

#### HIGH

3: Scalability will be checked every 0.25s (default for fx.NiagaraScalabilityUpdateTime_High).

<a id="unreal.NiagaraScalabilityUpdateFrequency.CONTINUOUS"></a>

#### CONTINUOUS

4: Scalability will be checked every frame.

<a id="unreal.NiagaraCullReaction"></a>