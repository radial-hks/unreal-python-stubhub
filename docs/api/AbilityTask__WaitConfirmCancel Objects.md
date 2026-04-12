## AbilityTask\_WaitConfirmCancel Objects

```python
class AbilityTask_WaitConfirmCancel(AbilityTask)
```

Fixme: this name is conflicting with AbilityTask_WaitConfirm
UAbilityTask_WaitConfirmCancel = Wait for Targeting confirm/cancel
UAbilityTask_WaitConfirm = Wait for server to confirm ability activation

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AbilityTask_WaitConfirmCancel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_cancel`` (WaitConfirmCancelDelegate):  [Read-Write]
- ``on_confirm`` (WaitConfirmCancelDelegate):  [Read-Write]

<a id="unreal.AbilityTask_WaitConfirmCancel.on_confirm"></a>

#### on\_confirm

```python
@property
def on_confirm() -> WaitConfirmCancelDelegate
```

(WaitConfirmCancelDelegate):  [Read-Write]

<a id="unreal.AbilityTask_WaitConfirmCancel.on_confirm"></a>

#### on\_confirm

```python
@on_confirm.setter
def on_confirm(value: WaitConfirmCancelDelegate) -> None
```

<a id="unreal.AbilityTask_WaitConfirmCancel.on_cancel"></a>

#### on\_cancel

```python
@property
def on_cancel() -> WaitConfirmCancelDelegate
```

(WaitConfirmCancelDelegate):  [Read-Write]

<a id="unreal.AbilityTask_WaitConfirmCancel.on_cancel"></a>

#### on\_cancel

```python
@on_cancel.setter
def on_cancel(value: WaitConfirmCancelDelegate) -> None
```

<a id="unreal.AbilityTask_WaitDelay"></a>