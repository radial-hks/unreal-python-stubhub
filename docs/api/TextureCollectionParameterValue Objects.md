## TextureCollectionParameterValue Objects

```python
class TextureCollectionParameterValue(StructBase)
```

Editable texture collection parameter.

**C++ Source:**

- **Module**: Engine
- **File**: MaterialInstance.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``parameter_info`` (MaterialParameterInfo):  [Read-Write]
- ``parameter_value`` (TextureCollection):  [Read-Write]

<a id="unreal.TextureCollectionParameterValue.__init__"></a>

#### __init__

```python
def __init__(parameter_info: MaterialParameterInfo = [
    "None", MaterialParameterAssociation.GLOBAL_PARAMETER, -1
],
             parameter_value: TextureCollection = None) -> None
```

<a id="unreal.TextureCollectionParameterValue.parameter_info"></a>

#### parameter_info

```python
@property
def parameter_info() -> MaterialParameterInfo
```

(MaterialParameterInfo):  [Read-Write]

<a id="unreal.TextureCollectionParameterValue.parameter_info"></a>

#### parameter_info

```python
@parameter_info.setter
def parameter_info(value: MaterialParameterInfo) -> None
```

<a id="unreal.TextureCollectionParameterValue.parameter_value"></a>

#### parameter_value

```python
@property
def parameter_value() -> TextureCollection
```

(TextureCollection):  [Read-Write]

<a id="unreal.TextureCollectionParameterValue.parameter_value"></a>

#### parameter_value

```python
@parameter_value.setter
def parameter_value(value: TextureCollection) -> None
```

<a id="unreal.RuntimeVirtualTextureParameterValue"></a>