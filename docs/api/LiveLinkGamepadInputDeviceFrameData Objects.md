## LiveLinkGamepadInputDeviceFrameData Objects

```python
class LiveLinkGamepadInputDeviceFrameData(LiveLinkBaseFrameData)
```

Struct for dynamic (per-frame) Gampead Input Device data

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkInputDeviceTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``d_pad_down`` (float):  [Read-Write]
- ``d_pad_left`` (float):  [Read-Write]
- ``d_pad_right`` (float):  [Read-Write]
- ``d_pad_up`` (float):  [Read-Write]
- ``face_button_bottom`` (float):  [Read-Write]
- ``face_button_left`` (float):  [Read-Write]
- ``face_button_right`` (float):  [Read-Write]
- ``face_button_top`` (float):  [Read-Write]
- ``left_analog_x`` (float):  [Read-Write]
- ``left_analog_y`` (float):  [Read-Write]
- ``left_shoulder`` (float):  [Read-Write]
- ``left_stick_down`` (float):  [Read-Write]
- ``left_stick_left`` (float):  [Read-Write]
- ``left_stick_right`` (float):  [Read-Write]
- ``left_stick_up`` (float):  [Read-Write]
- ``left_thumb`` (float):  [Read-Write]
- ``left_trigger_analog`` (float):  [Read-Write]
- ``left_trigger_threshold`` (float):  [Read-Write]
- ``meta_data`` (LiveLinkMetaData):  [Read-Write] Frame's metadata.
- ``property_values`` (Array[float]):  [Read-Write] Values of the properties defined in the static structure. Use FLiveLinkBaseStaticData.FindPropertyValue to evaluate.
- ``right_analog_x`` (float):  [Read-Write]
- ``right_analog_y`` (float):  [Read-Write]
- ``right_shoulder`` (float):  [Read-Write]
- ``right_stick_down`` (float):  [Read-Write]
- ``right_stick_left`` (float):  [Read-Write]
- ``right_stick_right`` (float):  [Read-Write]
- ``right_stick_up`` (float):  [Read-Write]
- ``right_thumb`` (float):  [Read-Write]
- ``right_trigger_analog`` (float):  [Read-Write]
- ``right_trigger_threshold`` (float):  [Read-Write]
- ``special_left`` (float):  [Read-Write]
- ``special_left_x`` (float):  [Read-Write]
- ``special_left_y`` (float):  [Read-Write]
- ``special_right`` (float):  [Read-Write]
- ``world_time`` (LiveLinkWorldTime):  [Read-Only] Time in seconds the frame was created.

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(meta_data: LiveLinkMetaData = [{}, [[0], [24, 1], 0.000000]],
             property_values: Array[float] = [],
             left_analog_x: float = 0.000000,
             left_analog_y: float = 0.000000,
             right_analog_x: float = 0.000000,
             right_analog_y: float = 0.000000,
             left_trigger_analog: float = 0.000000,
             right_trigger_analog: float = 0.000000,
             left_thumb: float = 0.000000,
             right_thumb: float = 0.000000,
             special_left: float = 0.000000,
             special_left_x: float = 0.000000,
             special_left_y: float = 0.000000,
             special_right: float = 0.000000,
             face_button_bottom: float = 0.000000,
             face_button_right: float = 0.000000,
             face_button_left: float = 0.000000,
             face_button_top: float = 0.000000,
             left_shoulder: float = 0.000000,
             right_shoulder: float = 0.000000,
             left_trigger_threshold: float = 0.000000,
             right_trigger_threshold: float = 0.000000,
             d_pad_up: float = 0.000000,
             d_pad_down: float = 0.000000,
             d_pad_right: float = 0.000000,
             d_pad_left: float = 0.000000,
             left_stick_up: float = 0.000000,
             left_stick_down: float = 0.000000,
             left_stick_right: float = 0.000000,
             left_stick_left: float = 0.000000,
             right_stick_up: float = 0.000000,
             right_stick_down: float = 0.000000,
             right_stick_right: float = 0.000000,
             right_stick_left: float = 0.000000) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_analog_x"></a>

#### left\_analog\_x

