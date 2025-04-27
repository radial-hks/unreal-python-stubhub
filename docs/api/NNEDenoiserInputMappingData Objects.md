## NNEDenoiserInputMappingData Objects

```python
class NNEDenoiserInputMappingData(NNEDenoiserBaseMappingData)
```

Table row base for denoiser input mapping

**C++ Source:**

- **Plugin**: NNEDenoiser
- **Module**: NNEDenoiser
- **File**: NNEDenoiserIOMappingData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``resource`` (InputResourceName):  [Read-Write] Mapped resource name
- ``resource_channel`` (int32):  [Read-Write] Resource channel
- ``tensor_channel`` (int32):  [Read-Write] Input/output tensor channel
- ``tensor_index`` (int32):  [Read-Write] Input/output tensor index

<a id="unreal.NNEDenoiserInputMappingData.__init__"></a>

#### __init__

```python
def __init__(tensor_index: int = 0,
             tensor_channel: int = 0,
             resource_channel: int = 0,
             resource: InputResourceName = InputResourceName.COLOR) -> None
```

<a id="unreal.NNEDenoiserInputMappingData.resource"></a>

#### resource

```python
@property
def resource() -> InputResourceName
```

(InputResourceName):  [Read-Write] Mapped resource name

<a id="unreal.NNEDenoiserInputMappingData.resource"></a>

#### resource

```python
@resource.setter
def resource(value: InputResourceName) -> None
```

<a id="unreal.NNEDenoiserOutputMappingData"></a>