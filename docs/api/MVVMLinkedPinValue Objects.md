## MVVMLinkedPinValue Objects

```python
class MVVMLinkedPinValue(StructBase)
```

MVVMLinked Pin Value

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModelEditor
- **File**: MVVMLinkedPinValue.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``conversion_function`` (Function):  [Read-Write]
- ``conversion_node`` (type(Class)):  [Read-Write]
- ``property_path`` (MVVMBlueprintPropertyPath):  [Read-Write]

<a id="unreal.MVVMLinkedPinValue.__init__"></a>

#### __init__

```python
def __init__(property_path: MVVMBlueprintPropertyPath = [],
             conversion_function: Function = None,
             conversion_node: Class = None) -> None
```

<a id="unreal.MVVMLinkedPinValue.property_path"></a>

#### property_path

```python
@property
def property_path() -> MVVMBlueprintPropertyPath
```

(MVVMBlueprintPropertyPath):  [Read-Write]

<a id="unreal.MVVMLinkedPinValue.property_path"></a>

#### property_path

```python
@property_path.setter
def property_path(value: MVVMBlueprintPropertyPath) -> None
```

<a id="unreal.MVVMLinkedPinValue.conversion_function"></a>

#### conversion_function

```python
@property
def conversion_function() -> Function
```

(Function):  [Read-Write]

<a id="unreal.MVVMLinkedPinValue.conversion_function"></a>

#### conversion_function

```python
@conversion_function.setter
def conversion_function(value: Function) -> None
```

<a id="unreal.MVVMLinkedPinValue.conversion_node"></a>

#### conversion_node

```python
@property
def conversion_node() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.MVVMLinkedPinValue.conversion_node"></a>

#### conversion_node

```python
@conversion_node.setter
def conversion_node(value: Class) -> None
```

<a id="unreal.DisplayClusterWarpGeometryPFM"></a>