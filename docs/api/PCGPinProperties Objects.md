## PCGPinProperties Objects

```python
class PCGPinProperties(StructBase)
```

PCGPin Properties

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPin.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``advanced_pin`` (bool):  [Read-Write] Advanced pin will be hidden by default in the UI and will be shown only if the user extend the node (in the UI) to see advanced pins.
  deprecated: Use IsAdvancedPin function or PinStatus property.
- ``allow_multiple_connections`` (bool):  [Read-Write]
- ``allow_multiple_data`` (bool):  [Read-Write]
- ``allowed_types`` (PCGDataType):  [Read-Write]
- ``invisible_pin`` (bool):  [Read-Write]
- ``label`` (Name):  [Read-Write]
- ``pin_status`` (PCGPinStatus):  [Read-Write] Define the status of a given pin (Normal, Required or Advanced)
- ``tooltip`` (Text):  [Read-Write]
- ``usage`` (PCGPinUsage):  [Read-Write]

<a id="unreal.PCGPinProperties.__init__"></a>

#### __init__

```python
def __init__(
        label: Name = "None",
        allow_multiple_data: bool = False,
        allow_multiple_connections: bool = False,
        is_advanced_pin: bool = False,
        allowed_type: PCGExclusiveDataType = PCGExclusiveDataType.ANY) -> None
```

<a id="unreal.PCGPinProperties.label"></a>

#### label

```python
@property
def label() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGPinProperties.label"></a>

#### label

```python
@label.setter
def label(value: Name) -> None
```

<a id="unreal.PCGPinProperties.usage"></a>

#### usage

```python
@property
def usage() -> PCGPinUsage
```

(PCGPinUsage):  [Read-Write]

<a id="unreal.PCGPinProperties.usage"></a>

#### usage

```python
@usage.setter
def usage(value: PCGPinUsage) -> None
```

<a id="unreal.PCGPinProperties.allowed_types"></a>

#### allowed_types

```python
@property
def allowed_types() -> PCGDataType
```

(PCGDataType):  [Read-Write]

<a id="unreal.PCGPinProperties.allowed_types"></a>

#### allowed_types

```python
@allowed_types.setter
def allowed_types(value: PCGDataType) -> None
```

<a id="unreal.PCGPinProperties.allow_multiple_data"></a>

#### allow_multiple_data

```python
@property
def allow_multiple_data() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGPinProperties.allow_multiple_data"></a>

#### allow_multiple_data

```python
@allow_multiple_data.setter
def allow_multiple_data(value: bool) -> None
```

<a id="unreal.PCGPinProperties.pin_status"></a>

#### pin_status

```python
@property
def pin_status() -> PCGPinStatus
```

(PCGPinStatus):  [Read-Write] Define the status of a given pin (Normal, Required or Advanced)

<a id="unreal.PCGPinProperties.pin_status"></a>

#### pin_status

```python
@pin_status.setter
def pin_status(value: PCGPinStatus) -> None
```

<a id="unreal.PCGPinProperties.invisible_pin"></a>

#### invisible_pin

```python
@property
def invisible_pin() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGPinProperties.invisible_pin"></a>

#### invisible_pin

```python
@invisible_pin.setter
def invisible_pin(value: bool) -> None
```

<a id="unreal.PCGPinProperties.advanced_pin"></a>

#### advanced_pin

```python
@property
def advanced_pin() -> bool
```

(bool):  [Read-Write] Advanced pin will be hidden by default in the UI and will be shown only if the user extend the node (in the UI) to see advanced pins.
deprecated: Use IsAdvancedPin function or PinStatus property.

<a id="unreal.PCGPinProperties.advanced_pin"></a>

#### advanced_pin

```python
@advanced_pin.setter
def advanced_pin(value: bool) -> None
```

<a id="unreal.PCGPinProperties.allow_multiple_connections"></a>

#### allow_multiple_connections

```python
@property
def allow_multiple_connections() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGPinProperties.allow_multiple_connections"></a>

#### allow_multiple_connections

```python
@allow_multiple_connections.setter
def allow_multiple_connections(value: bool) -> None
```

<a id="unreal.PCGPinProperties.set_required_pin"></a>

#### set_required_pin

```python
def set_required_pin() -> None
```

x.set_required_pin() -> None
Set Required Pin

<a id="unreal.PCGPinProperties.set_normal_pin"></a>

#### set_normal_pin

```python
def set_normal_pin() -> None
```

x.set_normal_pin() -> None
Set Normal Pin

<a id="unreal.PCGPinProperties.set_allow_multiple_connections"></a>

#### set_allow_multiple_connections

```python
def set_allow_multiple_connections(allow_multiple_connections: bool) -> None
```

x.set_allow_multiple_connections(allow_multiple_connections) -> None
Set Allow Multiple Connections

Args:
    allow_multiple_connections (bool):

<a id="unreal.PCGPinProperties.set_advanced_pin"></a>

#### set_advanced_pin

```python
def set_advanced_pin() -> None
```

x.set_advanced_pin() -> None
Set Advanced Pin

<a id="unreal.PCGPinProperties.is_required_pin"></a>

#### is_required_pin

```python
def is_required_pin() -> bool
```

x.is_required_pin() -> bool
Is Required Pin

Returns:
    bool:

<a id="unreal.PCGPinProperties.is_normal_pin"></a>

#### is_normal_pin

```python
def is_normal_pin() -> bool
```

x.is_normal_pin() -> bool
Is Normal Pin

Returns:
    bool:

<a id="unreal.PCGPinProperties.is_advanced_pin"></a>

#### is_advanced_pin

```python
def is_advanced_pin() -> bool
```

x.is_advanced_pin() -> bool
Is Advanced Pin

Returns:
    bool:

<a id="unreal.PCGPinProperties.allows_multiple_connections"></a>

#### allows_multiple_connections

```python
def allows_multiple_connections() -> bool
```

x.allows_multiple_connections() -> bool
Allows Multiple Connections

Returns:
    bool:

<a id="unreal.PCGObjectPropertyOverrideDescription"></a>