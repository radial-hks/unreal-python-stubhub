## PCGPackedCustomData Objects

```python
class PCGPackedCustomData(StructBase)
```

PCGPacked Custom Data

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGInstanceDataPackerBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_data`` (Array[float]):  [Read-Write]
- ``num_custom_data_floats`` (int32):  [Read-Write]

<a id="unreal.PCGPackedCustomData.__init__"></a>

#### __init__

```python
def __init__(num_custom_data_floats: int = 0,
             custom_data: Array[float] = []) -> None
```

<a id="unreal.PCGPackedCustomData.num_custom_data_floats"></a>

#### num_custom_data_floats

```python
@property
def num_custom_data_floats() -> int
```

(int32):  [Read-Write]

<a id="unreal.PCGPackedCustomData.num_custom_data_floats"></a>

#### num_custom_data_floats

```python
@num_custom_data_floats.setter
def num_custom_data_floats(value: int) -> None
```

<a id="unreal.PCGPackedCustomData.custom_data"></a>

#### custom_data

```python
@property
def custom_data() -> Array[float]
```

(Array[float]):  [Read-Write]

<a id="unreal.PCGPackedCustomData.custom_data"></a>

#### custom_data

```python
@custom_data.setter
def custom_data(value: Array[float]) -> None
```

<a id="unreal.PCGMatchAndSetByAttributeEntry"></a>