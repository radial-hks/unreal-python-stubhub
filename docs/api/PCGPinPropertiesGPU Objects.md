## PCGPinPropertiesGPU Objects

```python
class PCGPinPropertiesGPU(PCGPinProperties)
```

An extension of the pin properties that adds hints for GPU specific properties, such as buffer size and data layout.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPinPropertiesGPU.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``advanced_pin`` (bool):  [Read-Write] Advanced pin will be hidden by default in the UI and will be shown only if the user extend the node (in the UI) to see advanced pins.
  deprecated: Use IsAdvancedPin function or PinStatus property.
- ``allow_multiple_connections`` (bool):  [Read-Write]
- ``allow_multiple_data`` (bool):  [Read-Write]
- ``allowed_types`` (PCGDataType):  [Read-Write]
- ``invisible_pin`` (bool):  [Read-Write]
- ``label`` (Name):  [Read-Write]
- ``pin_status`` (PCGPinStatus):  [Read-Write] Define the status of a given pin (Normal, Required or Advanced)
- ``properties_gpu`` (PCGPinPropertiesGPUStruct):  [Read-Write]
- ``tooltip`` (Text):  [Read-Write]
- ``usage`` (PCGPinUsage):  [Read-Write]

<a id="unreal.PCGPinPropertiesGPU.__init__"></a>

#### __init__

```python
def __init__(
    label: Name = "None",
    usage: PCGPinUsage = PCGPinUsage.NORMAL,
    allowed_types: PCGDataType = 0,
    allow_multiple_data: bool = False,
    pin_status: PCGPinStatus = PCGPinStatus.NORMAL,
    invisible_pin: bool = False,
    allow_multiple_connections: bool = False,
    properties_gpu: PCGPinPropertiesGPUStruct = [
        PCGPinInitMode.FROM_INPUT_PINS, [], PCGDataCountMode.FROM_INPUT_DATA,
        PCGDataMultiplicity.PAIRWISE, 1, PCGElementCountMode.FROM_INPUT_DATA,
        PCGElementMultiplicity.PRODUCT, 1,
        PCGAttributeInheritanceMode.COPY_ATTRIBUTE_SETUP
    ]
) -> None
```

<a id="unreal.PCGPinPropertiesGPU.properties_gpu"></a>

#### properties_gpu

```python
@property
def properties_gpu() -> PCGPinPropertiesGPUStruct
```

(PCGPinPropertiesGPUStruct):  [Read-Write]

<a id="unreal.PCGPinPropertiesGPU.properties_gpu"></a>

#### properties_gpu

```python
@properties_gpu.setter
def properties_gpu(value: PCGPinPropertiesGPUStruct) -> None
```

<a id="unreal.PCGLandscapeDataProps"></a>