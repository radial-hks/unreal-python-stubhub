## SequenceLengthChangedPayload Objects

```python
class SequenceLengthChangedPayload(EmptyPayload)
```

Sequence Length Changed Payload

**C++ Source:**

- **Module**: Engine
- **File**: AnimDataNotifications.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame0`` (FrameNumber):  [Read-Write] Frame number at which the change in frames has been made
- ``frame1`` (FrameNumber):  [Read-Write] Amount of frames which is inserted or removed starting at Frame0
- ``previous_length`` (float):  [Read-Write]
- ``previous_number_of_frames`` (FrameNumber):  [Read-Write] Previous playable number of frames for the Model
- ``t0`` (float):  [Read-Write]
- ``t1`` (float):  [Read-Write]

<a id="unreal.SequenceLengthChangedPayload.__init__"></a>

#### __init__

```python
def __init__(previous_length: float = 0.000000,
             t0: float = 0.000000,
             t1: float = 0.000000,
             previous_number_of_frames: FrameNumber = [0],
             frame0: FrameNumber = [0],
             frame1: FrameNumber = [0]) -> None
```

<a id="unreal.SequenceLengthChangedPayload.previous_length"></a>

#### previous_length

```python
@property
def previous_length() -> float
```

(float):  [Read-Only]

<a id="unreal.SequenceLengthChangedPayload.t0"></a>

#### t0

```python
@property
def t0() -> float
```

(float):  [Read-Only]

<a id="unreal.SequenceLengthChangedPayload.t1"></a>

#### t1

```python
@property
def t1() -> float
```

(float):  [Read-Only]

<a id="unreal.SequenceLengthChangedPayload.previous_number_of_frames"></a>

#### previous_number_of_frames

```python
@property
def previous_number_of_frames() -> FrameNumber
```

(FrameNumber):  [Read-Only] Previous playable number of frames for the Model

<a id="unreal.SequenceLengthChangedPayload.frame0"></a>

#### frame0

```python
@property
def frame0() -> FrameNumber
```

(FrameNumber):  [Read-Only] Frame number at which the change in frames has been made

<a id="unreal.SequenceLengthChangedPayload.frame1"></a>

#### frame1

```python
@property
def frame1() -> FrameNumber
```

(FrameNumber):  [Read-Only] Amount of frames which is inserted or removed starting at Frame0

<a id="unreal.FrameRateChangedPayload"></a>