## AvaGameInstance Objects

```python
class AvaGameInstance(GameInstance)
```

Ava Game Instance

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: Avalanche
- **File**: AvaGameInstance.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_input_device_connection_change`` (OnUserInputDeviceConnectionChange):  [Read-Write] Callback for when an input device connection state has changed (a new gamepad was connected or disconnected)
- ``on_pawn_controller_changed_delegates`` (OnPawnControllerChanged):  [Read-Write] gets triggered shortly after a pawn's controller is set. Most of the time
      it signals that the Controller has changed but in edge cases (like during
      replication) it might end up broadcasting the same pawn-controller pair
      more than once
- ``on_user_input_device_pairing_change`` (OnUserInputDevicePairingChange):  [Read-Write] Callback when an input device has changed pairings (the owning platform user has changed for that device)

<a id="unreal.AvaGizmoComponent"></a>