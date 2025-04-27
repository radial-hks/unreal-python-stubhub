## NiagaraSpawnInfo Objects

```python
class NiagaraSpawnInfo(StructBase)
```

Data controlling the spawning of particles

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``count`` (int32):  [Read-Write] How many particles to spawn.
- ``interp_start_dt`` (float):  [Read-Write] The sub frame delta time at which to spawn the first particle.
- ``interval_dt`` (float):  [Read-Write] The sub frame delta time between each particle.
- ``spawn_group`` (int32):  [Read-Write] An integer used to identify this spawn info.
  Typically this is unused.
  An example usage is when using multiple spawn modules to spawn from multiple discreet locations.

<a id="unreal.NiagaraSpawnInfo.__init__"></a>

#### __init__

```python
def __init__(count: int = 0,
             interp_start_dt: float = 0.000000,
             interval_dt: float = 0.000000,
             spawn_group: int = 0) -> None
```

<a id="unreal.NiagaraSpawnInfo.count"></a>

#### count

```python
@property
def count() -> int
```

(int32):  [Read-Write] How many particles to spawn.

<a id="unreal.NiagaraSpawnInfo.count"></a>

#### count

```python
@count.setter
def count(value: int) -> None
```

<a id="unreal.NiagaraSpawnInfo.interp_start_dt"></a>

#### interp_start_dt

```python
@property
def interp_start_dt() -> float
```

(float):  [Read-Write] The sub frame delta time at which to spawn the first particle.

<a id="unreal.NiagaraSpawnInfo.interp_start_dt"></a>

#### interp_start_dt

```python
@interp_start_dt.setter
def interp_start_dt(value: float) -> None
```

<a id="unreal.NiagaraSpawnInfo.interval_dt"></a>

#### interval_dt

```python
@property
def interval_dt() -> float
```

(float):  [Read-Write] The sub frame delta time between each particle.

<a id="unreal.NiagaraSpawnInfo.interval_dt"></a>

#### interval_dt

```python
@interval_dt.setter
def interval_dt(value: float) -> None
```

<a id="unreal.NiagaraSpawnInfo.spawn_group"></a>

#### spawn_group

```python
@property
def spawn_group() -> int
```

(int32):  [Read-Write] An integer used to identify this spawn info.
Typically this is unused.
An example usage is when using multiple spawn modules to spawn from multiple discreet locations.

<a id="unreal.NiagaraSpawnInfo.spawn_group"></a>

#### spawn_group

```python
@spawn_group.setter
def spawn_group(value: int) -> None
```

<a id="unreal.NiagaraID"></a>