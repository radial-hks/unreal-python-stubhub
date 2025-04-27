## NiagaraBaselineController Objects

```python
class NiagaraBaselineController(Object)
```

Base class for baseline controllers. These can are responsible for spawning and manipulating the FX needed for the baseline perf tests.

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraPerfBaseline.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``effect_type`` (NiagaraEffectType):  [Read-Write] The effect type this controller is in use by.
- ``owner`` (NiagaraPerfBaselineActor):  [Read-Write] The owning actor for this baseline controller.
- ``system`` (NiagaraSystem):  [Read-Write] The baseline system to spawn.
- ``test_duration`` (float):  [Read-Write] Duration to gather performance stats for the given system.

<a id="unreal.NiagaraBaselineController.test_duration"></a>

#### test_duration

```python
@property
def test_duration() -> float
```

(float):  [Read-Write] Duration to gather performance stats for the given system.

<a id="unreal.NiagaraBaselineController.test_duration"></a>

#### test_duration

```python
@test_duration.setter
def test_duration(value: float) -> None
```

<a id="unreal.NiagaraBaselineController.effect_type"></a>

#### effect_type

```python
@property
def effect_type() -> NiagaraEffectType
```

(NiagaraEffectType):  [Read-Only] The effect type this controller is in use by.

<a id="unreal.NiagaraBaselineController.owner"></a>

#### owner

```python
@property
def owner() -> NiagaraPerfBaselineActor
```

(NiagaraPerfBaselineActor):  [Read-Only] The owning actor for this baseline controller.

<a id="unreal.NiagaraBaselineController.on_tick_test"></a>

#### on_tick_test

```python
def on_tick_test() -> bool
```

x.on_tick_test() -> bool
Returns whether the baseline test is complete.

Returns:
    bool:

<a id="unreal.NiagaraBaselineController.on_owner_tick"></a>

#### on_owner_tick

```python
def on_owner_tick(delta_time: float) -> None
```

x.on_owner_tick(delta_time) -> None
Called when the owning actor is ticked.

Args:
    delta_time (float):

<a id="unreal.NiagaraBaselineController.on_end_test"></a>

#### on_end_test

```python
def on_end_test(stats: NiagaraPerfBaselineStats) -> None
```

x.on_end_test(stats) -> None
Called from the stats system on completion of the test with the final stats for the given system asset.

Args:
    stats (NiagaraPerfBaselineStats):

<a id="unreal.NiagaraBaselineController.on_begin_test"></a>

#### on_begin_test

```python
def on_begin_test() -> None
```

x.on_begin_test() -> None
Called from the stats system when we begin gathering stats for the given System asset.

<a id="unreal.NiagaraBaselineController.get_system"></a>

#### get_system

```python
def get_system() -> NiagaraSystem
```

x.get_system() -> NiagaraSystem
Returns the System for this baseline. Will synchronously load the system if needed.

Returns:
    NiagaraSystem:

<a id="unreal.NiagaraBaselineController_Basic"></a>