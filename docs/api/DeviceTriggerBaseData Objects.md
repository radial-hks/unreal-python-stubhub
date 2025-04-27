## DeviceTriggerBaseData Objects

```python
class DeviceTriggerBaseData(StructBase)
```

UInputDeviceTriggerEffect

**C++ Source:**

- **Module**: Engine
- **File**: InputDeviceProperties.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affected_triggers`` (InputDeviceTriggerMask):  [Read-Write] Which trigger this property should effect
- ``reset_upon_completion`` (bool):  [Read-Write] True if the triggers should be reset after the duration of this device property

<a id="unreal.DeviceTriggerBaseData.__init__"></a>

#### __init__

```python
def __init__(affected_triggers: InputDeviceTriggerMask = InputDeviceTriggerMask
             .NONE,
             reset_upon_completion: bool = False) -> None
```

<a id="unreal.DeviceTriggerBaseData.affected_triggers"></a>

#### affected_triggers

```python
@property
def affected_triggers() -> InputDeviceTriggerMask
```

(InputDeviceTriggerMask):  [Read-Write] Which trigger this property should effect

<a id="unreal.DeviceTriggerBaseData.affected_triggers"></a>

#### affected_triggers

```python
@affected_triggers.setter
def affected_triggers(value: InputDeviceTriggerMask) -> None
```

<a id="unreal.DeviceTriggerBaseData.reset_upon_completion"></a>

#### reset_upon_completion

```python
@property
def reset_upon_completion() -> bool
```

(bool):  [Read-Write] True if the triggers should be reset after the duration of this device property

<a id="unreal.DeviceTriggerBaseData.reset_upon_completion"></a>

#### reset_upon_completion

```python
@reset_upon_completion.setter
def reset_upon_completion(value: bool) -> None
```

<a id="unreal.DeviceTriggerFeedbackData"></a>