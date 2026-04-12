## WdpMaterialObject Objects

```python
class WdpMaterialObject(StructBase)
```

Wdp Material Object

**C++ Source:**

- **Plugin**: WdpApplication
- **Module**: WdpMaterial
- **File**: WdpMaterialDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``id`` (str):  [Read-Write]
- ``name`` (str):  [Read-Write]
- ``parameters`` (WdpMaterialParams):  [Read-Write]

<a id="unreal.WdpMaterialObject.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    id: str = "",
    name: str = "",
    parameters: WdpMaterialParams = [
        [1.000000, 1.000000, 1.000000, 0.000000, 0.000000, 0.000000],
        [
            "", [0, 0, 0, 0], 1.000000, 1.000000, "", 1.000000, "",
            0.500000, "", 0.000000, "", 1.000000, "", 1.000000, "", "",
            [0, 0, 0, 0], "", 1.000000, 0.100000, [0, 0, 0, 0], 1.000000
        ]
    ]
) -> None
```

<a id="unreal.WdpMaterialObject.id"></a>

#### id

```python
@property
def id() -> str
```

(str):  [Read-Write]

<a id="unreal.WdpMaterialObject.id"></a>

#### id

```python
@id.setter
def id(value: str) -> None
```

<a id="unreal.WdpMaterialObject.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write]

<a id="unreal.WdpMaterialObject.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.WdpMaterialObject.parameters"></a>

#### parameters

```python
@property
def parameters() -> WdpMaterialParams
```

(WdpMaterialParams):  [Read-Write]

<a id="unreal.WdpMaterialObject.parameters"></a>

#### parameters

```python
@parameters.setter
def parameters(value: WdpMaterialParams) -> None
```

<a id="unreal.MaterialInstanceParams"></a>