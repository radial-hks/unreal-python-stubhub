## RigVMHost Objects

```python
class RigVMHost(Object)
```

set this to something larger than 0 to profile N runs

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMHost.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the asset

<a id="unreal.RigVMHost.supports_event"></a>

#### supports_event

```python
def supports_event(event_name: Name) -> bool
```

x.supports_event(event_name) -> bool
Supports Event

Args:
    event_name (Name): 

Returns:
    bool:

<a id="unreal.RigVMHost.set_variable_from_string"></a>

#### set_variable_from_string

```python
def set_variable_from_string(variable_name: Name, value: str) -> bool
```

x.set_variable_from_string(variable_name, value) -> bool
Returns the value of a given variable as a string

Args:
    variable_name (Name): 
    value (str): 

Returns:
    bool:

<a id="unreal.RigVMHost.set_frames_per_second"></a>

#### set_frames_per_second

```python
def set_frames_per_second(frames_per_second: float) -> None
```

x.set_frames_per_second(frames_per_second) -> None
Set the current fps

Args:
    frames_per_second (float):

<a id="unreal.RigVMHost.set_delta_time"></a>

#### set_delta_time

```python
def set_delta_time(delta_time: float) -> None
```

x.set_delta_time(delta_time) -> None
Set the current delta time

Args:
    delta_time (float):

<a id="unreal.RigVMHost.set_absolute_time"></a>

#### set_absolute_time

```python
def set_absolute_time(absolute_time: float,
                      set_delta_time_zero: bool = False) -> None
```

x.set_absolute_time(absolute_time, set_delta_time_zero=False) -> None
Set the current absolute time

Args:
    absolute_time (float): 
    set_delta_time_zero (bool):

<a id="unreal.RigVMHost.set_absolute_and_delta_time"></a>

#### set_absolute_and_delta_time

```python
def set_absolute_and_delta_time(absolute_time: float,
                                delta_time: float) -> None
```

x.set_absolute_and_delta_time(absolute_time, delta_time) -> None
Set the current absolute and delta times

Args:
    absolute_time (float): 
    delta_time (float):

<a id="unreal.RigVMHost.request_run_once_event"></a>

#### request_run_once_event

```python
def request_run_once_event(event_name: Name, event_index: int = -1) -> None
```

x.request_run_once_event(event_name, event_index=-1) -> None
Requests to run an event once

Args:
    event_name (Name): 
    event_index (int32):

<a id="unreal.RigVMHost.request_init"></a>

#### request_init

```python
def request_init() -> None
```

x.request_init() -> None
Requests to perform an init during the next execution

<a id="unreal.RigVMHost.remove_run_once_event"></a>

#### remove_run_once_event

```python
def remove_run_once_event(event_name: Name) -> bool
```

x.remove_run_once_event(event_name) -> bool
Removes an event running once

Args:
    event_name (Name): 

Returns:
    bool:

<a id="unreal.RigVMHost.is_init_required"></a>

#### is_init_required

```python
def is_init_required() -> bool
```

x.is_init_required() -> bool
Returns true if this host requires the VM memory to be initialized

Returns:
    bool:

<a id="unreal.RigVMHost.get_vm"></a>

#### get_vm

```python
def get_vm() -> RigVM
```

x.get_vm() -> RigVM
Get VM

Returns:
    RigVM:

<a id="unreal.RigVMHost.get_variable_type"></a>

#### get_variable_type

```python
def get_variable_type(variable_name: Name) -> Name
```

x.get_variable_type(variable_name) -> Name
Returns the type of a given variable

Args:
    variable_name (Name): 

Returns:
    Name:

<a id="unreal.RigVMHost.get_variable_as_string"></a>

#### get_variable_as_string

```python
def get_variable_as_string(variable_name: Name) -> str
```

x.get_variable_as_string(variable_name) -> str
Returns the value of a given variable as a string

Args:
    variable_name (Name): 

Returns:
    str:

<a id="unreal.RigVMHost.get_supported_events"></a>

#### get_supported_events

```python
def get_supported_events() -> Array[Name]
```

