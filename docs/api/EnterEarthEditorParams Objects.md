## EnterEarthEditorParams Objects

```python
class EnterEarthEditorParams(ParamsBase)
```

Enter Earth Editor Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: EarthEditorAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``language`` (str):  [Read-Write]

<a id="unreal.EnterEarthEditorParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(language: str = "") -> None
```

<a id="unreal.EnterEarthEditorParams.language"></a>

#### language

```python
@property
def language() -> str
```

(str):  [Read-Write]

<a id="unreal.EnterEarthEditorParams.language"></a>

#### language

```python
@language.setter
def language(value: str) -> None
```

<a id="unreal.UpdateEarthTilesParams"></a>