## InputDeviceLibrary Objects

```python
class InputDeviceLibrary(BlueprintFunctionLibrary)
```

A static BP library that exposes Input Device data to blueprints
see: IPlatformInputDeviceMapper
note: Keep any function comments up to date with those in GenericPlatformInputDeviceMapper.h!

**C++ Source:**

- **Module**: Engine
- **File**: InputDeviceLibrary.h

<a id="unreal.InputDeviceLibrary.not_equal_platform_user_id"></a>

#### not_equal_platform_user_id

```python
@classmethod
def not_equal_platform_user_id(cls, a: PlatformUserId,
                               b: PlatformUserId) -> bool
```

X.not_equal_platform_user_id(a, b) -> bool
Returns true if PlatformUserId A is not equal to PlatformUserId B (A != B)

Args:
    a (PlatformUserId): 
    b (PlatformUserId): 

Returns:
    bool:

<a id="unreal.InputDeviceLibrary.not_equal_input_device_id"></a>

#### not_equal_input_device_id

```python
@classmethod
def not_equal_input_device_id(cls, a: InputDeviceId, b: InputDeviceId) -> bool
```

X.not_equal_input_device_id(a, b) -> bool
Returns true if InputDeviceId A is not equal to InputDeviceId B (A != B)

Args:
    a (InputDeviceId): 
    b (InputDeviceId): 

Returns:
    bool:

<a id="unreal.InputDeviceLibrary.is_valid_platform_id"></a>

#### is_valid_platform_id

```python
@classmethod
def is_valid_platform_id(cls, user_id: PlatformUserId) -> bool
```

X.is_valid_platform_id(user_id) -> bool
Check if the given platform ID is valid

Args:
    user_id (PlatformUserId): 

Returns:
    bool: True if the platform ID is valid (it has been assigned by the PlatformInputDeviceMapper)

<a id="unreal.InputDeviceLibrary.is_valid_input_device"></a>

#### is_valid_input_device

```python
@classmethod
def is_valid_input_device(cls, device_id: InputDeviceId) -> bool
```

X.is_valid_input_device(device_id) -> bool
Check if the given input device is valid

Args:
    device_id (InputDeviceId): 

Returns:
    bool: True if the given input device is valid (it has been assigned an ID by the PlatformInputDeviceMapper)

<a id="unreal.InputDeviceLibrary.is_unpaired_user_id"></a>

#### is_unpaired_user_id

```python
@classmethod
def is_unpaired_user_id(cls, platform_id: PlatformUserId) -> bool
```

X.is_unpaired_user_id(platform_id) -> bool
Returns true if the given Platform User Id is the user for unpaired input devices on this platform.

Args:
    platform_id (PlatformUserId): 

Returns:
    bool:

<a id="unreal.InputDeviceLibrary.is_input_device_mapped_to_unpaired_user"></a>

#### is_input_device_mapped_to_unpaired_user

```python
@classmethod
def is_input_device_mapped_to_unpaired_user(
        cls, input_device: InputDeviceId) -> bool
```

X.is_input_device_mapped_to_unpaired_user(input_device) -> bool
Returns true if the given input device is mapped to the unpaired platform user id.

Args:
    input_device (InputDeviceId): 

Returns:
    bool:

<a id="unreal.InputDeviceLibrary.is_device_property_handle_valid"></a>

#### is_device_property_handle_valid

```python
@classmethod
def is_device_property_handle_valid(cls,
                                    handle: InputDevicePropertyHandle) -> bool
```

X.is_device_property_handle_valid(handle) -> bool
Returns true if the given handle is valid

Args:
    handle (InputDevicePropertyHandle): 

Returns:
    bool:

<a id="unreal.InputDeviceLibrary.get_user_for_unpaired_input_devices"></a>

#### get_user_for_unpaired_input_devices

```python
@classmethod
def get_user_for_unpaired_input_devices(cls) -> PlatformUserId
```

X.get_user_for_unpaired_input_devices() -> PlatformUserId
Returns the platform user id that is being used for unmapped input devices.
Will be PLATFORMUSERID_NONE if platform does not support this (this is the default behavior)

Returns:
    PlatformUserId:

<a id="unreal.InputDeviceLibrary.get_user_for_input_device"></a>

#### get_user_for_input_device

```python
@classmethod
def get_user_for_input_device(cls, device_id: InputDeviceId) -> PlatformUserId
```

X.get_user_for_input_device(device_id) -> PlatformUserId
Returns the platform user attached to this input device, or PLATFORMUSERID_NONE if invalid

Args:
    device_id (InputDeviceId): 

Returns:
    PlatformUserId:

<a id="unreal.InputDeviceLibrary.get_primary_platform_user"></a>

#### get_primary_platform_user

```python
@classmethod
def get_primary_platform_user(cls) -> PlatformUserId
```

X.get_primary_platform_user() -> PlatformUserId
Returns the 'Primary' Platform user for this platform.
This typically has an internal ID of '0' and is used as the default platform user to
map devices such as the keyboard and mouse that don't get assigned unique ID's from their
owning platform code.

Returns:
    PlatformUserId:

<a id="unreal.InputDeviceLibrary.get_primary_input_device_for_user"></a>

#### get_primary_input_device_for_user

```python
@classmethod
def get_primary_input_device_for_user(
        cls, user_id: PlatformUserId) -> InputDeviceId
```

