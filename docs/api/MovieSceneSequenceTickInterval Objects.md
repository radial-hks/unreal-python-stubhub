## MovieSceneSequenceTickInterval Objects

```python
class MovieSceneSequenceTickInterval(StructBase)
```

Structure defining a concrete tick interval for a Sequencer based evaluation

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneSequenceTickInterval.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_rounding`` (bool):  [Read-Write] When true, allow the sequence to be grouped with other sequences based on Sequencer.TickIntervalGroupingResolutionMs. Otherwise the interval will be used precisely.
- ``evaluation_budget_microseconds`` (float):  [Read-Write] Defines an approximate budget for evaluation of this sequence (and any other sequences with the same tick interval)
- ``tick_interval_seconds`` (float):  [Read-Write] Defines the rate at which the sequence should update, in seconds
- ``tick_when_paused`` (bool):  [Read-Write] When true, the sequence will continue to tick and progress even when the world is paused

<a id="unreal.MovieSceneSequenceTickInterval.__init__"></a>

#### __init__

```python
def __init__(tick_interval_seconds: float = 0.000000,
             evaluation_budget_microseconds: float = 0.000000,
             tick_when_paused: bool = False,
             allow_rounding: bool = False) -> None
```

<a id="unreal.MovieSceneSequenceTickInterval.tick_interval_seconds"></a>

#### tick_interval_seconds

```python
@property
def tick_interval_seconds() -> float
```

(float):  [Read-Write] Defines the rate at which the sequence should update, in seconds

<a id="unreal.MovieSceneSequenceTickInterval.tick_interval_seconds"></a>

#### tick_interval_seconds

```python
@tick_interval_seconds.setter
def tick_interval_seconds(value: float) -> None
```

<a id="unreal.MovieSceneSequenceTickInterval.evaluation_budget_microseconds"></a>

#### evaluation_budget_microseconds

```python
@property
def evaluation_budget_microseconds() -> float
```

(float):  [Read-Write] Defines an approximate budget for evaluation of this sequence (and any other sequences with the same tick interval)

<a id="unreal.MovieSceneSequenceTickInterval.evaluation_budget_microseconds"></a>

#### evaluation_budget_microseconds

```python
@evaluation_budget_microseconds.setter
def evaluation_budget_microseconds(value: float) -> None
```

<a id="unreal.MovieSceneSequenceTickInterval.tick_when_paused"></a>

#### tick_when_paused

```python
@property
def tick_when_paused() -> bool
```

(bool):  [Read-Write] When true, the sequence will continue to tick and progress even when the world is paused

<a id="unreal.MovieSceneSequenceTickInterval.tick_when_paused"></a>

#### tick_when_paused

```python
@tick_when_paused.setter
def tick_when_paused(value: bool) -> None
```

<a id="unreal.MovieSceneSequenceTickInterval.allow_rounding"></a>

#### allow_rounding

```python
@property
def allow_rounding() -> bool
```

(bool):  [Read-Write] When true, allow the sequence to be grouped with other sequences based on Sequencer.TickIntervalGroupingResolutionMs. Otherwise the interval will be used precisely.

<a id="unreal.MovieSceneSequenceTickInterval.allow_rounding"></a>

#### allow_rounding

```python
@allow_rounding.setter
def allow_rounding(value: bool) -> None
```

<a id="unreal.OptionalMovieSceneBlendType"></a>