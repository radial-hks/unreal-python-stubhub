## Text3DUpdateParams Objects

```python
class Text3DUpdateParams(ParamsBase)
```

Text 3DUpdate Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: Text3DAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write]
- ``eid`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``point_entity_eid`` (str):  [Read-Write]
- ``text3d_style`` (Text3DStyle):  [Read-Write]

<a id="unreal.Text3DUpdateParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             point_entity_eid: str = "",
             text3d_style: Text3DStyle = [
                 "51WORLD", "CF4300FF", "plain", 0.200000, False, 1.000000
             ],
             coord_z_ref: int = 0) -> None
```

<a id="unreal.Text3DUpdateParams.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.Text3DUpdateParams.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.Text3DUpdateParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@property
def point_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.Text3DUpdateParams.point_entity_eid"></a>

#### point\_entity\_eid

```python
@point_entity_eid.setter
def point_entity_eid(value: str) -> None
```

<a id="unreal.Text3DUpdateParams.text3d_style"></a>

#### text3d\_style

```python
@property
def text3d_style() -> Text3DStyle
```

(Text3DStyle):  [Read-Write]

<a id="unreal.Text3DUpdateParams.text3d_style"></a>

#### text3d\_style

```python
@text3d_style.setter
def text3d_style(value: Text3DStyle) -> None
```

<a id="unreal.Text3DUpdateParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.Text3DUpdateParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.ViewshedStyle"></a>