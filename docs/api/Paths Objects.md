## Paths Objects

```python
class Paths(BlueprintFunctionLibrary)
```

Function library to expose FPaths to Blueprints and Python

Function signatures are preserved for the most part with adjustments made to some
signatures to better match Blueprints / Python workflow

**C++ Source:**

- **Module**: Engine
- **File**: BlueprintPathsLibrary.h

<a id="unreal.Paths.video_capture_dir"></a>

#### video\_capture\_dir

```python
@classmethod
def video_capture_dir(cls) -> str
```

X.video_capture_dir() -> str
Returns the directory the engine uses to output user requested video capture files.

Returns:
    str: Video capture directory

<a id="unreal.Paths.validate_path"></a>

#### validate\_path

```python
@classmethod
def validate_path(cls, path: str) -> Tuple[bool, Text]
```

X.validate_path(path) -> (did_succeed=bool, out_reason=Text)
Validates that the parts that make up the path contain no invalid characters as dictated by the operating system
Note that this is a different set of restrictions to those imposed by FPackageName

Args:
    path (str): path to validate

Returns:
    tuple: 

    did_succeed (bool): Whether the path could be validated

    out_reason (Text): If validation fails, this is filled with the failure reason

<a id="unreal.Paths.split"></a>

#### split

```python
@classmethod
def split(cls, path: str) -> Tuple[str, str, str]
```

X.split(path) -> (path_part=str, filename_part=str, extension_part=str)
Parses a fully qualified or relative filename into its components (filename, path, extension).

Args:
    path (str): 

Returns:
    tuple: 

    path_part (str): 

    filename_part (str): 

    extension_part (str):

<a id="unreal.Paths.source_config_dir"></a>

#### source\_config\_dir

```python
@classmethod
def source_config_dir(cls) -> str
```

X.source_config_dir() -> str
Returns the directory the engine uses to look for the source leaf ini files. This
can't be an .ini variable for obvious reasons.

Returns:
    str: source config directory

<a id="unreal.Paths.should_save_to_user_dir"></a>

#### should\_save\_to\_user\_dir

```python
@classmethod
def should_save_to_user_dir(cls) -> bool
```

X.should_save_to_user_dir() -> bool
Should the "saved" directory structures be rooted in the user dir or relative to the "engine/game"

Returns:
    bool:

<a id="unreal.Paths.shader_working_dir"></a>

#### shader\_working\_dir

```python
@classmethod
def shader_working_dir(cls) -> str
```

X.shader_working_dir() -> str
Returns the Shader Working Directory

Returns:
    str: shader working directory

<a id="unreal.Paths.set_project_file_path"></a>

#### set\_project\_file\_path

```python
@classmethod
def set_project_file_path(cls, new_game_project_file_path: str) -> None
```

X.set_project_file_path(new_game_project_file_path) -> None
Sets the path to the project file.

Args:
    new_game_project_file_path (str): The project file path to set.

<a id="unreal.Paths.set_extension"></a>

#### set\_extension

```python
@classmethod
def set_extension(cls, path: str, new_extension: str) -> str
```

