## CustomProgramLibrary Objects

```python
class CustomProgramLibrary(BlueprintFunctionLibrary)
```

Custom Program Library

**C++ Source:**

- **Plugin**: CustomProgram
- **Module**: CustomProgram
- **File**: CustomProgramLibrary.h

<a id="unreal.CustomProgramLibrary.set_program_model"></a>

#### set\_program\_model

```python
@classmethod
def set_program_model(cls, scene_id: str, bind_actor: Actor, eid: str,
                      model_id: str, visible: bool,
                      is_remove: bool) -> Optional[str]
```

X.set_program_model(scene_id, bind_actor, eid, model_id, visible, is_remove) -> str or None
Set Program Model

Args:
    scene_id (str): 
    bind_actor (Actor): 
    eid (str): 
    model_id (str): 
    visible (bool): 
    is_remove (bool): 

Returns:
    str or None: 

    res (str):

<a id="unreal.CustomProgramLibrary.set_build_visible_by_eid"></a>

#### set\_build\_visible\_by\_eid

```python
@classmethod
def set_build_visible_by_eid(cls, scene_file_name: str, author: str, time: str,
                             eid: str, visible: bool) -> str
```

X.set_build_visible_by_eid(scene_file_name, author, time, eid, visible) -> str
Set Build Visible by EID

Args:
    scene_file_name (str): 
    author (str): 
    time (str): 
    eid (str): 
    visible (bool): 

Returns:
    str: 

    res (str):

<a id="unreal.CustomProgramLibrary.set_build_visible_by_actor"></a>

#### set\_build\_visible\_by\_actor

```python
@classmethod
def set_build_visible_by_actor(cls, scene_id: str, bind_actor: Actor, eid: str,
                               model_id: str, visible: bool) -> str
```

X.set_build_visible_by_actor(scene_id, bind_actor, eid, model_id, visible) -> str
Set Build Visible by Actor

Args:
    scene_id (str): 
    bind_actor (Actor): 
    eid (str): 
    model_id (str): 
    visible (bool): 

Returns:
    str: 

    res (str):

<a id="unreal.CustomProgramLibrary.save_viewport_scene_by_name"></a>

#### save\_viewport\_scene\_by\_name

```python
@classmethod
def save_viewport_scene_by_name(cls, scene_id: str, camera_roam_list: str,
                                camera: str, weather_data: str) -> bool
```

X.save_viewport_scene_by_name(scene_id, camera_roam_list, camera, weather_data) -> bool
Save Viewport Scene by Name

Args:
    scene_id (str): 
    camera_roam_list (str): 
    camera (str): 
    weather_data (str): 

Returns:
    bool: 

    save_state (bool):

<a id="unreal.CustomProgramLibrary.remove_build_visible_by_actor"></a>

#### remove\_build\_visible\_by\_actor

```python
@classmethod
def remove_build_visible_by_actor(cls, scene_id: str, bind_actor: Actor,
                                  eid: str, model_id: str,
                                  visible: bool) -> str
```

X.remove_build_visible_by_actor(scene_id, bind_actor, eid, model_id, visible) -> str
Remove Build Visible by Actor

Args:
    scene_id (str): 
    bind_actor (Actor): 
    eid (str): 
    model_id (str): 
    visible (bool): 

Returns:
    str: 

    res (str):

<a id="unreal.CustomProgramLibrary.query_viewport_scene"></a>

#### query\_viewport\_scene

```python
@classmethod
def query_viewport_scene(
        cls,
        scene_file: ViewportSceneFileParams) -> Array[ViewportSceneFileParams]
```

X.query_viewport_scene(scene_file) -> Array[ViewportSceneFileParams]
Query Viewport Scene

Args:
    scene_file (ViewportSceneFileParams): 

Returns:
    Array[ViewportSceneFileParams]: 

    file_list (Array[ViewportSceneFileParams]):

<a id="unreal.CustomProgramLibrary.new_viewport_scene"></a>

#### new\_viewport\_scene

```python
@classmethod
def new_viewport_scene(cls, scene_file_name: str, author: str,
                       time: str) -> str
```

X.new_viewport_scene(scene_file_name, author, time) -> str
New Viewport Scene

Args:
    scene_file_name (str): 
    author (str): 
    time (str): 

Returns:
    str: 

    viewport_scene_id (str):

<a id="unreal.CustomProgramLibrary.get_id_array"></a>

#### get\_id\_array

```python
@classmethod
def get_id_array(cls) -> Array[ViewportSceneFileParams]
```

X.get_id_array() -> Array[ViewportSceneFileParams]
Get IDArray

Returns:
    Array[ViewportSceneFileParams]:

<a id="unreal.CustomProgramLibrary.delete_viewport_scene"></a>

#### delete\_viewport\_scene

```python
@classmethod
def delete_viewport_scene(cls, sence_id: str) -> bool
```

X.delete_viewport_scene(sence_id) -> bool
Delete Viewport Scene

Args:
    sence_id (str): 

Returns:
    bool:

<a id="unreal.CustomProgramLibrary.create_split_screen_for_left_right"></a>

#### create\_split\_screen\_for\_left\_right

```python
@classmethod
def create_split_screen_for_left_right(cls, scene_left_id: str,
                                       scene_right_id: str) -> None
```

X.create_split_screen_for_left_right(scene_left_id, scene_right_id) -> None
Create Split Screen for Left Right

Args:
    scene_left_id (str): 
    scene_right_id (str):

<a id="unreal.CustomProgramLibrary.create_split_screen_for_four_grid"></a>

#### create\_split\_screen\_for\_four\_grid

```python
@classmethod
def create_split_screen_for_four_grid(cls, scene_left_top_id: str,
                                      scene_top_right_id: str,
                                      scene_bottom_left_id: str,
                                      scene_bottom_right_id: str) -> None
```

X.create_split_screen_for_four_grid(scene_left_top_id, scene_top_right_id, scene_bottom_left_id, scene_bottom_right_id) -> None
Create Split Screen for Four Grid

Args:
    scene_left_top_id (str): 
    scene_top_right_id (str): 
    scene_bottom_left_id (str): 
    scene_bottom_right_id (str):

<a id="unreal.CustomProgramLibrary.close_viewport_scene"></a>

#### close\_viewport\_scene

```python
@classmethod
def close_viewport_scene(cls) -> str
```

X.close_viewport_scene() -> str
Close Viewport Scene

Returns:
    str: 

    res (str):

<a id="unreal.CustomProgramLibrary.check_viewport_scene"></a>

#### check\_viewport\_scene

```python
@classmethod
def check_viewport_scene(cls, scene_id: str) -> bool
```

X.check_viewport_scene(scene_id) -> bool
Check Viewport Scene

Args:
    scene_id (str): 

Returns:
    bool:

<a id="unreal.CustomProgramLibrary.activate_splite_index"></a>

#### activate\_splite\_index

```python
@classmethod
def activate_splite_index(cls, player_index: int, is_acticate: bool) -> None
```

X.activate_splite_index(player_index, is_acticate) -> None
Activate Splite Index

Args:
    player_index (int32): 
    is_acticate (bool):

<a id="unreal.CustomProgramSubsystem"></a>