X.get_primary_input_device_for_user(user_id) -> InputDeviceId
Returns the primary input device used by a specific player, or INPUTDEVICEID_NONE if invalid

Args:
    user_id (PlatformUserId): 

Returns:
    InputDeviceId:

<a id="unreal.InputDeviceLibrary.get_player_controller_from_platform_user"></a>

#### get_player_controller_from_platform_user

```python
@classmethod
def get_player_controller_from_platform_user(
        cls, user_id: PlatformUserId) -> PlayerController
```

X.get_player_controller_from_platform_user(user_id) -> PlayerController
Get the player controller who has the given Platform User ID.

Args:
    user_id (PlatformUserId): 

Returns:
    PlayerController:

<a id="unreal.InputDeviceLibrary.get_player_controller_from_input_device"></a>

#### get_player_controller_from_input_device

```python
@classmethod
def get_player_controller_from_input_device(
        cls, device_id: InputDeviceId) -> PlayerController
```

X.get_player_controller_from_input_device(device_id) -> PlayerController
Get the player controller who owns the given input device id

Args:
    device_id (InputDeviceId): 

Returns:
    PlayerController:

<a id="unreal.InputDeviceLibrary.get_input_device_connection_state"></a>

#### get_input_device_connection_state

```python
@classmethod
def get_input_device_connection_state(
        cls, device_id: InputDeviceId) -> InputDeviceConnectionState
```

X.get_input_device_connection_state(device_id) -> InputDeviceConnectionState
Gets the connection state of the given input device.

Args:
    device_id (InputDeviceId): The device to get the connection state of

Returns:
    InputDeviceConnectionState: The connection state of the given device. EInputDeviceConnectionState::Unknown if the device is not mapped

<a id="unreal.InputDeviceLibrary.get_default_input_device"></a>

#### get_default_input_device

```python
@classmethod
def get_default_input_device(cls) -> InputDeviceId
```

X.get_default_input_device() -> InputDeviceId
Returns the default device id used for things like keyboard/mouse input

Returns:
    InputDeviceId:

<a id="unreal.InputDeviceLibrary.get_all_input_devices_for_user"></a>

#### get_all_input_devices_for_user

```python
@classmethod
def get_all_input_devices_for_user(
        cls, user_id: PlatformUserId) -> Tuple[int, Array[InputDeviceId]]
```

X.get_all_input_devices_for_user(user_id) -> (int32, out_input_devices=Array[InputDeviceId])
Populates the OutInputDevices array with any InputDeviceID's that are mapped to the given platform user

Args:
    user_id (PlatformUserId): The Platform User to gather the input devices of.

Returns:
    Array[InputDeviceId]: The number of mapped devices, INDEX_NONE if the user was not found.

    out_input_devices (Array[InputDeviceId]): Array of input device ID's that will be populated with the mapped devices.

<a id="unreal.InputDeviceLibrary.get_all_input_devices"></a>

#### get_all_input_devices

```python
@classmethod
def get_all_input_devices(cls) -> Tuple[int, Array[InputDeviceId]]
```

X.get_all_input_devices() -> (int32, out_input_devices=Array[InputDeviceId])
Get all mapped input devices on this platform regardless of their connection state.

Returns:
    Array[InputDeviceId]: The number of connected input devices

    out_input_devices (Array[InputDeviceId]): Array of input devices to populate

<a id="unreal.InputDeviceLibrary.get_all_connected_input_devices"></a>

#### get_all_connected_input_devices

```python
@classmethod
def get_all_connected_input_devices(cls) -> Tuple[int, Array[InputDeviceId]]
```

X.get_all_connected_input_devices() -> (int32, out_input_devices=Array[InputDeviceId])
Gather all currently connected input devices

Returns:
    Array[InputDeviceId]: The number of connected input devices

    out_input_devices (Array[InputDeviceId]): Array of input devices to populate

<a id="unreal.InputDeviceLibrary.get_all_active_users"></a>

#### get_all_active_users

```python
@classmethod
def get_all_active_users(cls) -> Tuple[int, Array[PlatformUserId]]
```

X.get_all_active_users() -> (int32, out_users=Array[PlatformUserId])
Get all currently active platform ids, anyone who has a mapped input device

Returns:
    Array[PlatformUserId]: The number of active platform users

    out_users (Array[PlatformUserId]): Array that will be populated with the platform users.

<a id="unreal.InputDeviceLibrary.equal_equal_platform_user_id"></a>

#### equal_equal_platform_user_id

```python
@classmethod
def equal_equal_platform_user_id(cls, a: PlatformUserId,
                                 b: PlatformUserId) -> bool
```

X.equal_equal_platform_user_id(a, b) -> bool
Returns true if PlatformUserId A is equal to PlatformUserId B (A == B)

Args:
    a (PlatformUserId): 
    b (PlatformUserId): 

Returns:
    bool:

<a id="unreal.InputDeviceLibrary.equal_equal_input_device_id"></a>

#### equal_equal_input_device_id

```python
@classmethod
def equal_equal_input_device_id(cls, a: InputDeviceId,
                                b: InputDeviceId) -> bool
```

X.equal_equal_input_device_id(a, b) -> bool
Returns true if InputDeviceId A is equal to InputDeviceId B (A == B)

Args:
    a (InputDeviceId): 
    b (InputDeviceId): 

Returns:
    bool:

<a id="unreal.PlatformInputDeviceMapperLibrary"></a>