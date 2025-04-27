## MaterialParameterInfo Objects

```python
class MaterialParameterInfo(StructBase)
```

Material Parameter Info

**C++ Source:**

- **Module**: Engine
- **File**: MaterialTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``association`` (MaterialParameterAssociation):  [Read-Write] Whether this is a global parameter, or part of a layer or blend
- ``index`` (int32):  [Read-Write] Layer or blend index this parameter is part of. INDEX_NONE for global parameters.
- ``name`` (Name):  [Read-Write]

<a id="unreal.MaterialParameterInfo.__init__"></a>

#### __init__

```python
def __init__(
        name: Name = "None",
        association: MaterialParameterAssociation = MaterialParameterAssociation
    .LAYER_PARAMETER,
        index: int = 0) -> None
```

<a id="unreal.MaterialParameterInfo.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.MaterialParameterInfo.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.MaterialParameterInfo.association"></a>

#### association

```python
@property
def association() -> MaterialParameterAssociation
```

(MaterialParameterAssociation):  [Read-Write] Whether this is a global parameter, or part of a layer or blend

<a id="unreal.MaterialParameterInfo.association"></a>

#### association

```python
@association.setter
def association(value: MaterialParameterAssociation) -> None
```

<a id="unreal.MaterialParameterInfo.index"></a>

#### index

```python
@property
def index() -> int
```

(int32):  [Read-Write] Layer or blend index this parameter is part of. INDEX_NONE for global parameters.

<a id="unreal.MaterialParameterInfo.index"></a>

#### index

```python
@index.setter
def index(value: int) -> None
```

<a id="unreal.ParameterChannelNames"></a>