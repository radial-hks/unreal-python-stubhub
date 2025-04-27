## DoubleVectorParameterValue Objects

```python
class DoubleVectorParameterValue(StructBase)
```

Editable vector parameter.

**C++ Source:**

- **Module**: Engine
- **File**: MaterialInstance.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``parameter_info`` (MaterialParameterInfo):  [Read-Write]
- ``parameter_value`` (Vector4d):  [Read-Write] LWC_TODO: Blueprint?

<a id="unreal.DoubleVectorParameterValue.__init__"></a>

#### __init__

```python
def __init__(
    parameter_info: MaterialParameterInfo = [
        "None", MaterialParameterAssociation.GLOBAL_PARAMETER, -1
    ]
) -> None
```

<a id="unreal.DoubleVectorParameterValue.parameter_info"></a>

#### parameter_info

```python
@property
def parameter_info() -> MaterialParameterInfo
```

(MaterialParameterInfo):  [Read-Write]

<a id="unreal.DoubleVectorParameterValue.parameter_info"></a>

#### parameter_info

```python
@parameter_info.setter
def parameter_info(value: MaterialParameterInfo) -> None
```

<a id="unreal.TextureParameterValue"></a>