```python
@property
def left_analog_x() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_analog_x"></a>

#### left\_analog\_x

```python
@left_analog_x.setter
def left_analog_x(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_analog_y"></a>

#### left\_analog\_y

```python
@property
def left_analog_y() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_analog_y"></a>

#### left\_analog\_y

```python
@left_analog_y.setter
def left_analog_y(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_analog_x"></a>

#### right\_analog\_x

```python
@property
def right_analog_x() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_analog_x"></a>

#### right\_analog\_x

```python
@right_analog_x.setter
def right_analog_x(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_analog_y"></a>

#### right\_analog\_y

```python
@property
def right_analog_y() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_analog_y"></a>

#### right\_analog\_y

```python
@right_analog_y.setter
def right_analog_y(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_trigger_analog"></a>

#### left\_trigger\_analog

```python
@property
def left_trigger_analog() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_trigger_analog"></a>

#### left\_trigger\_analog

```python
@left_trigger_analog.setter
def left_trigger_analog(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_trigger_analog"></a>

#### right\_trigger\_analog

```python
@property
def right_trigger_analog() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_trigger_analog"></a>

#### right\_trigger\_analog

```python
@right_trigger_analog.setter
def right_trigger_analog(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_thumb"></a>

#### left\_thumb

```python
@property
def left_thumb() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_thumb"></a>

#### left\_thumb

```python
@left_thumb.setter
def left_thumb(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_thumb"></a>

#### right\_thumb

```python
@property
def right_thumb() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_thumb"></a>

#### right\_thumb

```python
@right_thumb.setter
def right_thumb(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.special_left"></a>

#### special\_left

```python
@property
def special_left() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.special_left"></a>

#### special\_left

```python
@special_left.setter
def special_left(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.special_left_x"></a>

#### special\_left\_x

```python
@property
def special_left_x() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.special_left_x"></a>

#### special\_left\_x

```python
@special_left_x.setter
def special_left_x(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.special_left_y"></a>

#### special\_left\_y

```python
@property
def special_left_y() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.special_left_y"></a>

#### special\_left\_y

```python
@special_left_y.setter
def special_left_y(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.special_right"></a>

#### special\_right

```python
@property
def special_right() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.special_right"></a>

#### special\_right

```python
@special_right.setter
def special_right(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.face_button_bottom"></a>

#### face\_button\_bottom

```python
@property
def face_button_bottom() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.face_button_bottom"></a>

#### face\_button\_bottom

```python
@face_button_bottom.setter
def face_button_bottom(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.face_button_right"></a>

#### face\_button\_right

```python
@property
def face_button_right() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.face_button_right"></a>

#### face\_button\_right

```python
@face_button_right.setter
def face_button_right(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.face_button_left"></a>

#### face\_button\_left

```python
@property
def face_button_left() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.face_button_left"></a>

#### face\_button\_left

```python
@face_button_left.setter
def face_button_left(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.face_button_top"></a>

#### face\_button\_top

```python
@property
def face_button_top() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.face_button_top"></a>

#### face\_button\_top

```python
@face_button_top.setter
def face_button_top(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_shoulder"></a>

#### left\_shoulder

```python
@property
def left_shoulder() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_shoulder"></a>

#### left\_shoulder

```python
@left_shoulder.setter
def left_shoulder(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_shoulder"></a>

#### right\_shoulder

```python
@property
def right_shoulder() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_shoulder"></a>

#### right\_shoulder

```python
@right_shoulder.setter
def right_shoulder(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_trigger_threshold"></a>

#### left\_trigger\_threshold

```python
@property
def left_trigger_threshold() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_trigger_threshold"></a>

#### left\_trigger\_threshold

```python
@left_trigger_threshold.setter
def left_trigger_threshold(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_trigger_threshold"></a>

#### right\_trigger\_threshold

```python
@property
def right_trigger_threshold() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_trigger_threshold"></a>

#### right\_trigger\_threshold

```python
@right_trigger_threshold.setter
def right_trigger_threshold(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.d_pad_up"></a>

#### d\_pad\_up

```python
@property
def d_pad_up() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.d_pad_up"></a>

#### d\_pad\_up

```python
@d_pad_up.setter
def d_pad_up(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.d_pad_down"></a>

#### d\_pad\_down

```python
@property
def d_pad_down() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.d_pad_down"></a>

#### d\_pad\_down

```python
@d_pad_down.setter
def d_pad_down(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.d_pad_right"></a>

#### d\_pad\_right

```python
@property
def d_pad_right() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.d_pad_right"></a>

#### d\_pad\_right

```python
@d_pad_right.setter
def d_pad_right(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.d_pad_left"></a>

#### d\_pad\_left

```python
@property
def d_pad_left() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.d_pad_left"></a>

#### d\_pad\_left

```python
@d_pad_left.setter
def d_pad_left(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_stick_up"></a>

#### left\_stick\_up

```python
@property
def left_stick_up() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_stick_up"></a>

#### left\_stick\_up

```python
@left_stick_up.setter
def left_stick_up(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_stick_down"></a>

#### left\_stick\_down

```python
@property
def left_stick_down() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_stick_down"></a>

#### left\_stick\_down

```python
@left_stick_down.setter
def left_stick_down(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_stick_right"></a>

#### left\_stick\_right

```python
@property
def left_stick_right() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_stick_right"></a>

#### left\_stick\_right

```python
@left_stick_right.setter
def left_stick_right(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_stick_left"></a>

#### left\_stick\_left

```python
@property
def left_stick_left() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.left_stick_left"></a>

#### left\_stick\_left

```python
@left_stick_left.setter
def left_stick_left(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_stick_up"></a>

#### right\_stick\_up

```python
@property
def right_stick_up() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_stick_up"></a>

#### right\_stick\_up

```python
@right_stick_up.setter
def right_stick_up(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_stick_down"></a>

#### right\_stick\_down

```python
@property
def right_stick_down() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_stick_down"></a>

#### right\_stick\_down

```python
@right_stick_down.setter
def right_stick_down(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_stick_right"></a>

#### right\_stick\_right

```python
@property
def right_stick_right() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_stick_right"></a>

#### right\_stick\_right

```python
@right_stick_right.setter
def right_stick_right(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_stick_left"></a>

#### right\_stick\_left

```python
@property
def right_stick_left() -> float
```

(float):  [Read-Write]

<a id="unreal.LiveLinkGamepadInputDeviceFrameData.right_stick_left"></a>

#### right\_stick\_left

```python
@right_stick_left.setter
def right_stick_left(value: float) -> None
```

<a id="unreal.LiveLinkGamepadInputDeviceBlueprintData"></a>