## StructBase Objects

```python
class StructBase(_WrapperBase)
```

Type for all Unreal exposed struct instances

<a id="unreal.StructBase.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.StructBase._post_init"></a>

#### _post_init

```python
def _post_init() -> None
```

_post_init(self) -> None -- called during Unreal struct initialization (equivalent to PostInitProperties in C++)

<a id="unreal.StructBase.cast"></a>

#### cast

```python
@classmethod
def cast(cls: Type[_T], object: Union[object, Mapping[str, object],
                                      Iterable[object]]) -> _T
```

cast(cls: Type[_T], object: Union[object, Mapping[str, object], Iterable[object]]) -> _T -- cast the given object to this Unreal struct type. Can be partial Mapping[fieldName, fiedValue] or a sequence of field values

<a id="unreal.StructBase.static_struct"></a>

#### static_struct

```python
@classmethod
def static_struct(cls) -> ScriptStruct
```

static_struct(cls) -> ScriptStruct -- get the Unreal struct of this type

<a id="unreal.StructBase.__copy__"></a>

#### __copy__

```python
def __copy__() -> Any
```

__copy__(self) -> Any -- copy this Unreal struct

<a id="unreal.StructBase.copy"></a>

#### copy

```python
def copy() -> Any
```

copy(self) -> Any -- copy this Unreal struct

<a id="unreal.StructBase.assign"></a>

#### assign

```python
def assign(other: object) -> None
```

assign(self, other: object) -> None -- assign the value of this Unreal struct to value of the given object

<a id="unreal.StructBase.to_tuple"></a>

#### to_tuple

```python
def to_tuple() -> Tuple[object, ...]
```

to_tuple(self) -> Tuple[object, ...] -- break this Unreal struct into a tuple of its properties

<a id="unreal.StructBase.get_editor_property"></a>

#### get_editor_property

```python
def get_editor_property(name: Union[Name, str]) -> object
```

get_editor_property(self, name: Union[Name, str]) -> object -- get the value of any property visible to the editor

<a id="unreal.StructBase.set_editor_property"></a>

#### set_editor_property

```python
def set_editor_property(
    name: Union[Name, str],
    value: object,
    notify_mode: PropertyAccessChangeNotifyMode = PropertyAccessChangeNotifyMode
    .DEFAULT
) -> None
```

set_editor_property(self, name: Union[Name, str], value: object, notify_mode: PropertyAccessChangeNotifyMode=PropertyAccessChangeNotifyMode.DEFAULT) -> None -- set the value of any property visible to the editor, ensuring that the pre/post change notifications are called

<a id="unreal.StructBase.set_editor_properties"></a>

#### set_editor_properties

```python
def set_editor_properties(properties: Mapping[str, object]) -> None
```

set_editor_properties(self, properties: Mapping[str, object]) -> None -- set the value of any properties visible to the editor (from a name->value dict), ensuring that the pre/post change notifications are called

<a id="unreal.StructBase.export_text"></a>

#### export_text

```python
def export_text() -> str
```

export_text(self) -> str -- exports the content of the Unreal struct of this type

<a id="unreal.StructBase.import_text"></a>

#### import_text

```python
def import_text(content: str) -> bool
```

import_text(self, content: str) -> bool -- imports the provided string into the Unreal struct

<a id="unreal.EnumBase"></a>