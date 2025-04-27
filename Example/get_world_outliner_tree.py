import unreal

def get_world_outliner_tree():
    """获取世界大纲视图的目录树结构"""
    # 获取编辑器世界
    editor_world = unreal.UnrealEditorSubsystem().get_editor_world()
    
    # 获取所有Actor
    all_actors = unreal.EditorLevelLibrary.get_all_level_actors()
    
    # 构建目录树结构
    tree = {}
    for actor in all_actors:
        # 获取Actor的文件夹路径
        folder_path = actor.get_folder_path()
        path_parts = str(folder_path).split('/') if folder_path else []
        
        # 构建树结构
        current_level = tree
        for part in path_parts:
            if part not in current_level:
                current_level[part] = {}
            current_level = current_level[part]
        
        # 添加Actor到当前层级
        actor_name = actor.get_name()
        current_level[actor_name] = actor
    
    return tree

def print_tree(node, indent=0):
    """打印目录树结构"""
    for key, value in node.items():
        print(' ' * indent + '- ' + key)
        if isinstance(value, dict):
            print_tree(value, indent + 2)

if __name__ == "__main__":
    outliner_tree = get_world_outliner_tree()
    print_tree(outliner_tree)
