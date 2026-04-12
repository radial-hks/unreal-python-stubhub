## EarthDataTypeLibrary Objects

```python
class EarthDataTypeLibrary(BlueprintFunctionLibrary)
```

所有运行时可修改数据的基类的函数库，专为编辑器细节面板和蓝图创建预制体而提供的接口

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthDataTypeLibrary.h

<a id="unreal.EarthDataTypeLibrary.validate_fragment_type"></a>

#### validate\_fragment\_type

```python
@classmethod
def validate_fragment_type(
        cls,
        earth_data: EarthDataBase,
        keep_instanced_structs: bool = True) -> EarthDataBase
```

X.validate_fragment_type(earth_data, keep_instanced_structs=True) -> EarthDataBase
校验片段，专为编辑器细节面板和蓝图创建预制体而提供的接口，能移除相同类型的重复片段，并更新所有片段类型映射，可选择是否保留实例结构体类型的数据片段供Detail面板使用

Args:
    earth_data (EarthDataBase): 
    keep_instanced_structs (bool): 

Returns:
    EarthDataBase: 

    earth_data (EarthDataBase):

<a id="unreal.EarthDataTypeLibrary.type_map_to_fragments"></a>

#### type\_map\_to\_fragments

```python
@classmethod
def type_map_to_fragments(cls, earth_data: EarthDataBase) -> EarthDataBase
```

X.type_map_to_fragments(earth_data) -> EarthDataBase
Type Map to Fragments

Args:
    earth_data (EarthDataBase): 

Returns:
    EarthDataBase: 

    earth_data (EarthDataBase):

<a id="unreal.EarthDataTypeLibrary.remove_fragment"></a>

#### remove\_fragment

```python
@classmethod
def remove_fragment(cls, earth_data: EarthDataBase,
                    struct: ScriptStruct) -> Optional[EarthDataBase]
```

X.remove_fragment(earth_data, struct) -> EarthDataBase or None
移除片段（返回是否成功移除），专为编辑器细节面板和蓝图创建预制体而提供的接口

Args:
    earth_data (EarthDataBase): 
    struct (ScriptStruct): 

Returns:
    EarthDataBase or None: 

    earth_data (EarthDataBase):

<a id="unreal.EarthDataTypeLibrary.on_fragments_changed"></a>

#### on\_fragments\_changed

```python
@classmethod
def on_fragments_changed(cls, earth_data: EarthDataBase) -> EarthDataBase
```

X.on_fragments_changed(earth_data) -> EarthDataBase
当片段数据发生变更时触发处理逻辑，专为编辑器细节面板和蓝图创建预制体而提供的接口

Args:
    earth_data (EarthDataBase): 

Returns:
    EarthDataBase: 

    earth_data (EarthDataBase):

<a id="unreal.EarthDataTypeLibrary.get_fragments_mutable"></a>

#### get\_fragments\_mutable

```python
@classmethod
def get_fragments_mutable(
        cls, earth_data: EarthDataBase
) -> Tuple[Array[InstancedStruct], EarthDataBase]
```

X.get_fragments_mutable(earth_data) -> (Array[InstancedStruct], earth_data=EarthDataBase)
获取可修改的所有片段数据，专为编辑器细节面板和蓝图创建预制体而提供的接口

Args:
    earth_data (EarthDataBase): 

Returns:
    EarthDataBase: 

    earth_data (EarthDataBase):

<a id="unreal.EarthDataTypeLibrary.get_fragments"></a>

#### get\_fragments

```python
@classmethod
def get_fragments(cls, earth_data: EarthDataBase) -> Array[InstancedStruct]
```

X.get_fragments(earth_data) -> Array[InstancedStruct]
获取所有片段数据，专为编辑器细节面板和蓝图创建预制体而提供的接口

Args:
    earth_data (EarthDataBase): 

Returns:
    Array[InstancedStruct]:

<a id="unreal.EarthDataTypeLibrary.get_fragment"></a>

#### get\_fragment

```python
@classmethod
def get_fragment(cls, earth_data: EarthDataBase,
                 struct: ScriptStruct) -> InstancedStruct
```

