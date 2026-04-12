## EarthOutputFunctionLibrary Objects

```python
class EarthOutputFunctionLibrary(BlueprintFunctionLibrary)
```

输出函数库

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthOutputFunctionLibrary.h

<a id="unreal.EarthOutputFunctionLibrary.set_static_mesh_random_feature_id"></a>

#### set\_static\_mesh\_random\_feature\_id

```python
@classmethod
def set_static_mesh_random_feature_id(
        cls, static_mesh_component: StaticMeshComponent) -> None
```

X.set_static_mesh_random_feature_id(static_mesh_component) -> None
使用静态网格体组件的ObjectID作为特征ID

Args:
    static_mesh_component (StaticMeshComponent):

<a id="unreal.EarthOutputFunctionLibrary.set_static_mesh_feature_id"></a>

#### set\_static\_mesh\_feature\_id

```python
@classmethod
def set_static_mesh_feature_id(cls, static_mesh_component: StaticMeshComponent,
                               feature_id: int) -> None
```

X.set_static_mesh_feature_id(static_mesh_component, feature_id) -> None
为静态网格体组件设置特征ID

Args:
    static_mesh_component (StaticMeshComponent): 
    feature_id (int32):

<a id="unreal.EarthOutputFunctionLibrary.set_instance_random_feature_id"></a>

#### set\_instance\_random\_feature\_id

```python
@classmethod
def set_instance_random_feature_id(cls,
                                   ismc: InstancedStaticMeshComponent,
                                   clear_custom_data: bool = True) -> None
```

X.set_instance_random_feature_id(ismc, clear_custom_data=True) -> None
给实例化静态网格体设置随机特征ID

Args:
    ismc (InstancedStaticMeshComponent): 
    clear_custom_data (bool):

<a id="unreal.EarthOutputFunctionLibrary.set_instance_feature_id"></a>

#### set\_instance\_feature\_id

```python
@classmethod
def set_instance_feature_id(cls,
                            ismc: InstancedStaticMeshComponent,
                            feature_id: int,
                            clear_custom_data: bool = True) -> None
```

X.set_instance_feature_id(ismc, feature_id, clear_custom_data=True) -> None
为静态网格体组件设置特征ID

Args:
    ismc (InstancedStaticMeshComponent): 
    feature_id (int32): 
    clear_custom_data (bool):

<a id="unreal.EarthOutputFunctionLibrary.create_texture"></a>

#### create\_texture

```python
@classmethod
def create_texture(
    cls, render_target2d_fragment: EarthRenderTarget2DFragment
) -> EarthRenderTarget2DFragment
```

X.create_texture(render_target2d_fragment) -> EarthRenderTarget2DFragment
创建材质

Args:
    render_target2d_fragment (EarthRenderTarget2DFragment): 

Returns:
    EarthRenderTarget2DFragment: 

    render_target2d_fragment (EarthRenderTarget2DFragment):

<a id="unreal.EarthOutputFunctionLibrary.copy_properties_from_primitive_component_class"></a>

#### copy\_properties\_from\_primitive\_component\_class

```python
@classmethod
def copy_properties_from_primitive_component_class(
        cls, target_component: PrimitiveComponent,
        source_class: Class) -> None
```

X.copy_properties_from_primitive_component_class(target_component, source_class) -> None
复制源偏远组件类的属性到目标片元组件

Args:
    target_component (PrimitiveComponent): 
    source_class (type(Class)):

<a id="unreal.EarthOutputFunctionLibrary.copy_primitive_component_properties"></a>

#### copy\_primitive\_component\_properties

```python
@classmethod
def copy_primitive_component_properties(
        cls, target_component: PrimitiveComponent,
        source_component: PrimitiveComponent) -> None
```

X.copy_primitive_component_properties(target_component, source_component) -> None
复制源片元组件属性到目标片元组件

Args:
    target_component (PrimitiveComponent): 
    source_component (PrimitiveComponent):

<a id="unreal.EarthPlotPrefabAlgorithm"></a>