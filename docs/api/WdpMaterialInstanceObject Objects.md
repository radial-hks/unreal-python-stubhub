## WdpMaterialInstanceObject Objects

```python
class WdpMaterialInstanceObject(StructBase)
```

Wdp Material Instance Object

**C++ Source:**

- **Plugin**: WdpApplication
- **Module**: WdpMaterial
- **File**: WdpMaterialDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``category`` (str):  [Read-Write]
- ``friendly_name`` (str):  [Read-Write]
- ``id`` (str):  [Read-Write]
- ``name`` (str):  [Read-Write]
- ``parameters`` (MaterialInstanceParams):  [Read-Write]
- ``parent_material`` (str):  [Read-Write]

<a id="unreal.WdpMaterialInstanceObject.__init__"></a>

#### \_\_init\_\_

```python
def __init__(id: str = "",
             name: str = "",
             friendly_name: str = "",
             category: str = "",
             parent_material: str = "",
             parameters: MaterialInstanceParams = [[], []]) -> None
```

<a id="unreal.WdpMaterialInstanceObject.id"></a>

#### id

```python
@property
def id() -> str
```

(str):  [Read-Write]

<a id="unreal.WdpMaterialInstanceObject.id"></a>

#### id

```python
@id.setter
def id(value: str) -> None
```

<a id="unreal.WdpMaterialInstanceObject.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write]

<a id="unreal.WdpMaterialInstanceObject.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.WdpMaterialInstanceObject.friendly_name"></a>

#### friendly\_name

```python
@property
def friendly_name() -> str
```

(str):  [Read-Write]

<a id="unreal.WdpMaterialInstanceObject.friendly_name"></a>

#### friendly\_name

```python
@friendly_name.setter
def friendly_name(value: str) -> None
```

<a id="unreal.WdpMaterialInstanceObject.category"></a>

#### category

```python
@property
def category() -> str
```

(str):  [Read-Write]

<a id="unreal.WdpMaterialInstanceObject.category"></a>

#### category

```python
@category.setter
def category(value: str) -> None
```

<a id="unreal.WdpMaterialInstanceObject.parent_material"></a>

#### parent\_material

```python
@property
def parent_material() -> str
```

(str):  [Read-Write]

<a id="unreal.WdpMaterialInstanceObject.parent_material"></a>

#### parent\_material

```python
@parent_material.setter
def parent_material(value: str) -> None
```

<a id="unreal.WdpMaterialInstanceObject.parameters"></a>

#### parameters

```python
@property
def parameters() -> MaterialInstanceParams
```

(MaterialInstanceParams):  [Read-Write]

<a id="unreal.WdpMaterialInstanceObject.parameters"></a>

#### parameters

```python
@parameters.setter
def parameters(value: MaterialInstanceParams) -> None
```

<a id="unreal.WdpMaterialLibraryJson"></a>