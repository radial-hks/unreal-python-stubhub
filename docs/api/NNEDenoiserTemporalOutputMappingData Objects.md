## NNEDenoiserTemporalOutputMappingData Objects

```python
class NNEDenoiserTemporalOutputMappingData(NNEDenoiserBaseMappingData)
```

Table row base for temporal denoiser output mapping

**C++ Source:**

- **Plugin**: NNEDenoiser
- **Module**: NNEDenoiser
- **File**: NNEDenoiserIOMappingData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``resource`` (TemporalOutputResourceName):  [Read-Write] Mapped resource name
- ``resource_channel`` (int32):  [Read-Write] Resource channel
- ``tensor_channel`` (int32):  [Read-Write] Input/output tensor channel
- ``tensor_index`` (int32):  [Read-Write] Input/output tensor index

<a id="unreal.NNEDenoiserTemporalOutputMappingData.__init__"></a>

#### __init__

```python
def __init__(
    tensor_index: int = 0,
    tensor_channel: int = 0,
    resource_channel: int = 0,
    resource: TemporalOutputResourceName = TemporalOutputResourceName.OUTPUT
) -> None
```

<a id="unreal.NNEDenoiserTemporalOutputMappingData.resource"></a>

#### resource

```python
@property
def resource() -> TemporalOutputResourceName
```

(TemporalOutputResourceName):  [Read-Write] Mapped resource name

<a id="unreal.NNEDenoiserTemporalOutputMappingData.resource"></a>

#### resource

```python
@resource.setter
def resource(value: TemporalOutputResourceName) -> None
```

<a id="unreal.TilingConfig"></a>