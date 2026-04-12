## WdpCommonInput Objects

```python
class WdpCommonInput(ActorComponent)
```

Wdp Common Input

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpCommonInput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active_common_input`` (bool):  [Read-Write] 是否激活事件发送 可临时禁用
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``auto_bind_when_possessed`` (bool):  [Read-Write] 是否在在被控时启用自动绑定
- ``auto_unbind_when_un_possessed`` (bool):  [Read-Write] 是否在在不被控时启用自动解除绑定
- ``broadcast_when_not_possessed`` (bool):  [Read-Write] 如果不受控制，是否也要广播输入
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``ia_on_any_key_rotate_value_updated`` (OnAnyKeyRotateValueUpdated):  [Read-Write]
- ``ia_on_pointer_key_double_clicked`` (OnPointerKeyDoubleClicked):  [Read-Write]
- ``ia_on_pointer_key_pressed`` (OnPointerKeyPressed):  [Read-Write]
- ``ia_on_pointer_key_released`` (OnPointerKeyReleased):  [Read-Write]
- ``ia_on_pointer_key_rotate_value_updated`` (OnPointerKeyRotateValueUpdated):  [Read-Write]
- ``ia_on_pointer_key_triggered`` (OnPointerKeyTriggered):  [Read-Write]
- ``ia_on_remote_move_key_updated`` (RemoteMoveKeyTriggered):  [Read-Write]
- ``ia_on_rotate_key_pressed`` (OnRotateKeyPressed):  [Read-Write]
- ``ia_on_rotate_key_released`` (OnRotateKeyReleased):  [Read-Write]
- ``ia_on_rotate_key_triggered`` (OnRotateKeyTriggered):  [Read-Write]
- ``ia_on_rotate_key_value_updated`` (OnRotateKeyValueUpdated):  [Read-Write]
- ``ia_on_zoom_key_pressed`` (OnZoomKeyPressed):  [Read-Write]
- ``ia_on_zoom_key_released`` (OnZoomKeyReleased):  [Read-Write]
- ``ia_on_zoom_key_triggered`` (OnZoomKeyTriggered):  [Read-Write]
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_control_mode_changed`` (OnControlModeChanged):  [Read-Write]
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.WdpCommonInput.ia_on_pointer_key_pressed"></a>

#### ia\_on\_pointer\_key\_pressed

```python
@property
def ia_on_pointer_key_pressed() -> OnPointerKeyPressed
```

(OnPointerKeyPressed):  [Read-Write]

<a id="unreal.WdpCommonInput.ia_on_pointer_key_pressed"></a>

#### ia\_on\_pointer\_key\_pressed

```python
@ia_on_pointer_key_pressed.setter
def ia_on_pointer_key_pressed(value: OnPointerKeyPressed) -> None
```

<a id="unreal.WdpCommonInput.ia_on_pointer_key_triggered"></a>

#### ia\_on\_pointer\_key\_triggered

```python
@property
def ia_on_pointer_key_triggered() -> OnPointerKeyTriggered
```

(OnPointerKeyTriggered):  [Read-Write]

<a id="unreal.WdpCommonInput.ia_on_pointer_key_triggered"></a>

#### ia\_on\_pointer\_key\_triggered

```python
@ia_on_pointer_key_triggered.setter
def ia_on_pointer_key_triggered(value: OnPointerKeyTriggered) -> None
```

<a id="unreal.WdpCommonInput.ia_on_pointer_key_released"></a>

#### ia\_on\_pointer\_key\_released

```python
@property
def ia_on_pointer_key_released() -> OnPointerKeyReleased
```

(OnPointerKeyReleased):  [Read-Write]

<a id="unreal.WdpCommonInput.ia_on_pointer_key_released"></a>

#### ia\_on\_pointer\_key\_released

```python
@ia_on_pointer_key_released.setter
def ia_on_pointer_key_released(value: OnPointerKeyReleased) -> None
```

