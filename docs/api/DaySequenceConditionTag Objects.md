## DaySequenceConditionTag Objects

```python
class DaySequenceConditionTag(Object)
```

Day Sequence Condition Tag

**C++ Source:**

- **Plugin**: DaySequence
- **Module**: DaySequence
- **File**: DaySequenceConditionTag.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition_name`` (str):  [Read-Write] Derived classes should give this a meaningful default value which is displayed
  when prompting users with a list of possible conditions to apply to a given sequence.

<a id="unreal.DaySequenceConditionTag.setup_on_condition_value_changed"></a>

#### setup_on_condition_value_changed

```python
def setup_on_condition_value_changed() -> None
```

x.setup_on_condition_value_changed() -> None
Derived classes should override this function if the condition being evaluated is
associated with external delegates which are broadcast when the condition may change.
The intent is to bind BroadcastOnConditionValueChanged to all relevant external delegates so that we
can propagate those broadcasts to notify users of this condition that the condition needs reevaluating.

<a id="unreal.DaySequenceConditionTag.evaluate"></a>

#### evaluate

```python
def evaluate() -> bool
```

x.evaluate() -> bool
Evaluates a preconfigured boolean condition.

Returns:
    bool:

<a id="unreal.DaySequenceConditionTag.broadcast_on_condition_value_changed"></a>

#### broadcast_on_condition_value_changed

```python
def broadcast_on_condition_value_changed() -> None
```

x.broadcast_on_condition_value_changed() -> None
Derived classes should call this function to notify listeners that the underlying condition may have changed.
This will only trigger a broadcast if Evaluate() returns a different value than the last invocation of this function.

<a id="unreal.DaySequenceModifierComponent"></a>