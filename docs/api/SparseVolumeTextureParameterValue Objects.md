## SparseVolumeTextureParameterValue Objects

```python
class SparseVolumeTextureParameterValue(StructBase)
```

Editable sparse volume texture parameter.

**C++ Source:**

- **Module**: Engine
- **File**: MaterialInstance.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``parameter_info`` (MaterialParameterInfo):  [Read-Write]
- ``parameter_value`` (SparseVolumeTexture):  [Read-Write]

<a id="unreal.SparseVolumeTextureParameterValue.__init__"></a>

#### \_\_init\_\_

```python
def __init__(parameter_info: MaterialParameterInfo = [
    "None", MaterialParameterAssociation.GLOBAL_PARAMETER, -1
],
             parameter_value: SparseVolumeTexture = None) -> None
```

<a id="unreal.SparseVolumeTextureParameterValue.parameter_info"></a>

#### parameter\_info

```python
@property
def parameter_info() -> MaterialParameterInfo
```

(MaterialParameterInfo):  [Read-Write]

<a id="unreal.SparseVolumeTextureParameterValue.parameter_info"></a>

#### parameter\_info

```python
@parameter_info.setter
def parameter_info(value: MaterialParameterInfo) -> None
```

<a id="unreal.SparseVolumeTextureParameterValue.parameter_value"></a>

#### parameter\_value

```python
@property
def parameter_value() -> SparseVolumeTexture
```

(SparseVolumeTexture):  [Read-Write]

<a id="unreal.SparseVolumeTextureParameterValue.parameter_value"></a>

#### parameter\_value

```python
@parameter_value.setter
def parameter_value(value: SparseVolumeTexture) -> None
```

<a id="unreal.FontParameterValue"></a>