<a id="unreal.WdpCommonInput.ia_on_pointer_key_double_clicked"></a>

#### ia\_on\_pointer\_key\_double\_clicked

```python
@property
def ia_on_pointer_key_double_clicked() -> OnPointerKeyDoubleClicked
```

(OnPointerKeyDoubleClicked):  [Read-Write]

<a id="unreal.WdpCommonInput.ia_on_pointer_key_double_clicked"></a>

#### ia\_on\_pointer\_key\_double\_clicked

```python
@ia_on_pointer_key_double_clicked.setter
def ia_on_pointer_key_double_clicked(value: OnPointerKeyDoubleClicked) -> None
```

<a id="unreal.WdpCommonInput.ia_on_pointer_key_rotate_value_updated"></a>

#### ia\_on\_pointer\_key\_rotate\_value\_updated

```python
@property
def ia_on_pointer_key_rotate_value_updated() -> OnPointerKeyRotateValueUpdated
```

(OnPointerKeyRotateValueUpdated):  [Read-Write]

<a id="unreal.WdpCommonInput.ia_on_pointer_key_rotate_value_updated"></a>

#### ia\_on\_pointer\_key\_rotate\_value\_updated

```python
@ia_on_pointer_key_rotate_value_updated.setter
def ia_on_pointer_key_rotate_value_updated(
        value: OnPointerKeyRotateValueUpdated) -> None
```

<a id="unreal.WdpCommonInput.ia_on_rotate_key_pressed"></a>

#### ia\_on\_rotate\_key\_pressed

```python
@property
def ia_on_rotate_key_pressed() -> OnRotateKeyPressed
```

(OnRotateKeyPressed):  [Read-Write]

<a id="unreal.WdpCommonInput.ia_on_rotate_key_pressed"></a>

#### ia\_on\_rotate\_key\_pressed

```python
@ia_on_rotate_key_pressed.setter
def ia_on_rotate_key_pressed(value: OnRotateKeyPressed) -> None
```

<a id="unreal.WdpCommonInput.ia_on_rotate_key_triggered"></a>

#### ia\_on\_rotate\_key\_triggered

```python
@property
def ia_on_rotate_key_triggered() -> OnRotateKeyTriggered
```

(OnRotateKeyTriggered):  [Read-Write]

<a id="unreal.WdpCommonInput.ia_on_rotate_key_triggered"></a>

#### ia\_on\_rotate\_key\_triggered

```python
@ia_on_rotate_key_triggered.setter
def ia_on_rotate_key_triggered(value: OnRotateKeyTriggered) -> None
```

<a id="unreal.WdpCommonInput.ia_on_rotate_key_released"></a>

#### ia\_on\_rotate\_key\_released

```python
@property
def ia_on_rotate_key_released() -> OnRotateKeyReleased
```

(OnRotateKeyReleased):  [Read-Write]

<a id="unreal.WdpCommonInput.ia_on_rotate_key_released"></a>

#### ia\_on\_rotate\_key\_released

```python
@ia_on_rotate_key_released.setter
def ia_on_rotate_key_released(value: OnRotateKeyReleased) -> None
```

<a id="unreal.WdpCommonInput.ia_on_rotate_key_value_updated"></a>

#### ia\_on\_rotate\_key\_value\_updated

```python
@property
def ia_on_rotate_key_value_updated() -> OnRotateKeyValueUpdated
```

(OnRotateKeyValueUpdated):  [Read-Write]

<a id="unreal.WdpCommonInput.ia_on_rotate_key_value_updated"></a>

#### ia\_on\_rotate\_key\_value\_updated

```python
@ia_on_rotate_key_value_updated.setter
def ia_on_rotate_key_value_updated(value: OnRotateKeyValueUpdated) -> None
```

<a id="unreal.WdpCommonInput.ia_on_any_key_rotate_value_updated"></a>

#### ia\_on\_any\_key\_rotate\_value\_updated

