## EditorPerProjectUserSettings Objects

```python
class EditorPerProjectUserSettings(Object)
```

Editor Per Project User Settings

**C++ Source:**

- **Module**: UnrealEd
- **File**: EditorPerProjectUserSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``always_build_uat`` (bool):  [Read-Write] Always build UAT\UBT before launching the game. It will decrease iteration times if disabled
- ``always_gather_behavior_tree_debugger_data`` (bool):  [Read-Write] If enabled, behavior tree debugger will collect its data even when all behavior tree editor windows are closed
- ``animation_reimport_warnings`` (bool):  [Read-Write] If enabled, will compare an animation's sequence length and curves against the old data and inform the user if something changed
- ``automatically_hot_reload_new_classes`` (bool):  [Read-Write] If enabled, any newly added classes will be automatically compiled and trigger a hot-reload of the module they were added to
- ``confirm_editor_close`` (bool):  [Read-Write] If enabled, you'll be asked to confirm if you really want to close the editor.
- ``data_source_folder`` (DirectoryPath):  [Read-Write] Specify a project data source folder to store relative source file path to ease the re-import process
- ``display_blackboard_keys_in_alphabetical_order`` (bool):  [Read-Write] If enabled, blackboard keys displayed in blackboard editor and key selector will be sorted in alphabetical order .
- ``display_documentation_link`` (bool):  [Read-Write] If enabled, tooltips linked to documentation will show the developer the link bound to that UI item
- ``display_engine_version_in_badge`` (bool):  [Read-Write] When enabled, Engine Version Number is displayed in the ProjectBadge
- ``display_ui_extension_points`` (bool):  [Read-Write] If enabled, any newly opened UI menus, menu bars, and toolbars will show the developer hooks that would accept extensions
- ``enable_swarm_debugging`` (bool):  [Read-Write] Enable swarm debugging features. Temp ssf files are not removed. Detailed message printing
- ``get_attention_on_uat_completion`` (bool):  [Read-Write] If enabled, the Editor will attempt to get the users attention whenever a UAT task (such as cooking or packaging) is completed
- ``keep_attach_hierarchy`` (bool):  [Read-Write] If enabled, export level with attachment hierarchy set
- ``keep_fbx_namespace`` (bool):  [Read-Write] If enabled, the fbx parser will keep the fbx namespaces, otherwise the namespace will be append to fbx node.
- ``show_compiler_log_on_compile_error`` (bool):  [Read-Write] If enabled, the compile message log window will open if there is a compiler error on Hot Reload
- ``show_import_dialog_at_reimport`` (bool):  [Read-Write] If enabled, the fbx option dialog will show when user re-import a fbx
- ``simplygon_server_ip`` (str):  [Read-Write] Server IP for the distributed Simplygon server
- ``simplygon_swarm_delay`` (uint32):  [Read-Write] Time between JSON net requests for Simplygon Swarm
- ``swarm_intermediate_folder`` (str):  [Read-Write] Folder in which Simplygon Swarm will store intermediate texture and mesh data that is uploaded to the Swarm
- ``swarm_max_upload_chunk_size_in_mb`` (uint32):  [Read-Write]
- ``swarm_num_of_concurrent_jobs`` (uint32):  [Read-Write] Number of concurrent swarm jobs to execute. This is independent of the main job queue.
- ``use_simplygon_swarm`` (bool):  [Read-Write] When enabled, use SimplygonSwarm Module / server to create proxies

<a id="unreal.EditorUserSettings"></a>