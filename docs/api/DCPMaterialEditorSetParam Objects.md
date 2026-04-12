## DCPMaterialEditorSetParam Objects

```python
class DCPMaterialEditorSetParam(ParamsBase)
```

DCPMaterial Editor Set Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPMaterialEditorAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``material_name`` (str):  [Read-Write]
- ``mid`` (str):  [Read-Write]

<a id="unreal.DCPMaterialEditorSetParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(material_name: str = "", mid: str = "") -> None
```

<a id="unreal.DCPMaterialEditorSetParam.material_name"></a>

#### material\_name

```python
@property
def material_name() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPMaterialEditorSetParam.material_name"></a>

#### material\_name

```python
@material_name.setter
def material_name(value: str) -> None
```

<a id="unreal.DCPMaterialEditorSetParam.mid"></a>

#### mid

```python
@property
def mid() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPMaterialEditorSetParam.mid"></a>

#### mid

```python
@mid.setter
def mid(value: str) -> None
```

<a id="unreal.DCPMaterialNodeSetParam"></a>