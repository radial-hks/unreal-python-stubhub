## PCGPinPropertiesGPUStruct Objects

```python
class PCGPinPropertiesGPUStruct(StructBase)
```

Helper struct to nest GPU pin properties inside a UI category.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPinPropertiesGPU.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute_inheritance_mode`` (PCGAttributeInheritanceMode):  [Read-Write] How to inherit attribute names, types, and values.
- ``created_kernel_attribute_keys`` (Array[PCGKernelAttributeKey]):  [Read-Write] Add entries to create new attributes on data emitted by this pin.
- ``data_count`` (int32):  [Read-Write] Number of data to create.
- ``data_count_mode`` (PCGDataCountMode):  [Read-Write] How the number of data is determined.
- ``data_multiplicity`` (PCGDataMultiplicity):  [Read-Write] How to combine data counts.
- ``element_count`` (int32):  [Read-Write] Fixed number of elements to create in each output data.
- ``element_count_mode`` (PCGElementCountMode):  [Read-Write] How the number of elements is determined.
- ``element_multiplicity`` (PCGElementMultiplicity):  [Read-Write] How to combine element counts.
- ``initialization_mode`` (PCGPinInitMode):  [Read-Write] How the output data for this pin will be initialized.
- ``pins_to_inititalize_from`` (Array[Name]):  [Read-Write] Input pins to initialize this pin's data from.

<a id="unreal.PCGPinPropertiesGPUStruct.__init__"></a>

#### __init__

```python
def __init__(
    initialization_mode: PCGPinInitMode = PCGPinInitMode.FROM_INPUT_PINS,
    pins_to_inititalize_from: Array[Name] = [],
    data_count_mode: PCGDataCountMode = PCGDataCountMode.FROM_INPUT_DATA,
    data_multiplicity: PCGDataMultiplicity = PCGDataMultiplicity.PAIRWISE,
    data_count: int = 0,
    element_count_mode: PCGElementCountMode = PCGElementCountMode.
    FROM_INPUT_DATA,
    element_multiplicity: PCGElementMultiplicity = PCGElementMultiplicity.
    PRODUCT,
    element_count: int = 0,
    attribute_inheritance_mode:
    PCGAttributeInheritanceMode = PCGAttributeInheritanceMode.NONE
) -> None
```

<a id="unreal.PCGPinPropertiesGPUStruct.initialization_mode"></a>

#### initialization_mode

```python
@property
def initialization_mode() -> PCGPinInitMode
```

(PCGPinInitMode):  [Read-Write] How the output data for this pin will be initialized.

<a id="unreal.PCGPinPropertiesGPUStruct.initialization_mode"></a>

#### initialization_mode

```python
@initialization_mode.setter
def initialization_mode(value: PCGPinInitMode) -> None
```

<a id="unreal.PCGPinPropertiesGPUStruct.pins_to_inititalize_from"></a>

#### pins_to_inititalize_from

```python
@property
def pins_to_inititalize_from() -> Array[Name]
```

(Array[Name]):  [Read-Write] Input pins to initialize this pin's data from.

<a id="unreal.PCGPinPropertiesGPUStruct.pins_to_inititalize_from"></a>

#### pins_to_inititalize_from

```python
@pins_to_inititalize_from.setter
def pins_to_inititalize_from(value: Array[Name]) -> None
```

<a id="unreal.PCGPinPropertiesGPUStruct.data_count_mode"></a>

#### data_count_mode

```python
@property
def data_count_mode() -> PCGDataCountMode
```

(PCGDataCountMode):  [Read-Write] How the number of data is determined.

<a id="unreal.PCGPinPropertiesGPUStruct.data_count_mode"></a>

#### data_count_mode

```python
@data_count_mode.setter
def data_count_mode(value: PCGDataCountMode) -> None
```

<a id="unreal.PCGPinPropertiesGPUStruct.data_multiplicity"></a>

#### data_multiplicity

```python
@property
def data_multiplicity() -> PCGDataMultiplicity
```

(PCGDataMultiplicity):  [Read-Write] How to combine data counts.

<a id="unreal.PCGPinPropertiesGPUStruct.data_multiplicity"></a>

#### data_multiplicity

```python
@data_multiplicity.setter
def data_multiplicity(value: PCGDataMultiplicity) -> None
```

<a id="unreal.PCGPinPropertiesGPUStruct.data_count"></a>

#### data_count

```python
@property
def data_count() -> int
```

(int32):  [Read-Write] Number of data to create.

<a id="unreal.PCGPinPropertiesGPUStruct.data_count"></a>

#### data_count

```python
@data_count.setter
def data_count(value: int) -> None
```

<a id="unreal.PCGPinPropertiesGPUStruct.element_count_mode"></a>

#### element_count_mode

```python
@property
def element_count_mode() -> PCGElementCountMode
```

(PCGElementCountMode):  [Read-Write] How the number of elements is determined.

<a id="unreal.PCGPinPropertiesGPUStruct.element_count_mode"></a>

#### element_count_mode

```python
@element_count_mode.setter
def element_count_mode(value: PCGElementCountMode) -> None
```

<a id="unreal.PCGPinPropertiesGPUStruct.element_multiplicity"></a>

#### element_multiplicity

```python
@property
def element_multiplicity() -> PCGElementMultiplicity
```

(PCGElementMultiplicity):  [Read-Write] How to combine element counts.

<a id="unreal.PCGPinPropertiesGPUStruct.element_multiplicity"></a>

#### element_multiplicity

```python
@element_multiplicity.setter
def element_multiplicity(value: PCGElementMultiplicity) -> None
```

<a id="unreal.PCGPinPropertiesGPUStruct.element_count"></a>

#### element_count

```python
@property
def element_count() -> int
```

(int32):  [Read-Write] Fixed number of elements to create in each output data.

<a id="unreal.PCGPinPropertiesGPUStruct.element_count"></a>

#### element_count

```python
@element_count.setter
def element_count(value: int) -> None
```

<a id="unreal.PCGPinPropertiesGPUStruct.attribute_inheritance_mode"></a>

#### attribute_inheritance_mode

```python
@property
def attribute_inheritance_mode() -> PCGAttributeInheritanceMode
```

(PCGAttributeInheritanceMode):  [Read-Write] How to inherit attribute names, types, and values.

<a id="unreal.PCGPinPropertiesGPUStruct.attribute_inheritance_mode"></a>

#### attribute_inheritance_mode

```python
@attribute_inheritance_mode.setter
def attribute_inheritance_mode(value: PCGAttributeInheritanceMode) -> None
```

<a id="unreal.PCGPinPropertiesGPU"></a>