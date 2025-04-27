## BaseComponent Objects

```python
class BaseComponent(ActorComponent)
```

* 1、UCLASS: 这是 Unreal Engine 的宏，用于声明一个 UClass（Unreal Class）。UClass 是 Unreal Engine 类系统的核心，它用于声明可以在引擎中使用的类。在这个宏之后，您可以列出一系列的属性和修饰符，以定义这个类的行为。
* 2、Blueprintable 和 BlueprintType: 这些是元标记（meta tag），用于标记这个类可用于蓝图编辑器。Blueprintable 表示这个类可以用于创建蓝图（Blueprint），BlueprintType 表示这个类可以被蓝图引用和操作。
* 3、abstract: 这个关键字表示这个类是抽象类，不能直接实例化。抽象类通常用于定义通用的行为和属性，而具体的子类才可以被实例化。在 Unreal Engine 中，抽象类通常用于创建一组相关的子类，而不是单独的实例。
* 4、ClassGroup: 这是一个自定义的类分组标记，用于在 Unreal Engine 编辑器中组织和分类类。这可以帮助开发者更容易地浏览和管理不同类型的类。
* 5、meta: 这是 Unreal Engine 元标记的开头，用于设置类的元数据。在这里，BlueprintSpawnableComponent 是一个元数据，它告诉引擎这个类可以在蓝图中生成为可放置的组件。
// UCLASS(Blueprintable, BlueprintType, abstract, ClassGroup = (Custom), meta = (BlueprintSpawnableComponent))

**C++ Source:**

- **Plugin**: SunFunctionLibrary
- **Module**: BaseTypeTrain
- **File**: BaseComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``function_name`` (Name):  [Read-Write] * 蓝图方法名称
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``name`` (str):  [Read-Write]
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``ower`` (Actor):  [Read-Write] Ower
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``tag_array`` (Array[Name]):  [Read-Write]

<a id="unreal.BaseComponent.ower"></a>

#### ower

```python
@property
def ower() -> Actor
```

(Actor):  [Read-Write] Ower

<a id="unreal.BaseComponent.ower"></a>

#### ower

```python
@ower.setter
def ower(value: Actor) -> None
```

<a id="unreal.BaseComponent.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write]

<a id="unreal.BaseComponent.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.BaseComponent.tag_array"></a>

#### tag_array

```python
@property
def tag_array() -> Array[Name]
```

(Array[Name]):  [Read-Write]

<a id="unreal.BaseComponent.tag_array"></a>

#### tag_array

```python
@tag_array.setter
def tag_array(value: Array[Name]) -> None
```

<a id="unreal.BaseComponent.function_name"></a>

#### function_name

```python
@property
def function_name() -> Name
```

(Name):  [Read-Write] * 蓝图方法名称

<a id="unreal.BaseComponent.function_name"></a>

#### function_name

```python
@function_name.setter
def function_name(value: Name) -> None
```

<a id="unreal.BaseComponent.get_box_center"></a>

#### get_box_center

```python
def get_box_center() -> Vector
```

x.get_box_center() -> Vector
Get Box Center

Returns:
    Vector:

<a id="unreal.BaseEum"></a>