## FieldNotificationLibrary Objects

```python
class FieldNotificationLibrary(BlueprintFunctionLibrary)
```

The Field Notification system allows a user to know when a property value is modified at runtime (note that it can be a function return value).
The class needs to implement the INotifyFieldValueChanged interface.
The property' setter  usually follows this pattern "if (new value != old value) assign the new value; broadcast that the value changed;".
The Blueprint implementation handles that setter logic automatically with SetPropertyValueAndBroadcast.
When a property value is modified by replication, the RepNotify will call BroadcastFieldValueChanged.
A function can also be a Field Notify. The function needs to be const and return a single value.

**C++ Source:**

- **Module**: Engine
- **File**: FieldNotificationLibrary.h

<a id="unreal.FieldNotificationLibrary.broadcast_field_value_changed"></a>

#### broadcast_field_value_changed

```python
@classmethod
def broadcast_field_value_changed(cls, object: Object,
                                  field_id: FieldNotificationId) -> None
```

X.broadcast_field_value_changed(object, field_id) -> None
Broadcast that the Field value changed.

Args:
    object (Object): 
    field_id (FieldNotificationId):

<a id="unreal.FieldNotificationLibrary.broadcast_fields_value_changed"></a>

#### broadcast_fields_value_changed

```python
@classmethod
def broadcast_fields_value_changed(
        cls, object: Object, field_ids: Array[FieldNotificationId]) -> None
```

X.broadcast_fields_value_changed(object, field_ids) -> None
Broadcast that a list of Field values changed.

Args:
    object (Object): 
    field_ids (Array[FieldNotificationId]):

<a id="unreal.ForceFeedbackAttenuation"></a>