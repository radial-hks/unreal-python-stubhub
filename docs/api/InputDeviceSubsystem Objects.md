## InputDeviceSubsystem Objects

```python
class InputDeviceSubsystem(EngineSubsystem)
```

The input device subsystem provides an interface to allow users to set Input Device Properties
on any Platform User.

**C++ Source:**

- **Module**: Engine
- **File**: InputDeviceSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_input_hardware_device_changed`` (HardwareInputDeviceChanged):  [Read-Write] A delegate that is fired when a platform user changes what Hardware Input device they are using

<a id="unreal.InputDeviceSubsystem.on_input_hardware_device_changed"></a>

#### on_input_hardware_device_changed

```python
@property
def on_input_hardware_device_changed() -> HardwareInputDeviceChanged
```

(HardwareInputDeviceChanged):  [Read-Write] A delegate that is fired when a platform user changes what Hardware Input device they are using

<a id="unreal.InputDeviceSubsystem.on_input_hardware_device_changed"></a>

#### on_input_hardware_device_changed

```python
@on_input_hardware_device_changed.setter
def on_input_hardware_device_changed(
        value: HardwareInputDeviceChanged) -> None
```

<a id="unreal.InputDeviceSubsystem.remove_device_property_handles"></a>

#### remove_device_property_handles

```python
def remove_device_property_handles(
        handles_to_remove: Set[InputDevicePropertyHandle]) -> None
```

x.remove_device_property_handles(handles_to_remove) -> None
Remove a set of device properties based on their handles.

Args:
    handles_to_remove (Set[InputDevicePropertyHandle]): The set of device property handles to remove

<a id="unreal.InputDeviceSubsystem.remove_device_property_by_handle"></a>

#### remove_device_property_by_handle

```python
def remove_device_property_by_handle(
        handle_to_remove: InputDevicePropertyHandle) -> None
```

x.remove_device_property_by_handle(handle_to_remove) -> None
Remove a single device property based on it's handle

Args:
    handle_to_remove (InputDevicePropertyHandle):

<a id="unreal.InputDeviceSubsystem.remove_all_device_properties"></a>

#### remove_all_device_properties

```python
def remove_all_device_properties() -> None
```

x.remove_all_device_properties() -> None
Removes all the current Input Device Properties that are active, regardless of the Platform User

<a id="unreal.InputDeviceSubsystem.is_property_active"></a>

#### is_property_active

```python
def is_property_active(handle: InputDevicePropertyHandle) -> bool
```

x.is_property_active(handle) -> bool
Returns true if the property associated with the given handle is currently active, and it is not pending removal

Args:
    handle (InputDevicePropertyHandle): 

Returns:
    bool:

<a id="unreal.InputDeviceSubsystem.get_most_recently_used_input_device_id"></a>

#### get_most_recently_used_input_device_id

```python
def get_most_recently_used_input_device_id(
        user_id: PlatformUserId) -> InputDeviceId
```

x.get_most_recently_used_input_device_id(user_id) -> InputDeviceId
Returns the most recently used FInputDeviceId for the given platform user id.

This will be INPUTDEVICEID_NONE if there is no known device for the given user.

Args:
    user_id (PlatformUserId): 

Returns:
    InputDeviceId:

<a id="unreal.InputDeviceSubsystem.get_most_recently_used_hardware_device"></a>

#### get_most_recently_used_hardware_device

```python
def get_most_recently_used_hardware_device(
        user_id: PlatformUserId) -> HardwareDeviceIdentifier
```

x.get_most_recently_used_hardware_device(user_id) -> HardwareDeviceIdentifier
Gets the most recently used hardware input device for the given platform user

Args:
    user_id (PlatformUserId): 

Returns:
    HardwareDeviceIdentifier:

<a id="unreal.InputDeviceSubsystem.get_input_device_hardware_identifier"></a>

#### get_input_device_hardware_identifier

```python
def get_input_device_hardware_identifier(
        input_device: InputDeviceId) -> HardwareDeviceIdentifier
```

x.get_input_device_hardware_identifier(input_device) -> HardwareDeviceIdentifier
Get Input Device Hardware Identifier

Args:
    input_device (InputDeviceId): 

Returns:
    HardwareDeviceIdentifier:

<a id="unreal.InputDeviceSubsystem.get_active_device_property"></a>

#### get_active_device_property

```python
def get_active_device_property(
        handle: InputDevicePropertyHandle) -> InputDeviceProperty
```

x.get_active_device_property(handle) -> InputDeviceProperty
Returns a pointer to the active input device property with the given handle. Returns null if the property doesn't exist

Args:
    handle (InputDevicePropertyHandle): 

Returns:
    InputDeviceProperty:

<a id="unreal.InputDeviceSubsystem.activate_device_property_of_class"></a>

#### activate_device_property_of_class

```python
def activate_device_property_of_class(
        property_class: Class,
        params: ActivateDevicePropertyParams) -> InputDevicePropertyHandle
```

x.activate_device_property_of_class(property_class, params) -> InputDevicePropertyHandle
Spawn a new instance of the given device property class and activate it.

Args:
    property_class (type(Class)): 
    params (ActivateDevicePropertyParams): 

Returns:
    InputDevicePropertyHandle:

<a id="unreal.SaveGame"></a>