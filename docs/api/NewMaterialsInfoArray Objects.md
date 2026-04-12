## NewMaterialsInfoArray Objects

```python
class NewMaterialsInfoArray(ParamsBase)
```

New Materials Info Array

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: MaterialToolAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``new_materials_info`` (Array[NewMaterialsInfo]):  [Read-Write]

<a id="unreal.NewMaterialsInfoArray.__init__"></a>

#### \_\_init\_\_

```python
def __init__(new_materials_info: Array[NewMaterialsInfo] = []) -> None
```

<a id="unreal.NewMaterialsInfoArray.new_materials_info"></a>

#### new\_materials\_info

```python
@property
def new_materials_info() -> Array[NewMaterialsInfo]
```

(Array[NewMaterialsInfo]):  [Read-Write]

<a id="unreal.NewMaterialsInfoArray.new_materials_info"></a>

#### new\_materials\_info

```python
@new_materials_info.setter
def new_materials_info(value: Array[NewMaterialsInfo]) -> None
```

<a id="unreal.ApplyMaterialToEntityParams"></a>