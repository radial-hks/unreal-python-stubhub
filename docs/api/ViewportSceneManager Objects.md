## ViewportSceneManager Objects

```python
class ViewportSceneManager(Object)
```

Viewport Scene Manager

**C++ Source:**

- **Plugin**: CustomProgram
- **Module**: CustomProgram
- **File**: ViewportSceneManager.h

<a id="unreal.ViewportSceneManager.save_viewport_scene_ext_parm"></a>

#### save\_viewport\_scene\_ext\_parm

```python
def save_viewport_scene_ext_parm(author: str, name: str, date: str,
                                 camera_roam_list: str, camera: str,
                                 weather_data: str) -> bool
```

x.save_viewport_scene_ext_parm(author, name, date, camera_roam_list, camera, weather_data) -> bool
Save Viewport Scene Ext Parm

Args:
    author (str): 
    name (str): 
    date (str): 
    camera_roam_list (str): 
    camera (str): 
    weather_data (str): 

Returns:
    bool:

<a id="unreal.ViewportSceneManager.new_viewport_scene"></a>

#### new\_viewport\_scene

```python
def new_viewport_scene(author: str, name: str, time: str) -> ViewportScene
```

x.new_viewport_scene(author, name, time) -> ViewportScene
New Viewport Scene

Args:
    author (str): 
    name (str): 
    time (str): 

Returns:
    ViewportScene:

<a id="unreal.ViewportSceneManager.local_player_shallow_copy"></a>

#### local\_player\_shallow\_copy

```python
@classmethod
def local_player_shallow_copy(cls, from_local_player: LocalPlayer,
                              to_local_player: LocalPlayer) -> None
```

X.local_player_shallow_copy(from_local_player, to_local_player) -> None
Local Player Shallow Copy

Args:
    from_local_player (LocalPlayer): 
    to_local_player (LocalPlayer):

<a id="unreal.ViewportSceneManager.get_viewport_scene_by_id"></a>

#### get\_viewport\_scene\_by\_id

```python
def get_viewport_scene_by_id(viewport_scene_id: Name) -> ViewportScene
```

x.get_viewport_scene_by_id(viewport_scene_id) -> ViewportScene
Get Viewport Scene by Id

Args:
    viewport_scene_id (Name): 

Returns:
    ViewportScene:

<a id="unreal.ViewportSceneManager.get_local_viewport_scene_file_list"></a>

#### get\_local\_viewport\_scene\_file\_list

```python
def get_local_viewport_scene_file_list(author: str,
                                       name: str,
                                       data: str = "") -> Array[str]
```

x.get_local_viewport_scene_file_list(author, name, data="") -> Array[str]
Get Local Viewport Scene File List

Args:
    author (str): 
    name (str): 
    data (str): 

Returns:
    Array[str]:

<a id="unreal.ViewportSceneManager.get"></a>

#### get

```python
@classmethod
def get(cls) -> ViewportSceneManager
```

X.get() -> ViewportSceneManager
Get

Returns:
    ViewportSceneManager:

<a id="unreal.ViewportSceneManager.delete_viewport_scene_by_name"></a>

#### delete\_viewport\_scene\_by\_name

```python
def delete_viewport_scene_by_name(author: str, scene_file_name: str) -> bool
```

x.delete_viewport_scene_by_name(author, scene_file_name) -> bool
Delete Viewport Scene by Name

Args:
    author (str): 
    scene_file_name (str): 

Returns:
    bool:

<a id="unreal.ViewportSceneManager.create_split_screen_four_grid"></a>

#### create\_split\_screen\_four\_grid

```python
def create_split_screen_four_grid(author1: str, scene_file_name1: str,
                                  author2: str, scene_file_name2: str,
                                  author3: str, scene_file_name3: str,
                                  author4: str, scene_file_name4: str) -> bool
```

x.create_split_screen_four_grid(author1, scene_file_name1, author2, scene_file_name2, author3, scene_file_name3, author4, scene_file_name4) -> bool
Create Split Screen Four Grid

Args:
    author1 (str): 
    scene_file_name1 (str): 
    author2 (str): 
    scene_file_name2 (str): 
    author3 (str): 
    scene_file_name3 (str): 
    author4 (str): 
    scene_file_name4 (str): 

Returns:
    bool:

<a id="unreal.ViewportSceneManager.create_split_screen"></a>

#### create\_split\_screen

```python
def create_split_screen(author1: str, scene_file_name1: str, author2: str,
                        scene_file_name2: str) -> bool
```

x.create_split_screen(author1, scene_file_name1, author2, scene_file_name2) -> bool
Create Split Screen

Args:
    author1 (str): 
    scene_file_name1 (str): 
    author2 (str): 
    scene_file_name2 (str): 

Returns:
    bool:

<a id="unreal.ViewportSceneManager.create_and_set_local_player"></a>

#### create\_and\_set\_local\_player

```python
@classmethod
def create_and_set_local_player(
        cls, world_context_object: Object, local_player_class: Class,
        player_index: int, create_new_player_controller: bool,
        bind_to_other_player_index: int) -> LocalPlayer
```

X.create_and_set_local_player(world_context_object, local_player_class, player_index, create_new_player_controller, bind_to_other_player_index) -> LocalPlayer
Create and Set Local Player

Args:
    world_context_object (Object): 
    local_player_class (type(Class)): 
    player_index (int32): 
    create_new_player_controller (bool): 
    bind_to_other_player_index (int32): 

Returns:
    LocalPlayer: 

    local_player (LocalPlayer):

<a id="unreal.ViewportSceneManager.close_viewport_scenes"></a>

#### close\_viewport\_scenes

```python
def close_viewport_scenes() -> bool
```

x.close_viewport_scenes() -> bool
Close Viewport Scenes

Returns:
    bool:

<a id="unreal.ViewportSceneManager.check_viewport_scene"></a>

#### check\_viewport\_scene

```python
def check_viewport_scene(author: str, name: str, time: str) -> bool
```

x.check_viewport_scene(author, name, time) -> bool
Check Viewport Scene

Args:
    author (str): 
    name (str): 
    time (str): 

Returns:
    bool:

<a id="unreal.ViewportSceneManager.check_repeat_player_index"></a>

#### check\_repeat\_player\_index

```python
def check_repeat_player_index(player_index: int) -> bool
```

x.check_repeat_player_index(player_index) -> bool
Check Repeat Player Index

Args:
    player_index (int32): 

Returns:
    bool:

<a id="unreal.ViewportSceneManager.activate_splite_index"></a>

#### activate\_splite\_index

```python
def activate_splite_index(player_index: int, is_acticate: bool) -> None
```

x.activate_splite_index(player_index, is_acticate) -> None
Activate Splite Index

Args:
    player_index (int32): 
    is_acticate (bool):

<a id="unreal.LaunchExternalExeLib"></a>