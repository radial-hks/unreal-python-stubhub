## MVVMViewModelBase Objects

```python
class MVVMViewModelBase(Object)
```

Base class for MVVM viewmodel.

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModel
- **File**: MVVMViewModelBase.h

<a id="unreal.MVVMViewModelBase.remove_field_value_changed_delegate"></a>

#### remove_field_value_changed_delegate

```python
def remove_field_value_changed_delegate(
        field_id: FieldNotificationId,
        delegate: FieldValueChangedDynamicDelegate) -> None
```

x.remove_field_value_changed_delegate(field_id, delegate) -> None
K2 Remove Field Value Changed Delegate

Args:
    field_id (FieldNotificationId): 
    delegate (FieldValueChangedDynamicDelegate):

<a id="unreal.MVVMViewModelBase.broadcast_field_value_changed"></a>

#### broadcast_field_value_changed

```python
def broadcast_field_value_changed(field_id: FieldNotificationId) -> None
```

x.broadcast_field_value_changed(field_id) -> None
K2 Broadcast Field Value Changed
deprecated: Function 'K2_BroadcastFieldValueChanged' is deprecated.

Args:
    field_id (FieldNotificationId):

<a id="unreal.MVVMViewModelBase.add_field_value_changed_delegate"></a>

#### add_field_value_changed_delegate

```python
def add_field_value_changed_delegate(
        field_id: FieldNotificationId,
        delegate: FieldValueChangedDynamicDelegate) -> None
```

x.add_field_value_changed_delegate(field_id, delegate) -> None
K2 Add Field Value Changed Delegate

Args:
    field_id (FieldNotificationId): 
    delegate (FieldValueChangedDynamicDelegate):

<a id="unreal.MVVMViewModelCollectionObject"></a>