## NNEDenoiserTemporalInputMappingData Objects

```python
class NNEDenoiserTemporalInputMappingData(NNEDenoiserBaseMappingData)
```

Table row base for temporal denoiser input mapping

**C++ Source:**

- **Plugin**: NNEDenoiser
- **Module**: NNEDenoiser
- **File**: NNEDenoiserIOMappingData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_index`` (int32):  [Read-Write] Resource frame index
- ``resource`` (TemporalInputResourceName):  [Read-Write] Mapped resource name
- ``resource_channel`` (int32):  [Read-Write] Resource channel
- ``tensor_channel`` (int32):  [Read-Write] Input/output tensor channel
- ``tensor_index`` (int32):  [Read-Write] Input/output tensor index

<a id="unreal.NNEDenoiserTemporalInputMappingData.__init__"></a>

#### __init__

```python
def __init__(
        tensor_index: int = 0,
        tensor_channel: int = 0,
        resource_channel: int = 0,
        resource: TemporalInputResourceName = TemporalInputResourceName.COLOR,
        frame_index: int = 0) -> None
```

<a id="unreal.NNEDenoiserTemporalInputMappingData.resource"></a>

#### resource

```python
@property
def resource() -> TemporalInputResourceName
```

(TemporalInputResourceName):  [Read-Write] Mapped resource name

<a id="unreal.NNEDenoiserTemporalInputMappingData.resource"></a>

#### resource

```python
@resource.setter
def resource(value: TemporalInputResourceName) -> None
```

<a id="unreal.NNEDenoiserTemporalInputMappingData.frame_index"></a>

#### frame_index

```python
@property
def frame_index() -> int
```

(int32):  [Read-Write] Resource frame index

<a id="unreal.NNEDenoiserTemporalInputMappingData.frame_index"></a>

#### frame_index

```python
@frame_index.setter
def frame_index(value: int) -> None
```

<a id="unreal.NNEDenoiserTemporalOutputMappingData"></a>