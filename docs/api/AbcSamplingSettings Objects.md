## AbcSamplingSettings Objects

```python
class AbcSamplingSettings(StructBase)
```

Abc Sampling Settings

**C++ Source:**

- **Plugin**: AlembicImporter
- **Module**: AlembicLibrary
- **File**: AbcImportSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_end`` (int32):  [Read-Write] Ending index to stop sampling the animation at
- ``frame_start`` (int32):  [Read-Write] Starting index to start sampling the animation from
- ``frame_steps`` (int32):  [Read-Write] Steps to take when sampling the animation
- ``sampling_type`` (AlembicSamplingType):  [Read-Write] Type of sampling performed while importing the animation
- ``skip_empty`` (bool):  [Read-Write] Skip empty (pre-roll) frames and start importing at the frame which actually contains data
- ``time_steps`` (float):  [Read-Write] Time steps to take when sampling the animation

<a id="unreal.AbcSamplingSettings.__init__"></a>

#### __init__

```python
def __init__(
        sampling_type: AlembicSamplingType = AlembicSamplingType.PER_FRAME,
        frame_steps: int = 0,
        time_steps: float = 0.000000,
        frame_start: int = 0,
        frame_end: int = 0,
        skip_empty: bool = False) -> None
```

<a id="unreal.AbcSamplingSettings.sampling_type"></a>

#### sampling_type

```python
@property
def sampling_type() -> AlembicSamplingType
```

(AlembicSamplingType):  [Read-Write] Type of sampling performed while importing the animation

<a id="unreal.AbcSamplingSettings.sampling_type"></a>

#### sampling_type

```python
@sampling_type.setter
def sampling_type(value: AlembicSamplingType) -> None
```

<a id="unreal.AbcSamplingSettings.frame_steps"></a>

#### frame_steps

```python
@property
def frame_steps() -> int
```

(int32):  [Read-Write] Steps to take when sampling the animation

<a id="unreal.AbcSamplingSettings.frame_steps"></a>

#### frame_steps

```python
@frame_steps.setter
def frame_steps(value: int) -> None
```

<a id="unreal.AbcSamplingSettings.time_steps"></a>

#### time_steps

```python
@property
def time_steps() -> float
```

(float):  [Read-Write] Time steps to take when sampling the animation

<a id="unreal.AbcSamplingSettings.time_steps"></a>

#### time_steps

```python
@time_steps.setter
def time_steps(value: float) -> None
```

<a id="unreal.AbcSamplingSettings.frame_start"></a>

#### frame_start

```python
@property
def frame_start() -> int
```

(int32):  [Read-Write] Starting index to start sampling the animation from

<a id="unreal.AbcSamplingSettings.frame_start"></a>

#### frame_start

```python
@frame_start.setter
def frame_start(value: int) -> None
```

<a id="unreal.AbcSamplingSettings.frame_end"></a>

#### frame_end

```python
@property
def frame_end() -> int
```

(int32):  [Read-Write] Ending index to stop sampling the animation at

<a id="unreal.AbcSamplingSettings.frame_end"></a>

#### frame_end

```python
@frame_end.setter
def frame_end(value: int) -> None
```

<a id="unreal.AbcSamplingSettings.skip_empty"></a>

#### skip_empty

```python
@property
def skip_empty() -> bool
```

(bool):  [Read-Write] Skip empty (pre-roll) frames and start importing at the frame which actually contains data

<a id="unreal.AbcSamplingSettings.skip_empty"></a>

#### skip_empty

```python
@skip_empty.setter
def skip_empty(value: bool) -> None
```

<a id="unreal.AbcNormalGenerationSettings"></a>