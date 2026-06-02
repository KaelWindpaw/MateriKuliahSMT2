class FileNode:
    """Representasi satu entitas (Folder atau File) dalam sistem"""
    def __init__(self, name, is_folder=True):
        self.name = name
        self.is_folder = is_folder
        self.children = [] # List untuk menyimpan anak-anak (Sub-folder/File)

class FileSystemTree:
    """Implementasi General Tree untuk Manajemen Folder"""
    def __init__(self):
        # Inisialisasi Root sebagai folder utama
        self.root = FileNode("C:", is_folder=True)

    def add_node(self, parent_name, child_name, is_folder=True):
        """Menemukan parent berdasarkan nama dan menambahkan anak baru"""
        parent_node = self._find_node(self.root, parent_name)
        if parent_node and parent_node.is_folder:
            # Cek apakah sudah ada anak dengan nama yang sama
            if not any(child.name == child_name for child in parent_node.children):
                new_node = FileNode(child_name, is_folder)
                parent_node.children.append(new_node)
                return True
        return False

    def _find_node(self, current_node, target_name):
        """Pencarian node secara rekursif (Depth-First Search)"""
        if current_node.name == target_name:
            return current_node
        
        for child in current_node.children:
            found = self._find_node(child, target_name)
            if found:
                return found
        return None

    def get_all_folders(self):
        """Mengambil semua daftar folder untuk opsi input di UI"""
        folders = []
        self._collect_folders(self.root, folders)
        return folders

    def _collect_folders(self, current_node, folders):
        if current_node.is_folder:
            folders.append(current_node.name)
            for child in current_node.children:
                self._collect_folders(child, folders)

    def get_structure(self, current_node=None):
        """Mengambil data struktur untuk visualisasi graphviz"""
        if current_node is None:
            current_node = self.root
        
        structure = []
        for child in current_node.children:
            structure.append((current_node.name, child.name, child.is_folder))
            structure.extend(self.get_structure(child))
        return structure
