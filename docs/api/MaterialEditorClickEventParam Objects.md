## MaterialEditorClickEventParam Objects

```python
class MaterialEditorClickEventParam(EventArgsBase)
```

Material Editor Click Event Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPMaterialEditorAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``material_lable`` (str):  [Read-Write]
- ``material_name`` (str):  [Read-Write]

<a id="unreal.MaterialEditorClickEventParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(material_name: str = "", material_lable: str = "") -> None
```

<a id="unreal.MaterialEditorClickEventParam.material_name"></a>

#### material\_name

```python
@property
def material_name() -> str
```

(str):  [Read-Write]

<a id="unreal.MaterialEditorClickEventParam.material_name"></a>

#### material\_name

```python
@material_name.setter
def material_name(value: str) -> None
```

<a id="unreal.MaterialEditorClickEventParam.material_lable"></a>

#### material\_lable

```python
@property
def material_lable() -> str
```

(str):  [Read-Write]

<a id="unreal.MaterialEditorClickEventParam.material_lable"></a>

#### material\_lable

```python
@material_lable.setter
def material_lable(value: str) -> None
```

<a id="unreal.DCPLoadParams"></a>