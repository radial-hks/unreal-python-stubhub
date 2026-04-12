## ModelerEntityInfo Objects

```python
class ModelerEntityInfo(StructBase)
```

Modeler Entity Info

**C++ Source:**

- **Plugin**: AesModeler
- **Module**: AesModeler
- **File**: UrbanEntityModelerActor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_classes`` (Array[type(Class)]):  [Read-Write]
- ``property_strings`` (Array[str]):  [Read-Write]

<a id="unreal.ModelerEntityInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(entity_classes: Array[Class] = [],
             property_strings: Array[str] = []) -> None
```

<a id="unreal.ModelerEntityInfo.entity_classes"></a>

#### entity\_classes

```python
@property
def entity_classes() -> Array[Class]
```

(Array[type(Class)]):  [Read-Write]

<a id="unreal.ModelerEntityInfo.entity_classes"></a>

#### entity\_classes

```python
@entity_classes.setter
def entity_classes(value: Array[Class]) -> None
```

<a id="unreal.ModelerEntityInfo.property_strings"></a>

#### property\_strings

```python
@property
def property_strings() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.ModelerEntityInfo.property_strings"></a>

#### property\_strings

```python
@property_strings.setter
def property_strings(value: Array[str]) -> None
```

<a id="unreal.TAPythonPrimitiveHitResult"></a>