```python
@property
def ia_on_any_key_rotate_value_updated() -> OnAnyKeyRotateValueUpdated
```

(OnAnyKeyRotateValueUpdated):  [Read-Write]

<a id="unreal.WdpCommonInput.ia_on_any_key_rotate_value_updated"></a>

#### ia\_on\_any\_key\_rotate\_value\_updated

```python
@ia_on_any_key_rotate_value_updated.setter
def ia_on_any_key_rotate_value_updated(
        value: OnAnyKeyRotateValueUpdated) -> None
```

<a id="unreal.WdpCommonInput.ia_on_zoom_key_pressed"></a>

#### ia\_on\_zoom\_key\_pressed

```python
@property
def ia_on_zoom_key_pressed() -> OnZoomKeyPressed
```

(OnZoomKeyPressed):  [Read-Write]

<a id="unreal.WdpCommonInput.ia_on_zoom_key_pressed"></a>

#### ia\_on\_zoom\_key\_pressed

```python
@ia_on_zoom_key_pressed.setter
def ia_on_zoom_key_pressed(value: OnZoomKeyPressed) -> None
```

<a id="unreal.WdpCommonInput.ia_on_zoom_key_triggered"></a>

#### ia\_on\_zoom\_key\_triggered

```python
@property
def ia_on_zoom_key_triggered() -> OnZoomKeyTriggered
```

(OnZoomKeyTriggered):  [Read-Write]

<a id="unreal.WdpCommonInput.ia_on_zoom_key_triggered"></a>

#### ia\_on\_zoom\_key\_triggered

```python
@ia_on_zoom_key_triggered.setter
def ia_on_zoom_key_triggered(value: OnZoomKeyTriggered) -> None
```

<a id="unreal.WdpCommonInput.ia_on_zoom_key_released"></a>

#### ia\_on\_zoom\_key\_released

```python
@property
def ia_on_zoom_key_released() -> OnZoomKeyReleased
```

(OnZoomKeyReleased):  [Read-Write]

<a id="unreal.WdpCommonInput.ia_on_zoom_key_released"></a>

#### ia\_on\_zoom\_key\_released

```python
@ia_on_zoom_key_released.setter
def ia_on_zoom_key_released(value: OnZoomKeyReleased) -> None
```

<a id="unreal.WdpCommonInput.ia_on_remote_move_key_updated"></a>

#### ia\_on\_remote\_move\_key\_updated

```python
@property
def ia_on_remote_move_key_updated() -> RemoteMoveKeyTriggered
```

(RemoteMoveKeyTriggered):  [Read-Write]

<a id="unreal.WdpCommonInput.ia_on_remote_move_key_updated"></a>

#### ia\_on\_remote\_move\_key\_updated

```python
@ia_on_remote_move_key_updated.setter
def ia_on_remote_move_key_updated(value: RemoteMoveKeyTriggered) -> None
```

<a id="unreal.WdpCommonInput.on_control_mode_changed"></a>

#### on\_control\_mode\_changed

```python
@property
def on_control_mode_changed() -> OnControlModeChanged
```

(OnControlModeChanged):  [Read-Write]

<a id="unreal.WdpCommonInput.on_control_mode_changed"></a>

#### on\_control\_mode\_changed

```python
@on_control_mode_changed.setter
def on_control_mode_changed(value: OnControlModeChanged) -> None
```

<a id="unreal.WdpCommonInput.broadcast_when_not_possessed"></a>

#### broadcast\_when\_not\_possessed

```python
@property
def broadcast_when_not_possessed() -> bool
```

(bool):  [Read-Write] 如果不受控制，是否也要广播输入

<a id="unreal.WdpCommonInput.broadcast_when_not_possessed"></a>

#### broadcast\_when\_not\_possessed

```python
@broadcast_when_not_possessed.setter
def broadcast_when_not_possessed(value: bool) -> None
```