X.get_fragment(earth_data, struct) -> InstancedStruct
获取指定类型片段的只读引用（不存在则返回默认结构），专为编辑器细节面板和蓝图创建预制体而提供的接口

Args:
    earth_data (EarthDataBase): 
    struct (ScriptStruct): 

Returns:
    InstancedStruct:

<a id="unreal.EarthDataTypeLibrary.get_diff_fragments"></a>

#### get\_diff\_fragments

```python
@classmethod
def get_diff_fragments(cls, earth_data: EarthDataBase,
                       other_data: EarthDataBase) -> Array[InstancedStruct]
```

X.get_diff_fragments(earth_data, other_data) -> Array[InstancedStruct]
获取当前数据与指定数据实例的差异片段数据，专为编辑器细节面板和蓝图创建预制体而提供的接口

Args:
    earth_data (EarthDataBase): 
    other_data (EarthDataBase): 

Returns:
    Array[InstancedStruct]: 

    out_diff_fragments (Array[InstancedStruct]):

<a id="unreal.EarthDataTypeLibrary.copy_to_shared_fragments"></a>

#### copy\_to\_shared\_fragments

```python
@classmethod
def copy_to_shared_fragments(cls, earth_data: EarthDataBase) -> EarthDataBase
```

X.copy_to_shared_fragments(earth_data) -> EarthDataBase
将实例化结构体类型的数据片段转为共享指针类型的数据片段

Args:
    earth_data (EarthDataBase): 

Returns:
    EarthDataBase: 

    earth_data (EarthDataBase):

<a id="unreal.EarthDataTypeLibrary.copy_to_instanced_fragments"></a>

#### copy\_to\_instanced\_fragments

```python
@classmethod
def copy_to_instanced_fragments(cls,
                                earth_data: EarthDataBase) -> EarthDataBase
```

X.copy_to_instanced_fragments(earth_data) -> EarthDataBase
将共享指针类型的数据片段转为实例化结构体类型的数据片段

Args:
    earth_data (EarthDataBase): 

Returns:
    EarthDataBase: 

    earth_data (EarthDataBase):

<a id="unreal.EarthDataTypeLibrary.append_fragments"></a>

#### append\_fragments

```python
@classmethod
def append_fragments(cls, earth_data: EarthDataBase,
                     fragments: Array[InstancedStruct]) -> EarthDataBase
```

X.append_fragments(earth_data, fragments) -> EarthDataBase
批量添加若干指定片段，专为编辑器细节面板和蓝图创建预制体而提供的接口

Args:
    earth_data (EarthDataBase): 
    fragments (Array[InstancedStruct]): 

Returns:
    EarthDataBase: 

    earth_data (EarthDataBase):

<a id="unreal.EarthDataTypeLibrary.add_or_replace_fragment"></a>

#### add\_or\_replace\_fragment

```python
@classmethod
def add_or_replace_fragment(
        cls, earth_data: EarthDataBase,
        fragment: InstancedStruct) -> Optional[EarthDataBase]
```

X.add_or_replace_fragment(earth_data, fragment) -> EarthDataBase or None
添加新片段（返回是否成功添加），专为编辑器细节面板和蓝图创建预制体而提供的接口

Args:
    earth_data (EarthDataBase): 
    fragment (InstancedStruct): 

Returns:
    EarthDataBase or None: 

    earth_data (EarthDataBase):

<a id="unreal.EarthDataTypeLibrary.add_fragment"></a>

#### add\_fragment

```python
@classmethod
def add_fragment(cls, earth_data: InstancedStruct,
                 fragment: InstancedStruct) -> Optional[InstancedStruct]
```

X.add_fragment(earth_data, fragment) -> InstancedStruct or None
添加新片段（返回是否成功添加），专为编辑器细节面板和蓝图创建预制体而提供的接口

Args:
    earth_data (InstancedStruct): 
    fragment (InstancedStruct): 

Returns:
    InstancedStruct or None: 

    earth_data (InstancedStruct):

<a id="unreal.EarthDynamicMeshFunctionLibrary"></a>