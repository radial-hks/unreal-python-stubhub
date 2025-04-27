## GameInstance Objects

```python
class GameInstance(Object)
```

GameInstance: high-level manager object for an instance of the running game.
Spawned at game creation and not destroyed until game instance is shut down.
Running as a standalone game, there will be one of these.
Running in PIE (play-in-editor) will generate one of these per PIE instance.

**C++ Source:**

- **Module**: Engine
- **File**: GameInstance.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_input_device_connection_change`` (OnUserInputDeviceConnectionChange):  [Read-Write] Callback for when an input device connection state has changed (a new gamepad was connected or disconnected)
- ``on_pawn_controller_changed_delegates`` (OnPawnControllerChanged):  [Read-Write] gets triggered shortly after a pawn's controller is set. Most of the time
      it signals that the Controller has changed but in edge cases (like during
      replication) it might end up broadcasting the same pawn-controller pair
      more than once
- ``on_user_input_device_pairing_change`` (OnUserInputDevicePairingChange):  [Read-Write] Callback when an input device has changed pairings (the owning platform user has changed for that device)

<a id="unreal.GameInstance.on_pawn_controller_changed_delegates"></a>

#### on_pawn_controller_changed_delegates

```python
@property
def on_pawn_controller_changed_delegates() -> OnPawnControllerChanged
```

(OnPawnControllerChanged):  [Read-Write] gets triggered shortly after a pawn's controller is set. Most of the time
    it signals that the Controller has changed but in edge cases (like during
    replication) it might end up broadcasting the same pawn-controller pair
    more than once

<a id="unreal.GameInstance.on_pawn_controller_changed_delegates"></a>

#### on_pawn_controller_changed_delegates

```python
@on_pawn_controller_changed_delegates.setter
def on_pawn_controller_changed_delegates(
        value: OnPawnControllerChanged) -> None
```

<a id="unreal.GameInstance.on_input_device_connection_change"></a>

#### on_input_device_connection_change

```python
@property
def on_input_device_connection_change() -> OnUserInputDeviceConnectionChange
```

(OnUserInputDeviceConnectionChange):  [Read-Write] Callback for when an input device connection state has changed (a new gamepad was connected or disconnected)

<a id="unreal.GameInstance.on_input_device_connection_change"></a>

#### on_input_device_connection_change

```python
@on_input_device_connection_change.setter
def on_input_device_connection_change(
        value: OnUserInputDeviceConnectionChange) -> None
```

<a id="unreal.GameInstance.on_user_input_device_pairing_change"></a>

#### on_user_input_device_pairing_change

```python
@property
def on_user_input_device_pairing_change() -> OnUserInputDevicePairingChange
```

(OnUserInputDevicePairingChange):  [Read-Write] Callback when an input device has changed pairings (the owning platform user has changed for that device)

<a id="unreal.GameInstance.on_user_input_device_pairing_change"></a>

#### on_user_input_device_pairing_change

```python
@on_user_input_device_pairing_change.setter
def on_user_input_device_pairing_change(
        value: OnUserInputDevicePairingChange) -> None
```

<a id="unreal.GameInstance.receive_shutdown"></a>

#### receive_shutdown

```python
def receive_shutdown() -> None
```

x.receive_shutdown() -> None
Opportunity for blueprints to handle the game instance being shutdown.

<a id="unreal.GameInstance.receive_init"></a>

#### receive_init

```python
def receive_init() -> None
```

x.receive_init() -> None
Opportunity for blueprints to handle the game instance being initialized.

<a id="unreal.GameInstance.handle_travel_error"></a>

#### handle_travel_error

```python
def handle_travel_error(failure_type: TravelFailure) -> None
```

x.handle_travel_error(failure_type) -> None
Opportunity for blueprints to handle travel errors.

Args:
    failure_type (TravelFailure):

<a id="unreal.GameInstance.handle_network_error"></a>

#### handle_network_error

```python
def handle_network_error(failure_type: NetworkFailure,
                         is_server: bool) -> None
```

x.handle_network_error(failure_type, is_server) -> None
Opportunity for blueprints to handle network errors.

Args:
    failure_type (NetworkFailure): 
    is_server (bool):

<a id="unreal.GameModeBase"></a>