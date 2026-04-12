## AesFacadeShapeGrammar Objects

```python
class AesFacadeShapeGrammar(StructBase)
```

Aes Facade Shape Grammar

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesFacadeAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``level_corners`` (str):  [Read-Write]
- ``level_definition`` (Map[Name, AesFacadeLevelData]):  [Read-Write]
- ``level_grammar`` (str):  [Read-Write]
- ``module_definition`` (Map[Name, AesFacadeModuleData]):  [Read-Write]

<a id="unreal.AesFacadeShapeGrammar.__init__"></a>

#### \_\_init\_\_

```python
def __init__(module_definition: Map[Name, AesFacadeModuleData] = {},
             level_definition: Map[Name, AesFacadeLevelData] = {},
             level_grammar: str = "") -> None
```

<a id="unreal.AesFacadeShapeGrammar.module_definition"></a>

#### module\_definition

```python
@property
def module_definition() -> Map[Name, AesFacadeModuleData]
```

(Map[Name, AesFacadeModuleData]):  [Read-Write]

<a id="unreal.AesFacadeShapeGrammar.module_definition"></a>

#### module\_definition

```python
@module_definition.setter
def module_definition(value: Map[Name, AesFacadeModuleData]) -> None
```

<a id="unreal.AesFacadeShapeGrammar.level_definition"></a>

#### level\_definition

```python
@property
def level_definition() -> Map[Name, AesFacadeLevelData]
```

(Map[Name, AesFacadeLevelData]):  [Read-Write]

<a id="unreal.AesFacadeShapeGrammar.level_definition"></a>

#### level\_definition

```python
@level_definition.setter
def level_definition(value: Map[Name, AesFacadeLevelData]) -> None
```

<a id="unreal.AesFacadeShapeGrammar.level_grammar"></a>

#### level\_grammar

```python
@property
def level_grammar() -> str
```

(str):  [Read-Write]

<a id="unreal.AesFacadeShapeGrammar.level_grammar"></a>

#### level\_grammar

```python
@level_grammar.setter
def level_grammar(value: str) -> None
```

<a id="unreal.AesFacadeMaterialInfo"></a>