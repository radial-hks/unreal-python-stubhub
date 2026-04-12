## FieldObjectCommands Objects

```python
class FieldObjectCommands(StructBase)
```

Field Commands container that will be stored in the construction script

**C++ Source:**

- **Module**: FieldSystemEngine
- **File**: FieldSystemObjects.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``meta_datas`` (Array[FieldSystemMetaData]):  [Read-Write] Commands Meta Data
- ``root_nodes`` (Array[FieldNodeBase]):  [Read-Write] Commands Root Node
- ``target_names`` (Array[Name]):  [Read-Write] Commands Target Name

<a id="unreal.FieldObjectCommands.__init__"></a>

#### \_\_init\_\_

```python
def __init__(target_names: Array[Name] = [],
             root_nodes: Array[FieldNodeBase] = [],
             meta_datas: Array[FieldSystemMetaData] = []) -> None
```

<a id="unreal.FieldObjectCommands.target_names"></a>

#### target\_names

```python
@property
def target_names() -> Array[Name]
```

(Array[Name]):  [Read-Write] Commands Target Name

<a id="unreal.FieldObjectCommands.target_names"></a>

#### target\_names

```python
@target_names.setter
def target_names(value: Array[Name]) -> None
```

<a id="unreal.FieldObjectCommands.root_nodes"></a>

#### root\_nodes

```python
@property
def root_nodes() -> Array[FieldNodeBase]
```

(Array[FieldNodeBase]):  [Read-Write] Commands Root Node

<a id="unreal.FieldObjectCommands.root_nodes"></a>

#### root\_nodes

```python
@root_nodes.setter
def root_nodes(value: Array[FieldNodeBase]) -> None
```

<a id="unreal.FieldObjectCommands.meta_datas"></a>

#### meta\_datas

```python
@property
def meta_datas() -> Array[FieldSystemMetaData]
```

(Array[FieldSystemMetaData]):  [Read-Write] Commands Meta Data

<a id="unreal.FieldObjectCommands.meta_datas"></a>

#### meta\_datas

```python
@meta_datas.setter
def meta_datas(value: Array[FieldSystemMetaData]) -> None
```

<a id="unreal.ChaosBreakingEventRequestSettings"></a>