<a id="unreal.WdpCommonInput.auto_bind_when_possessed"></a>

#### auto\_bind\_when\_possessed

```python
@property
def auto_bind_when_possessed() -> bool
```

(bool):  [Read-Write] 是否在在被控时启用自动绑定

<a id="unreal.WdpCommonInput.auto_bind_when_possessed"></a>

#### auto\_bind\_when\_possessed

```python
@auto_bind_when_possessed.setter
def auto_bind_when_possessed(value: bool) -> None
```

<a id="unreal.WdpCommonInput.auto_unbind_when_un_possessed"></a>

#### auto\_unbind\_when\_un\_possessed

```python
@property
def auto_unbind_when_un_possessed() -> bool
```

(bool):  [Read-Write] 是否在在不被控时启用自动解除绑定

<a id="unreal.WdpCommonInput.auto_unbind_when_un_possessed"></a>

#### auto\_unbind\_when\_un\_possessed

```python
@auto_unbind_when_un_possessed.setter
def auto_unbind_when_un_possessed(value: bool) -> None
```

<a id="unreal.WdpCommonInput.active_common_input"></a>

#### active\_common\_input

```python
@property
def active_common_input() -> bool
```

(bool):  [Read-Write] 是否激活事件发送 可临时禁用

<a id="unreal.WdpCommonInput.active_common_input"></a>

#### active\_common\_input

```python
@active_common_input.setter
def active_common_input(value: bool) -> None
```

<a id="unreal.WdpCommonInput.un_bind_common_input_event"></a>

#### un\_bind\_common\_input\_event

```python
def un_bind_common_input_event(wdp_controller: WdpPlayerController) -> bool
```

x.un_bind_common_input_event(wdp_controller) -> bool
解除绑定输入事件

Args:
    wdp_controller (WdpPlayerController): 

Returns:
    bool:

<a id="unreal.WdpCommonInput.toggle_common_input_active"></a>

#### toggle\_common\_input\_active

```python
def toggle_common_input_active(active: bool) -> None
```

x.toggle_common_input_active(active) -> None
切换激活Common Input

Args:
    active (bool):

<a id="unreal.WdpCommonInput.should_broadcast_input_event"></a>

#### should\_broadcast\_input\_event

```python
def should_broadcast_input_event() -> bool
```

x.should_broadcast_input_event() -> bool
检测是否允许发送事件

Returns:
    bool:

<a id="unreal.WdpCommonInput.init_common_input_comp"></a>

#### init\_common\_input\_comp

```python
def init_common_input_comp() -> None
```

x.init_common_input_comp() -> None
初始化组件

<a id="unreal.WdpCommonInput.get_owning_wdp_player_controller"></a>

#### get\_owning\_wdp\_player\_controller

```python
def get_owning_wdp_player_controller() -> WdpPlayerController
```

x.get_owning_wdp_player_controller() -> WdpPlayerController
尝试获取OwningActor的PlayerController，如果没有被控制或基类不是Pawn，则使用默认的0

Returns:
    WdpPlayerController:

<a id="unreal.WdpCommonInput.get_current_control_mode"></a>

#### get\_current\_control\_mode

```python
def get_current_control_mode() -> ControlMode
```

x.get_current_control_mode() -> ControlMode
获取当前的Control Mode

Returns:
    ControlMode:

<a id="unreal.WdpCommonInput.clean_common_input_comp"></a>

#### clean\_common\_input\_comp

```python
def clean_common_input_comp() -> None
```

x.clean_common_input_comp() -> None
结束初始化组件

<a id="unreal.WdpCommonInput.bind_common_input_event"></a>

#### bind\_common\_input\_event

```python
def bind_common_input_event(wdp_controller: WdpPlayerController) -> bool
```

x.bind_common_input_event(wdp_controller) -> bool
绑定输入事件

Args:
    wdp_controller (WdpPlayerController): 

Returns:
    bool:

<a id="unreal.WdpGameModeBase"></a>