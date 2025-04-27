## NiagaraPerfBaselineStats Objects

```python
class NiagaraPerfBaselineStats(StructBase)
```

Niagara Perf Baseline Stats

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraPerfBaseline.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``per_instance_avg_gt`` (float):  [Read-Write] Per instance average time spent on the GameThread (µs).
- ``per_instance_avg_rt`` (float):  [Read-Write] Per instance average time spent on the RenderThread (µs).
- ``per_instance_max_gt`` (float):  [Read-Write] Per instance max time spent on the GameThread (µs).
- ``per_instance_max_rt`` (float):  [Read-Write] Per instance max time spent on the RenderThread (µs).

<a id="unreal.NiagaraPerfBaselineStats.__init__"></a>

#### __init__

```python
def __init__(per_instance_avg_gt: float = 0.000000,
             per_instance_avg_rt: float = 0.000000,
             per_instance_max_gt: float = 0.000000,
             per_instance_max_rt: float = 0.000000) -> None
```

<a id="unreal.NiagaraPerfBaselineStats.per_instance_avg_gt"></a>

#### per_instance_avg_gt

```python
@property
def per_instance_avg_gt() -> float
```

(float):  [Read-Write] Per instance average time spent on the GameThread (µs).

<a id="unreal.NiagaraPerfBaselineStats.per_instance_avg_gt"></a>

#### per_instance_avg_gt

```python
@per_instance_avg_gt.setter
def per_instance_avg_gt(value: float) -> None
```

<a id="unreal.NiagaraPerfBaselineStats.per_instance_avg_rt"></a>

#### per_instance_avg_rt

```python
@property
def per_instance_avg_rt() -> float
```

(float):  [Read-Write] Per instance average time spent on the RenderThread (µs).

<a id="unreal.NiagaraPerfBaselineStats.per_instance_avg_rt"></a>

#### per_instance_avg_rt

```python
@per_instance_avg_rt.setter
def per_instance_avg_rt(value: float) -> None
```

<a id="unreal.NiagaraPerfBaselineStats.per_instance_max_gt"></a>

#### per_instance_max_gt

```python
@property
def per_instance_max_gt() -> float
```

(float):  [Read-Write] Per instance max time spent on the GameThread (µs).

<a id="unreal.NiagaraPerfBaselineStats.per_instance_max_gt"></a>

#### per_instance_max_gt

```python
@per_instance_max_gt.setter
def per_instance_max_gt(value: float) -> None
```

<a id="unreal.NiagaraPerfBaselineStats.per_instance_max_rt"></a>

#### per_instance_max_rt

```python
@property
def per_instance_max_rt() -> float
```

(float):  [Read-Write] Per instance max time spent on the RenderThread (µs).

<a id="unreal.NiagaraPerfBaselineStats.per_instance_max_rt"></a>

#### per_instance_max_rt

```python
@per_instance_max_rt.setter
def per_instance_max_rt(value: float) -> None
```

<a id="unreal.NiagaraPosition"></a>