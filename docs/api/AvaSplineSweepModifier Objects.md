## AvaSplineSweepModifier Objects

```python
class AvaSplineSweepModifier(AvaGeometryBaseModifier)
```

Ava Spline Sweep Modifier

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaSplineSweepModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``capped`` (bool):  [Read-Write] Whether start and end are closed, loop must be false
- ``looped`` (bool):  [Read-Write] Whether we close the whole spline path, if spline loops this will be true
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``progress_end`` (float):  [Read-Write] Sample end range of the spline
- ``progress_offset`` (float):  [Read-Write] Sample range offset of the spline, for closed loop spline range can wrap around
- ``progress_start`` (float):  [Read-Write] Sample start range of the spline
- ``sample_distance`` (float):  [Read-Write] Custom sample distance for steps per distance mode
- ``sample_mode`` (AvaSplineSweepSampleMode):  [Read-Write] How do we sample the spline
- ``scale_end`` (float):  [Read-Write] End scale of the spline mesh
- ``scale_start`` (float):  [Read-Write] Start scale of the spline mesh
- ``spline_actor_weak`` (Actor):  [Read-Write] Spline actor to retrieve the USplineComponent from
- ``steps`` (int32):  [Read-Write] The sample count defines the precision of the sweep

<a id="unreal.AvaSplineSweepModifier.set_steps"></a>

#### set_steps

```python
def set_steps(steps: int) -> None
```

x.set_steps(steps) -> None
Set Steps

Args:
    steps (int32):

<a id="unreal.AvaSplineSweepModifier.set_spline_actor"></a>

#### set_spline_actor

```python
def set_spline_actor(actor: Actor) -> None
```

x.set_spline_actor(actor) -> None
Set Spline Actor

Args:
    actor (Actor):

<a id="unreal.AvaSplineSweepModifier.set_scale_start"></a>

#### set_scale_start

```python
def set_scale_start(scale_start: float) -> None
```

x.set_scale_start(scale_start) -> None
Set Scale Start

Args:
    scale_start (float):

<a id="unreal.AvaSplineSweepModifier.set_scale_end"></a>

#### set_scale_end

```python
def set_scale_end(scale_end: float) -> None
```

x.set_scale_end(scale_end) -> None
Set Scale End

Args:
    scale_end (float):

<a id="unreal.AvaSplineSweepModifier.set_sample_mode"></a>

#### set_sample_mode

```python
def set_sample_mode(mode: AvaSplineSweepSampleMode) -> None
```

x.set_sample_mode(mode) -> None
Set Sample Mode

Args:
    mode (AvaSplineSweepSampleMode):

<a id="unreal.AvaSplineSweepModifier.set_sample_distance"></a>

#### set_sample_distance

```python
def set_sample_distance(distance: float) -> None
```

x.set_sample_distance(distance) -> None
Set Sample Distance

Args:
    distance (float):

<a id="unreal.AvaSplineSweepModifier.set_progress_start"></a>

#### set_progress_start

```python
def set_progress_start(start: float) -> None
```

x.set_progress_start(start) -> None
Set Progress Start

Args:
    start (float):

<a id="unreal.AvaSplineSweepModifier.set_progress_offset"></a>

#### set_progress_offset

```python
def set_progress_offset(offset: float) -> None
```

x.set_progress_offset(offset) -> None
Set Progress Offset

Args:
    offset (float):

<a id="unreal.AvaSplineSweepModifier.set_progress_end"></a>

#### set_progress_end

```python
def set_progress_end(end: float) -> None
```

x.set_progress_end(end) -> None
Set Progress End

Args:
    end (float):

<a id="unreal.AvaSplineSweepModifier.set_looped"></a>

#### set_looped

```python
def set_looped(looped: bool) -> None
```

x.set_looped(looped) -> None
Set Looped

Args:
    looped (bool):

<a id="unreal.AvaSplineSweepModifier.set_capped"></a>

#### set_capped

```python
def set_capped(capped: bool) -> None
```

x.set_capped(capped) -> None
Set Capped

Args:
    capped (bool):

<a id="unreal.AvaSplineSweepModifier.get_steps"></a>

#### get_steps

```python
def get_steps() -> int
```

x.get_steps() -> int32
Get Steps

Returns:
    int32:

<a id="unreal.AvaSplineSweepModifier.get_spline_actor"></a>

#### get_spline_actor

```python
def get_spline_actor() -> Actor
```

x.get_spline_actor() -> Actor
Get Spline Actor

Returns:
    Actor:

<a id="unreal.AvaSplineSweepModifier.get_scale_start"></a>

#### get_scale_start

```python
def get_scale_start() -> float
```

x.get_scale_start() -> float
Get Scale Start

Returns:
    float:

<a id="unreal.AvaSplineSweepModifier.get_scale_end"></a>

#### get_scale_end

```python
def get_scale_end() -> float
```

x.get_scale_end() -> float
Get Scale End

Returns:
    float:

<a id="unreal.AvaSplineSweepModifier.get_sample_mode"></a>

#### get_sample_mode

```python
def get_sample_mode() -> AvaSplineSweepSampleMode
```

x.get_sample_mode() -> AvaSplineSweepSampleMode
Get Sample Mode

Returns:
    AvaSplineSweepSampleMode:

<a id="unreal.AvaSplineSweepModifier.get_sample_distance"></a>

#### get_sample_distance

```python
def get_sample_distance() -> float
```

x.get_sample_distance() -> float
Get Sample Distance

Returns:
    float:

<a id="unreal.AvaSplineSweepModifier.get_progress_start"></a>

#### get_progress_start

```python
def get_progress_start() -> float
```

x.get_progress_start() -> float
Get Progress Start

Returns:
    float:

<a id="unreal.AvaSplineSweepModifier.get_progress_offset"></a>

#### get_progress_offset

```python
def get_progress_offset() -> float
```

x.get_progress_offset() -> float
Get Progress Offset

Returns:
    float:

<a id="unreal.AvaSplineSweepModifier.get_progress_end"></a>

#### get_progress_end

```python
def get_progress_end() -> float
```

x.get_progress_end() -> float
Get Progress End

Returns:
    float:

<a id="unreal.AvaSplineSweepModifier.get_looped"></a>

#### get_looped

```python
def get_looped() -> bool
```

x.get_looped() -> bool
Get Looped

Returns:
    bool:

<a id="unreal.AvaSplineSweepModifier.get_capped"></a>

#### get_capped

```python
def get_capped() -> bool
```

x.get_capped() -> bool
Get Capped

Returns:
    bool:

<a id="unreal.AvaSubdivideModifier"></a>