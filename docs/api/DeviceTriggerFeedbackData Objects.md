## DeviceTriggerFeedbackData Objects

```python
class DeviceTriggerFeedbackData(StructBase)
```

UInputDeviceTriggerFeedbackProperty

**C++ Source:**

- **Module**: Engine
- **File**: InputDeviceProperties.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``feedback_position_curve`` (CurveFloat):  [Read-Write] What position on the trigger that the feedback should be applied to over time (1-9)
- ``feedback_strengh_curve`` (CurveFloat):  [Read-Write] How strong the feedback is over time (1-8)

<a id="unreal.DeviceTriggerFeedbackData.__init__"></a>

#### __init__

```python
def __init__(feedback_position_curve: CurveFloat = None,
             feedback_strengh_curve: CurveFloat = None) -> None
```

<a id="unreal.DeviceTriggerFeedbackData.feedback_position_curve"></a>

#### feedback_position_curve

```python
@property
def feedback_position_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] What position on the trigger that the feedback should be applied to over time (1-9)

<a id="unreal.DeviceTriggerFeedbackData.feedback_position_curve"></a>

#### feedback_position_curve

```python
@feedback_position_curve.setter
def feedback_position_curve(value: CurveFloat) -> None
```

<a id="unreal.DeviceTriggerFeedbackData.feedback_strengh_curve"></a>

#### feedback_strengh_curve

```python
@property
def feedback_strengh_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] How strong the feedback is over time (1-8)

<a id="unreal.DeviceTriggerFeedbackData.feedback_strengh_curve"></a>

#### feedback_strengh_curve

```python
@feedback_strengh_curve.setter
def feedback_strengh_curve(value: CurveFloat) -> None
```

<a id="unreal.DeviceTriggerTriggerResistanceData"></a>