x.get_supported_events() -> Array[Name]
Get Supported Events

Returns:
    Array[Name]:

<a id="unreal.RigVMHost.get_script_accessible_variables"></a>

#### get_script_accessible_variables

```python
def get_script_accessible_variables() -> Array[Name]
```

x.get_script_accessible_variables() -> Array[Name]
Returns the names of variables accessible in scripting

Returns:
    Array[Name]:

<a id="unreal.RigVMHost.get_extended_execute_context"></a>

#### get_extended_execute_context

```python
def get_extended_execute_context() -> RigVMExtendedExecuteContext
```

x.get_extended_execute_context() -> RigVMExtendedExecuteContext
Get Extended Execute Context
deprecated: This function has been deprecated and it is no longer supported.

Returns:
    RigVMExtendedExecuteContext:

<a id="unreal.RigVMHost.get_delta_time"></a>

#### get_delta_time

```python
def get_delta_time() -> float
```

x.get_delta_time() -> float
Gets the current delta time

Returns:
    float:

<a id="unreal.RigVMHost.get_current_frames_per_second"></a>

#### get_current_frames_per_second

```python
def get_current_frames_per_second() -> float
```

x.get_current_frames_per_second() -> float
Returns the current frames per second (this may change over time)

Returns:
    float:

<a id="unreal.RigVMHost.get_absolute_time"></a>

#### get_absolute_time

```python
def get_absolute_time() -> float
```

x.get_absolute_time() -> float
Gets the current absolute time

Returns:
    float:

<a id="unreal.RigVMHost.find_rig_vm_hosts"></a>

#### find_rig_vm_hosts

```python
@classmethod
def find_rig_vm_hosts(cls, outer: Object,
                      optional_class: Class) -> Array[RigVMHost]
```

X.find_rig_vm_hosts(outer, optional_class) -> Array[RigVMHost]
Find Rig VMHosts

Args:
    outer (Object): 
    optional_class (type(Class)): 

Returns:
    Array[RigVMHost]:

<a id="unreal.RigVMHost.execute_event"></a>

#### execute_event

```python
def execute_event(event_name: Name) -> bool
```

x.execute_event(event_name) -> bool
Execute a user defined event

Args:
    event_name (Name): 

Returns:
    bool:

<a id="unreal.RigVMHost.execute"></a>

#### execute

```python
def execute(event_name: Name) -> bool
```

x.execute(event_name) -> bool
Execute

Args:
    event_name (Name): 

Returns:
    bool:

<a id="unreal.RigVMHost.can_execute"></a>

#### can_execute

```python
def can_execute() -> bool
```

x.can_execute() -> bool
Is valid for execution

Returns:
    bool:

<a id="unreal.RigVMHost.has_asset_user_data_of_class"></a>

#### has_asset_user_data_of_class

```python
def has_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.has_asset_user_data_of_class(user_data_class) -> bool
Checks whether or not an instance of the provided AssetUserData class is contained.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to check for

Returns:
    bool: Whether or not an instance of InUserDataClass was found

<a id="unreal.RigVMHost.get_asset_user_data_of_class"></a>

#### get_asset_user_data_of_class

```python
def get_asset_user_data_of_class(user_data_class: Class) -> AssetUserData
```

x.get_asset_user_data_of_class(user_data_class) -> AssetUserData
Returns an instance of the provided AssetUserData class if it's contained in the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to get

Returns:
    AssetUserData: The instance of the UAssetUserData class contained, or null if it doesn't exist

<a id="unreal.RigVMHost.add_asset_user_data_of_class"></a>

#### add_asset_user_data_of_class

```python
def add_asset_user_data_of_class(user_data_class: Class) -> bool
```

x.add_asset_user_data_of_class(user_data_class) -> bool
Creates and adds an instance of the provided AssetUserData class to the target asset.

Args:
    user_data_class (type(Class)): UAssetUserData sub class to create

Returns:
    bool: Whether or not an instance of InUserDataClass was succesfully added

<a id="unreal.RigVMProjectSettings"></a>