X.set_extension(path, new_extension) -> str
Sets the extension of the given filename (like ChangeExtension, but also applies the extension if the file doesn't have one)

Args:
    path (str): 
    new_extension (str): 

Returns:
    str:

<a id="unreal.Paths.screen_shot_dir"></a>

#### screen\_shot\_dir

```python
@classmethod
def screen_shot_dir(cls) -> str
```

X.screen_shot_dir() -> str
Returns the directory the engine uses to output screenshot files.

Returns:
    str: screenshot directory

<a id="unreal.Paths.sandboxes_dir"></a>

#### sandboxes\_dir

```python
@classmethod
def sandboxes_dir(cls) -> str
```

X.sandboxes_dir() -> str
Returns the directory the engine stores sandbox output

Returns:
    str: sandbox directory

<a id="unreal.Paths.root_dir"></a>

#### root\_dir

```python
@classmethod
def root_dir(cls) -> str
```

X.root_dir() -> str
Returns the root directory of the engine directory tree

Returns:
    str: Root directory.

<a id="unreal.Paths.remove_duplicate_slashes"></a>

#### remove\_duplicate\_slashes

```python
@classmethod
def remove_duplicate_slashes(cls, path: str) -> str
```

X.remove_duplicate_slashes(path) -> str
Removes duplicate slashes in paths.
Assumes all slashes have been converted to TEXT('/').
For example, takes the string:
      BaseDirectory/SomeDirectory//SomeOtherDirectory////Filename.ext
and converts it to:
      BaseDirectory/SomeDirectory/SomeOtherDirectory/Filename.ext

Args:
    path (str): 

Returns:
    str: 

    out_path (str):

<a id="unreal.Paths.project_user_dir"></a>

#### project\_user\_dir

```python
@classmethod
def project_user_dir(cls) -> str
```

X.project_user_dir() -> str
Returns the root directory for user-specific game files.

Returns:
    str: game user directory

<a id="unreal.Paths.project_saved_dir"></a>

#### project\_saved\_dir

```python
@classmethod
def project_saved_dir(cls) -> str
```

X.project_saved_dir() -> str
Returns the saved directory of the current game by looking at FApp::GetProjectName().

Returns:
    str: saved directory

<a id="unreal.Paths.project_plugins_dir"></a>

#### project\_plugins\_dir

```python
@classmethod
def project_plugins_dir(cls) -> str
```

X.project_plugins_dir() -> str
Returns the plugins directory of the current game by looking at FApp::GetProjectName().

Returns:
    str: plugins directory

<a id="unreal.Paths.project_persistent_download_dir"></a>

#### project\_persistent\_download\_dir

```python
@classmethod
def project_persistent_download_dir(cls) -> str
```

X.project_persistent_download_dir() -> str
* Returns the writable directory for downloaded data that persists across play sessions.

Returns:
    str:

<a id="unreal.Paths.project_mods_dir"></a>

#### project\_mods\_dir

```python
@classmethod
def project_mods_dir(cls) -> str
```

X.project_mods_dir() -> str
Returns the mods directory of the current project by looking at FApp::GetProjectName().

Returns:
    str: mods directory

<a id="unreal.Paths.project_log_dir"></a>

#### project\_log\_dir

```python
@classmethod
def project_log_dir(cls) -> str
```

X.project_log_dir() -> str
Returns the directory the engine uses to output logs. This currently can't
be an .ini setting as the game starts logging before it can read from .ini
files.

Returns:
    str: log directory

<a id="unreal.Paths.project_intermediate_dir"></a>

#### project\_intermediate\_dir

```python
@classmethod
def project_intermediate_dir(cls) -> str
```

X.project_intermediate_dir() -> str
Returns the intermediate directory of the current game by looking at FApp::GetProjectName().

Returns:
    str: intermediate directory

<a id="unreal.Paths.project_dir"></a>

#### project\_dir

```python
@classmethod
def project_dir(cls) -> str
```

X.project_dir() -> str
Returns the base directory of the current project by looking at FApp::GetProjectName().
This is usually a subdirectory of the installation
root directory and can be overridden on the command line to allow self
contained mod support.

Returns:
    str: base directory

<a id="unreal.Paths.project_content_dir"></a>

#### project\_content\_dir

```python
@classmethod
def project_content_dir(cls) -> str
```

X.project_content_dir() -> str
Returns the content directory of the current game by looking at FApp::GetProjectName().

Returns:
    str: content directory

<a id="unreal.Paths.project_config_dir"></a>

#### project\_config\_dir

```python
@classmethod
def project_config_dir(cls) -> str
```

X.project_config_dir() -> str
Returns the directory the root configuration files are located.

Returns:
    str: root config directory

<a id="unreal.Paths.profiling_dir"></a>

#### profiling\_dir

```python
@classmethod
def profiling_dir(cls) -> str
```

X.profiling_dir() -> str
Returns the directory the engine uses to output profiling files.

Returns:
    str: log directory

<a id="unreal.Paths.normalize_filename"></a>

#### normalize\_filename

```python
@classmethod
def normalize_filename(cls, path: str) -> str
```

X.normalize_filename(path) -> str
Convert all / and \ to TEXT("/")

Args:
    path (str): 

Returns:
    str: 

    out_path (str):

<a id="unreal.Paths.normalize_directory_name"></a>

#### normalize\_directory\_name

```python
@classmethod
def normalize_directory_name(cls, path: str) -> str
```

X.normalize_directory_name(path) -> str
Normalize all / and \ to TEXT("/") and remove any trailing TEXT("/") if the character before that is not a TEXT("/") or a colon

Args:
    path (str): 

Returns:
    str: 

    out_path (str):

<a id="unreal.Paths.make_valid_file_name"></a>

#### make\_valid\_file\_name

```python
@classmethod
def make_valid_file_name(cls, string: str, replacement_char: str = "") -> str
```

X.make_valid_file_name(string, replacement_char="") -> str
Returns a string that is safe to use as a filename because all items in
GetInvalidFileSystemChars() are removed

Optionally specify the character to replace invalid characters with

Args:
    string (str): 
    replacement_char (str): 

Returns:
    str:

<a id="unreal.Paths.make_standard_filename"></a>

#### make\_standard\_filename

```python
@classmethod
def make_standard_filename(cls, path: str) -> str
```

X.make_standard_filename(path) -> str
Make fully standard "Unreal" pathname:
   - Normalizes path separators [NormalizeFilename]
   - Removes extraneous separators  [NormalizeDirectoryName, as well removing adjacent separators]
   - Collapses internal ..'s
   - Makes relative to Engine\Binaries\<Platform> (will ALWAYS start with ..\..\..)

Args:
    path (str): 

Returns:
    str: 

    out_path (str):

<a id="unreal.Paths.make_platform_filename"></a>

#### make\_platform\_filename

```python
@classmethod
def make_platform_filename(cls, path: str) -> str
```

X.make_platform_filename(path) -> str
Takes an "Unreal" pathname and converts it to a platform filename.

Args:
    path (str): 

Returns:
    str: 

    out_path (str):

<a id="unreal.Paths.make_path_relative_to"></a>

#### make\_path\_relative\_to

```python
@classmethod
def make_path_relative_to(cls, path: str, relative_to: str) -> Optional[str]
```

X.make_path_relative_to(path, relative_to) -> str or None
Assuming both paths (or filenames) are relative to the same base dir, converts InPath to be relative to InRelativeTo

Args:
    path (str): Path to change to be relative to InRelativeTo
    relative_to (str): Path to use as the new relative base

Returns:
    str or None: true if OutPath was changed to be relative

    out_path (str):

<a id="unreal.Paths.launch_dir"></a>

#### launch\_dir

```python
@classmethod
def launch_dir(cls) -> str
```

X.launch_dir() -> str
Returns the directory the application was launched from (useful for commandline utilities)

Returns:
    str:

<a id="unreal.Paths.is_same_path"></a>

#### is\_same\_path

```python
@classmethod
def is_same_path(cls, path_a: str, path_b: str) -> bool
```

X.is_same_path(path_a, path_b) -> bool
Checks if two paths are the same.

Args:
    path_a (str): First path to check.
    path_b (str): Second path to check.

Returns:
    bool: True if both paths are the same. False otherwise.

<a id="unreal.Paths.is_restricted_path"></a>

#### is\_restricted\_path

```python
@classmethod
def is_restricted_path(cls, path: str) -> bool
```

X.is_restricted_path(path) -> bool
Determines if supplied path uses a restricted/internal subdirectory.  Note that slashes are normalized and character case is ignored for the comparison.

Args:
    path (str): 

Returns:
    bool:

<a id="unreal.Paths.is_relative"></a>

#### is\_relative

```python
@classmethod
def is_relative(cls, path: str) -> bool
```

X.is_relative(path) -> bool
Returns true if this path is relative to another path

Args:
    path (str): 

Returns:
    bool:

<a id="unreal.Paths.is_project_file_path_set"></a>

#### is\_project\_file\_path\_set

```python
@classmethod
def is_project_file_path_set(cls) -> bool
```

X.is_project_file_path_set() -> bool
Checks whether the path to the project file, if any, is set.

Returns:
    bool: true if the path is set, false otherwise.

<a id="unreal.Paths.is_drive"></a>

#### is\_drive

```python
@classmethod
def is_drive(cls, path: str) -> bool
```

X.is_drive(path) -> bool
Returns true if this path represents a root drive or volume

Args:
    path (str): 

Returns:
    bool:

<a id="unreal.Paths.has_project_persistent_download_dir"></a>

#### has\_project\_persistent\_download\_dir

```python
@classmethod
def has_project_persistent_download_dir(cls) -> bool
```

X.has_project_persistent_download_dir() -> bool
* Returns true if a writable directory for downloaded data that persists across play sessions is available

Returns:
    bool:

<a id="unreal.Paths.get_tool_tip_localization_paths"></a>

#### get\_tool\_tip\_localization\_paths

```python
@classmethod
def get_tool_tip_localization_paths(cls) -> Array[str]
```

X.get_tool_tip_localization_paths() -> Array[str]
Returns a list of tool tip localization paths

Returns:
    Array[str]:

<a id="unreal.Paths.get_restricted_folder_names"></a>

#### get\_restricted\_folder\_names

```python
@classmethod
def get_restricted_folder_names(cls) -> Array[str]
```

X.get_restricted_folder_names() -> Array[str]
Returns a list of restricted/internal folder names (without any slashes) which may be tested against full paths to determine if a path is restricted or not.

Returns:
    Array[str]:

<a id="unreal.Paths.get_relative_path_to_root"></a>

#### get\_relative\_path\_to\_root

```python
@classmethod
def get_relative_path_to_root(cls) -> str
```

X.get_relative_path_to_root() -> str
Gets the relative path to get from BaseDir to RootDirectory

Returns:
    str:

<a id="unreal.Paths.get_property_name_localization_paths"></a>

#### get\_property\_name\_localization\_paths

```python
@classmethod
def get_property_name_localization_paths(cls) -> Array[str]
```

X.get_property_name_localization_paths() -> Array[str]
Returns a list of property name localization paths

Returns:
    Array[str]:

<a id="unreal.Paths.get_project_file_path"></a>

#### get\_project\_file\_path

```python
@classmethod
def get_project_file_path(cls) -> str
```

X.get_project_file_path() -> str
Gets the path to the project file.

Returns:
    str: Project file path.

<a id="unreal.Paths.get_path"></a>

#### get\_path

```python
@classmethod
def get_path(cls, path: str) -> str
```

X.get_path(path) -> str
Returns the path in front of the filename

Args:
    path (str): 

Returns:
    str:

<a id="unreal.Paths.get_invalid_file_system_chars"></a>

#### get\_invalid\_file\_system\_chars

```python
@classmethod
def get_invalid_file_system_chars(cls) -> str
```

X.get_invalid_file_system_chars() -> str
Returns a string containing all invalid characters as dictated by the operating system

Returns:
    str:

<a id="unreal.Paths.get_game_localization_paths"></a>

#### get\_game\_localization\_paths

```python
@classmethod
def get_game_localization_paths(cls) -> Array[str]
```

X.get_game_localization_paths() -> Array[str]
Returns a list of game-specific localization paths

Returns:
    Array[str]:

<a id="unreal.Paths.get_extension"></a>

#### get\_extension

```python
@classmethod
def get_extension(cls, path: str, include_dot: bool = False) -> str
```

X.get_extension(path, include_dot=False) -> str
Gets the extension for this filename.

Args:
    path (str): 
    include_dot (bool): if true, includes the leading dot in the result

Returns:
    str: the extension of this filename, or an empty string if the filename doesn't have an extension.

<a id="unreal.Paths.get_engine_localization_paths"></a>

#### get\_engine\_localization\_paths

```python
@classmethod
def get_engine_localization_paths(cls) -> Array[str]
```

X.get_engine_localization_paths() -> Array[str]
Returns a list of engine-specific localization paths

Returns:
    Array[str]:

<a id="unreal.Paths.get_editor_localization_paths"></a>

#### get\_editor\_localization\_paths

```python
@classmethod
def get_editor_localization_paths(cls) -> Array[str]
```

X.get_editor_localization_paths() -> Array[str]
Returns a list of editor-specific localization paths

Returns:
    Array[str]:

<a id="unreal.Paths.get_clean_filename"></a>

#### get\_clean\_filename

```python
@classmethod
def get_clean_filename(cls, path: str) -> str
```

X.get_clean_filename(path) -> str
Returns the filename (with extension), minus any path information.

Args:
    path (str): 

Returns:
    str:

<a id="unreal.Paths.get_base_filename"></a>

#### get\_base\_filename

```python
@classmethod
def get_base_filename(cls, path: str, remove_path: bool = True) -> str
```

X.get_base_filename(path, remove_path=True) -> str
Returns the same thing as GetCleanFilename, but without the extension

Args:
    path (str): 
    remove_path (bool): 

Returns:
    str:

<a id="unreal.Paths.generated_config_dir"></a>

#### generated\_config\_dir

```python
@classmethod
def generated_config_dir(cls) -> str
```

X.generated_config_dir() -> str
Returns the directory the engine saves generated config files.

Returns:
    str: config directory

<a id="unreal.Paths.game_user_developer_dir"></a>

#### game\_user\_developer\_dir

```python
@classmethod
def game_user_developer_dir(cls) -> str
```

X.game_user_developer_dir() -> str
Returns the directory that contains developer-specific content for the current user

Returns:
    str:

<a id="unreal.Paths.game_source_dir"></a>

#### game\_source\_dir

```python
@classmethod
def game_source_dir(cls) -> str
```

X.game_source_dir() -> str
Returns the directory where game source code files are kept

Returns:
    str:

<a id="unreal.Paths.game_developers_dir"></a>

#### game\_developers\_dir

```python
@classmethod
def game_developers_dir(cls) -> str
```

X.game_developers_dir() -> str
Returns the directory that contains subfolders for developer-specific content

Returns:
    str:

<a id="unreal.Paths.game_agnostic_saved_dir"></a>

#### game\_agnostic\_saved\_dir

```python
@classmethod
def game_agnostic_saved_dir(cls) -> str
```

X.game_agnostic_saved_dir() -> str
Returns the saved directory that is not game specific. This is usually the same as
EngineSavedDir().

Returns:
    str: saved directory

<a id="unreal.Paths.file_exists"></a>

#### file\_exists

```python
@classmethod
def file_exists(cls, path: str) -> bool
```

X.file_exists(path) -> bool
Returns true if this file was found, false otherwise

Args:
    path (str): 

Returns:
    bool:

<a id="unreal.Paths.feature_pack_dir"></a>

#### feature\_pack\_dir

```python
@classmethod
def feature_pack_dir(cls) -> str
```

X.feature_pack_dir() -> str
Returns the directory where feature packs are kept

Returns:
    str:

<a id="unreal.Paths.enterprise_plugins_dir"></a>

#### enterprise\_plugins\_dir

```python
@classmethod
def enterprise_plugins_dir(cls) -> str
```

X.enterprise_plugins_dir() -> str
Returns the enterprise plugins directory

Returns:
    str: Plugins directory.

<a id="unreal.Paths.enterprise_feature_pack_dir"></a>

#### enterprise\_feature\_pack\_dir

```python
@classmethod
def enterprise_feature_pack_dir(cls) -> str
```

X.enterprise_feature_pack_dir() -> str
Returns the enterprise FeaturePack directory

Returns:
    str: FeaturePack directory.

<a id="unreal.Paths.enterprise_dir"></a>

#### enterprise\_dir

```python
@classmethod
def enterprise_dir(cls) -> str
```

X.enterprise_dir() -> str
Returns the base directory enterprise directory.

Returns:
    str: enterprise directory

<a id="unreal.Paths.engine_version_agnostic_user_dir"></a>

#### engine\_version\_agnostic\_user\_dir

```python
@classmethod
def engine_version_agnostic_user_dir(cls) -> str
```

X.engine_version_agnostic_user_dir() -> str
Returns the root directory for user-specific engine files which can be shared between versions. Always writable.

Returns:
    str: root user directory

<a id="unreal.Paths.engine_user_dir"></a>

#### engine\_user\_dir

```python
@classmethod
def engine_user_dir(cls) -> str
```

X.engine_user_dir() -> str
Returns the root directory for user-specific engine files. Always writable.

Returns:
    str: root user directory

<a id="unreal.Paths.engine_source_dir"></a>

#### engine\_source\_dir

```python
@classmethod
def engine_source_dir(cls) -> str
```

X.engine_source_dir() -> str
Returns the directory where engine source code files are kept

Returns:
    str:

<a id="unreal.Paths.engine_saved_dir"></a>

#### engine\_saved\_dir

```python
@classmethod
def engine_saved_dir(cls) -> str
```

X.engine_saved_dir() -> str
Returns the saved directory of the engine

Returns:
    str: Saved directory.

<a id="unreal.Paths.engine_plugins_dir"></a>

#### engine\_plugins\_dir

```python
@classmethod
def engine_plugins_dir(cls) -> str
```

X.engine_plugins_dir() -> str
Returns the plugins directory of the engine

Returns:
    str: Plugins directory.

<a id="unreal.Paths.engine_intermediate_dir"></a>

#### engine\_intermediate\_dir

```python
@classmethod
def engine_intermediate_dir(cls) -> str
```

X.engine_intermediate_dir() -> str
Returns the intermediate directory of the engine

Returns:
    str: content directory

<a id="unreal.Paths.engine_dir"></a>

#### engine\_dir

```python
@classmethod
def engine_dir(cls) -> str
```

X.engine_dir() -> str
Returns the base directory of the "core" engine that can be shared across
several games or across games & mods. Shaders and base localization files
e.g. reside in the engine directory.

Returns:
    str: engine directory

<a id="unreal.Paths.engine_content_dir"></a>

#### engine\_content\_dir

```python
@classmethod
def engine_content_dir(cls) -> str
```

X.engine_content_dir() -> str
Returns the content directory of the "core" engine that can be shared across
several games or across games & mods.

Returns:
    str: engine content directory

<a id="unreal.Paths.engine_config_dir"></a>

#### engine\_config\_dir

```python
@classmethod
def engine_config_dir(cls) -> str
```

X.engine_config_dir() -> str
Returns the directory the root configuration files are located.

Returns:
    str: root config directory

<a id="unreal.Paths.directory_exists"></a>

#### directory\_exists

```python
@classmethod
def directory_exists(cls, path: str) -> bool
```

X.directory_exists(path) -> bool
Returns true if this directory was found, false otherwise

Args:
    path (str): 

Returns:
    bool:

<a id="unreal.Paths.diff_dir"></a>

#### diff\_dir

```python
@classmethod
def diff_dir(cls) -> str
```

X.diff_dir() -> str
Returns the directory for temp files used for diffing

Returns:
    str:

<a id="unreal.Paths.create_temp_filename"></a>

#### create\_temp\_filename

```python
@classmethod
def create_temp_filename(cls,
                         path: str,
                         prefix: str = "",
                         extension: str = ".tmp") -> str
```

X.create_temp_filename(path, prefix="", extension=".tmp") -> str
Creates a temporary filename with the specified prefix.

Args:
    path (str): The file pathname.
    prefix (str): The file prefix.
    extension (str): File extension ('.' required).

Returns:
    str:

<a id="unreal.Paths.convert_to_sandbox_path"></a>

#### convert\_to\_sandbox\_path

```python
@classmethod
def convert_to_sandbox_path(cls, path: str, sandbox_name: str) -> str
```

X.convert_to_sandbox_path(path, sandbox_name) -> str
Converts a normal path to a sandbox path (in Saved/Sandboxes).

Args:
    path (str): 
    sandbox_name (str): The name of the sandbox.

Returns:
    str:

<a id="unreal.Paths.convert_relative_path_to_full"></a>

#### convert\_relative\_path\_to\_full

```python
@classmethod
def convert_relative_path_to_full(cls, path: str, base_path: str = "") -> str
```

X.convert_relative_path_to_full(path, base_path="") -> str
Converts a relative path name to a fully qualified name relative to the specified BasePath.
BasePath will be the process BaseDir() if not BasePath is given

Args:
    path (str): 
    base_path (str): 

Returns:
    str:

<a id="unreal.Paths.convert_from_sandbox_path"></a>

#### convert\_from\_sandbox\_path

```python
@classmethod
def convert_from_sandbox_path(cls, path: str, sandbox_name: str) -> str
```

X.convert_from_sandbox_path(path, sandbox_name) -> str
Converts a sandbox (in Saved/Sandboxes) path to a normal path.

Args:
    path (str): 
    sandbox_name (str): The name of the sandbox.

Returns:
    str:

<a id="unreal.Paths.combine"></a>

#### combine

```python
@classmethod
def combine(cls, paths: Array[str]) -> str
```

X.combine(paths) -> str
Combine two or more Paths into one single Path

Args:
    paths (Array[str]): 

Returns:
    str:

<a id="unreal.Paths.collapse_relative_directories"></a>

#### collapse\_relative\_directories

```python
@classmethod
def collapse_relative_directories(cls, path: str) -> Optional[str]
```

X.collapse_relative_directories(path) -> str or None
Takes a fully pathed string and eliminates relative pathing (eg: annihilates ".." with the adjacent directory).
Assumes all slashes have been converted to TEXT('/').
For example, takes the string:
      BaseDirectory/SomeDirectory/../SomeOtherDirectory/Filename.ext
and converts it to:
      BaseDirectory/SomeOtherDirectory/Filename.ext

Args:
    path (str): 

Returns:
    str or None: 

    out_path (str):

<a id="unreal.Paths.cloud_dir"></a>

#### cloud\_dir

```python
@classmethod
def cloud_dir(cls) -> str
```

X.cloud_dir() -> str
Returns the directory for local files used in cloud emulation or support

Returns:
    str:

<a id="unreal.Paths.change_extension"></a>

#### change\_extension

```python
@classmethod
def change_extension(cls, path: str, new_extension: str) -> str
```

X.change_extension(path, new_extension) -> str
Changes the extension of the given filename (does nothing if the file has no extension)

Args:
    path (str): 
    new_extension (str): 

Returns:
    str:

<a id="unreal.Paths.bug_it_dir"></a>

#### bug\_it\_dir

```python
@classmethod
def bug_it_dir(cls) -> str
```

X.bug_it_dir() -> str
Returns the directory the engine uses to output BugIt files.

Returns:
    str: screenshot directory

<a id="unreal.Paths.automation_transient_dir"></a>

#### automation\_transient\_dir

```python
@classmethod
def automation_transient_dir(cls) -> str
```

X.automation_transient_dir() -> str
Returns the directory for automation save files that are meant to be deleted every run

Returns:
    str:

<a id="unreal.Paths.automation_log_dir"></a>

#### automation\_log\_dir

```python
@classmethod
def automation_log_dir(cls) -> str
```

X.automation_log_dir() -> str
Returns the directory for automation log files

Returns:
    str:

<a id="unreal.Paths.automation_dir"></a>

#### automation\_dir

```python
@classmethod
def automation_dir(cls) -> str
```

X.automation_dir() -> str
Returns the directory for automation save files

Returns:
    str:

<a id="unreal.PlatformGameInstance"></a>