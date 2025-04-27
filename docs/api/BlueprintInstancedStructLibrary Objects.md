## BlueprintInstancedStructLibrary Objects

```python
class BlueprintInstancedStructLibrary(BlueprintFunctionLibrary)
```

Blueprint Instanced Struct Library

**C++ Source:**

- **Module**: Engine
- **File**: BlueprintInstancedStructLibrary.h

<a id="unreal.BlueprintInstancedStructLibrary.reset"></a>

#### reset

```python
@classmethod
def reset(cls,
          instanced_struct: InstancedStruct,
          struct_type: ScriptStruct = None) -> InstancedStruct
```

X.reset(instanced_struct, struct_type=None) -> InstancedStruct
Resets an InstancedStruct.

Args:
    instanced_struct (InstancedStruct): 
    struct_type (ScriptStruct): 

Returns:
    InstancedStruct: 

    instanced_struct (InstancedStruct):

<a id="unreal.BlueprintInstancedStructLibrary.not_equal_instanced_struct"></a>

#### not_equal_instanced_struct

```python
@classmethod
def not_equal_instanced_struct(cls, a: InstancedStruct,
                               b: InstancedStruct) -> bool
```

X.not_equal_instanced_struct(a, b) -> bool
Checks whether two InstancedStructs are not equal.

Args:
    a (InstancedStruct): 
    b (InstancedStruct): 

Returns:
    bool:

<a id="unreal.BlueprintInstancedStructLibrary.is_valid_instanced_struct"></a>

#### is_valid_instanced_struct

```python
@classmethod
def is_valid_instanced_struct(cls, instanced_struct: InstancedStruct) -> bool
```

X.is_valid_instanced_struct(instanced_struct) -> bool
Checks whether the InstancedStruct contains value.

Args:
    instanced_struct (InstancedStruct): 

Returns:
    bool:

<a id="unreal.BlueprintInstancedStructLibrary.is_instanced_struct_valid"></a>

#### is_instanced_struct_valid

```python
@classmethod
def is_instanced_struct_valid(
        cls, instanced_struct: InstancedStruct) -> StructUtilsResult
```

X.is_instanced_struct_valid(instanced_struct) -> StructUtilsResult
Checks whether an InstancedStruct contains value.

Args:
    instanced_struct (InstancedStruct): 

Returns:
    StructUtilsResult:

<a id="unreal.BlueprintInstancedStructLibrary.equal_equal_instanced_struct"></a>

#### equal_equal_instanced_struct

```python
@classmethod
def equal_equal_instanced_struct(cls, a: InstancedStruct,
                                 b: InstancedStruct) -> bool
```

X.equal_equal_instanced_struct(a, b) -> bool
Checks whether two InstancedStructs (and the values contained within) are equal.

Args:
    a (InstancedStruct): 
    b (InstancedStruct): 

Returns:
    bool:

<a id="unreal.StructUtilsFunctionLibrary"></a>