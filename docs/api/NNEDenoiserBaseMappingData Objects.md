## NNEDenoiserBaseMappingData Objects

```python
class NNEDenoiserBaseMappingData(TableRowBase)
```

Table row base for denoiser basic input and output mapping

**C++ Source:**

- **Plugin**: NNEDenoiser
- **Module**: NNEDenoiser
- **File**: NNEDenoiserIOMappingData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``resource_channel`` (int32):  [Read-Write] Resource channel
- ``tensor_channel`` (int32):  [Read-Write] Input/output tensor channel
- ``tensor_index`` (int32):  [Read-Write] Input/output tensor index

<a id="unreal.NNEDenoiserBaseMappingData.__init__"></a>

#### __init__

```python
def __init__(tensor_index: int = 0,
             tensor_channel: int = 0,
             resource_channel: int = 0) -> None
```

<a id="unreal.NNEDenoiserBaseMappingData.tensor_index"></a>

#### tensor_index

```python
@property
def tensor_index() -> int
```

(int32):  [Read-Write] Input/output tensor index

<a id="unreal.NNEDenoiserBaseMappingData.tensor_index"></a>

#### tensor_index

```python
@tensor_index.setter
def tensor_index(value: int) -> None
```

<a id="unreal.NNEDenoiserBaseMappingData.tensor_channel"></a>

#### tensor_channel

```python
@property
def tensor_channel() -> int
```

(int32):  [Read-Write] Input/output tensor channel

<a id="unreal.NNEDenoiserBaseMappingData.tensor_channel"></a>

#### tensor_channel

```python
@tensor_channel.setter
def tensor_channel(value: int) -> None
```

<a id="unreal.NNEDenoiserBaseMappingData.resource_channel"></a>

#### resource_channel

```python
@property
def resource_channel() -> int
```

(int32):  [Read-Write] Resource channel

<a id="unreal.NNEDenoiserBaseMappingData.resource_channel"></a>

#### resource_channel

```python
@resource_channel.setter
def resource_channel(value: int) -> None
```

<a id="unreal.NNEDenoiserInputMappingData"></a>