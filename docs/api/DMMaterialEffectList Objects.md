## DMMaterialEffectList Objects

```python
class DMMaterialEffectList(StructBase)
```

DMMaterial Effect List

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DynamicMaterialEditorSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``effects`` (Array[MaterialFunctionInterface]):  [Read-Write]
- ``name`` (str):  [Read-Write]

<a id="unreal.DMMaterialEffectList.__init__"></a>

#### __init__

```python
def __init__(name: str = "",
             effects: Array[MaterialFunctionInterface] = []) -> None
```

<a id="unreal.DMMaterialEffectList.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write]

<a id="unreal.DMMaterialEffectList.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.DMMaterialEffectList.effects"></a>

#### effects

```python
@property
def effects() -> Array[MaterialFunctionInterface]
```

(Array[MaterialFunctionInterface]):  [Read-Write]

<a id="unreal.DMMaterialEffectList.effects"></a>

#### effects

```python
@effects.setter
def effects(value: Array[MaterialFunctionInterface]) -> None
```

<a id="unreal.DMDefaultMaterialPropertySlotValue"></a>