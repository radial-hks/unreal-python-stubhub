## TapDelayInfo Objects

```python
class TapDelayInfo(StructBase)
```

Tap Delay Info

**C++ Source:**

- **Plugin**: Synthesis
- **Module**: Synthesis
- **File**: SubmixEffectTapDelay.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``delay_length`` (float):  [Read-Write] Amount of time before this echo is heard in milliseconds.
- ``gain`` (float):  [Read-Write] How loud this echo should be, in decibels.
- ``output_channel`` (int32):  [Read-Write] When the Tap Line Mode is set to Send To Channel, designates index of channel from which the echo should play.
- ``pan_in_degrees`` (float):  [Read-Write] When the Tap Line Mode is set to Panning, designates the angle at which the echo should be panned.
  On Surround systems, 0 is directly in front of the listener, -90 is left, 90 is right, and 180/-180 is directly behind the listener.
  On Stereo systems, <-90 is fully in the left ear, and >90 is fully in the right ear
- ``tap_line_mode`` (TapLineMode):  [Read-Write] Whether the tap line should send directly to a channel, pan, or not produce sound at all.

<a id="unreal.TapDelayInfo.__init__"></a>

#### __init__

```python
def __init__(tap_line_mode: TapLineMode = TapLineMode.SEND_TO_CHANNEL,
             delay_length: float = 0.000000,
             gain: float = 0.000000,
             output_channel: int = 0,
             pan_in_degrees: float = 0.000000) -> None
```

<a id="unreal.TapDelayInfo.tap_line_mode"></a>

#### tap_line_mode

```python
@property
def tap_line_mode() -> TapLineMode
```

(TapLineMode):  [Read-Write] Whether the tap line should send directly to a channel, pan, or not produce sound at all.

<a id="unreal.TapDelayInfo.tap_line_mode"></a>

#### tap_line_mode

```python
@tap_line_mode.setter
def tap_line_mode(value: TapLineMode) -> None
```

<a id="unreal.TapDelayInfo.delay_length"></a>

#### delay_length

```python
@property
def delay_length() -> float
```

(float):  [Read-Write] Amount of time before this echo is heard in milliseconds.

<a id="unreal.TapDelayInfo.delay_length"></a>

#### delay_length

```python
@delay_length.setter
def delay_length(value: float) -> None
```

<a id="unreal.TapDelayInfo.gain"></a>

#### gain

```python
@property
def gain() -> float
```

(float):  [Read-Write] How loud this echo should be, in decibels.

<a id="unreal.TapDelayInfo.gain"></a>

#### gain

```python
@gain.setter
def gain(value: float) -> None
```

<a id="unreal.TapDelayInfo.output_channel"></a>

#### output_channel

```python
@property
def output_channel() -> int
```

(int32):  [Read-Write] When the Tap Line Mode is set to Send To Channel, designates index of channel from which the echo should play.

<a id="unreal.TapDelayInfo.output_channel"></a>

#### output_channel

```python
@output_channel.setter
def output_channel(value: int) -> None
```

<a id="unreal.TapDelayInfo.pan_in_degrees"></a>

#### pan_in_degrees

```python
@property
def pan_in_degrees() -> float
```

(float):  [Read-Write] When the Tap Line Mode is set to Panning, designates the angle at which the echo should be panned.
On Surround systems, 0 is directly in front of the listener, -90 is left, 90 is right, and 180/-180 is directly behind the listener.
On Stereo systems, <-90 is fully in the left ear, and >90 is fully in the right ear

<a id="unreal.TapDelayInfo.pan_in_degrees"></a>

#### pan_in_degrees

```python
@pan_in_degrees.setter
def pan_in_degrees(value: float) -> None
```

<a id="unreal.SubmixEffectTapDelaySettings"></a>