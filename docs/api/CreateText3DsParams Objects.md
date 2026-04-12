## CreateText3DsParams Objects

```python
class CreateText3DsParams(StructBase)
```

Create Text 3Ds Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: Text3DAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write]
- ``point_entity_eid`` (str):  [Read-Write]
- ``text3d_style`` (Text3DStyle):  [Read-Write]

<a id="unreal.CreateText3DsParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(point_entity_eid: str = "",
             text3d_style: Text3DStyle = [
                 "51WORLD", "CF4300FF", "plain", 0.200000, False, 1.000000
             ],
             coord_z_ref: int = 0) -> None
```

<a id="unreal.CreateText3DsParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@property
def point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.CreateText3DsParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@point_entity_eid.setter
def point_entity_eid(value: str) -> None
```

<a id="unreal.CreateText3DsParams.text3d_style"></a>

#### text3d\_style

```python
@property
def text3d_style() -> Text3DStyle
```

(Text3DStyle):  [Read-Write]

<a id="unreal.CreateText3DsParams.text3d_style"></a>

#### text3d\_style

```python
@text3d_style.setter
def text3d_style(value: Text3DStyle) -> None
```

<a id="unreal.CreateText3DsParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.CreateText3DsParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.CreateText3DParams_Batch"></a>