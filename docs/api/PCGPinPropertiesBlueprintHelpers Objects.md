## PCGPinPropertiesBlueprintHelpers Objects

```python
class PCGPinPropertiesBlueprintHelpers(BlueprintFunctionLibrary)
```

Helper class to allow the BP to call the custom functions on FPCGPinProperties.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPin.h

<a id="unreal.PCGPinPropertiesBlueprintHelpers.set_required_pin"></a>

#### set_required_pin

```python
@classmethod
def set_required_pin(cls,
                     pin_properties: PCGPinProperties) -> PCGPinProperties
```

X.set_required_pin(pin_properties) -> PCGPinProperties
Set Required Pin

Args:
    pin_properties (PCGPinProperties): 

Returns:
    PCGPinProperties: 

    pin_properties (PCGPinProperties):

<a id="unreal.PCGPinPropertiesBlueprintHelpers.set_normal_pin"></a>

#### set_normal_pin

```python
@classmethod
def set_normal_pin(cls, pin_properties: PCGPinProperties) -> PCGPinProperties
```

X.set_normal_pin(pin_properties) -> PCGPinProperties
Set Normal Pin

Args:
    pin_properties (PCGPinProperties): 

Returns:
    PCGPinProperties: 

    pin_properties (PCGPinProperties):

<a id="unreal.PCGPinPropertiesBlueprintHelpers.set_allow_multiple_connections"></a>

#### set_allow_multiple_connections

```python
@classmethod
def set_allow_multiple_connections(
        cls, pin_properties: PCGPinProperties,
        allow_multiple_connections: bool) -> PCGPinProperties
```

X.set_allow_multiple_connections(pin_properties, allow_multiple_connections) -> PCGPinProperties
Set Allow Multiple Connections

Args:
    pin_properties (PCGPinProperties): 
    allow_multiple_connections (bool): 

Returns:
    PCGPinProperties: 

    pin_properties (PCGPinProperties):

<a id="unreal.PCGPinPropertiesBlueprintHelpers.set_advanced_pin"></a>

#### set_advanced_pin

```python
@classmethod
def set_advanced_pin(cls,
                     pin_properties: PCGPinProperties) -> PCGPinProperties
```

X.set_advanced_pin(pin_properties) -> PCGPinProperties
Set Advanced Pin

Args:
    pin_properties (PCGPinProperties): 

Returns:
    PCGPinProperties: 

    pin_properties (PCGPinProperties):

<a id="unreal.PCGPinPropertiesBlueprintHelpers.is_required_pin"></a>

#### is_required_pin

```python
@classmethod
def is_required_pin(cls, pin_properties: PCGPinProperties) -> bool
```

X.is_required_pin(pin_properties) -> bool
Is Required Pin

Args:
    pin_properties (PCGPinProperties): 

Returns:
    bool:

<a id="unreal.PCGPinPropertiesBlueprintHelpers.is_normal_pin"></a>

#### is_normal_pin

```python
@classmethod
def is_normal_pin(cls, pin_properties: PCGPinProperties) -> bool
```

X.is_normal_pin(pin_properties) -> bool
Is Normal Pin

Args:
    pin_properties (PCGPinProperties): 

Returns:
    bool:

<a id="unreal.PCGPinPropertiesBlueprintHelpers.is_advanced_pin"></a>

#### is_advanced_pin

```python
@classmethod
def is_advanced_pin(cls, pin_properties: PCGPinProperties) -> bool
```

X.is_advanced_pin(pin_properties) -> bool
Is Advanced Pin

Args:
    pin_properties (PCGPinProperties): 

Returns:
    bool:

<a id="unreal.PCGPinPropertiesBlueprintHelpers.allows_multiple_connections"></a>

#### allows_multiple_connections

```python
@classmethod
def allows_multiple_connections(cls, pin_properties: PCGPinProperties) -> bool
```

X.allows_multiple_connections(pin_properties) -> bool
Allows Multiple Connections

Args:
    pin_properties (PCGPinProperties): 

Returns:
    bool:

<a id="unreal.PCGSettingsInstance"></a>